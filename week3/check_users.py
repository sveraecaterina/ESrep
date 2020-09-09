
def check_users(current_users, new_users):

    new_us_lc = [new_users.lower() for new_users in new_us]
    current_us_lc = [current_users.lower() for current_users in current_us]
    xlist=[]
    olist=[]

    for new_users in new_us_lc:
     
        if new_users in current_us_lc:
            xlist.append(new_users)
        else:
            olist.append(new_users)
    
    if not xlist:
        print("No unavailable usernames entered")
    else:
        print("Unavailable usernames, please enter a new one:")
        print(xlist)

    if not olist:
        print("No available usernames entered")
    else:
        print("These usernames are available:")
        print(olist)


if __name__ == "__main__":
    current_us = ['chris','haritha', 'sally', 'darnell', 'superman']
    new_us = ['george', 'ringo', 'superman', 'hannibal']
    check_users(current_us, new_us)