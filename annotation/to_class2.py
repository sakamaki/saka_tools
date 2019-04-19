import os

from bs4 import BeautifulSoup

# target_dir = 'datasets_class13_test1112_2class/test/Annotations'
target_dir = 'test300'
output_dir = 'class2_test300/Annotations'
remove_classes = ['sentence', 'table', 'pie', 'band', 'histogram', 'quadratic', 'figure', 'caption', 'image']


def main():
    for filename in os.listdir(path=target_dir):
        with open(os.path.join(target_dir, filename), 'r', encoding='utf-8', errors='ignore') as doc:
            soup = BeautifulSoup(doc, 'xml')
        for obj in soup.findAll('object'):
            for name in obj.findAll(name='name'):
                if name.contents[0] in 'bar':
                    name.contents[0].replaceWith('bar')
                else:
                    name.contents[0].replaceWith('xy')
        with open(os.path.join(output_dir, filename), 'w') as doc:
            doc.write(str(soup))


if __name__ == '__main__':
    main()

