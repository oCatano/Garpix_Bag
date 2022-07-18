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

        for i in range(len(self.boxes)):
            self.boxes[i]['real_size'] = self.boxes[i]['size'].copy()
            new_dict = dict(self.boxes[i])

            tmp = new_dict['size']
            k = tmp['length']
            tmp['length'] = tmp['width']
            tmp['width'] = k

            self.boxes.append(new_dict)
            new_dict = dict(self.boxes[i])

            tmp = new_dict['size']
            k = tmp['length']
            tmp['length'] = tmp['height']
            tmp['height'] = k

            self.boxes.append(new_dict)
            new_dict = dict(self.boxes[i])

            tmp = new_dict['size']
            k = tmp['width']
            tmp['width'] = tmp['height']
            tmp['height'] = k

            self.boxes.append(new_dict)
