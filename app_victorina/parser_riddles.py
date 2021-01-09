import requests
from bs4 import BeautifulSoup
import csv

list_diсt_riddles = []


def run():
    global list_diсt_riddles
    for i in range(1, 172):  # (1, 172)
        diсt_riddles = {}
        url = f'https://zagadki.info/detyam/page-{i}.html'

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        content = soup.findAll('div', class_="cont_text")

        for ind, str in enumerate(content):
            tmp = str.text.split()
            if len(tmp) < 2:
                continue
            if 'Загадка' in tmp:
                tmp_join = ' '.join(tmp[4:])
                diсt_riddles[tmp_join] = None
                s = tmp_join
            else:
                tmp2 = ' '.join(tmp[1:])
                diсt_riddles[s] = tmp2

        for k, v in diсt_riddles.items():
            list_diсt_riddles.append({'riddles': k, 'response': v})
            print(k, v)

        print(f'===================>>>___{i}___<<<===================')


def writer_to_csv(dict_riddles):
    with open('list_riddles.csv', "w", newline="", encoding="utf-8") as file:
        columns = ["riddles", "response"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writerows(dict_riddles)


if __name__ == '__main__':
    run()
    writer_to_csv(list_diсt_riddles)
    print(list_diсt_riddles)
