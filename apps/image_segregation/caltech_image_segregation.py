import os
import shutil

source = '/home/charan/Documents/research/256_ObjectCategories/'
destination = '/home/charan/Documents/research/caltech-transfer-learning/'

number_train = 60
number_valid = 10
train_folder = 'train'
test_folder = 'test'
valid_folder = 'valid'

source_destination_dict = {
    '009.bear': 'bear',
    '038.chimp': 'chimp',
    '084.giraffe': 'giraffe',
    '090.gorilla': 'gorilla',
    '134.llama-101': 'llama',
    '151.ostrich': 'ostrich',
    '164.porcupine': 'porcupine',
    '186.skunk': 'skunk',
    '228.triceratops': 'triceratops',
    '250.zebra': 'zebra'
}

for key, value in source_destination_dict.items():
    source_path = os.path.join(source, key)
    internal_count = 0
    print('{} - {}'.format(key, value))
    for file in os.listdir(source_path):
        internal_count += 1
        source_file = os.path.join(source_path, file)
        if internal_count <= number_train:
            if not os.path.exists(os.path.join(destination, train_folder, value)):
                os.makedirs(os.path.join(destination, train_folder, value))
            shutil.copy(source_file, os.path.join(destination, train_folder, value))
        elif internal_count <= (number_train + number_valid):
            if not os.path.exists(os.path.join(destination, valid_folder, value)):
                os.makedirs(os.path.join(destination, valid_folder, value))
            shutil.copy(source_file, os.path.join(destination, valid_folder, value))
        else:
            if not os.path.exists(os.path.join(destination, test_folder, value)):
                os.makedirs(os.path.join(destination, test_folder, value))
            shutil.copy(source_file, os.path.join(destination, test_folder, value))
