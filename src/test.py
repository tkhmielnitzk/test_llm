import json
import requests

if __name__ == '__main__':
    model = 'llama3'
    model = 'description_immo'
    url = 'http://localhost:11435/api/generate'
    headers = {'Content-Type': 'application/json'}
    data = {
        'model': model,
        'prompt': 'Appartement T3 de 60m² avec une terrasse de 20m² au 3e étage et ta mère à 4 pattes. third floor avec loyer de 900euros par mois.',
        'stream': False,
    }


    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data['response']
        print(actual_response)
    else:
        print('Error: ', response.status_code, response.text)