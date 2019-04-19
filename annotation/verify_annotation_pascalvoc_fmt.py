import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("root_path", help="Pascal Voc root path")
args = vars(ap.parse_args())

root_path = args.get('root_path')


def verify(line):
    for target_dir, ext in zip(['./JPEGImages', './Annotations'], ['jpg', 'xml']):
        file_name = f'{line}.{ext}'
        if not os.path.isfile(os.path.join(root_path, target_dir, file_name)):
            print(f'Notfound: {file_name}')


def main():
    with open(os.path.join(root_path, 'ImageSets/Main/test.txt'), 'r') as f:
        lines = [l.strip('\n') for l in f.readlines()]
        for line in lines:
            verify(line)


if __name__ == '__main__':
    main()
