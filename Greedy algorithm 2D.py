from Parser_and_other_functions import parser
from Parser_and_other_functions import count_bags


bags_num = count_bags(path = '_vg_85_bgg5jsons/125000/125018_cl.json')
c_space, c_groups = parser(path = '_vg_85_bgg5jsons/125000/125018_cl.json')

max_square = 0

"""fullness_list = [[{x11,y11,z11},{x12,y12,z12},{a1,b1,c2}, max_square],[{x11,y11,z11},{x12,y12,z12},{a1,b1,c2}, max_square]] - примерная структура массива заполненности"""
"""sort по max_square"""

for i in c_groups:
    if i['size[0]'] * i['size[1]'] > i['size[0]'] * i['size[2]'] and i['size[0]'] * i['size[1]'] > i['size[1]'] * i['size[2]']:
        max_square = i['size[0]'] * i['size[1]']
    elif i['size[0]'] * i['size[2]'] > i['size[0]'] * i['size[1]'] and i['size[0]'] * i['size[2]'] > i['size[1]'] * i['size[2]']:
        max_square = i['size[0]'] * i['size[2]']
    elif i['size[1]'] * i['size[2]'] > i['size[0]'] * i['size[1]'] and i['size[1]'] * i['size[2]'] > i['size[0]'] * i['size[2]']:
        max_square = i['size[1]'] * i['size[2]']


