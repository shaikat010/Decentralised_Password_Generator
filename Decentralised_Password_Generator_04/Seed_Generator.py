import random

def generate_partial_phrase(x):
    random.seed(10)
    x = random.random()
    return x

x = generate_partial_phrase(10)
print(x)

