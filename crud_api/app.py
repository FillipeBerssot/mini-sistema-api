from crud_api.src.servico_albuns import ServicoAlbuns
from crud_api.src.servico_comments import ServicoComments
from crud_api.src.servico_photos import ServicoPhotos
from crud_api.src.servico_post import ServicoPosts
from crud_api.src.servico_todos import ServicoTodos
from crud_api.src.servico_users import ServicoUsers


class Menu:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def exibir_menu_todos():
        print('\n========================')
        print('     Gerenciar Todos')
        print('========================')
        print('1. 📝 Listar todos os todos')
        print('2. 🔍 Visualizar um todo')
        print('3. ➕ Criar um novo todo')
        print('4. ✏️ Atualizar um todo existente')
        print('5. 🗑️ Deletar um todo')
        print('6. 🔙 Voltar ao menu inicial')
        print('========================\n')

    @staticmethod
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


class GerenciadorDados:
    @staticmethod
    def listar(**kwargs):
        itens = kwargs.get('itens')
        nome_item = kwargs.get('nome_item')

        if itens is None or nome_item is None:
            print("Erro: Parâmetros 'itens' ou 'nome_item' não fornecidos.")
            return

        if isinstance(itens, list):
            for item in itens:
                if 'id' in item and 'title' in item:
                    print(f"ID: {item['id']} | Título: {item['title']}")
                elif 'name' in item:
                    print(f"ID: {item['id']} | Nome: {item['name']}")
                else:
                    print(f'{nome_item} incompleto ou inválido.')
        else:
            print(f'Erro ao listar {nome_item.casefold()}.')

    @staticmethod
    def visualizar(**kwargs):
        item = kwargs.get('item')
        nome_item = kwargs.get('nome_item')

        if item is None or nome_item is None:
            print("Erro: Parâmetros 'item' ou 'nome_item' não fornecidos.")
            return

        if item and 'id' in item:
            for chave, valor in item.items():
                print(f'{chave.capitalize()}: {valor}')
        else:
            print(f'❌ Erro: {nome_item} não encontrado ou dados incompletos.')

    @staticmethod
    def criar(**kwargs):
        novo_item = kwargs.get('novo_item')
        nome_item = kwargs.get('nome_item')

        if novo_item is None or nome_item is None:
            print(
                "Erro: Parâmetros 'novo_item' ou 'nome_item' não fornecidos."
            )
            return

        if 'erro' in novo_item:
            print(
                f"\n❌ Erro ao criar {nome_item.casefold()}: {novo_item['erro']}"
            )
        else:
            print(
                f'\n✅ {nome_item} criado com sucesso! ID: {novo_item["id"]}'
            )

    @staticmethod
    def atualizar(**kwargs):
        item_atualizado = kwargs.get('item_atualizado')
        nome_item = kwargs.get('nome_item')

        if item_atualizado is None or nome_item is None:
            print(
                "Erro: Parâmetros 'item_atualizado' ou 'nome_item' não fornecidos."
            )
            return

        if 'erro' in item_atualizado:
            print(
                f"\n❌ Erro ao atualizar {nome_item.casefold()}: {item_atualizado['erro']}"
            )
        else:
            print(
                f'\n✅ {nome_item} atualizado com sucesso! ID: {item_atualizado["id"]}'
            )

    @staticmethod
    def deletar(**kwargs):
        status = kwargs.get('status')
        item_id = kwargs.get('item_id')
        nome_item = kwargs.get('nome_item')

        if status is None or item_id is None or nome_item is None:
            print(
                "Erro: Parâmetros 'status', 'item_id' ou 'nome_item' não fornecidos."
            )
            return

        if isinstance(status, dict) and 'erro' in status:
            print(
                f'\n❌ Erro ao deletar {nome_item.casefold()}: {status['erro']}'
            )
        elif isinstance(status, int) and status == 404:
            print(f'\n❌ {nome_item} com ID {item_id} não encontrado.')
        elif isinstance(status, int) and status == 200:
            print(f'\n🗑️ {nome_item} deletado com sucesso! ID: {item_id}')
        else:
            print(f'\n❌ Erro ao deletar {nome_item.casefold()}: {status}')


