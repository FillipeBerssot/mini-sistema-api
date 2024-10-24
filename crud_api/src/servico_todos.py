from crud_api.src.requisicoes_api import (
    requisicao_delete,
    requisicao_get,
    requisicao_post,
    requisicao_put,
)


def listar_todos():
    return requisicao_get('todos')


def obter_todo(todo_id):
    return requisicao_get(f'todos/{todo_id}')


def criar_todo(titulo, usuario_id, completed=False):
    dados_todo = {
        'title': titulo,
        'userId': usuario_id,
        'completed': completed,
    }
    return requisicao_post('todos', dados_todo)


def atualizar_todo(todo_id, titulo=None, completed=None):
    dados_atualizados = {'title': titulo, 'completed': completed}
    return requisicao_put(f'todos/{todo_id}', dados_atualizados)


def deletar_todo(todo_id):
    return requisicao_delete(f'todos/{todo_id}')
