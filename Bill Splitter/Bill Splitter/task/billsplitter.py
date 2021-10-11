# initialize a new list to capture friend names
friend_list = []

# verify input of number of friends entered, if invalid, print note to user
try:
    # retrieve input of number of people joining the dinner party
    num_friends = int(input("Enter the number of friends joining (including you):\n"))

    # if at least one friend joins, add their name to the friend list
    if num_friends > 0:
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(num_friends):
            friend_name = input()
            friend_list.append(friend_name)

        # initialize a new dictionary to capture all friends attending the dinner party, set the value = 0
        friend_dict = dict.fromkeys(friend_list, 0)

        # retrieve input of total bill amount
        bill = float(input("Enter the total bill value:\n"))

        # divide the bill equally among number of friends
        split_bill = round(bill/num_friends, 2)

        # assign the split bill to each friend in the dictionary
        for key in friend_dict:
            friend_dict[key] = split_bill

        # print results from dictionary
        print(friend_dict)

    # if no friends are joining, print note to user
    else:
        print("No one is joining for the party")

except ValueError:
    print("No one is joining for the party")
