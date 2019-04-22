import os
import collections
import argparse
from glob import glob

from bs4 import BeautifulSoup


ap = argparse.ArgumentParser()
ap.add_argument("input_path", help="Annotation dir path")
args = vars(ap.parse_args())

input_path = args.get('input_path')


def main():
    file_count = 0
    result = []
    for path in glob(os.path.join(input_path, '*.xml')):
        with open(path, 'r') as doc:
            soup = BeautifulSoup(doc, 'xml')
        for obj in soup.findAll(name='name'):
            result.append(obj.string)
        file_count += 1
    counter = collections.Counter(result)
    print('file_count: {}\n'.format(file_count))
    for k, v in counter.items():
        print(f'{k}\t{v}')


if __name__ == '__main__':
    main()
