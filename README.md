# Fusion Project

Este é o projeto Fusion, desenvolvido como parte do curso da GeekUniversity sobre Django.

## Descrição

O Fusion é uma aplicação web construída com Django, um framework de desenvolvimento web em Python. O objetivo deste projeto é demonstrar as funcionalidades básicas e avançadas do Django, incluindo:

- Configuração do ambiente de desenvolvimento
- Criação de modelos de dados
- Desenvolvimento de views e templates
- Implementação de autenticação e autorização
- Integração com banco de dados
- Testes automatizados

## Requisitos

- Python 3.x
- Django 3.x
- Banco de dados SQLite (ou outro de sua preferência)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/fusion-project.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd fusion-project
    ```

3. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:

    - No Windows:
      ```bash
      venv\Scripts\activate
      ```
    - No Linux/Mac:
      ```bash
      source venv/bin/activate
      ```

5. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

6. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

7. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

## Uso

Acesse o servidor de desenvolvimento em `http://127.0.0.1:8000` e explore as funcionalidades do projeto Fusion.

## Contribuição

Se você deseja contribuir com este projeto, por favor, siga os passos abaixo:

1. Faça um fork do repositório
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas alterações (`git commit -am 'Adiciona nova funcionalidade'`)
4. Faça o push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, entre em contato com [seu-email@dominio.com](mailto:seu-email@dominio.com).
