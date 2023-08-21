import argparse
import app


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Rename Scores",
        description="Renames the scores automatically."
    )
    parser.add_argument("-i", "--input", type=str, help="path to folder", default="test")
    args = parser.parse_args()

    # gui = app.App(folder=args.input)
    # gui.title("Rename scores")
    # gui.geometry("1080x720")
    # gui.mainloop()