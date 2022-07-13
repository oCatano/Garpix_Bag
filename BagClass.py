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
