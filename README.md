
# Mini Sistema API

Este projeto de estudo, consiste em um mini sistema API desenvolvido em Python, utilizando o `requests` para realizar operações CRUD em uma API externa (JSONPlaceholder). Ele segue uma arquitetura modular, utilizando classes para facilitar a manutenção e escalabilidade do código.

## Estrutura do Projeto

```
mini-sistema-api/
├── crud_api/                  # Código principal da API
│   ├── __init__.py            # Inicialização do módulo
│   ├── app.py                 # Arquivo principal de execução da aplicação
│   ├── configuracoes.py       # Configurações gerais da API
│   ├── src/                   # Pacote contendo funcionalidades específicas
│   │   ├── gerenciador_api.py # Gerenciamento das operações CRUD
│   │   ├── menu_api.py        # Menu de interação com o usuário
│   │   ├── requisicoes_api.py # Funções para realizar requisições à API externa
│   │   ├── servico_albuns.py  # Serviço responsável pelas operações sobre álbuns
│   │   ├── servico_comments.py# Serviço responsável pelas operações sobre comentários
│   │   ├── servico_photos.py  # Serviço responsável pelas operações sobre fotos
│   │   ├── servico_post.py    # Serviço responsável pelas operações sobre posts
│   │   ├── servico_todos.py   # Serviço responsável pelas operações sobre "todos"
│   │   ├── servico_users.py   # Serviço responsável pelas operações sobre usuários
│   │   └── __pycache__/       # Cache de compilação dos módulos Python
├── tests/                     # Testes automatizados do sistema
│   ├── __init__.py            # Inicialização do módulo de testes
├── pyproject.toml             # Configurações do Poetry e dependências do projeto
├── poetry.lock                # Registro de versões bloqueadas das dependências
├── README.md                  # Arquivo de documentação (você está aqui!)
└── .gitignore                 # Arquivo de ignorância de arquivos para controle de versão Git

```

## Funcionalidades

- **Gerenciar Posts**: Listar, visualizar, criar, atualizar e deletar posts.
- **Gerenciar Comments**: Listar, visualizar, criar, atualizar e deletar comentários.
- **Gerenciar Álbuns**: Listar, visualizar, criar, atualizar e deletar álbuns.
- **Gerenciar Photos**: Listar, visualizar, criar, atualizar e deletar fotos.
- **Gerenciar Todos**: Listar, visualizar, criar, atualizar e deletar tarefas (todos).
- **Gerenciar Users**: Listar, visualizar, criar, atualizar e deletar usuários.

## Requisitos

- **Python 3.8 ou superior**
- **Poetry** (para gerenciamento de dependências)

## Instalação

1. Clone o repositório:

```
git clone https://github.com/FillipeBerssot/mini-sistema-api.git
```

2. Navegue até o diretório do projeto:

```
cd mini-sistema-api
```

3. Instale as dependências utilizando o Poetry:

```
poetry install
```

## Uso

Para executar o sistema, utilize o seguinte comando:

```
poetry run python crud_api/app.py
```

Siga as instruções no menu para realizar as operações CRUD nas diferentes entidades.

## Estrutura do Código

### `crud_api/`
- **`__init__.py`**: Arquivo de inicialização do pacote `crud_api`.
- **`app.py`**: Arquivo principal do sistema. Responsável por executar o sistema CRUD e gerenciar o fluxo da aplicação.
- **`configuracoes.py`**: Contém as configurações gerais do sistema, como a URL base da API e outros parâmetros de configuração.

### `crud_api/src/`
- **`gerenciador_api.py`**: Gerencia todas as operações CRUD para entidades como posts, comentários, álbuns, fotos, "todos" e usuários. Contém a lógica principal de manipulação dos dados.
- **`menu_api.py`**: Define os menus de interação com o usuário, permitindo navegar entre as opções de gerenciamento de entidades.
- **`requisicoes_api.py`**: Centraliza as funções responsáveis pelas requisições HTTP (GET, POST, PUT, DELETE) feitas para a API externa.

#### Módulos de Serviço (para cada entidade):
- **`servico_albuns.py`**: Contém funções específicas para operações CRUD relacionadas a álbuns.
- **`servico_comments.py`**: Gerencia as operações CRUD de comentários.
- **`servico_photos.py`**: Funções para lidar com fotos (criar, listar, deletar, etc.).
- **`servico_post.py`**: Lida com as operações CRUD relacionadas a posts.
- **`servico_todos.py`**: Gerencia operações CRUD de tarefas (todos).
- **`servico_users.py`**: Contém funções para gerenciar usuários (criar, listar, atualizar, deletar).

### `tests/`
- **`__init__.py`**: Inicializa o pacote de testes.
- **Arquivos de Testes**: Contém testes automatizados para validar o comportamento de cada módulo e funcionalidade do sistema.

### Arquivos de Configuração:
- **`pyproject.toml`**: Configuração do Poetry que gerencia as dependências e scripts do projeto.
- **`poetry.lock`**: Arquivo que fixa as versões exatas das dependências utilizadas no projeto, garantindo consistência entre ambientes.

### Outros Arquivos:
- **`.gitignore`**: Define os arquivos e diretórios que serão ignorados pelo Git (como arquivos temporários e dependências).

## Contribuição

Este projeto é apenas para fins educacionais.

## Licença

Este projeto está sob a licença MIT - veja o arquivo LICENSE.md para mais detalhes.
