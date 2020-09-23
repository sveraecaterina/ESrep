import sys


def add_them_all(filename):
    sum = 0
    ### Your code here

    f = open(fname, "r")
    value_as_int=0
    splitted_line=()

    for line in f:
        splitted_line = line.split()
        for values in splitted_line:
            value_as_int = int(values)
            sum+=value_as_int
       
    ### End of your code
    return sum

if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))