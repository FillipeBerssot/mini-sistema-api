from crud_api.src.servico_albuns import (
    atualizar_album,
    criar_album,
    deletar_album,
    listar_albuns,
    obter_album,
)
from crud_api.src.servico_comments import (
    atualizar_comment,
    criar_comment,
    deletar_comment,
    listar_comments,
    obter_comment,
)
from crud_api.src.servico_photos import (
    atualizar_photo,
    criar_photo,
    deletar_photo,
    listar_photos,
    obter_photo,
)
from crud_api.src.servico_post import (
    atualizar_post,
    criar_post,
    deletar_post,
    listar_posts,
    obter_post,
)
from crud_api.src.servico_todos import (
    atualizar_todo,
    criar_todo,
    deletar_todo,
    listar_todos,
    obter_todo,
)
from crud_api.src.servico_users import (
    atualizar_user,
    criar_user,
    deletar_user,
    listar_users,
    obter_user,
)


def exibir_menu_principal():
    print('\n========================')
    print('     SISTEMA CRUD')
    print('========================')
    print('1. 📄 Gerenciar Posts')
    print('2. 💬 Gerenciar Comments')
    print('3. 📓 Gerenciar Álbuns')
    print('4. 📸 Gerenciar Photos')
    print('5. 📝 Gerenciar Todos')
    print('6. 🙋 Gerenciar Users')
    print('7. ❌ Finalizar o sistema')
    print('========================\n')


def exibir_menu_posts():
    print('\n========================')
    print('     Gerenciar Posts')
    print('========================')
    print('1. 📄 Listar todos os posts')
    print('2. 🔍 Visualizar um post')
    print('3. ➕ Criar um novo post')
    print('4. ✏️ Atualizar um post existente')
    print('5. 🗑️ Deletar um post')
    print('6. 🔙 Voltar ao menu inicial')
    print('========================\n')


def exibir_menu_comments():
    print('\n========================')
    print('     Gerenciar Comments')
    print('========================')
    print('1. 💬 Listar todos os comments')
    print('2. 🔍 Visualizar um comment')
    print('3. ➕ Criar um novo comment')
    print('4. ✏️ Atualizar um comment existente')
    print('5. 🗑️ Deletar um comment')
    print('6. 🔙 Voltar ao menu inicial')
    print('========================\n')


def exibir_menu_albuns():
    print('\n========================')
    print('     Gerenciar Álbuns')
    print('========================')
    print('1. 📓 Listar todos os álbuns')
    print('2. 🔍 Visualizar um álbum')
    print('3. ➕ Criar um novo álbum')
    print('4. ✏️ Atualizar um álbum existente')
    print('5. 🗑️ Deletar um álbum')
    print('6. 🔙 Voltar ao menu inicial')
    print('========================\n')


def exibir_menu_photos():
    print('\n========================')
    print('     Gerenciar Photos')
    print('========================')
    print('1. 📸 Listar todas as photos')
    print('2. 🔍 Visualizar uma photo')
    print('3. ➕ Criar uma nova photo')
    print('4. ✏️ Atualizar uma photo existente')
    print('5. 🗑️ Deletar uma photo')
    print('6. 🔙 Voltar ao menu inicial')
    print('========================\n')


def exibir_menu_todos():
    print('\n========================')
    print('     Gerenciar Todos')
    print('========================')
    print('1. 📝 Listar todas os todos')
    print('2. 🔍 Visualizar um todo')
    print('3. ➕ Criar um novo todo')
    print('4. ✏️ Atualizar um todo existente')
    print('5. 🗑️ Deletar um todo')
    print('6. 🔙 Voltar ao menu inicial')
    print('========================\n')


def exibir_menu_users():
    print('\n========================')
    print('     Gerenciar Users')
    print('========================')
    print('1. 🙋 Listar todos os users')
    print('2. 🔍 Visualizar um user')
    print('3. ➕ Criar um novo user')
    print('4. ✏️ Atualizar um user existente')
    print('5. 🗑️ Deletar um user')
    print('6. 🔙 Voltar ao menu inicial')
    print('========================\n')


