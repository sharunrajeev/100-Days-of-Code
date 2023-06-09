import requests
from datetime import datetime

TOKEN = 'u2ry8EGwr9b0A4ud'
pixela_endpoint = 'https://pixe.la/v1/users'
GRAPH_ID = 'avenger'
headers = {
    'X-USER-TOKEN': TOKEN
}
USERNAME = 'hyphen'
date = f'{datetime.now().strftime("%Y%m%d")}'


def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": 'yes',
        "notMinor": 'yes'
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_params = {
        'id': GRAPH_ID,
        'name': 'Addict Free Day Graph',
        'unit': 'commit',
        'type': 'int',
        'color': 'shibafu',
    }
    res = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    print(res.text)


def post_pixel():
    post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
    post_pixel_params = {
        'date': date,
        'quantity': '1'
    }
    res = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
    print(res.text)


def update_pixel_data(quantity):
    update_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}'
    update_pixel_params = {
        'quantity': quantity
    }
    res = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
    print(res.text)


def delete_pixel(date_to_change):
    delete_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_change}'
    print(requests.delete(url=delete_pixel_endpoint, headers=headers).text)


delete_pixel(date)
