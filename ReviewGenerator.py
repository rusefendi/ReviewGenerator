import requests
from bs4 import BeautifulSoup
import random

url_raw = 'https://market.yandex.ru/product/14271793/spec'
reviews_count = 3
text_path = "reviews.txt"
reviews = open(text_path, 'r').read()
many_reviews = reviews.split('\n')
first_type_splitting_items = {'CPU': [], 'GPU': [], 'storage_type': [], 'screen_resolution': []}
second_type_splitting_items = {'RAM': [], 'hard_drive_capacity': []}


def get_html(url):
    r = requests.get(url)
    return r.text


def get_specifications(html):
    names = {'CPU': 'Процессор', 'GPU': 'Видеокарта', 'RAM': 'Объем оперативной памяти (точно)',
             'storage_type': 'Тип жесткого диска', 'hard_drive_capacity': 'Объем жесткого диска',
             'screen_resolution': 'Разрешение экрана'}
    soup = BeautifulSoup(html, 'lxml')

    for key in first_type_splitting_items:
        first_type_splitting_items[key] = soup.find('span', text=names[key]).parent.parent.find_all()[-1].text.rstrip().split(' / ')

    for key in second_type_splitting_items:
        second_type_splitting_items[key] = soup.find('span', text=names[key]).parent.parent.find_all()[-1].text.rstrip().split('...')
        second_type_splitting_items[key][0] += ' Гб'


def print_reviews(n):
    for i in range(0, n):
        print(random.choice(many_reviews).format(CPU=random.choice(first_type_splitting_items["CPU"]), GPU=random.choice(first_type_splitting_items["GPU"]),
                                                 RAM=random.choice(second_type_splitting_items["RAM"]),
                                                 storage_type=random.choice(first_type_splitting_items["storage_type"]),
                                                 hard_drive_capacity=random.choice(second_type_splitting_items["hard_drive_capacity"]),
                                                 screen_resolution=random.choice(first_type_splitting_items["screen_resolution"])))


def main():
    html = get_html(url_raw)
    get_specifications(html)
    print_reviews(reviews_count)


if __name__ == '__main__':
    main()
