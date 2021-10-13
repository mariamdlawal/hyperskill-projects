# import functions
import random

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

        # divide the bill equally among number of friends, round to two decimal places
        split_bill = round(bill/num_friends, 2)

        # assign the split bill to each friend in the dictionary
        for key in friend_dict:
            friend_dict[key] = split_bill

        # implement who is lucky feature
        lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

        # verify if user input is yes
        if lucky_feature == 'Yes':
            lucky_friend = random.choice(list(friend_dict))
            # print lucky friend
            print(lucky_friend + " is the lucky one!")
            # re-split bill for unlucky friends
            split_bill = round(bill/(num_friends - 1), 2)
            # assign new split bill to each friend, assign value of 0 to lucky friend
            for key in friend_dict:
                friend_dict[key] = split_bill
            friend_dict[lucky_friend] = 0
            # print the updated dictionary
            print(friend_dict)
        else:
            print("No one is going to be lucky")
            print(friend_dict)

    # if no friends are joining, print note to user
    else:
        print("No one is joining for the party")

except ValueError:
    print("No one is joining for the party")
