array = []
def miin():
    for _ in range(3):
        array.append(int(input('Введите число ')))
    mini = array[0]
    for item in array:
        if mini > item :
            mini = item
    print(mini)
miin()