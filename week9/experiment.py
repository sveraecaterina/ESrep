import sys
import json 

def add_them_all(filename):

    with open(fname) as json_file: 
        data = json.load(json_file) 

    return  print(type(data)),[d['screen_name'] for d in data]

if __name__ == "__main__":
    fname = sys.argv[1]
    print(add_them_all(fname))