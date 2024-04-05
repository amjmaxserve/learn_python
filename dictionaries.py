username ={
    "lydia": "lydiahallie",
    "sarah": "sarah123",
    "max": "max_",
    "joe": "joejoe" 
}

print(username["sarah"])


# print(username["antony"]) //error for items not in dictionaries


# dictionary.keys()
# dictionary.values()
# dictionary.items()

print(username.keys())

for key in username.keys():
    print(key + "-" + username[key])

print(username.values())
print(username.items())

username["max"]="max123"
print(username["max"])

username.update({"chloe": "chloe123"})
print(username)

del username["max"]
print(username)

username.clear()
print(username)


username ={
    "lydia": "lydiahallie",
    "sarah": "sarah123",
    "max": "max_",
    "joe": "joejoe" 
}


username.popitem()
print(username)

usernames_copy = username.copy()
print(usernames_copy)