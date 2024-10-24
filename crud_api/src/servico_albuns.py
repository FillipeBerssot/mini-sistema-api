from crud_api.src.requisicoes_api import RequisicoesAPI


class ServicoAlbuns:
    @staticmethod
    def listar_albuns():
        return RequisicoesAPI.requisicao_get('albums')

    @staticmethod
    def obter_album(album_id):
        return RequisicoesAPI.requisicao_get(f'albums/{album_id}')

    @staticmethod
    def criar_album(titulo, usuario_id):
        dados_album = {'title': titulo, 'userId': usuario_id}
        return RequisicoesAPI.requisicao_post('albums', dados_album)

    @staticmethod
    def atualizar_album(album_id, titulo=None):
        dados_atualizados = {'title': titulo}
        return RequisicoesAPI.requisicao_put(
            f'albums/{album_id}', dados_atualizados
        )

    @staticmethod
    def deletar_album(album_id):
        return RequisicoesAPI.requisicao_delete(f'albums/{album_id}')
