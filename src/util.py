import os

def extract_part_names(part_names):
    with open(part_names, "r") as f:
        parts = [_.strip("\n") for _ in f]
    return parts

def run(var_list):
    print(var_list)
