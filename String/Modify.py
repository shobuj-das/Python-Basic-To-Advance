str = "This is string type english"
l1 = len(str)
print(l1)
print(str.upper())
print(str.lower())

print(str.islower())
print(str.isupper())

str1 = " This is string type english "
print(str1.strip())
print(len(str1.strip()))

str1 = str1.strip()
print(len(str1))

# replace
str = str.replace("english","bengali")
print(str)
str1 = "This is, string type-english"
# split
print(str1.split(","))