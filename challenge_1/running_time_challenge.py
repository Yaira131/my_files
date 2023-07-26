import sys
import argparse

# Instantiate argparser
parser = argparse.ArgumentParser()
parser.add_argument("--num_file", type=str, required=True, help='Numbers File To Use')
parser.add_argument("--target", type=int, required=True, help='Target Number To Check')

args = parser.parse_args()


NUM_FILE = args.num_file
TARGET_NUM = args.target
NUM_LIST = []

def format_num_list(num_file):
    with open(num_file, "r") as f:
        temp = f.readlines()
        for n in temp:
            NUM_LIST.append(int(n.rstrip()))

def check_sum_exist(num_list, target):
    print(f"Checking {target} As a Target")
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
           if (num_list[i] + num_list[j]) == target:
                print(f"{num_list[i]} + {num_list[j]} = {target}")
                print(f"index of {num_list[i]} is {i}")
                print(f"index of {num_list[j]} is {j}")  
    
    """Previous Answer"""
    # for index_i, num_i in enumerate(num_list):
    #     for index_j, num_j in enumerate(num_list):
    #         if index_i == index_j:
    #             continue
    #         if num_i + num_j == target:
    #             print(f"{num_i} + {num_j} = {target}")
    #             print(f"index of {num_i} is {index_i}")
    #             print(f"index of {num_j} is {index_j}")
    #             sys.exit()


if __name__ == "__main__":
    format_num_list(NUM_FILE)
    check_sum_exist(NUM_LIST, TARGET_NUM)



