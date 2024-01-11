a = 89
b = 10
c = b  # Store the original value of b in c
b = a  # Assign the value of a to b
a = c  # Assign the original value of b (now in c) to a
print("a={:d} - b={:d}".format(a, b))
