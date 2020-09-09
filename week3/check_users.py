
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
    print("Unavailable usernames, please enter a new one:")
    print(xlist)
    print("Available usernames:")
    print(olist)

if __name__ == "__main__":
    current_us = ['chris','haritha', 'sally', 'darnell', 'superman']
    new_us = ['George', 'ringo', 'Superman', 'hannibal']
    check_users(current_us, new_us)