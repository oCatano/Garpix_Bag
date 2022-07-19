import json
from BagClass import Bag
from Parser_and_other_functions import parser
from Parser_and_other_functions import count_bags, get_results
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
    final_arr = []
    ind_1 = 0
    ind_2 = 0
    square = gr[0]['width']*gr[0]['length']
    for i in range (len(gr)):
        if gr[i]['width']*gr[i]['length'] != square:
            ind_2 = i
            tmp = gr[ind_1:ind_2]
            final_arr+=sorted(tmp, key=lambda x: x['length'], reverse=True)
            ind_1 = i
            square = gr[i]['width'] * gr[i]['length']
    return final_arr

'''def list_print(d_list):
    for i in d_list:
        for j in i:
            for k in j:
                print(k)'''


def last_ground_box(f_list):
    if len(f_list) == 0:
        return None
    for j in range(len(f_list) - 1, -1, -1):
        if f_list[j][0][2] == 0:
            return f_list[j]


'''Добавить Individ вместо d_list, d_list: Individ;   Также подаётся Cargo_space'''
def fill_cargo(Individ: Individ, space):
    d_list = size_groups(Individ.boxes)
    cargo_list = size_space(space)
    fullness_list = []
    array_of_base = [[0] * cargo_list['width'] for i in range(cargo_list['length'])]
    test_find_smallest = find_the_smallest_length(d_list, fullness_list)
    test_count_flength = count_free_length(array_of_base, fullness_list)
    while(test_find_smallest < test_count_flength):
        fill_row(d_list, cargo_list, fullness_list, array_of_base)
        test_find_smallest = find_the_smallest_length(d_list, fullness_list)
        test_count_flength = count_free_length(array_of_base, fullness_list)
    Individ.solved_individ = fullness_list
    return fullness_list


def fill_row(d_list, cargo_list, f_list, arr_b):
    empty = True
    min_w, checker = find_the_smallest_width(d_list, f_list)
    fre = count_free_width(arr_b, f_list, empty)
    new_row = False
    if f_list != []:
        new_row = True

    len_f_list = len(f_list)
    while(min_w <= fre and checker):
        # fill_tower(d_list, cargo_list, arr_b, f_list, count_free_length(arr_b) - 1, len(arr_b[0]) - count_free_width(arr_b) - 1)
        tmpi = last_ground_box(f_list)
        if new_row:
            for j in range(len(f_list) - 1, -1, -1):
                if f_list[j][0][2] == 0 and f_list[j][0][1] == 0:
                    fill_tower(d_list, cargo_list, arr_b, f_list,len(arr_b) - 1 - f_list[j][1][0], 0)
                    new_row = False
                    break
        elif not tmpi:
            fill_tower(d_list, cargo_list, arr_b, f_list, len(arr_b) - 1, 0)
        else:
            fill_tower(d_list, cargo_list, arr_b, f_list, len(arr_b) - 1 - tmpi[0][0], tmpi[1][1])
        if len_f_list != len(f_list):
            empty = False
        min_w, checker = find_the_smallest_width(d_list, f_list)
        fre = count_free_width(arr_b, f_list, empty)

def fill_tower(d_list, cargo_list, arr_b, f_list, x_cor, y_cor):
    last_w = cargo_list['width'] - 1
    last_l = cargo_list['length'] - 1
    sum_of_high = 0
    smallest_high, checker = find_the_smallest_high(d_list, f_list, sum_of_high)
    while((sum_of_high < cargo_list['height'] - smallest_high) and checker):
        '''нужно условие для того, чтобы коробка стояла основанием именно в цикле(нужно использовать last_l и last_w'''
        high, last_l, last_w = put_block(d_list, cargo_list, f_list, arr_b, x_cor, y_cor, sum_of_high, last_w, last_l)
        sum_of_high += high
        smallest_high, checker = find_the_smallest_high(d_list, f_list, sum_of_high)

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
                    last_l = i['length']
                    last_w = i['width']
                    for j in range(x_cor, x_cor - i['length'], -1):
                        for k in range(y_cor, y_cor + i['width'], 1):
                            arr_b[j][k] = 1
                    break
                else:
                    test = count_length(arr_b, y_cor)
                    if(i['length'] < last_ground_box(f_list)[2][0]):
                        a = [[cargo_list['length'] - x_cor - 1, y_cor, z_cor], [cargo_list['length'] - x_cor - 1 + i['length'], y_cor + i['width'], z_cor + i['height']], [i['length'], i['width'], i['height']], [0, i['id']]]
                        f_list.append(a)
                        high = i['height']
                        last_l = i['length']
                        last_w = i['width']
                        for j in range(x_cor, x_cor - i['length'], -1):
                            for k in range(y_cor, y_cor + i['width'], 1):
                                arr_b[j][k] = 1
                        break

            else:
                if (i['length'] <= last_l) and (i['width'] <= last_w):
                    last_l = i['length']
                    last_w = i['width']
                    a = [[cargo_list['length'] - x_cor - 1, y_cor, z_cor], [cargo_list['length'] - x_cor + i['length'] - 1, y_cor + i['width'], z_cor + i['height']], [i['length'], i['width'], i['height']], [0, i['id']]]
                    f_list.append(a)
                    high = i['height']
                    break
    print(len(f_list))
    if(len(f_list) == 89):
        print()
    return high, last_l, last_w


