from crud_api.src.requisicoes_api import RequisicoesAPI


class ServicoPhotos:
    @staticmethod
    def listar_photos():
        return RequisicoesAPI.requisicao_get('photos')

    @staticmethod
    def listar_photos_por_album(album_id):
        return RequisicoesAPI.requisicao_get(f'photos?albumId={album_id}')

    @staticmethod
    def obter_photo(photo_id):
        return RequisicoesAPI.requisicao_get(f'photos/{photo_id}')

    @staticmethod
    def criar_photo(album_id, titulo, url, thumbnail_url):
        dados_photo = {
            'albumId': album_id,
            'title': titulo,
            'url': url,
            'thumbnailUrl': thumbnail_url,
        }
        return RequisicoesAPI.requisicao_post('photos', dados_photo)

    @staticmethod
    def atualizar_photo(photo_id, titulo=None, url=None, thumbnail_url=None):
        dados_atualizados = {
            'title': titulo,
            'url': url,
            'thumbnailUrl': thumbnail_url,
        }
        return RequisicoesAPI.requisicao_put(
            f'photos/{photo_id}', dados_atualizados
        )

    @staticmethod
    def deletar_photo(photo_id):
        return RequisicoesAPI.requisicao_delete(f'photos/{photo_id}')
