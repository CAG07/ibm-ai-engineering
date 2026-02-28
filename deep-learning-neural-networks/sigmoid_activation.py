import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

z = 0.4  # set this to whatever value you want
output = sigmoid(z)
print("sigma(z) =", output)
