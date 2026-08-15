a = 5
b = 10
sum = a+b

# normal formatting 
print("Sum of {} & {} is {}".format(a, b, sum))
print("Language is {}".format("python"))

# index based formatting
print("Sum of {1} & {0} is {2}".format(a, b, sum))

# value based fromatting 
print("Values of var {a} & {b}".format(a = 5, b = 4))


# f string 
print(f"sum of {a} & {b} is {sum}")