from Parser_and_other_functions import parser
from random import randrange


class Bag:
    # дублировать коробки вместо count = 2
    individs = None  # Список индивидов

    def __init__(self, path='_vg_85_bgg5jsons/125000/125018_cl.json'):
        self.space, self.boxes = parser(path)

    def mutations(self, num_of_individ):
        mutatted_index = randrange(0, len(self.boxes), 1)
        while self.boxes[mutatted_index] in self.individs:
            mutatted_index = randrange(0, len(self.boxes), 1)
        index_of_box = randrange(0, len(self.individs[num_of_individ].boxes), 1)
        self.individs[num_of_individ].boxes[index_of_box] = self.boxes[mutatted_index]

    def crossover(self, ind1, ind2):
        len1 = len(self.individs[ind1].boxes)       # Кол-во коробек у первого индивида
        len2 = len(self.individs[ind2].boxes)       # Кол-во коробок в второго индивида
        if len1 > len2:     # нахожу точку скрещевения
            cross_point = randrange(0, len2, 1)
        else:
            cross_point = randrange(0, len1, 1)
        par1 = self.individs[ind1]  # создаю переменную для обмена
        del self.individs[ind1].boxes[cross_point:len1-1]
        h = 0

        for obj in self.individs[ind2].boxes:
            for obj1 in self.individs[ind1].boxes:
                if obj == obj1:
                    h = 1
            if h == 0:
                self.individs[ind1].boxes.append(obj)
            else:
                h = 0
            if len(self.individs[ind1].boxes) == len1:
                break

        del self.individs[ind2].boxes[cross_point:len2 - 1]
        l = 0
        for obj in par1.boxes:
            for obj1 in self.individs[ind2].boxes:
                if obj == obj1:
                    l = 1
            if l == 0:
                self.individs[ind2].boxes.append(obj)
            else:
                l = 0
            if len(self.individs[ind2].boxes) == len2:
                break
