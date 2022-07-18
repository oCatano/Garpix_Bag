import json
from BagClass import Bag
from Parser_and_other_functions import parser
from Parser_and_other_functions import count_bags
from IndividClass import Individ
'''class Bags:
    def __size_space__(self):
        with open(path, "r") as json_file:
            data_list = json.load(json_file)

        c_space = (dict(data_list['cargo_space']['size']))
        c_space_edvard = (data_list['cargo_space']['id'])
        c_space['id'] = c_space_edvard
        return c_space
    def __size_grops__(self):
        with open(path, "r") as json_file:
            data_list = json.load(json_file)
        c_grops = data_list['cargo_groups']
        len_c_groups = len(c_grops)
        time_edvard = []
        ''''''c_grops_edvard = (data_list['mass'])
        c_grops['id'] = c_grops_edvard''''''
        while len_c_groups != 0:
            len_c_groups = len_c_groups - 1
            data_size = dict(c_grops[len_c_groups])
            data_size_abc = (data_size["size"])
            c_groups_edvard = (data_size['group_id'])
            data_size_abc['group_id'] = c_groups_edvard
            time_edvard.append(data_size_abc)
        c_grops = time_edvard

        return c_grops
path='_vg_85_bgg5jsons/125000/125018_cl.json'
endi = Bags()
c_groups = endi.__size_grops__()
c_cargo_space = endi.__size_space__()
c_groups.sort(key=lambda x: x['width'] * x['length']) '''

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

def id_checker(id, f_list):
    if(f_list == []):
        return False
    for i in f_list:
        if(i[3][1] == id):
            return True
        '''True - при условии наличия коробки в f_list'''
    return False


def size_space(d_list: Individ):
    c_space = (dict(d_list['size']))
    c_space_edvard = (d_list['id'])
    c_space['id'] = c_space_edvard
    return c_space


def size_groups(d_list: Individ):
    c_grops = d_list
    len_c_groups = len(c_grops)
    time_edvard = []
    while len_c_groups != 0:
        len_c_groups = len_c_groups - 1
        data_size = dict(c_grops[len_c_groups])
        data_size_abc = (data_size["size"])
        c_groups_edvard = (data_size['id'])
        '''на backlog - различать массив и словарь по size'''
        data_size_abc['id'] = c_groups_edvard
        time_edvard.append(data_size_abc)
    c_grops = time_edvard
    gr = sorted(c_grops, key=lambda x: x['width'] * x['length'], reverse=True)
    return gr

def list_print(d_list):
    for i in d_list:
        for j in i:
            for k in j:
                print(k)


def last_ground_box(f_list):
    if len(f_list) == 0:
        yield None
    for i in f_list:
        if i[0][2] == 0: yield i


'''Добавить Individ вместо d_list, d_list: Individ;   Также подаётся Cargo_space'''
def fill_cargo(Individ: Individ, space):
    d_list = size_groups(Individ.boxes)
    cargo_list = size_space(space)
    fullness_list = []
    array_of_base = [[0] * cargo_list['width'] for i in range(cargo_list['length'])]
    while(find_the_smallest_length(d_list, fullness_list) < count_free_length(array_of_base)):
        fill_row(d_list, cargo_list, fullness_list, array_of_base)
    return fullness_list


def fill_row(d_list, cargo_list, f_list, arr_b):
    iterator = last_ground_box(f_list)
    while(find_the_smallest_width(d_list, f_list) < count_free_width(arr_b)):
        # fill_tower(d_list, cargo_list, arr_b, f_list, count_free_length(arr_b) - 1, len(arr_b[0]) - count_free_width(arr_b) - 1)
        tmpi = next(iterator)
        if not tmpi:
            fill_tower(d_list, cargo_list, arr_b, f_list, len(arr_b) - 1, 0)
        else:
            fill_tower(d_list, cargo_list, arr_b, f_list, len(arr_b) - 1 - tmpi[0][0], tmpi[1][1] - tmpi[0][1])


