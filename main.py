import requests

API_KEY = 'trnsl.1.1.20191221T182928Z.89d057a013bb8893.5fff3656c5cd2767da844205795cdc1e917fb06c'\

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_file(name):
    with open(name, 'r' , encoding='utf-8') as f:
        content = f.read()

    params = {
        'key': API_KEY,
        'text': content,
        'lang': 'ru'
    }

    with open(name + '_tran.txt', 'w', encoding='utf-8') as file:
        response = requests.get(URL, params=params)
        json_ = response.json()
        # print(json_)
        text = (' '.join(json_['text']))
        # print(text)
        file.write(text)


# translate_file('Fr.txt')

def main():
    while True:
        name = input('Введите имя файла, который надо перевести:')
        if name == 'DE':
            translate_file('DE.txt')
        elif name == 'ES':
            translate_file('ES.txt')
        elif name == 'FR':
            translate_file('FR.txt')
        else:
            print('Неккоректный ввод, поторите')

main()