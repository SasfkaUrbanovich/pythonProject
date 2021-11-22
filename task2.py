def palidrom():
    word = str(input())
    if word == word[::-1]:
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    palidrom()