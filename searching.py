from csv import DictReader
from pathlib import Path
import json
#
#
# def read_data(file_name, key):
#     with open("sequential.json","r") as file:
#         data=json.load(file)
#     if key in data:
#         return data[key]
#     else:
#         return None
#
# print(read_data("sequential.json","ordered_numbers"))
#
# def linear_search(rada, hledane):
#     positions = []
#
#     for index, value in enumerate(rada):
#         if value == hledane:
#             positions.append(index)
#
#     result = {
#         "positions": positions,
#         "count": len(positions)
#     }
#
#     return result
#
#
# def main():
#     data = read_data("sequential.json","ordered_numbers")
#     hledane= 0
#
#     result = linear_search(data, hledane)
#
#     print(f"Hledané císlo: {hledane}")
#     print(f"Pozice výskytů: {result['positions']}")
#     print(f"Počet vyskytů: {result['count']}")
#
#
# if __name__ == "__main__":
#     main()
#
#
#
#     # # get current working directory path
#     # cwd_path = Path.cwd()
#     #
#     # file_path = cwd_path / file_name
#
#
# def main():
#
#     pass
#
#
# if __name__ == "__main__":
#     main
# c=[-51, -12, -3, -3, -1, 2, 8, 13, 14, 14, 14, 21, 22, 23, 24, 25, 48, 63, 64, 70, 72, 78, 90, 102, 120]
# cisla=sorted(c)
# print(cisla)
# print(serazene_cisla)
# prostredni=len(serazene_cisla)//2
# print(prostredni)
# for i,numbers in enumerate(serazene_cisla):
#

# mid=left+right//2
def binary_search(cisla,target):
    left=0
    right = len(cisla)-1
    print(right)
    while left <=right:
        mid=left+right//2
        if cisla[mid]==target:
            return mid
        elif cisla[mid]<target:
            left=mid+1
        elif cisla[mid]>target:
            right=mid-1
    return None
print(binary_search([-51, -12, -3, -3, -1, 2, 8, 13, 14, 14, 14, 21, 22, 23, 24, 25, 48, 63, 64, 70, 72, 78, 90, 102, 120],-3))

