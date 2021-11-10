for i in range(1,51):
    print("No {0:4} square is {1:3} and cube is {2:3}".format(i, i**2, i**3))
print()
for i in range(1,51):
    print("No {0:2} square is {1:<3} and cube is {2:<3}".format(i, i**2, i**3))
print()
print("The approximate value of pi is {0}".format(22/7))
print("The approximate value of pi is {0:12f}".format(22/7))
print("The approximate value of pi is {0:12.50f}".format(22/7))
print("The approximate value of pi is {0:12.2f}".format(22/7))
print("The approximate value of pi is {0:20.53f}".format(22/7))