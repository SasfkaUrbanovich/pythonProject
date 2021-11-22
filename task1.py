def card_hide(card):
    return print('*' * len(card[:-4]) + card[-4:])


if __name__ == '__main__':
    card_hide(input("Введите данные карты"))