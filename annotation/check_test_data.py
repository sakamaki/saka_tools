"""
テストデータ画像がトレーニングデータに含まれてないかチェックする
"""
import os
import argparse
import hashlib
from glob import glob

ap = argparse.ArgumentParser()
ap.add_argument("test_path", help="Test dataset path")
ap.add_argument("train_path", help="Training dataset path")
args = vars(ap.parse_args())

test_path = args.get('test_path')
train_path = args.get('train_path')
train_md5_hash_list = []
train_md5_filename_list = []


def collect_train_md5_list():
    for train_file_path in glob(f'{train_path}/*.jpg'):
        with open(train_file_path, 'rb') as f:
            train_md5_hash = hashlib.md5(f.read()).hexdigest()
        train_md5_hash_list.append(train_md5_hash)
        train_md5_filename_list.append(os.path.basename(train_file_path))


def main():
    collect_train_md5_list()
    find_flg = False
    for test_file_path in glob(f'{test_path}/*.jpg'):
        with open(test_file_path, 'rb') as f:
            test_md5_hash = hashlib.md5(f.read()).hexdigest()
        if test_md5_hash in train_md5_hash_list:
            print(f'Error: {test_file_path} is training data.')
            find_flg = True
        if os.path.basename(test_file_path) in train_md5_filename_list:
            print(f'Error: {test_file_path} is same filename in training data.')
            find_flg = True
    if not find_flg:
        print('Check OK!')


if __name__ == '__main__':
    main()
