from crud_api.src.requisicoes_api import (
    requisicao_delete,
    requisicao_get,
    requisicao_post,
    requisicao_put,
)


def listar_posts():
    return requisicao_get('posts')


def obter_post(post_id):
    return requisicao_get(f'posts/{post_id}')


def criar_post(titulo, corpo, usuario_id):
    dados_post = {'title': titulo, 'body': corpo, 'userId': usuario_id}
    return requisicao_post('posts', dados_post)


def atualizar_post(post_id, titulo=None, corpo=None):
    dados_atualizados = {'title': titulo, 'body': corpo}
    resposta = requisicao_put(f'posts/{post_id}', dados_atualizados)

    if 'erro' in resposta:
        return f'Erro ao atualizar post: {resposta['erro']}'
    return resposta


def deletar_post(post_id):
    resposta = requisicao_delete(f'posts/{post_id}')

    if isinstance(resposta, dict) and 'erro' in resposta:
        return f'Erro ao deletar post: {resposta['erro']}'
    return resposta
