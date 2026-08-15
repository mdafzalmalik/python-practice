info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

# n = len(info)

# courses = []

# for i in  range(0, n):
#     course = info[i][1]
#     courses.append(course)

# print(set(courses))

# for name, course in info:
#     if(course == "English"):
#         print(name)

dict = {} 

for name, course in info:
    if dict.get(name) == None:
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)
