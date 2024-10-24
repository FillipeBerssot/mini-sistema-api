from crud_api.src.requisicoes_api import RequisicoesAPI


class ServicoUsers:
    @staticmethod
    def listar_users():
        return RequisicoesAPI.requisicao_get('users')

    @staticmethod
    def obter_user(user_id):
        return RequisicoesAPI.requisicao_get(f'users/{user_id}')

    @staticmethod
    def criar_user(nome, username, email):
        dados_user = {'name': nome, 'username': username, 'email': email}
        return RequisicoesAPI.requisicao_post('users', dados_user)

    @staticmethod
    def atualizar_user(user_id, nome=None, username=None, email=None):
        dados_atualizados = {
            'name': nome,
            'username': username,
            'email': email,
        }
        return RequisicoesAPI.requisicao_put(
            f'users/{user_id}', dados_atualizados
        )

    @staticmethod
    def deletar_user(user_id):
        return RequisicoesAPI.requisicao_delete(f'users/{user_id}')
