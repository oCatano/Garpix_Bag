import json
from BagClass import Bag
from Parser_and_other_functions import parser
from Parser_and_other_functions import count_bags
from IndividClass import Individ
class Bags:
    def __size_space__(self):
        with open(path, "r") as json_file:
            data_list = json.load(json_file)
        c_space = dict(data_list['cargo_space']['size'])
        c_space_edvard = (data_list['cargo_space']['id'])
        c_space['id'] = c_space_edvard
        return c_space
    def __size_grops__(self):
        with open(path, "r") as json_file:
            data_list = json.load(json_file)
        c_grops = data_list['cargo_groups']
        len_c_groups = len(c_grops)
        time_edvard = []
        '''c_grops_edvard = (data_list['mass'])
        c_grops['id'] = c_grops_edvard'''
        while len_c_groups != 0:
            len_c_groups = len_c_groups - 1
            data_size = dict(c_grops[len_c_groups])
            data_size_abc = (data_size["size"])
            c_groups_edvard = (data_size['group_id'])
            data_size_abc['id'] = c_groups_edvard
            time_edvard.append(data_size_abc)
        c_grops = time_edvard

        return c_grops

path='_vg_85_bgg5jsons/125000/125018_cl.json'
endi = Bags()
c_groups = endi.__size_grops__()
c_cargo_space = endi.__size_space__()
print(endi.__size_grops__())
print(endi.__size_space__())
c_groups.sort(key=lambda x: x['width'] * x['length'])
print(c_groups)
""""
path="_vg_85_bgg5jsons/125000/125018_cl.json"
with open(path, "r") as json_file:
    data_list = json.load(json_file)
c_space = dict(data_list['cargo_space']['size'])
c_grops = data_list['cargo_groups']
len_c_groups = len(c_grops)
time_edvard = []
while len_c_groups != 0:
    len_c_groups = len_c_groups - 1
    data_size = dict(c_grops[len_c_groups])
    data_count = dict(c_grops[len_c_groups])
    data_size_abc = (data_size["size"])
    time_edvard.append(data_size_abc)
c_grops = time_edvard
print("c_space:", c_space)
print("c_grops:", c_grops)
print(data_list) """


def list_print(d_list):
    for i in d_list:
        for j in i:
            for k in j:
                print(k)


'''Добавить Individ вместо d_list, d_list: Individ;   Также подаётся Cargo_space'''
def fill_cargo(d_list, cargo_list):
    fullness_list = []
    array_of_base = [[0] * cargo_list['width'] for i in range(cargo_list['length'])]
    while(find_the_smallest_length(d_list) < count_free_length(array_of_base)):
        fill_row(d_list, cargo_list, fullness_list, array_of_base)
    return fullness_list


def fill_row(d_list, cargo_list, f_list, arr_b):
    while(find_the_smallest_width(d_list) < count_free_width(arr_b)):
        fill_tower(d_list, cargo_list, arr_b, f_list, count_free_length(arr_b) - 1, count_free_width(arr_b) - 1)


def fill_tower(d_list, cargo_list, arr_b, f_list, x_cor, y_cor):
    last_w = cargo_list['width']
    last_l = cargo_list['length']
    sum_of_high = 0
    num_of_boxes_in_the_tower = 0
    while(sum_of_high < cargo_list['high'] - find_the_smallest_high(d_list)):
        sum_of_high += put_block(d_list, cargo_list, f_list, arr_b, x_cor, y_cor, sum_of_high, num_of_boxes_in_the_tower, last_w, last_l)


def put_block(d_list, cargo_list, f_list, arr_b, x_cor, y_cor, z_cor, num_b, last_w, last_l):
    '''max_square = 0 в последнем листе'''
    high = 0
    for i in cargo_list(len(d_list), 0, -1):
        if((i['length'] < x_cor) and (y_cor + i['width'] < cargo_list['width']) and (z_cor + i['high'] < cargo_list['high'])):
            if(num_b == 0):
                num_b += 1
                if(y_cor == 0):
                    a = [[cargo_list['length'] - x_cor, y_cor, z_cor], [cargo_list['length'] - x_cor + i['length'], y_cor + i['width'], z_cor + i['high']], [i['length'], i['width'], i['high']], [0, i['id']]]
                    f_list.append(a)
                    d_list[i].pop()
                    high = i['high']
                    for j in range(x_cor + i['length'], x_cor, -1):
                        for k in range(y_cor, y_cor + i['width'], 1):
                            arr_b[j][k] = 1
                    break
                else:
                    if(i['length'] < count_length(arr_b, y_cor) - x_cor):
                        a = [[cargo_list['length'] - x_cor, y_cor, z_cor], [cargo_list['length'] - x_cor + i['length'], y_cor + i['width'], z_cor + i['high']], [i['length'], i['width'], i['high']], [0, i['id']]]
                        f_list.append(a)
                        d_list[i].pop()
                        high = i['high']
                        for j in range(x_cor + i['length'], x_cor, -1):
                            for k in range(y_cor, y_cor + i['width'], 1):
                                arr_b[j][k] = 1
                        break

            else:
                num_b+=1
                if((i['length'] <= last_l) and (i['width'] <= last_w)):
                    last_l = i['length']
                    last_w = i['width']
                    a = [[cargo_list['length'] - x_cor, y_cor, z_cor], [cargo_list['length'] - x_cor + i['length'], y_cor + i['width'], z_cor + i['high']], [i['length'], i['width'], i['high']], [0, i['id']]]
                    f_list.append(a)
                    d_list[i].pop()
                    high = i['high']

                    
            break
    return high


def find_the_smallest_length(d_list):
    min_l = d_list[len(d_list) - 1]['length']
    for i in d_list:
        if(i['length'] < min_l): min_l = i['length']
    return min_l


def find_the_smallest_width(d_list):
    min_w = d_list[len(d_list) - 1]['width']
    for i in d_list:
        if(i['width'] < min_w): min_w = i['width']
    return min_w


def find_the_smallest_high(d_list):
    min_h = d_list[len(d_list) - 1]['high']
    for i in d_list:
        if(i['high'] < min_h): min_h = i['high']
    return min_h


def count_length(arr_b, y_cor):
    i = 0
    if(y_cor == 0):
        return len(arr_b)
    while(arr_b[i][y_cor - 1] < 1):
        i+=1
    return (len(arr_b) - i)

def count_free_length(arr_b):
    i = len(arr_b[0])
    n = 0
    while(arr_b[i][0] < 1 and i >= 0):
        i-=1
        n+=1
    return n


def count_free_width(arr_b):
    i = 0
    while((arr_b[0][i] < 1) and (i < len(arr_b[0]) - 1)):
        i+=1
    return i

'''max_square = 0
size = 0
sort по max_square
a1 = 2
b1 = 3
c1 = 4
x11 = 1
y11 = 1
z11 = 1
x12 = 1
y12 = 1
z12 = 1
a = [[x11, y11, z11], [x12, y12, z12], [a1, b1, c1, max_square]]
c = list(a[2])

max1 = c[0]*c[1]
max2 = c[0]*c[2]
max3 = c[1]*c[2]
if max1 > max2:
    if max1 > max3:
        max_square = max1
    else: max_square = max3
else:
    if max2 > max3:
        max_square = max2
    else: max_square = max3
a[2][3] = max_square
data_list.append(a)'''
space, boxes = parser(path='_vg_85_bgg5jsons/125000/125018_cl.json')
ind = Individ(boxes)

print(fill_cargo(c_groups, c_cargo_space))
