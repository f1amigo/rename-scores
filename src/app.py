import util
import os
from pathlib import Path

def run(input_folder, part_list):
    """
    Runs the renaming portion of the programme.

    Args:
        input_folder (str): path to the input folder
        part_list (str): path to text file containing list of part names
    """
    # Get piece title and list of parts
    piece_title = util.get_piece()
    part_names = util.extract_part_names(part_list)

    # Create destination folder
    count = 0
    dst_dir = f"{input_folder}\\renamed_scores"
    Path(dst_dir).mkdir(parents=True, exist_ok=True)

    # Rename all files in folder
    for file, part in zip(os.listdir(input_folder), part_names):
        os.rename(f"{input_folder}\\{file}", f"{dst_dir}\\{count:02}-{piece_title}-{part.get()}.pdf", dst_dir_fd=dst_dir)
        count += 1    
    
    return 0