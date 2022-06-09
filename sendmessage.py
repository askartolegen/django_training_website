import requests

token = '5519780320:AAHPlw1mNbJ80NkmfxsZWkTsnvb4ut63--A'
chat_id = '-782885191'
text = 'test_number_2'


def send_telegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
    })

send_telegram()
