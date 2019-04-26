import os

from bs4 import BeautifulSoup

# target_dir = 'datasets_class13_test1112_2class/test/Annotations'
target_dir = 'datasets_class13_520_0723_2class/Annotations'
target_file = 'datasets_class13_520_0723_2class/ImageSets/Main/test.txt'
output_dir = 'test300'
remove_classes = ['sentence', 'table', 'pie', 'band', 'histogram', 'quadratic', 'figure', 'caption', 'image']


def main():
    with open(target_file, 'r') as f:
        for path in f.readlines():
            filename = path.strip('\n') + '.xml'
            with open(os.path.join(target_dir, filename)) as doc:
                soup = BeautifulSoup(doc, 'xml')
            for obj in soup.findAll('object'):
                for name in obj.findAll(name='name'):
                    if name.contents[0] in remove_classes:
                        obj.extract()
                        break
            if len(soup.findAll('object')):
                with open(os.path.join(output_dir, filename), 'w') as doc:
                    doc.write(str(soup))


if __name__ == '__main__':
    main()
