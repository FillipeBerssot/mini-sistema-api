from crud_api.src.requisicoes_api import (
    requisicao_delete,
    requisicao_get,
    requisicao_post,
    requisicao_put,
)


def listar_photos():
    return requisicao_get('photos')


def obter_photo(photo_id):
    return requisicao_get(f'photos/{photo_id}')


def criar_photo(album_id, titulo, url, thumbnail_url):
    dados_photo = {
        'albumId': album_id,
        'title': titulo,
        'url': url,
        'thumbnailUrl': thumbnail_url,
    }
    return requisicao_post('photos', dados_photo)


def atualizar_photo(photo_id, titulo=None, url=None, thumbnail_url=None):
    dados_atualizados = {
        'title': titulo,
        'url': url,
        'thumbnailUrl': thumbnail_url,
    }
    return requisicao_put(f'photos/{photo_id}', dados_atualizados)


def deletar_photo(photo_id):
    return requisicao_delete(f'photos/{photo_id}')
