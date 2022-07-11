from Parser_and_other_functions import parser
from Parser_and_other_functions import count_bags


bags_num = count_bags(path = '_vg_85_bgg5jsons/125000/125018_cl.json')
c_space, c_groups = parser(path = '_vg_85_bgg5jsons/125000/125018_cl.json')
max_square = 0
a1 = 2
b1 = 3
c1 = 4
x11 = 1
y11 = 1
z11 = 1
x12 = 1
y12 = 1
z12 = 1
fullness_list = []
a = [(x11, y11, z11), (x12, y12, z12), (a1, b1, c1), max_square]
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
a[3] = max_square
fullness_list.append(a)




