# Directory Tree Generator
 
import os
import argparse
import sys

def genTree(args):
    path = args.d
    print(path)
    text = ""

    for root, dirs, files in os.walk(path):
        root = root.replace(path, "")
        level = root.count(os.sep)

        if level == 0:
            text += path + "\n"
            for f in files:
                text += "  "*level + "|--"
                text += f + "\n"

        else:
            text += "|" + "--"*level + root + "\n"
            for f in files:
                text += "|" + "  "*level + "|--"
                text += f + "\n"

        text += "|\n"
    return text

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--d', type=str, help="Enter directory path.")

args = parser.parse_args()
sys.stdout.write(str(genTree(args)))


