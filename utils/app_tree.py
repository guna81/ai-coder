import os
import json
from const.const import OUTPUT_PATH, APP_TREE_PATH, FILE_TREE_FILE_NAME

def update_file_tree(json_data):

    if not os.path.exists(OUTPUT_PATH + '/' + APP_TREE_PATH):
        os.makedirs(OUTPUT_PATH + '/' + APP_TREE_PATH)

    with open(OUTPUT_PATH + '/' + APP_TREE_PATH + '/' + FILE_TREE_FILE_NAME, 'w') as f:
        json.dump(json_data, f, indent=4)
