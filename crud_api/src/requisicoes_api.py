import requests

from crud_api.configuracoes import URL_BASE


def requisicao_get(endpoint):
    resposta = requests.get(f'{URL_BASE}/{endpoint}')
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return {'erro': f'Falha na requisição GET: {resposta.status_code}'}


def requisicao_post(endpoint, dados):
    resposta = requests.post(f'{URL_BASE}/{endpoint}', json=dados)
    if resposta.status_code == 201:
        return resposta.json()
    else:
        return {'erro': f'Falha na requisição POST: {resposta.status_code}'}


def requisicao_put(endpoint, dados):
    resposta = requests.put(f'{URL_BASE}/{endpoint}', json=dados)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return {'erro': f'Falha na requisição PUT: {resposta.status_code}'}


def requisicao_delete(endpoint):
    resposta = requests.delete(f'{URL_BASE}/{endpoint}')
    if resposta.status_code == 200:
        return resposta.status_code
    else:
        return {'erro': f'Falha na requisição DELETE: {resposta.status_code}'}
