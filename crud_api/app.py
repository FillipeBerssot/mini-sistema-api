from crud_api.src.gerenciador_api import GerenciadorCRUD
from crud_api.src.menu_api import Menu


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
                    '\nSaindo... Obrigado por utilizar '
                    'nosso sistema e até mais!'
                )
                break
            else:
                print('\n⚠️ Opção inválida. Tente novamente.')


if __name__ == '__main__':
    sistema = SistemaCRUD()
    sistema.executar()
