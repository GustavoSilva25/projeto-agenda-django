# Agenda de Contatos Simples
Visite o site em: [https://gustavosilva.pythonanywhere.com/]

## Descrição
A **Agenda de Contatos** é um aplicativo web desenvolvido com Django que permite aos usuários gerenciar suas informações de contato.
O sistema implementa autenticação de usuários, garantindo que apenas usuários logados possam criar, editar e excluir contatos.
Cada contato é associado ao usuário que o criou, permitindo que apenas o proprietário possa alterá-lo.

## Funcionalidade
- **Cadastro e Login de Usuários:** Autenticação segura para acesso ao sistema.
- **Gerenciamento de Contatos:** Adicione, edite e exclua contatos.
- **Associação de Contatos ao Usuário:** Cada contato é vinculado ao usuário que o criou, garantindo privacidade e segurança.
- **Interface:** Design simples e fácil de usar, adaptável a dispositivos móveis e desktops.

## Tecnologias Utilizadas

- **Backend:** Django
- **Banco de Dados:** MySQL
- **Frontend:** HTML, CSS (Bootstrap)
- **Hospedagem:** PythonAnywhere

## Requisitos necessário para rodar o projeto

 Python 3
- Django
- MySQL
- Ambiente Virtual (recomendado)
- 
## Passos para Execução Local 

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/GustavoSilva25/projeto-agenda-django.git
   cd projeto-agenda-django

2. **Crie e Ative um Anbiente Virtual**
   ```bash
   python -m venv venv
   source ./venv/bin/activate # linux
   venv\Scripts\activate # Windows
   
3. **Instale as Dependências**
   ```bash
   pip install -r requirements.txt

 4. **Configuração do Banco de Dados**
       - Crie um banco de dados MySQL no seu ambiente local.
       - Configuração no `settings.py`
       - Aplicação das Migrações:
         ```bash
         python manage.py migrate
        
5. **Criação de um Superusuário (Opcional):**

     ```bash
     python manage.py createsuperuser
     ```
     Siga as instruções fornecidas no terminal para definir o nome de usuário, e-mail e senha.

6. **Início do Servidor de Desenvolvimento:**

     ```bash
     python manage.py runserver
     ```

## Contribuição

Contribuições são bem-vindas! Para contribuir:

   ```bash
   git checkout -b feature/nome-da-feature