def find_the_smallest_length(d_list, f_list):
    k = max(d_list, key=lambda i: i['length'])
    min_l = k['length']
    for i in d_list:
        if (i['length'] < min_l) and not id_checker(i['id'], f_list):
            min_l = i['length']
    return min_l


def find_the_smallest_width(d_list, f_list):
    k = max(d_list, key=lambda i: i['width'])
    checker = False
    min_w = k['width']
    for i in d_list:
        if(i['width'] < min_w) and not id_checker(i['id'], f_list):
            min_w = i['width']
            checker =True
    return min_w, checker


def find_the_smallest_high(d_list, f_list, sum_of_high):
    k = max(d_list, key=lambda i: i['height'])
    checker = False
    min_h = k['height']
    if(sum_of_high == 0):
        for i in d_list:
            if(i['height'] <= min_h) and not id_checker(i['id'], f_list):
                min_h = i['height']
                checker = True
    else:
        for i in d_list:
            l = f_list[-1][2][0]
            w = f_list[-1][2][1]
            if(i['height'] <= min_h) and not id_checker(i['id'], f_list) and ( l >= i['length']) and \
                    (w >= i['width']):
                min_h = i['height']
                checker = True
   # mh = min(d_list, key=lambda i: i['height'])
    return min_h, checker


def count_length(arr_b, y_cor):
    i = 0
    if(y_cor == 0):
        return len(arr_b)
    while(arr_b[i][y_cor - 1] < 1 and i < len(arr_b) - 1):
        i+=1
    return (len(arr_b) - i)

def count_free_length(arr_b, f_list):
    if f_list == []:
        return len(arr_b) - 1
    elif len(f_list) != 0:
        for j in range(len(f_list) - 1, -1, -1):
            if f_list[j][0][2] == 0 and f_list[j][0][1] == 0:
                return len(arr_b) - f_list[j][1][0]


def count_free_width(arr_b, f_list, empty):
    if f_list == []:
        return len(arr_b[0]) - 1
    elif f_list and not empty:
        for j in range(len(f_list) - 1, -1, -1):
            if f_list[j][0][2] == 0 and f_list[j][2][0] <= last_ground_box(f_list)[2][0]:
                return len(arr_b[0]) - f_list[j][1][1]
    elif f_list and empty:
        return len(arr_b[0]) - 1


    '''if (f_list == []):
        while((arr_b[0][i] < 1) and (i < len(arr_b[0]) - 1)):
            i+=1
        return i
    else:
        for j in f_list:
            if j[0][1] == 0 and j[0][2] == 0:
                x_r = j[1][0]
        return len(arr_b[0]) - x_r'''
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

'''c_groups = sorted(misha.boxes, key=lambda x: x['width'] * x['length'])'''
'''print(fill_cargo(c_gggroups, c_cargggo_space))'''
'''for i in tmp_list.boxes:
    if i['size']['height'] == 40:
        k.append(i)'''



if __name__ == '__main__':
    space, boxes = parser(path='_vg_85_bgg5jsons/125000/125018_cl.json')
    tmp_list = Individ(boxes)
    f = fill_cargo(tmp_list, space)
    print(tmp_list.solved_individ)
    get_results(tmp_list, space)