def fill_tower(d_list, cargo_list, arr_b, f_list, x_cor, y_cor):
    last_w = cargo_list['width'] - 1
    last_l = cargo_list['length'] - 1
    sum_of_high = 0
    while(sum_of_high < cargo_list['height'] - find_the_smallest_high(d_list, f_list)):
        '''нужно условие для того, чтобы коробка стояла основанием именно в цикле(нужно использовать last_l и last_w'''
        sum_of_high += put_block(d_list, cargo_list, f_list, arr_b, x_cor, y_cor, sum_of_high, last_w, last_l)


def put_block(d_list, cargo_list, f_list, arr_b, x_cor, y_cor, z_cor, last_w, last_l):
    '''max_square = 0 в последнем листе'''
    high = 0
    for i in d_list:
        if(i['length'] <= x_cor) and (y_cor + i['width'] <= cargo_list['width']) and (z_cor + i['height'] <= cargo_list['height']) and not id_checker(i['id'], f_list):
            if z_cor == 0:
                if(y_cor == 0):
                    a = [[cargo_list['length'] - x_cor - 1, y_cor, z_cor], [cargo_list['length'] - x_cor - 1 + i['length'], y_cor + i['width'], z_cor + i['height']], [i['length'], i['width'], i['height']], [0, i['id']]]
                    f_list.append(a)
                    high = i['height']
                    for j in range(x_cor, x_cor - i['length'], -1):
                        for k in range(y_cor, y_cor + i['width'], 1):
                            arr_b[j][k] = 1
                    break
                else:
                    if(i['length'] < x_cor - count_length(arr_b, y_cor)):
                        a = [[cargo_list['length'] - x_cor - 1, y_cor, z_cor], [cargo_list['length'] - x_cor - 1 + i['length'], y_cor + i['width'], z_cor + i['height']], [i['length'], i['width'], i['height']], [0, i['id']]]
                        f_list.append(a)
                        high = i['height']
                        for j in range(x_cor, x_cor - i['length'], -1):
                            for k in range(y_cor, y_cor + i['width'], 1):
                                arr_b[j][k] = 1
                        break

            else:
                if((i['length'] <= last_l) and (i['width'] <= last_w)):
                    last_l = i['length']
                    last_w = i['width']
                    a = [[cargo_list['length'] - x_cor - 1, y_cor, z_cor], [cargo_list['length'] - x_cor + i['length'] - 1, y_cor + i['width'], z_cor + i['height']], [i['length'], i['width'], i['height']], [0, i['id']]]
                    f_list.append(a)
                    high = i['height']
                    break
    print(len(f_list))
    if len(f_list) == 130:
        print()
    return high


def find_the_smallest_length(d_list, f_list):
    min_l = d_list[len(d_list) - 1]['length']
    for i in d_list:
        if(i['length'] < min_l) and not id_checker(i['id'], f_list): min_l = i['length']
    return min_l


def find_the_smallest_width(d_list, f_list):
    min_w = d_list[len(d_list) - 1]['width']
    for i in d_list:
        if(i['width'] < min_w) and not id_checker(i['id'], f_list): min_w = i['width']
    return min_w


def find_the_smallest_high(d_list, f_list):
    min_h = d_list[len(d_list) - 1]['height']
    for i in d_list:
        if(i['height'] < min_h) and not id_checker(i['id'], f_list): min_h = i['height']
    return min_h


def count_length(arr_b, y_cor):
    i = 0
    if(y_cor == 0):
        return len(arr_b)
    while(arr_b[i][y_cor - 1] < 1 and i < len(arr_b) - 1):
        i+=1
    return (len(arr_b) - i)

def count_free_length(arr_b):
    i = len(arr_b) - 1
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
tmp_list = Individ(boxes)
'''c_groups = sorted(misha.boxes, key=lambda x: x['width'] * x['length'])'''
'''print(fill_cargo(c_gggroups, c_cargggo_space))'''

fill_cargo(tmp_list, space)

'''if __name__ == '__main__':'''

