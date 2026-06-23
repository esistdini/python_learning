#!/bin/python3

def linearsearch(row,n):
    global pos
    i = 0
    while i < len(row):
        if row[i] == n:
            pos = i
            return True
        else:
            i += 1

    return False

if __name__ == "__main__":
    row = list(map(int,input().split(sep=" ")))
    n = int(input("Enter the value to search : "))
    pos = -1
    if linearsearch(row,n):
        print(f"{n} is found at index position {pos}")
    else:
        print("Value is not found in the list")
