from crud_api.src.requisicoes_api import (
    requisicao_delete,
    requisicao_get,
    requisicao_post,
    requisicao_put,
)


def listar_users():
    return requisicao_get('users')


def obter_user(user_id):
    return requisicao_get(f'users/{user_id}')


def criar_user(nome, username, email):
    dados_user = {'name': nome, 'username': username, 'email': email}
    return requisicao_post('users', dados_user)


def atualizar_user(user_id, nome=None, username=None, email=None):
    dados_atualizados = {'name': nome, 'username': username, 'email': email}
    return requisicao_put(f'users/{user_id}', dados_atualizados)


def deletar_user(user_id):
    return requisicao_delete(f'users/{user_id}')
