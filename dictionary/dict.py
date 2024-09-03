keys = {
    'Date' : str,
    'Time' : str,
    'Reach' : float,
    'Engagement' : float,
    'Duration' : float,
    'Category' : str
}

info = {}
for key, datatype in keys.items():
    value = input(f"Enter Post {key}: ")
    info[key] = datatype(value)

print()
print("Post Scheduled:")
print(f"Date: {info['Date']}")
print(f"Time: {info['Time']}")
print(f"Reach: {info['Reach']:.2f}")
print(f"Engagement: {info['Engagement']:.2f}")
print(f"Duration: {info['Duration']:.2f}")
print(f"Category: {info['Category']}")