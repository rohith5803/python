print("start value and stop value ")
print(" ")
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[0:26])      # postive slicing 
print(letters[0:])
print(letters[:])
print(" ")
print("negative value ")
print(" ")
print(letters[-26::])     #negative slicing 
print(" ")
print("start value stop value and step value ")
print(" ")
print(letters[0:26:1])
print(letters[0:26:2])
print(letters[0:26:3])
print(" ")
print("slicing backward")
print(" ")
print(letters[25::-1])
print(letters[::-1])

#mini challenge 

#slice pqo and edcba
#then produce the last eight character in the reverse order 

#solution

# 123456789012345678901234
# ABCDEFGHIKLMNOPQRSTUVWYZ

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[26:17:-1])
#or 
print(letters[:-9:-1])