range(6)
[0, 1, 2, 3, 4, 5]
for i in range(11):
    print(f'Hello python developer {i}')


counter = 10
while True:
    # counter = counter - 1
    counter -= 1
    print(counter)
    if counter == 5:
        break

print('Далі після While...')


for i in range(6):  # [0,1,2,3,4,5]
    if i == 3:
        continue
    print(i)


# Вивести перше число з кінця, яке ділиться націло на 5. Діапазон від 99 до 0.

for e in reversed(range(100)):
    if e % 5 == 0:
        print(e)
        break

for i in range(-99, 0):
    if i % 5 == 0:
        print(abs(i))
        break