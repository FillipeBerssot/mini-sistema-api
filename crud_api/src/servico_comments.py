from crud_api.src.requisicoes_api import (
    requisicao_delete,
    requisicao_get,
    requisicao_post,
    requisicao_put,
)


def listar_comments():
    return requisicao_get('comments')


def obter_comment(comment_id):
    return requisicao_get(f'comments/{comment_id}')


def criar_comment(post_id, nome, email, corpo):
    dados_comment = {
        'postId': post_id,
        'name': nome,
        'email': email,
        'body': corpo,
    }
    return requisicao_post('comments', dados_comment)


def atualizar_comment(comment_id, nome=None, email=None, corpo=None):
    dados_atualizados = {'name': nome, 'email': email, 'body': corpo}
    return requisicao_put(f'comments/{comment_id}', dados_atualizados)


def deletar_comment(comment_id):
    return requisicao_delete(f'comments/{comment_id}')
