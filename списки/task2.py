import random

def miin():
    array = [random.randint(1, 50) for x in range(3)]
    mini = array[0]
    for item in array:
        if mini > item :
            mini = item
    print(mini)


if __name__ == '__main__':
    miin()