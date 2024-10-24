import requests

from crud_api.configuracoes import ConfiguracoesAPI


class RequisicoesAPI:
    @staticmethod
    def requisicao_get(endpoint):
        url = f'{ConfiguracoesAPI.get_url_base()}/{endpoint}'
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return {'erro': f'Falha na requisição GET: {resposta.status_code}'}

    @staticmethod
    def requisicao_post(endpoint, dados):
        url = f'{ConfiguracoesAPI.get_url_base()}/{endpoint}'
        resposta = requests.post(url, json=dados)
        if resposta.status_code == 201:
            return resposta.json()
        else:
            return {
                'erro': f'Falha na requisição POST: {resposta.status_code}'
            }

    @staticmethod
    def requisicao_put(endpoint, dados):
        url = f'{ConfiguracoesAPI.get_url_base()}/{endpoint}'
        resposta = requests.put(url, json=dados)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return {'erro': f'Falha na requisição PUT: {resposta.status_code}'}

    @staticmethod
    def requisicao_delete(endpoint):
        url = f'{ConfiguracoesAPI.get_url_base()}/{endpoint}'
        resposta = requests.delete(url)
        if resposta.status_code == 200:
            return resposta.status_code
        else:
            return {
                'erro': f'Falha na requisição DELETE: {resposta.status_code}'
            }
