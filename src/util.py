

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

def get_piece():
    """
    Get the title of the piece from the user.

    Returns:
        str: title of piece
    """
    print("Enter the title of the piece:\n")
    piece = input()
    return piece

