import os
from pathlib import Path

def extract_part_names(part_names):
    """
    Extracts the part names from a fixed TXT to a list and returns the list.

    Args:
        part_names (str): file path to a TXT file containing the default part names

    Returns:
        list: list of part names to be displayed
    """
    with open(part_names, "r") as f:
        parts = [_.strip("\n") for _ in f]
    return parts

def run(folder, piece, var_list):
    """
    Runs the renaming portion of the programme.

    Args:
        folder (str): path to the input folder
        piece (str): path to the 
        var_list (list): list of part names
    """
    for var in var_list:
        print(var.get())
    count = 0
    dst_dir = f"{folder}\\renamed_scores"
    Path(dst_dir).mkdir(parents=True, exist_ok=True)

    # Rename all files in folder
    for file, var in zip(os.listdir(folder), var_list):
        os.rename(f"{folder}\\{file}", f"{dst_dir}\\{count:02}-{piece}-{var.get()}.pdf", dst_dir_fd=dst_dir)
        count += 1