class GerenciadorCRUD(GerenciadorDados):
    def gerenciar_posts(self):
        while True:
            Menu.exibir_menu_posts()
            opcao_post = input('Escolha uma opção de Posts: ')
            if opcao_post == '1':
                posts = ServicoPosts.listar_posts()
                self.listar(itens=posts, nome_item='Posts')
            elif opcao_post == '2':
                post_id = input('Digite o ID do post: ')
                post = ServicoPosts.obter_post(post_id)
                self.visualizar(item=post, nome_item='Post')
            elif opcao_post == '3':
                titulo = input('Digite o título do post: ')
                corpo = input('Digite o corpo do post: ')
                usuario_id = input('Digite o UserID do usuário: ')
                novo_post = ServicoPosts.criar_post(titulo, corpo, usuario_id)
                self.criar(novo_item=novo_post, nome_item='Post')
            elif opcao_post == '4':
                post_id = input('Digite o ID do post: ')
                post = ServicoPosts.obter_post(post_id)
                if 'id' in post:
                    titulo = input(
                        'Digite o novo título (ou deixe em branco): '
                    )
                    corpo = input('Digite o novo corpo (ou deixe em branco): ')
                    post_atualizado = ServicoPosts.atualizar_post(
                        post_id, titulo, corpo
                    )
                    self.atualizar(
                        item_atualizado=post_atualizado, nome_item='Post'
                    )
                else:
                    print(f'\n❌ Erro: Post com ID {post_id} não encontrado.')
            elif opcao_post == '5':
                post_id = input('Digite o ID do post a ser deletado: ')
                post = ServicoPosts.obter_post(post_id)

                if 'id' in post:
                    status = ServicoPosts.deletar_post(post_id)
                    self.deletar(
                        status=status, item_id=post_id, nome_item='Post'
                    )
                else:
                    print(f'\n❌ Erro: Post com ID {post_id} não encontrado.')
            elif opcao_post == '6':
                break
            else:
                print('\n⚠️ Opção inválida. Tente novamente.')

    def gerenciar_comments(self):
        while True:
            Menu.exibir_menu_comments()
            opcao_comment = input('Escolha uma opção de Comments: ')
            if opcao_comment == '1':
                comments = ServicoComments.listar_comments()
                self.listar(itens=comments, nome_item='Comments')
            elif opcao_comment == '2':
                comment_id = input('Digite o ID do comment: ')
                comment = ServicoComments.obter_comment(comment_id)
                self.visualizar(item=comment, nome_item='Comment')
            elif opcao_comment == '3':
                post_id = input('Digite o PostID do post: ')
                nome = input('Digite o nome do comment: ')
                email = input('Digite o email do comment: ')
                corpo = input('Digite o corpo do comment: ')
                novo_comment = ServicoComments.criar_comment(
                    post_id, nome, email, corpo
                )
                self.criar(novo_item=novo_comment, nome_item='Comment')
            elif opcao_comment == '4':
                comment_id = input('Digite o ID do comment: ')
                comment = ServicoComments.obter_comment(comment_id)
                if 'id' in comment:
                    nome = input('Digite o novo nome (ou deixe em branco): ')
                    email = input('Digite o novo email (ou deixe em branco): ')
                    corpo = input('Digite o novo corpo (ou deixe em branco): ')
                    comment_atualizado = ServicoComments.atualizar_comment(
                        comment_id, nome, email, corpo
                    )
                    self.atualizar(
                        item_atualizado=comment_atualizado, nome_item='Comment'
                    )
                else:
                    print(
                        f'\n❌ Erro: Comment com ID {comment_id} não encontrado.'
                    )
            elif opcao_comment == '5':
                comment_id = input('Digite o ID do comment a ser deletado: ')
                comment = ServicoComments.obter_comment(comment_id)
                if 'id' in comment:
                    status = ServicoComments.deletar_comment(comment_id)
                    self.deletar(
                        status=status, item_id=comment_id, nome_item='Comment'
                    )
                else:
                    print(
                        f'\n❌ Erro: Comment com ID {comment_id} não encontrado.'
                    )
            elif opcao_comment == '6':
                break
            else:
                print('\n⚠️ Opção inválida. Tente novamente.')

    def gerenciar_albuns(self):
        while True:
            Menu.exibir_menu_albuns()
            opcao_album = input('Escolha um opção de Álbuns: ')
            if opcao_album == '1':
                albuns = ServicoAlbuns.listar_albuns()
                self.listar(itens=albuns, nome_item='Álbums')
            elif opcao_album == '2':
                album_id = input('Digite o ID do álbum: ')
                album = ServicoAlbuns.obter_album(album_id)
                self.visualizar(item=album, nome_item='Álbum')
            elif opcao_album == '3':
                titulo = input('Digite o título do álbum: ')
                usuario_id = input('Digite o UserID do usuário: ')
                novo_album = ServicoAlbuns.criar_album(titulo, usuario_id)
                self.criar(novo_item=novo_album, nome_item='Álbum')
            elif opcao_album == '4':
                album_id = input('Digite o ID do álbum: ')
                album = ServicoAlbuns.obter_album(album_id)
                if 'id' in album:
                    titulo = input(
                        'Digite o novo título (ou deixe em branco): '
                    )
                    album_atualizado = ServicoAlbuns.atualizar_album(
                        album_id, titulo
                    )
                    self.atualizar(
                        item_atualizado=album_atualizado, nome_item='Álbum'
                    )
                else:
                    print(
                        f'\n❌ Erro: Álbum com ID {album_id} não encontrado.'
                    )
            elif opcao_album == '5':
                album_id = input('Digite o ID do álbum a ser deletado: ')
                album = ServicoAlbuns.obter_album(album_id)
                if 'id' in album:
                    status = ServicoAlbuns.deletar_album(album_id)
                    self.deletar(
                        status=status, item_id=album_id, nome_item='Álbum'
                    )
                else:
                    print(
                        f'\n❌ Erro: Álbum com ID {album_id} não encontrado.'
                    )
            elif opcao_album == '6':
                break
            else:
                print('\n⚠️ Opção inválida. Tente novamente.')

    def gerenciar_photos(self):
        while True:
            Menu.exibir_menu_photos()
            opcao_photo = input('Escolha uma opção de Photos: ')
            if opcao_photo == '1':
                photos = ServicoPhotos.listar_photos()
                self.listar(itens=photos, nome_item='Photos')
            elif opcao_photo == '2':
                photo_id = input('Digite o ID da photo: ')
                photo = ServicoPhotos.obter_photo(photo_id)
                self.visualizar(item=photo, nome_item='Photo')
            elif opcao_photo == '3':
                album_id = input('Digite o AlbumID da photo: ')
                titulo = input('Digite o título da photo: ')
                url = input('Digite a url da photo: ')
                thumbnail_url = input('Digite o Thumbnail URL da photo: ')
                nova_photo = ServicoPhotos.criar_photo(
                    album_id, titulo, url, thumbnail_url
                )
                self.criar(novo_item=nova_photo, nome_item='Photo')
            elif opcao_photo == '4':
                photo_id = input('Digite o ID da photo: ')
                photo = ServicoPhotos.obter_photo(photo_id)
                if 'id' in photo:
                    titulo = input(
                        'Digite o novo título (ou deixe em branco): '
                    )
                    url = input('Digite o novo URL (ou deixe em branco): ')
                    thumbnail_url = input(
                        'Digite o novo Thumbnail URL (ou deixe em branco): '
                    )
                    photo_atualizada = ServicoPhotos.atualizar_photo(
                        photo_id, titulo, url, thumbnail_url
                    )
                    self.atualizar(
                        item_atualizado=photo_atualizada, nome_item='Photo'
                    )
                else:
                    print(f'\n❌ Erro: Foto com ID {photo_id} não encontrada.')
            elif opcao_photo == '5':
                photo_id = input('Digite o ID da photo a ser deletada: ')
                photo = ServicoPhotos.obter_photo(photo_id)
                if 'id' in photo:
                    status = ServicoPhotos.deletar_photo(photo_id)
                    self.deletar(
                        status=status, item_id=photo_id, nome_item='Photo'
                    )
                else:
                    print(
                        f'\n❌ Erro: Photo com ID {photo_id} não encontrada.'
                    )
            elif opcao_photo == '6':
                break
            else:
                print('\n⚠️ Opção inválida. Tente novamente.')

    def gerenciar_todos(self):
        while True:
            Menu.exibir_menu_todos()
            opcao_todo = input('Escolha uma opção de Todos: ')
            if opcao_todo == '1':
                todos = ServicoTodos.listar_todos()
                self.listar(itens=todos, nome_item='Todos')
            elif opcao_todo == '2':
                todo_id = input('Digite o ID do todo: ')
                todo = ServicoTodos.obter_todo(todo_id)
                self.visualizar(item=todo, nome_item='Todo')
            elif opcao_todo == '3':
                usuario_id = input('Digite o UserID do usuário: ')
                titulo = input('Digite o título do todo: ')
                completo = self.obter_status_todo()
                novo_todo = ServicoTodos.criar_todo(
                    usuario_id, titulo, completo
                )
                self.criar(novo_item=novo_todo, nome_item='Todo')
            elif opcao_todo == '4':
                todo_id = input('Digite o ID do todo: ')
                todo = ServicoTodos.obter_todo(todo_id)
                if 'id' in todo:
                    titulo = input(
                        'Digite o novo título (ou deixe em branco): '
                    )
                    completo = self.obter_status_todo()
                    todo_atualizado = ServicoTodos.atualizar_todo(
                        todo_id, titulo, completo
                    )
                    self.atualizar(
                        item_atualizado=todo_atualizado, nome_item='Todo'
                    )
                else:
                    print(
                        f'\n❌ Erro: Tarefa com ID {todo_id} não encontrada.'
                    )
            elif opcao_todo == '5':
                todo_id = input('Digite o ID do todo a ser deletado: ')
                todo = ServicoTodos.obter_todo(todo_id)
                if 'id' in todo:
                    status = ServicoTodos.deletar_todo(todo_id)
                    self.deletar(
                        status=status, item_id=todo_id, nome_item='Todo'
                    )
                else:
                    print(f'\n❌ Erro: Todo com ID {todo_id} não encontrado.')
            elif opcao_todo == '6':
                break
            else:
                print('\n⚠️ Opção inválida. Tente novamente.')

    @staticmethod
    def obter_status_todo():
        while True:
            completo_input = input('O todo está completo? (Sim/Não): ').lower()
            if completo_input == 'sim':
                return True
            elif completo_input in {'não', 'nao'}:
                return False
            else:
                print("❌ Resposta inválida. Digite 'Sim' ou 'Não'.")

    def gerenciar_users(self):
        while True:
            Menu.exibir_menu_users()
            opcao_user = input('Escolha sua opção de Users: ')
            if opcao_user == '1':
                users = ServicoUsers.listar_users()
                self.listar(itens=users, nome_item='Users')
            elif opcao_user == '2':
                user_id = input('Digite o ID do user: ')
                user = ServicoUsers.obter_user(user_id)
                self.visualizar(item=user, nome_item='User')
            elif opcao_user == '3':
                nome = input('Digite o nome do user: ')
                username = input('Digite o username do user: ')
                email = input('Digite o email do user: ')
                novo_user = ServicoUsers.criar_user(nome, username, email)
                self.criar(novo_item=novo_user, nome_item='User')
            elif opcao_user == '4':
                user_id = input('Digite o ID do user: ')
                user = ServicoUsers.obter_user(user_id)
                if 'id' in user:
                    nome = input('Digite o novo nome (ou deixe em branco): ')
                    username = input(
                        'Digite o novo username (ou deixe em branco): '
                    )
                    email = input('Digite o novo email (ou deixe em branco): ')
                    user_atualizado = ServicoUsers.atualizar_user(
                        user_id, nome, username, email
                    )
                    self.atualizar(
                        item_atualizado=user_atualizado, nome_item='User'
                    )
                else:
                    print(
                        f'\n❌ Erro: Usuário com ID {user_id} não encontrado.'
                    )
            elif opcao_user == '5':
                user_id = input('Digite o ID do user a ser deletado: ')
                user = ServicoUsers.obter_user(user_id)
                if 'id' in user:
                    status = ServicoUsers.deletar_user(user_id)
                    self.deletar(
                        status=status, item_id=user_id, nome_item='User'
                    )
                else:
                    print(f'\n❌ Erro: User com ID {user_id} não encontrado.')
            elif opcao_user == '6':
                break
            else:
                print('\n⚠️ Opção inválida. Tente novamente.')


class SistemaCRUD:
    def __init__(self):
        self.gerenciador = GerenciadorCRUD()

    def executar(self):
        while True:
            Menu.exibir_menu_principal()
            opcao = input('Escolha uma opção: ')
            if opcao == '1':
                self.gerenciador.gerenciar_posts()
            elif opcao == '2':
                self.gerenciador.gerenciar_comments()
            elif opcao == '3':
                self.gerenciador.gerenciar_albuns()
            elif opcao == '4':
                self.gerenciador.gerenciar_photos()
            elif opcao == '5':
                self.gerenciador.gerenciar_todos()
            elif opcao == '6':
                self.gerenciador.gerenciar_users()
            elif opcao == '7':
                print(
                    '\nSaindo... Obrigado por utilizar nosso sistema e até mais!'
                )
                break
            else:
                print('\n⚠️ Opção inválida. Tente novamente.')


if __name__ == '__main__':
    sistema = SistemaCRUD()
    sistema.executar()
