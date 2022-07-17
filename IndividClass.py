class Individ:
    solved_individ = None
    num = 228

    def __init__(self, boxes):
        self.boxes = boxes
        count = 0
        for i in self.boxes:
            i['id'] = count
            count += 1
            while i['count'] != 1:
                tmp = i.copy()
                tmp['count'] = 1
                self.boxes.append(tmp)
                i['count'] -= 1

