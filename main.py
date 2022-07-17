from Parser_and_other_functions import count_bags
from Parser_and_other_functions import get_results
from Parser_and_other_functions import Individ

from platform import python_version
# _vg_85_bgg5jsons/104000/104004_cl.json
# _vg_85_bgg5jsons/0/100_cl.json
# _vg_85_bgg5jsons/13000/13169_cl.json

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
    [[0, 0, 0], [240, 149, 190], [240, 149, 190], [45600, '717488S2']],
    [[240, 149, 0], [490, 391, 190], [250, 242, 190],[60500,'257551Z4']]
]
individ = Individ(box)
individ.solved_individ = solved
cargo_space = {'id': 953309, 'mass': 20, 'size': [1250, 2100, 1800],
               'params': {'protrusion': [50, 50], 'indentation': [50, 50]}, 'carrying_capacity': 800}


print(count_bags('_vg_85_bgg5jsons/0/100_cl.json'))
print(get_results(individ, cargo_space))
