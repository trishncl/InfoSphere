keys = {
    "recipient": str,
    "message": str,
    "name": str,
    "subject": str,
    "version": float,
    "discount": float,
    "status": str,
    "code": str,
    "location": str,
    "age": int,
    "company name": str,
    "website": str,
    "phone": str,
    "job title": str,
    "department": str
}

info = {}
for key, datatype in keys.items():
    value = input(f"Enter the {key}: ")
    info[key] = datatype(value)

# Print the information using the dictionary
print(f"Dear {info['recipient']}, I hope this email finds you well.")
print(info['message'])
print(f"Subject: {info['subject']}")
print(f"Sender: {info['name']}")
print(f"Version: {info['version']:.1f}")
print(f"Discount: {info['discount']:.2f}%")
print(f"Status: {info['status']}")
print(f"Code: {info['code']}")
print(f"Location: {info['location']}")
print(f"Age: {info['age']}")
print(f"Company: {info['company name']}")
print(f"Website: {info['website']}")
print(f"Phone: {info['phone']}")
print(f"Job Title: {info['job title']}")
print(f"Department: {info['department']}")