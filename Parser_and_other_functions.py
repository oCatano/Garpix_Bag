import json
import os
import shutil
from IndividClass import Individ


def parser(path='_vg_85_bgg5jsons/125000/125018_cl.json'):
    """
    :param path: path to json file example '_vg_85_bgg5jsons/125000/125018_cl.json'
    :return: tuple with dict with cargo_space and list of dicts with boxes
    """
    with open(path) as f:
        d = json.load(f)
    cargo_space = d['cargo_space']
    cargo_grops = d['cargo_groups']
    return cargo_space, cargo_grops


def count_bags(path: str):
    spase, groups = parser(path)
    count = 0
    for i in groups:
        count += i['count']
    return count


def get_cargo_space(space):
    a = space['size']
    cargoSpace = {'loading_size': {"height": 0, "length": 0, "width": 0}, 'position': [0, 0, 0], 'type': "pallet"}
    cargoSpace['loading_size']["height"] = a[0] / 1000
    cargoSpace['loading_size']['length'] = a[1] / 1000
    cargoSpace['loading_size']['width'] = a[2] / 1000
    cargoSpace['position'][0] = a[1] / 2000
    cargoSpace['position'][1] = a[0] / 2000
    cargoSpace['position'][2] = a[2] / 2000

    return cargoSpace


def get_cargos(solved, box):
    cargos = []
    unpacked = []
    id_list = []
    k = 0
    for i in solved:
        a = {"calculated_size": {"height": 0, "length": 0, "width": 0}, "cargo_id": "", "id": k, "mass": 0,
             "position": {"x": 0, "y": 0, "z": 0}, "size": {"height": 0, "length": 0, "width": 0}, "sort": 1,
             "stacking": True, "turnover": True, "type": "box"}
        a["cargo_id"] = i[3][1]
        id_list.append(i[3][1])
        a["size"]["height"] = i[2][2] / 1000
        a["size"]["length"] = i[2][0] / 1000
        a["size"]["width"] = i[2][1] / 1000
        a["position"]["x"] = (i[0][1] + i[1][1]) / 2000    # если что поменять в зависимости от координат в алгосе
        a["position"]["y"] = (i[0][2] + i[1][2]) / 2000
        a["position"]["z"] = (i[0][0] + i[1][0]) / 2000
        a["calculated_size"]["height"] = (i[1][2] - i[0][2]) / 1000  # если что поменять в зависимости от координат в алгосе
        a["calculated_size"]["length"] = (i[1][1] - i[0][1]) / 1000
        a["calculated_size"]["width"] = (i[1][0] - i[0][0]) / 1000
        a["mass"] = next((x for x in box if x["group_id"] == i[3][1]), 0)["mass"]
        cargos.append(a)
        k += 1
    q = 0
    for j in box:
        if j["group_id"] not in id_list:
            b = {"group_id": 0, "id": 0, "mass": 0, "position": {"x": -1, "y": 0, "z": -1},
            "size": {"height": 0, "length": 0, "width": 0}, "sort": 1, "stacking": True, "turnover": True}
            b["group_id"] = j["group_id"]
            b["id"] = k
            b["mass"] = j["mass"]
            b["size"]["height"] = j["size"][0] / 1000
            b["size"]["length"] = j["size"][1] / 1000
            b["size"]["width"] = j["size"][2] / 1000
            k += 1
            unpacked.append(b)
            q += 1
            break

    return cargos, unpacked


def get_results(individ: Individ, cargo_space):
    output_data = {}
    boxes = individ.boxes
    solved = individ.solved_individ
    cargoSpace = get_cargo_space(cargo_space)
    cargos, unpacked = get_cargos(solved, boxes)
    output_data['cargoSpace'] = cargoSpace
    output_data['cargos'] = cargos
    output_data['unpacked'] = unpacked
    # os.chdir("output_files")
    # добавить генерацию нового названия файла (как в файле со входными)
    with open('output_files/test.json', 'w') as f:
        json.dump(output_data, f)
    return output_data


def get_the_path():
    for address, dirs, files in os.walk(os.path.abspath('_vg_85_bgg5jsons')):
        for name in files:
            yield os.path.join(address, name)