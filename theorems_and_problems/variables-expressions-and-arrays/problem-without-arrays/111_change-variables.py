# given two integer variables a and b, you must swap their values

# option 1: through the third variable
print("option 1: through the third variable")
a = 3
b = 4
print("original variables: a = " + str(a) + ", b = " + str(b))
t = a
a = b
b = a
print("swap values: a = " + str(a) + ", b = " + str(b) + "\n")

# option 2: without the third variable
print("option 2: without the third variable")
c = 7
d = 21
print("original variables: c = " + str(c) + ", d = " + str(d))
c = c + d
d = c - d
c = c - d
print("swap values: c = " + str(c) + ", d = " + str(d) + "\n")

# option 3: exchange through a temporary tuple (python feature)
print("option 3: exchange through a temporary tuple (python feature)")
e = 24
f = 55
print("original variables: e = " + str(e) + ", f = " + str(f))
e, f = f, e
print("swap values: e = " + str(e) + ", f = " + str(f) + "\n")
