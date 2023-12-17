import random
symbols='+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password=''

print(len(symbols))

length = int(input('Сколько символов в пароле?: '))

for i in range(length):
    password+=random.choice(symbols)

print(password)
