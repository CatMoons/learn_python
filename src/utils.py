import json
import os
from typing import List, Union, Any


def get_info_transactions_json(file_path: str)->List[Any]:

    data_empty_list: list = []

    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            operation = json.load(f)
            if len(operation) == 0 or type(operation) != list:
                return data_empty_list
            else:
                return operation
        except json.decoder.JSONDecodeError:
            return data_empty_list


if __name__ == '__main__':
    data = get_info_transactions_json("E:\pycharm_project\widget_personal_cabinet\data\operations.json")
    print(data)


