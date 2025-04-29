"""
======================================================================
PARSE_INTO_JSON --- 

    Author: Zi Liang <zi1415926.liang@connect.polyu.hk>
    Copyright © 2025, ZiLiang, all rights reserved.
    Created: 28 April 2025
======================================================================
"""


# ------------------------ Code --------------------------------------

# normal import
import json
from typing import List, Tuple, Dict
import random
from pprint import pprint as ppp
# import pickle
import os
# from os.path import join, exists
# from collections import Counter,OrderedDict
# from bisect import bisect
# from copy import deepcopy
# import pickle

# import sys
# # sys.path.append("./")
# from tqdm import tqdm

# import numpy as np

# import argparse
# import logging
from datasets import load_dataset


def readAllEditorPrompts():
    read_dir = "./PromptsOfToolsEditors/"
    res_dict = {}

    for fname in os.listdir(read_dir):
        readp = read_dir+fname

        if not fname.endswith(".txt"):
            continue

        prompt_name = fname.replace(".txt", "")

        with open(readp, "r", encoding="utf8") as f:
            prompt = f.readlines()
        prompt = "".join(prompt)
        res_dict[prompt_name] = prompt
    return res_dict


def readFromCSV():
    csv_file = "./agent_prompts.csv"
    res_dict = {}
    with open(csv_file, "r", encoding="utf8") as f:
        all_lines = f.readlines()
    for i, line in enumerate(all_lines):
        if i == 0:
            continue
        res = line.split('"')
        name=res[1]
        prompt='"'.join(res[3:-1])
        # try:
        #     assert len(res) == 5
        # except Exception as e:
        #     print(res)
        #     raise e
        # print(prompt)
        # break
        res_dict[name] = prompt
    return res_dict


def readFromHF():
    dataset_name = "fka/awesome-chatgpt-prompts"
    res_dict = {}

    dataset = load_dataset(dataset_name, split="train")

    for item in dataset:
        res_dict[item["act"]] = item["prompt"]

    return res_dict


def main():
    save_path = "OverallPromptsV1.json"
    Overall_Dict = {
        "Tools & Devs": readAllEditorPrompts(),
        "Agents": readFromCSV(),
        "GPTs": readFromHF(),
    }
    with open(save_path, 'w', encoding='utf8') as f:
        json.dump(Overall_Dict, f, ensure_ascii=False, indent=4)
    print("Save done.")


if __name__ == "__main__":
    main()
