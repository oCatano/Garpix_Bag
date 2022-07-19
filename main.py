import Greedy_algorithm_2D
from Parser_and_other_functions import count_bags
from Parser_and_other_functions import get_results
from Parser_and_other_functions import parser, get_the_path
from Parser_and_other_functions import Individ

from platform import python_version
# _vg_85_bgg5jsons/104000/104004_cl.json
# _vg_85_bgg5jsons/0/100_cl.json
# _vg_85_bgg5jsons/13000/13169_cl.json

"""
box = [{'id': '57053Y1', 'mass': 4179, 'size': [240, 149, 190], 'sort': 1, 'count': 1, 'stacking': True,
        'turnover': False, 'overhang_angle': 50, 'stacking_limit': 0, 'stacking_is_limited': False,
        'group_id': '717488S2'},
       {'id': '56081Y1', 'mass': 6522, 'size': [250, 242, 190], 'sort': 2, 'count': 1, 'stacking': True,
        'turnover': True, 'overhang_angle': 50, 'stacking_limit': 0, 'stacking_is_limited': False,
        'group_id': '257551Z4'},
       {'id': '56080Y1', 'mass': 9912, 'size': [380, 206, 300], 'sort': 3, 'count': 1, 'stacking': True,
        'turnover': True, 'overhang_angle': 50, 'stacking_limit': 0, 'stacking_is_limited': False,
        'group_id': '853578C4'}]



solved = [
    [[0, 0, 0], [240, 149, 190], [240, 149, 190], [45600, 1]],
    [[240, 149, 0], [490, 391, 190], [250, 242, 190],[60500, 2]]
]


space, boxes = parser('_vg_85_bgg5jsons/125000/125018_cl.json')

individ = Individ(boxes)
individ.solved_individ = solved

print(count_bags('_vg_85_bgg5jsons/0/100_cl.json'))
print(get_results(individ, space))
"""
if __name__ == '__main__':
    print('Введите путь до файла')
    path = input()
    for i in get_the_path(path):
        space, boxes = parser(i)
        individ = Individ(boxes)
        Greedy_algorithm_2D.fill_cargo(individ, space)
        get_results(individ, space)
