import argparse
import app
import gui


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Rename Scores",
        description="Renames the scores automatically."
    )
    parser.add_argument("-i", "--input", type=str, help="path to folder", default="test")
    args = parser.parse_args()

    

    # interface = gui.App(folder=args.input)
    # interface.title("Rename scores")
    # interface.geometry("1080x720")
    # interface.mainloop()