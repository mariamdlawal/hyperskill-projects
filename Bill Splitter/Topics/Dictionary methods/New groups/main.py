# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
# initializing a new dictionary and assigning the list of groups as keys with value = None
group_dict = dict.fromkeys(groups, None)

# first input is the number of kid groups
num_groups = int(input())

# iterating over the input of number of kids in the group and assigned each group to a key
for i in range(num_groups):
    number_of_kids = int(input())
    group_dict[groups[i]] = number_of_kids

# print the final dictionary
print(group_dict)
