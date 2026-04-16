from csv import DictReader
from pathlib import Path
import json


def read_data(file_name, key):
    with open("sequential.json","r") as file:
        data=json.load(file)
    if key in data:
        return data[key]
    else:
        return None

print(read_data("sequential.json","unordered_numbers"))

def linear_search(rada, hledane):
    positions = []

    for index, value in enumerate(rada):
        if value == hledane:
            positions.append(index)

    result = {
        "positions": positions,
        "count": len(positions)
    }

    return result


def main():
    data = read_data("sequential.json","unordered_numbers")
    hledane= 0

    result = linear_search(data, hledane)

    print(f"Hledané číslo: {hledane}")
    print(f"Pozice výskytů: {result['positions']}")
    print(f"Počet výskytů: {result['count']}")


if __name__ == "__main__":
    main()



    # # get current working directory path
    # cwd_path = Path.cwd()
    #
    # file_path = cwd_path / file_name


def main():

    pass


if __name__ == "__main__":
    main()
