dct = {
    "name": "Afzal",
    "sec": "CB",
    "roll no": 30
}

dct.update({
    "city": "Agra"
})

print(type(dct))
print(dct["name"])

print(list(dct.keys()))
print(list(dct.values()))
print(dct.items())