def executar():
    while True:
        exibir_menu_principal()
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            while True:
                exibir_menu_posts()
                opcao_post = input('Escolha uma opção de Posts: ')
                if opcao_post == '1':
                    posts = listar_posts()
                    if isinstance(posts, list):
                        for post in posts:
                            if 'id' in post and 'title' in post:
                                print(
                                    f'ID: {post['id']} | Título: {post['title']}'
                                )
                            else:
                                print('Post incompleto ou inválido.')

                    else:
                        print('Erro ao listar posts.')

                elif opcao_post == '2':
                    post_id = input('Digite o ID do post: ')
                    post = obter_post(post_id)
                    if 'id' in post and 'title' in post and 'body' in post:
                        print(
                            f"ID: {post['id']}\nTítulo: {post['title']}\nCorpo: {post['body']}"
                        )
                    else:
                        print(
                            '❌ Erro: Post não encontrado ou dados incompletos.'
                        )

                elif opcao_post == '3':
                    titulo = input('Digite o título do post: ')
                    corpo = input('Digite o corpo do post: ')
                    usuario_id = input('Digite o UserID do usuário: ')
                    novo_post = criar_post(titulo, corpo, usuario_id)
                    if 'erro' in novo_post:
                        print(f"\n❌ Erro ao criar post: {novo_post['erro']}")
                    else:
                        print(f'\n✅ Post criado com sucesso! ID: {novo_post}')

                elif opcao_post == '4':
                    post_id = input('Digite o ID do post: ')
                    post = obter_post(post_id)
                    if 'id' in post:
                        titulo = input(
                            'Digite o novo título (ou deixe em branco): '
                        )
                        corpo = input(
                            'Digite o novo corpo (ou deixe em branco): '
                        )
                        post_atualizado = atualizar_post(
                            post_id, titulo, corpo
                        )
                        if 'erro' in post_atualizado:
                            print(
                                f"\n❌ Erro ao atualizar post: {post_atualizado['erro']}"
                            )
                        else:
                            print(
                                f"\n✅ Post atualizado com sucesso! ID: {post_atualizado['id']}"
                            )
                    else:
                        print(
                            f'\n❌ Erro: Post com ID {post_id} não encontrado.'
                        )

                elif opcao_post == '5':
                    post_id = input('Digite o ID do post a ser deletado: ')
                    post = obter_post(post_id)
                    if 'id' in post:
                        mensagem = deletar_post(post_id)
                        if isinstance(mensagem, int) and mensagem == 200:
                            print(
                                f'\n🗑️ Post deletado com sucesso! ID: {post_id}'
                            )
                        else:
                            print(f'\n❌ Erro ao deletar post: {mensagem}')
                    else:
                        print(
                            f'\n❌ Erro: Post com ID {post_id} não encontrado.'
                        )

                elif opcao_post == '6':
                    break

                else:
                    print('\n⚠️ Opção inválida. Tente novamente.')

        elif opcao == '2':
            while True:
                exibir_menu_comments()
                opcao_comment = input('Escolha uma opção de Comments: ')

                if opcao_comment == '1':
                    comments = listar_comments()
                    if isinstance(comments, list):
                        for comment in comments:
                            if 'id' in comment and 'name' in comment:
                                print(
                                    f"ID: {comment['id']} | Nome: {comment['name']}"
                                )
                            else:
                                print('Comment incompleto ou inválido.')
                    else:
                        print('Erro ao listar comments.')

                elif opcao_comment == '2':
                    comment_id = input('Digite o ID do comment: ')
                    comment = obter_comment(comment_id)
                    if (
                        'id' in comment
                        and 'name' in comment
                        and 'body' in comment
                    ):
                        print(
                            f"ID: {comment['id']}\nNome: {comment['name']}\nCorpo: {comment['body']}"
                        )
                    else:
                        print(
                            f'\n❌ Erro: Comment com ID {comment_id} não encontrado ou dados incompletos.'
                        )

                elif opcao_comment == '3':
                    post_id = input('Digite o PostID do post: ')
                    nome = input('Digite o nome do comment: ')
                    email = input('Digite o email do comment: ')
                    corpo = input('Digite o corpo do comment: ')
                    novo_comment = criar_comment(post_id, nome, email, corpo)
                    print(f'\n✅ Comment criado: {novo_comment}')

                elif opcao_comment == '4':
                    comment_id = input('Digite o ID do comment: ')
                    comment = obter_comment(comment_id)
                    if (
                        'id' in comment
                        and 'name' in comment
                        and 'email' in comment
                        and 'body' in comment
                    ):
                        nome = input(
                            'Digite o novo nome (ou deixe em branco): '
                        )
                        email = input(
                            'Digite o novo email (ou deixe em branco): '
                        )
                        corpo = input(
                            'Digite o novo corpo (ou deixe em branco): '
                        )
                        comment_atualizado = atualizar_comment(
                            comment_id, nome, email, corpo
                        )
                        print(f'\n✅ Comment atualizado: {comment_atualizado}')
                    else:
                        print(
                            f'\n❌ Erro: Comment com ID {comment_id} não encontrado ou dados incompletos.'
                        )

                elif opcao_comment == '5':
                    comment_id = input(
                        'Digite o ID do comment a ser deletado: '
                    )
                    comment = obter_comment(comment_id)
                    if 'id' in comment:
                        mensagem = deletar_comment(comment_id)
                        if isinstance(mensagem, int) and mensagem == 200:
                            print(
                                f'\n🗑️ Comment deletado com sucesso! ID: {comment_id}'
                            )
                        else:
                            print(f'\n❌ Erro ao deletar comment: {mensagem}')
                    else:
                        print(
                            f'\n❌ Erro: Comment com ID {comment_id} não encontrado.'
                        )

                elif opcao_comment == '6':
                    break

                else:
                    print('\n⚠️ Opção inválida. Tente novamente.')

        elif opcao == '3':
            while True:
                exibir_menu_albuns()
                opcao_album = input('Escolha um opção de Álbuns: ')

                if opcao_album == '1':
                    albuns = listar_albuns()
                    if isinstance(albuns, list):
                        for album in albuns:
                            if 'id' in album and 'title' in album:
                                print(
                                    f'ID: {album['id']} | Título: {album['title']}'
                                )
                            else:
                                print('Álbum incompleto ou inválido.')
                    else:
                        print('Erro ao listar álbuns.')

                elif opcao_album == '2':
                    album_id = input('Digite o ID do álbum: ')
                    album = obter_album(album_id)
                    if 'id' in album and 'title' in album:
                        print(f'ID: {album['id']}\nTítulo: {album['title']}')
                    else:
                        print(
                            '❌ Erro: Álbum não encontrado ou dados incompletos.'
                        )

                elif opcao_album == '3':
                    titulo = input('Digite o título do álbum: ')
                    usuario_id = input('Digite o UserID do usuário: ')
                    novo_album = criar_album(titulo, usuario_id)
                    if 'erro' in novo_album:
                        print(
                            f"\n❌ Erro ao criar álbum: {novo_album['erro']}"
                        )
                    else:
                        print(
                            f'\n✅ Álbum criado com sucesso! ID: {novo_album["id"]}'
                        )

                elif opcao_album == '4':
                    album_id = input('Digite o ID do álbum: ')
                    album = obter_album(album_id)
                    if 'id' in album:
                        titulo = input(
                            'Digite o novo título (ou deixe em branco): '
                        )
                        album_atualizado = atualizar_album(album_id, titulo)
                        if 'erro' in album_atualizado:
                            print(
                                f"\n❌ Erro ao atualizar álbum: {album_atualizado['erro']}"
                            )
                        else:
                            print(
                                f"\n✅ Álbum atualizado com sucesso! ID: {album_atualizado['id']}"
                            )
                    else:
                        print(
                            f'\n❌ Erro: Álbum com ID {album_id} não encontrado.'
                        )

                elif opcao_album == '5':
                    album_id = input('Digite o ID do álbum a ser deletado: ')
                    album = obter_album(album_id)
                    if 'id' in album:
                        mensagem = deletar_album(album_id)
                        if isinstance(mensagem, int) and mensagem == 200:
                            print(
                                f'\n🗑️ Álbum deletado com sucesso! ID: {album_id}'
                            )
                        else:
                            print(f'\n❌ Erro ao deletar álbum: {mensagem}')
                    else:
                        print(
                            f'\n❌ Erro: Álbum com ID {album_id} não encontrado.'
                        )

                elif opcao_album == '6':
                    break

                else:
                    print('\n⚠️ Opção inválida. Tente novamente.')

        elif opcao == '4':
            while True:
                exibir_menu_photos()
                opcao_photo = input('Escolha uma opção de Photos: ')

                if opcao_photo == '1':
                    photos = listar_photos()
                    if isinstance(photos, list):
                        for photo in photos:
                            if 'id' in photo and 'title' in photo:
                                print(
                                    f'ID: {photo['id']} | Título: {photo['title']} | URL: {photo['url']}'
                                )
                            else:
                                print('Foto incompleta ou inválida.')
                    else:
                        print('Erro ao listar photos.')

                elif opcao_photo == '2':
                    photo_id = input('Digite o ID da photo: ')
                    photo = obter_photo(photo_id)
                    if (
                        'id' in photo
                        and 'title' in photo
                        and 'url' in photo
                        and 'thumbnailUrl' in photo
                    ):
                        print(
                            f'ID: {photo['id']}\nTítulo: {photo['title']}\nURL: {photo['url']}\nThumbnail Url: {photo['thumbnailUrl']}'
                        )
                    else:
                        print(
                            '❌ Erro: Foto não encontrada ou dados incompletos.'
                        )

                elif opcao_photo == '3':
                    album_id = input('Digite o AlbumID da photo: ')
                    titulo = input('Digite o título da photo: ')
                    url = input('Digite a url da photo: ')
                    thumbnail_url = input('Digite o Thumbnail URL da photo: ')
                    nova_photo = criar_photo(
                        album_id, titulo, url, thumbnail_url
                    )
                    if 'erro' in nova_photo:
                        print(f"\n❌ Erro ao criar foto: {nova_photo['erro']}")
                    else:
                        print(
                            f'\n✅ Foto criada com sucesso! ID: {nova_photo["id"]}'
                        )

                elif opcao_photo == '4':
                    photo_id = input('Digite o ID da photo: ')
                    photo = obter_photo(photo_id)
                    if 'id' in photo:
                        titulo = input(
                            'Digite o novo título (ou deixe em branco): '
                        )
                        url = input('Digite o novo URL (ou deixe em branco): ')
                        thumbnail_url = input(
                            'Digite o novo Thumbnail URL (ou deixe em branco): '
                        )
                        photo_atualizada = atualizar_photo(
                            photo_id, titulo, url, thumbnail_url
                        )
                        if 'erro' in photo_atualizada:
                            print(
                                f"\n❌ Erro ao atualizar foto: {photo_atualizada['erro']}"
                            )
                        else:
                            print(
                                f"\n✅ Foto atualizada com sucesso! ID: {photo_atualizada['id']}"
                            )
                    else:
                        print(
                            f'\n❌ Erro: Foto com ID {photo_id} não encontrada.'
                        )

                elif opcao_photo == '5':
                    photo_id = input('Digite o ID da photo a ser deletada: ')
                    photo = obter_photo(photo_id)
                    if 'id' in photo:
                        mensagem = deletar_photo(photo_id)
                        if isinstance(mensagem, int) and mensagem == 200:
                            print(
                                f'\n🗑️ Foto deletada com sucesso! ID: {photo_id}'
                            )
                        else:
                            print(f'\n❌ Erro ao deletar foto: {mensagem}')
                    else:
                        print(
                            f'\n❌ Erro: Foto com ID {photo_id} não encontrada.'
                        )

                elif opcao_photo == '6':
                    break

                else:
                    print('\n⚠️ Opção inválida. Tente novamente.')

        elif opcao == '5':
            while True:
                exibir_menu_todos()
                opcao_todo = input('Escolha uma opção de Todos: ')

                if opcao_todo == '1':
                    todos = listar_todos()
                    if isinstance(todos, list):
                        for todo in todos:
                            if 'id' in todo and 'title' in todo:
                                status = (
                                    '✔️ Completo'
                                    if todo['completed']
                                    else '❌ Incompleto'
                                )
                                print(
                                    f"ID: {todo['id']} | Título: {todo['title']} | Status: {status}"
                                )
                            else:
                                print('Tarefa incompleta ou inválida.')
                    else:
                        print('Erro ao listar tarefas.')

                elif opcao_todo == '2':
                    todo_id = input('Digite o ID do todo: ')
                    todo = obter_todo(todo_id)
                    if (
                        'id' in todo
                        and 'title' in todo
                        and 'completed' in todo
                    ):
                        status = (
                            '✔️ Completo'
                            if todo['completed']
                            else '❌ Incompleto'
                        )
                        print(
                            f"ID: {todo['id']}\nTítulo: {todo['title']}\nStatus: {status}"
                        )
                    else:
                        print(
                            '❌ Erro: Tarefa não encontrada ou dados incompletos.'
                        )

                elif opcao_todo == '3':
                    usuario_id = input('Digite o UserID do usuário: ')
                    titulo = input('Digite o título do todo: ')
                    completo = (
                        input('O todo está completo? (Sim/Não): ').lower()
                        == 'sim'
                    )
                    novo_todo = criar_todo(usuario_id, titulo, completo)
                    if 'erro' in novo_todo:
                        print(
                            f"\n❌ Erro ao criar tarefa: {novo_todo['erro']}"
                        )
                    else:
                        print(
                            f'\n✅ Tarefa criada com sucesso! ID: {novo_todo["id"]}'
                        )

                elif opcao_todo == '4':
                    todo_id = input('Digite o ID do todo: ')
                    todo = obter_todo(todo_id)
                    if 'id' in todo:
                        titulo = input(
                            'Digite o novo título (ou deixe em branco): '
                        )
                        completo = (
                            input('O todo está completo? (Sim/Não): ').lower()
                            == 'sim'
                        )
                        todo_atualizado = atualizar_todo(
                            todo_id, titulo, completo
                        )
                        if 'erro' in todo_atualizado:
                            print(
                                f"\n❌ Erro ao atualizar tarefa: {todo_atualizado['erro']}"
                            )
                        else:
                            print(
                                f"\n✅ Tarefa atualizada com sucesso! ID: {todo_atualizado['id']}"
                            )
                    else:
                        print(
                            f'\n❌ Erro: Tarefa com ID {todo_id} não encontrada.'
                        )

                elif opcao_todo == '5':
                    todo_id = input('Digite o ID do todo a ser deletado: ')
                    todo = obter_todo(todo_id)
                    if 'id' in todo:
                        mensagem = deletar_todo(todo_id)
                        if isinstance(mensagem, int) and mensagem == 200:
                            print(
                                f'\n🗑️ Tarefa deletada com sucesso! ID: {todo_id}'
                            )
                        else:
                            print(f'\n❌ Erro ao deletar tarefa: {mensagem}')
                    else:
                        print(
                            f'\n❌ Erro: Tarefa com ID {todo_id} não encontrada.'
                        )

                elif opcao_todo == '6':
                    break

                else:
                    print('\n⚠️ Opção inválida. Tente novamente.')

        elif opcao == '6':
            while True:
                exibir_menu_users()
                opcao_user = input('Escolha sua opção de Users: ')

                if opcao_user == '1':
                    users = listar_users()
                    if isinstance(users, list):
                        for user in users:
                            if 'id' in user and 'name' in user:
                                print(
                                    f'ID: {user['id']} | Nome: {user['name']} | Username: {user['username']} | Email: {user['email']}'
                                )
                            else:
                                print('Usuário incompleto ou inválido.')

                    else:
                        print('Erro ao listar users.')

                elif opcao_user == '2':
                    user_id = input('Digite o ID do user: ')
                    user = obter_user(user_id)
                    if (
                        'id' in user
                        and 'name' in user
                        and 'username' in user
                        and 'email' in user
                    ):
                        print(
                            f"ID: {user['id']}\nNome: {user['name']}\nUsername: {user['username']}\nEmail: {user['email']}"
                        )
                    else:
                        print(
                            '❌ Erro: Usuário não encontrado ou dados incompletos.'
                        )

                elif opcao_user == '3':
                    nome = input('Digite o nome do user: ')
                    username = input('Digite o username do user: ')
                    email = input('Digite o email do user: ')
                    novo_user = criar_user(nome, username, email)
                    if 'erro' in novo_user:
                        print(
                            f"\n❌ Erro ao criar usuário: {novo_user['erro']}"
                        )
                    else:
                        print(
                            f'\n✅ Usuário criado com sucesso! ID: {novo_user["id"]}'
                        )

                elif opcao_user == '4':
                    user_id = input('Digite o ID do user: ')
                    user = obter_user(user_id)
                    if 'id' in user:
                        nome = input(
                            'Digite o novo nome (ou deixe em branco): '
                        )
                        username = input(
                            'Digite o novo username (ou deixe em branco): '
                        )
                        email = input(
                            'Digite o novo email (ou deixe em branco): '
                        )
                        user_atualizado = atualizar_user(
                            user_id, nome, username, email
                        )
                        if 'erro' in user_atualizado:
                            print(
                                f"\n❌ Erro ao atualizar usuário: {user_atualizado['erro']}"
                            )
                        else:
                            print(
                                f"\n✅ Usuário atualizado com sucesso! ID: {user_atualizado['id']}"
                            )
                    else:
                        print(
                            f'\n❌ Erro: Usuário com ID {user_id} não encontrado.'
                        )

                elif opcao_user == '5':
                    user_id = input('Digite o ID do user a ser deletado: ')
                    user = obter_user(user_id)
                    if 'id' in user:
                        mensagem = deletar_user(user_id)
                        if isinstance(mensagem, int) and mensagem == 200:
                            print(
                                f'\n🗑️ Usuário deletado com sucesso! ID: {user_id}'
                            )
                        else:
                            print(f'\n❌ Erro ao deletar usuário: {mensagem}')
                    else:
                        print(
                            f'\n❌ Erro: Usuário com ID {user_id} não encontrado.'
                        )

                elif opcao_user == '6':
                    break

                else:
                    print('\n⚠️ Opção inválida. Tente novamente.')

        elif opcao == '7':
            print(
                '\nSaindo... Obrigado por utilizar nosso sistema e até mais!'
            )
            break

        else:
            print('\n⚠️ Opção inválida. Tente novamente.')


if __name__ == '__main__':
    executar()
