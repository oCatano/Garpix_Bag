import json


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



def get_cargo_space(path: str):
    output_data = {}
    space, groups = parser(path)
    a = []
    a = space['size']
    cargoSpace = {'loading_size': {"height": 0, "length": 0, "width": 0}, 'position': [0,0,0], 'type': "pallet"}
    cargoSpace['loading_size']["height"] = a[0] / 1000
    cargoSpace['loading_size']['length'] = a[1] / 1000
    cargoSpace['loading_size']['width'] = a[2] / 1000
    cargoSpace['position'][0] = a[1] / 2000
    cargoSpace['position'][1] = a[0] / 2000
    cargoSpace['position'][2] = a[2] / 2000

    output_data['cargoSpace'] = cargoSpace

    with open('output_data_test.json', 'w') as f:
        json.dump(output_data, f)

    return output_data

