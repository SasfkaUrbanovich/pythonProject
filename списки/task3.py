def exponentiation():
    exponen = 1
    number = int(input("Введите число "))
    for _ in range(int(input("Введите степень "))):
        exponen = exponen * number
    print(exponen)

exponentiation()