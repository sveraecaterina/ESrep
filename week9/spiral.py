def spiral(x):
#im sorry if some of this is redundant, i spent hours on this i'm afraid to break it now

    a=0
    i=1
    value=1
    val=0

    my_list=[y for y in range(1,x) if y%2==0 ] 
    for item in my_list:
 
        for i in range(1,5):
            
            a=value
            a+=1+i*(item)+val
            value=a
            i+=1

        val+=4*(item)

    return print(a)

if __name__ == "__main__":
    x=501
    spiral(x)