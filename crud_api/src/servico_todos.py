from crud_api.src.requisicoes_api import RequisicoesAPI


class ServicoTodos:
    @staticmethod
    def listar_todos():
        return RequisicoesAPI.requisicao_get('todos')

    @staticmethod
    def obter_todo(todo_id):
        return RequisicoesAPI.requisicao_get(f'todos/{todo_id}')

    @staticmethod
    def criar_todo(titulo, usuario_id, completed=False):
        dados_todo = {
            'title': titulo,
            'userId': usuario_id,
            'completed': completed,
        }
        return RequisicoesAPI.requisicao_post('todos', dados_todo)

    @staticmethod
    def atualizar_todo(todo_id, titulo=None, completed=None):
        dados_atualizados = {'title': titulo, 'completed': completed}
        return RequisicoesAPI.requisicao_put(
            f'todos/{todo_id}', dados_atualizados
        )

    @staticmethod
    def deletar_todo(todo_id):
        return RequisicoesAPI.requisicao_delete(f'todos/{todo_id}')
