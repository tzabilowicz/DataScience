# Generator
def generate_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Natural Number Generator
def natural_numbers():
    i = 0
    while True:
        yield i
        i += 1

# Consume yielded values until none are left
for i in generate_range(10):
    print(f"i: {i}")

# Generators only execute when you iterate over them
# NOTE: The functions below dont do anything (yet)
data = natural_numbers()
evens = (x for x in data if x % 2 == 0) # Even natural numbers

for e in evens:
    if e >= 20:
        break

    print(e)

# Enumeration (index, value) pairs
names = ["Trevor", "John", "Steven", "Perry", "Ferb"]

for i, name in enumerate(names):
    print(f"{i}: {name}")