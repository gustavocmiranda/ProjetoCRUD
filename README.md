# CRUD Application

Este projeto é um sistema de CRUD simples desenvolvido em Python, usando FastAPI para o backend e Streamlit para o frontend. Foi meu primeiro contato com Docker, utilizado aqui para facilitar a configuração e a implantação do ambiente.

## Tecnologias Utilizadas

- **Backend:**
  - [FastAPI](https://fastapi.tiangolo.com/): Framework para criação de APIs rápidas e robustas.
  - [SQLAlchemy](https://www.sqlalchemy.org/): Mapeador objeto-relacional (ORM) para a gestão de banco de dados.
  - [Pydantic](https://pydantic-docs.helpmanual.io/): Validação e criação de dados tipados.
  
- **Frontend:**
  - [Streamlit](https://streamlit.io/): Ferramenta de criação de interfaces visuais para visualização e interação com o CRUD.
  - **Requests**: Biblioteca para fazer chamadas à API do backend.
  
- **Containerização:**
  - [Docker](https://www.docker.com/): Usado para facilitar a configuração e o deployment.

## Estrutura do Projeto

- `backend/`: Contém o código do servidor FastAPI, incluindo os modelos, a configuração do banco de dados e as rotas de CRUD.
- `frontend/`: Contém o código do Streamlit para a interface de usuário, onde são exibidas e manipuladas as informações.
- `docker-compose.yml`: Arquivo para configuração dos contêineres Docker para o backend e o banco de dados.

## Configuração e Instalação

### Pré-requisitos

Certifique-se de ter **Docker** instalado em sua máquina.

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/gustavocmiranda/ProjetoCRUD.git
   cd ProjetoCRUD
   ```

2. **Inicie os contêineres com Docker Compose:**
   ```bash
   docker-compose up -d
   ```

3. **Acesse o frontend no navegador:**
   - Acesse `http://localhost:8501` para interagir com o sistema CRUD.

4. **Testando o backend:**
   - Acesse `http://localhost:8000/docs` para a documentação interativa do FastAPI (Swagger), onde é possível testar as rotas diretamente.

## Funcionalidades

- **Criação, leitura, atualização e exclusão (CRUD)** de registros no banco de dados.
- **Interface visual** para o usuário interagir com os dados, usando Streamlit.
- **Validação de dados** com Pydantic e mapeamento de banco com SQLAlchemy.
  
## Contribuição

Feedbacks e melhorias são bem-vindos! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
