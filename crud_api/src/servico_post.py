from crud_api.src.requisicoes_api import RequisicoesAPI


class ServicoPosts:
    @staticmethod
    def listar_posts():
        return RequisicoesAPI.requisicao_get('posts')

    @staticmethod
    def listar_post_por_usuario(user_id):
        return RequisicoesAPI.requisicao_get(f'posts?userId={user_id}')

    @staticmethod
    def obter_post(post_id):
        return RequisicoesAPI.requisicao_get(f'posts/{post_id}')

    @staticmethod
    def criar_post(titulo, corpo, usuario_id):
        dados_post = {'title': titulo, 'body': corpo, 'userId': usuario_id}
        return RequisicoesAPI.requisicao_post('posts', dados_post)

    @staticmethod
    def atualizar_post(post_id, titulo=None, corpo=None):
        dados_atualizados = {'title': titulo, 'body': corpo}
        resposta = RequisicoesAPI.requisicao_put(
            f'posts/{post_id}', dados_atualizados
        )

        if 'erro' in resposta:
            return f'Erro ao atualizar post: {resposta['erro']}'
        return resposta

    @staticmethod
    def deletar_post(post_id):
        resposta = RequisicoesAPI.requisicao_delete(f'posts/{post_id}')

        if isinstance(resposta, dict) and 'erro' in resposta:
            return f'Erro ao deletar post: {resposta['erro']}'
        return resposta
