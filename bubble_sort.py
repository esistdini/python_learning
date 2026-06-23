
#!/bin/python3


def bubble_sort(row):
    
    for i in range(len(row)-1,0,-1):
        for j in range(len(row) -1):
            if row[j] > row[j+1]: #Comparing one value with another value
                temp = row[j+1] #Temporary variable to hold value
                row[j+1] = row[j]
                row[j] = temp 

    print(row)


if __name__ == "__main__":
    n = list(map(int,input().split(sep=" ")))
    bubble_sort(n)