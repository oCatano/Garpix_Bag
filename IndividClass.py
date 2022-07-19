class Individ:
    solved_individ = None
    towers = []

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
            new_dict = self.boxes[i].copy()
            changed_dict = {'length': new_dict['size']['width'],
                            'width': new_dict['size']['length'],
                            'height': new_dict['size']['height']
                            }
            new_dict['size'] = changed_dict
            self.boxes.append(new_dict)

            new_dict = self.boxes[i].copy()
            changed_dict = {'length': new_dict['size']['height'],
                            'width': new_dict['size']['width'],
                            'height': new_dict['size']['length']
                            }
            new_dict['size'] = changed_dict
            self.boxes.append(new_dict)

            new_dict = self.boxes[i].copy()
            changed_dict = {'length': new_dict['size']['length'],
                            'width': new_dict['size']['height'],
                            'height': new_dict['size']['width']
                            }
            new_dict['size'] = changed_dict
            self.boxes.append(new_dict)

            # {"height": 1.25, "length": 2.1, "width": 1.8}
    def towers_list(self):
        ind_of_ground_box = 0
        for i in range(1, len(self.solved_individ)):
            if self.solved_individ[i][0][2] == 0:
                self.towers.append(self.solved_individ[ind_of_ground_box:i])
                ind_of_ground_box = i
        self.towers.append(self.solved_individ[ind_of_ground_box:len(self.solved_individ)])