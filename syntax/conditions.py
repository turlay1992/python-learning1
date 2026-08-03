animal = input('Fill up your animal\n')
# print(type(animal))

if animal == 'cat':
    print('Meo')
elif animal == 'dog':
    print('Wof')
elif animal == 'snake':
    print('Shshsh')
else:
    print("I don't know this animal")


line = input('any line\n \t')
if line:
    print(line)
else:
    print(None)

# ternary
print(line if line else None)