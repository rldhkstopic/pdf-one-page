import os
import sys
import argparse
import re

def main(argument):
    directory = os.getcwd()
    files = os.listdir(directory)

    output_dir = os.path.join(directory, 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in files:
        match = re.search(r'20\d\d', file)
        if match:
            year = match.group()
            new_filename = f"{year}_{argument}_Solution{os.path.splitext(file)[1]}"
            os.rename(os.path.join(directory, file), os.path.join(output_dir, new_filename))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename files by moving the year and adding a custom string')
    parser.add_argument('custom_string', type=str, help='The custom string to be added in the filename')

    args = parser.parse_args()
    main(args.custom_string)
