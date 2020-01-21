import requests

import os


API_KEY = 'trnsl.1.1.20191221T182928Z.89d057a013bb8893.5fff3656c5cd2767da844205795cdc1e917fb06c'\

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_file(file_name, final_name, from_lang, to_lang ='ru'):
    # name_of_file = os.path.join(input('Введите имя файла'))
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    # from_lang = input('C какого языка вы хотите перевести?:')

    params = {
        'key': API_KEY,
        'text': content,
        'lang': f'{from_lang}-{to_lang}'
    }

    # final_name = os.path.join(input('Введите название переведенного файла:'))

    with open(final_name, 'w', encoding='utf-8') as file:
        response = requests.get(URL, params=params)
        json_ = response.json()
        # print(json_)
        text = (' '.join(json_['text']))
        # print(text)
        file.write(text)


# translate_file('Fr.txt')

def main():
    while True:
        name = os.path.join(input('Введите имя файла, который надо перевести:'))
        if name == os.path.join('DE.txt'):
            translate_file('DE.txt','DE_tran.txt','de')
        elif name == os.path.join('ES.txt'):
            translate_file('ES.txt','ES_tran.txt','de')
        elif name == os.path.join('FR.txt'):
            translate_file('FR.txt','FR_tran.txt','de')
        else:
            print('Неккоректный ввод, поторите')
        print('Конец программы')
        break
main()