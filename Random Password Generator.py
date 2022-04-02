import random
passlen = int(input("Enter the length of password"))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!~@#$%^&*()_+=<>?:;.,[{]}"
p = "".join(random.sample(s, passlen))
print(p)