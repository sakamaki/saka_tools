import os
import shutil
import random


target_file = 'output123.txt'
input_dir = 'datasets1293'
output_train_dir = 'train1000/.'
output_test_dir = 'test293/.'


def main():
    with open(os.path.join(target_file), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        indexs = [i for i in range(0, len(lines))]
        random.shuffle(indexs)
        train_list = lines[:1000]
        test_list = lines[1000:]
        print(len(train_list))
        print(len(test_list))
        for basename in train_list:
            for ext_name in ['.jpg', '.xml']:
                bn = basename.strip('\n')
                src = f'{input_dir}/{bn}{ext_name}'
                out = f'{output_train_dir}/{bn}{ext_name}'
                print(src, out)
                shutil.copyfile(src, out)
        for basename in test_list:
            for ext_name in ['.jpg', '.xml']:
                bn = basename.strip('\n')
                src = f'{input_dir}/{bn}{ext_name}'
                out = f'{output_test_dir}/{bn}{ext_name}'
                print(src, out)
                shutil.copyfile(src, out)


if __name__ == '__main__':
    main()

