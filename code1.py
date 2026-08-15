age = int(input("Eenter your age: "))

if(age < 13):
    print("child")
elif(age < 18 and age >= 13):
    print("teenager")
else:
    print("adult")