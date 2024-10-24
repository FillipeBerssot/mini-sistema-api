from crud_api.src.requisicoes_api import RequisicoesAPI


class ServicoComments:
    @staticmethod
    def listar_comments():
        return RequisicoesAPI.requisicao_get('comments')

    @staticmethod
    def obter_comment(comment_id):
        return RequisicoesAPI.requisicao_get(f'comments/{comment_id}')

    @staticmethod
    def criar_comment(post_id, nome, email, corpo):
        dados_comment = {
            'postId': post_id,
            'name': nome,
            'email': email,
            'body': corpo,
        }
        return RequisicoesAPI.requisicao_post('comments', dados_comment)

    @staticmethod
    def atualizar_comment(comment_id, nome=None, email=None, corpo=None):
        dados_atualizados = {'name': nome, 'email': email, 'body': corpo}
        return RequisicoesAPI.requisicao_put(
            f'comments/{comment_id}', dados_atualizados
        )

    @staticmethod
    def deletar_comment(comment_id):
        return RequisicoesAPI.requisicao_delete(f'comments/{comment_id}')
