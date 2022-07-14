from Parser_and_other_functions import parser
from random import randrange


class Bag:
    # дублировать коробки вместо count = 2
    individs = None  # Список индивидов
    new_individs = []
    def __init__(self, path='_vg_85_bgg5jsons/125000/125018_cl.json'):
        self.space, self.boxes = parser(path)

    def mutations(self, num_of_individ):
        mutatted_index = randrange(0, len(self.boxes), 1)
        while self.boxes[mutatted_index] in self.individs:
            mutatted_index = randrange(0, len(self.boxes), 1)
        index_of_box = randrange(0, len(self.individs[num_of_individ].boxes), 1)
        self.individs[num_of_individ].boxes[index_of_box] = self.boxes[mutatted_index]

    def crossover(self, ind1, ind2):
        id_=len(self.new_individs)
        len_ = len(self.individs[ind1].boxes)       # Кол-во коробек у первого индивида
        cross_point = randrange(0, len_, 1)
        self.new_individs[id_].boxes = self.individs[ind1].boxes[0:cross_point]
        id_ += 1
        self.new_individs[id_].boxes = self.individs[ind2].boxes[0:cross_point]
        id_ -= 1
        h = 0
        for obj in self.individs[ind2].boxes:
            for obj1 in self.individs[ind1].boxes:
                if obj1 == self.individs[ind1].boxes[cross_point]:
                    break
                if obj == obj1:
                    h = 1
            if h == 0:
                self.new_individs[id_].boxes.append(obj)
            else:
                h = 0
            if len(self.new_individs[ind1].boxes) == len_:
                break
        del self.individs[ind2].boxes[cross_point:len_ - 1]
        l = 0
        id_+=1
        for obj in self.individs[ind1].boxes:
            for obj1 in self.individs[ind2].boxes:
                if obj1 == self.individs[ind2].boxes[cross_point]:
                    break
                if obj == obj1:
                    l = 1
            if l == 0:
                self.new_individs[id_].boxes.append(obj)
            else:
                l = 0
            if len(self.new_individs[id_].boxes) == len_:
                break
