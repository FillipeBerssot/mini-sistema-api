from crud_api.src.requisicoes_api import (
    requisicao_delete,
    requisicao_get,
    requisicao_post,
    requisicao_put,
)


def listar_albuns():
    return requisicao_get('albums')


def obter_album(album_id):
    return requisicao_get(f'albums/{album_id}')


def criar_album(titulo, usuario_id):
    dados_album = {'title': titulo, 'userId': usuario_id}
    return requisicao_post('albums', dados_album)


def atualizar_album(album_id, titulo=None):
    dados_atualizados = {'title': titulo}
    return requisicao_put(f'albums/{album_id}', dados_atualizados)


def deletar_album(album_id):
    return requisicao_delete(f'albums/{album_id}')
