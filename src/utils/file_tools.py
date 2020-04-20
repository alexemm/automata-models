from typing import Dict

import json


def load_json(file: str) -> Dict[str, any]:
    """
    Loads json file as a dictionary
    :param file: Path to file
    :return: Dictionary of given file
    """
    with open(file) as f:
        data: Dict[str, any] = json.load(f)
    return data


def save_json(file: str, dic: Dict[str, any]) -> None:
    """
    Saves dictionary in json file
    :param file: Path to file
    :param dic: Dictionary which is saved
    :return: None
    """
    with open(file, 'w+') as f:
        json.dump(dic, f)
