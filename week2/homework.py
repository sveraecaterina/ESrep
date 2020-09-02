import logging
logging.basicConfig(level=logging.DEBUG)
def squared_threes():
   
    return_value = [x ** 2 for x in range(0,100) if x%3==0 and x!=0]
   
    return return_value
if __name__ == "__main__":
   for x in squared_threes():
       print(x)

   # should print out all numbers between 0 and 99 (inclusive)
   # that are evenly divisible by 3, then squared.
   # e.g 
   # 9
   # 36
   # 81 
   # .....   etc
