import os
import json
from const.const import OUTPUT_PATH, APP_TREE_PATH, FILE_TREE_FILE_NAME


def get_file_tree(topdir):
    file_tree = {}
    for root, dirs, files in os.walk(topdir):
        relative_path = os.path.relpath(root, topdir)
        file_tree[relative_path] = {"dirs": dirs, "files": files}
    return file_tree



def update_file_tree(app_name, json_data):
    app_path = OUTPUT_PATH + '/' + app_name + '/' + APP_TREE_PATH

    if not os.path.exists(app_path):
        os.makedirs(app_path)

    with open(app_path + '/' + FILE_TREE_FILE_NAME, 'w') as f:
        json.dump(json_data, f, indent=4)
