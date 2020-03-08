import json


def get_json_data(file_path, file_name):
    with open(file_path + '\\' + file_name + '.json', 'r') as json_file:
        json_data = json_file.read()
    json_object = json.loads(json_data)
    return json_object

'''TODO create other file formats if we want to use them '''