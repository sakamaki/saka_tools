import os
import shutil
import random
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("input_path", help="Dataset path")
ap.add_argument("image_set_file_path", help="Image set file path")
ap.add_argument("-od", "--output_train_dir", required=True, help="Output train datasets dir")
ap.add_argument("-ot", "--output_test_dir", required=True, help="Output test datasets dir")
ap.add_argument("-tc", "--train_file_count", required=True, help="Train file count")
args = vars(ap.parse_args())


input_dir = args.get('input_path')
image_set_file_path = args.get('image_set_file_path')
output_train_dir = args.get('output_train_dir')
output_test_dir = args.get('output_test_dir')
train_file_count = int(args.get('train_file_count'))


def main():
    with open(os.path.join(image_set_file_path), 'r', encoding='utf-8') as f:
        lines = f.readlines()
    index_list = [i for i in range(0, len(lines))]
    random.shuffle(index_list)
    train_index = index_list[:train_file_count]
    test_index = index_list[train_file_count:]
    train_list = [lines[index] for index in train_index]
    test_list = [lines[index] for index in test_index]
    print(len(train_list))
    print(len(test_list))
    for output_dir, data_list in zip([output_train_dir, output_test_dir], [train_list, test_list]):
        for basename in data_list:
            for ext_name in ['.jpg', '.xml']:
                file_name = basename.strip('\n') + ext_name
                src = os.path.join(input_dir, file_name)
                out = os.path.join(output_dir, file_name)
                print(src, out)
                shutil.copyfile(src, out)


if __name__ == '__main__':
    main()

