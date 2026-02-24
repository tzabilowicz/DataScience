import random

random.seed(10)

# Generate 5 uniform random numbers between 0 and 1
r = [random.random() for _ in range(5)]

print(r)

# Choose random number from range
r_1 = random.randrange(10)   # 0-9
r_2 = random.randrange(3, 6) # 3-5

print(r_1)
print(r_2)

# Randomly reorder elements
e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(e)

print(e)


# Randomly uniform sampling (with replacement)
nums = range(20)

selection = random.choice(nums)

print(selection)

# Random uniform sampling (without replacement)
selections = random.sample(nums, 6) # Choose 6 numbers

print(selections)