import random
charsCU = list('ACDEFGHIJKLMNOPQRSTWXYZ')
charscs = list('abcdefghijklmnopqrstwxyz')
name = ""
for x in range(1):
    name += random.choice(charsCU)
for x in range(10):
    name += random.choice(charscs)
name += " "
for x in range(1):
    name += random.choice(charsCU)
for x in range(6):
    name += random.choice(charscs)
print(name)