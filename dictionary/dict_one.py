keys = {
    'the book title' : str,
    'the author' : str,
    'the year of publication' : int,
    'the genre' : str,
    'the library' : str,
    'your member ID' : int,
    'the return date' : str 
}

info = {}
for key, datatype in keys.items():
    value = input(f"Enter {key}: ")
    info[key] = datatype(value)

print(f"You have successfully reserved the book \'{info['the book title']}\' by {info['the author']}.")
print(f"Year of Publication: {info['the year of publication']}")
print(f"Genre: {info['the genre']}")
print(f"Library: {info['the library']}")
print(f"Member ID: {info['your member ID']}")
print(f"Return Date: {info['the return date']}")