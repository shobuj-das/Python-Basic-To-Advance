# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x = int(5)
print(type(x))
x = float(4.6)
print(type(x))

x = str("Hello world")
print(type(x))

x = list(("hello", "world", "im"))
print(x)
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(type(x))

x = tuple(["apple", "banana", "cherry"])
print(type(x))

x = dict(name="John", age=36)
print(x)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))
x = set(["apple", "banana", "banana"])
print(x)
print(type(x))

x = bool(5)
print(x)
print(type(x))
x = bool(0)
print(x)
print(type(x))
x = bool(-9)
print(x)
print(type(x))