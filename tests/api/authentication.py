import requests
import os

BASE_URL = os.getenv("BASE_URL") or 'https://api.github.com'
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME") or 'patrickromo1'
TOKEN = os.getenv("GITHUB_TOKEN")


def get(URI):
    response = requests.get(BASE_URL + URI,
                            auth=(GITHUB_USERNAME, TOKEN))
    return dict([
        ('body', response.json()),
        ('status_code', response.status_code)
    ])


def get_with_custom_headers(URI, headers):
    response = requests.get(BASE_URL + URI,
                            auth=(GITHUB_USERNAME, TOKEN), headers=headers)
    return dict([
        ('body', response.json()),
        ('status_code', response.status_code)
    ])


def post_with_custom_headers(URI, headers, payload):
    response = requests.post(BASE_URL + URI,
                             auth=(GITHUB_USERNAME, TOKEN), headers=headers, json=payload)
    return dict([
        ('body', response.json()),
        ('status_code', response.status_code)
    ])


def delete_with_custom_header(URI, headers):
    response = requests.delete(BASE_URL + URI,
                               auth=(GITHUB_USERNAME, TOKEN), headers=headers)
    return dict([
        ('status_code', response.status_code)
    ])
