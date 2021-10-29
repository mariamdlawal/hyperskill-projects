# sample input
number = input()

my_numbers = [int(x) for x in number]

x = 0
running_total = []

for i in my_numbers:
    x += i
    running_total.append(x)

print(running_total)
