import os


def main():
    with open('./ImageSets/Main/test.txt', 'r') as f:
        lines = [l.strip('\n') for l in f.readlines()]
        for l in lines:
            if not os.path.isfile('./JPEGImages/{}.jpg'.format(l)):
                print('Notfound: {}.jpg'.format(l))
            if not os.path.isfile('./Annotations/{}.xml'.format(l)):
                print('Notfound: {}.xml'.format(l))


if __name__ == '__main__':
    main()
