class Tomato:

    states = {0: 'is growing', 1: 'green', 2: 'red'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 2:
            self._state += 1
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 2:
            print(f'Tomato {self._index} созрел')
            return True
        return False


class TomatoBush:

    def __init__(self, count):
        self.tomatoes = [Tomato(index) for index in range(0, count)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        print("Томаты упали в корзину для сбора урожая")
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f'Садовник {self.name} выполняет свою работу - ухаживая за томатами ')
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f'{self.name} собирает томаты ')
            self._plant.give_away_all()
        else:
            print('Урожай ещё не созрел ,либо вы ничего не поссадили ещё ')

    @staticmethod
    def knowledge_base():
        print('У вас есть помощник Садовник и рассада томатов \n'
              'Что бы томаты подросли скажите садовнику работать gardener.work \n'
              'Если нужно собрать готовый урожай Садовник вам поможет gardener.harvest \n')


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(int(input("Введите количество томатов ")))
    gardener = Gardener(input("Введите имя садовника "), great_tomato_bush)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
