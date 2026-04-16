from csv import DictReader
from pathlib import Path
import json


def read_data(file_name, key):
    with open("sequential.json","r") as file:
        data=json.load(file)
    return data




    # # get current working directory path
    # cwd_path = Path.cwd()
    #
    # file_path = cwd_path / file_name


def main():
    pass


if __name__ == "__main__":
    main()
