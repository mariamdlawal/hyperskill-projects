#  You can experiment here, it won’t be checked
a = True
b = False
c = a and not b

val_one: bool = not(c or b)
value_two: bool = a and (not c or b)

print(val_one)

