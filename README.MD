# WoMakers Code 🦋 - Bootcamp BackEnd - Python Django (SQUAD - ENIAC)

🦋 Este repositório contém o Desafio API desevolvido pelo Squad ENIAC durante o Bootcamp de Python & Django oferecido pela WoMakersCode. O objetivo deste bootcamp é fornecer uma base sólida em Python e Django, capacitando as mulheres a desenvolverem aplicações web completas 🦋

## Desafio API - Consumo de API com Flask

### 📜 Descrição

O projeto será baseado em um servidor Flask com várias rotas para consumir os dados da API pública do Rick and Morty. Vamos criar rotas, templates, e usar a biblioteca requests para obter os dados da API.
  
#### 📚 Exercício  Rick e Morty:

📋 **O seriado Rick and Morty é um desenho animado americano de comédia e ficção científica criado por Justin Roiland e Dan Harmon para o bloco de programação noturno Adult Swim, exibido no canal Cartoon Network.** **A série acompanha as perigosas aventuras do cientista louco Rick e seu neto Morty, que divide seu tempo entre a vida familiar e viagens interdimensionais. A série é inspirada em Back to the Future e Doctor Who.** **A API do Rick and Morty é uma API pública que contém informações sobre os personagens da série.** **A documentação da API pode ser encontrada em: https://rickandmortyapi.com/documentation/#rest**


- 1️⃣. Criação da Rota de Localização:
    - Criar uma nova rota para listar as localizações. A rota deverá ser acessível através do caminho /locations.
    - A página deverá ser renderizada através do template locations.html. 
    - A página deverá conter uma tabela com as seguintes informações: nome, tipo e dimensão.
    - A tabela deverá conter um link para a página de perfil da localização

- 2️⃣. Criação da Rota para listar os Episódios:
    - Criar uma nova rota para listar os episódios.
    - A rota deverá ser acessível através do caminho /episodes.
    - A página deverá ser renderizada através do template episodes.html.
    - A página deverá conter uma tabela com as seguintes informações: nome, data de lançamento e código.
    - A tabela deverá conter um link para a página de perfil do episódio.


- 3️⃣. Criação de rota para exibir o perfil da Localização:
    - Criar uma nova rota para exibir o perfil da localização.
    - A rota deverá ser acessível através do caminho /location/<id>.
    - A página deverá ser renderizada através do template location.html.
    - A página deverá conter as seguintes informações: nome, tipo, dimensão e uma lista com os personagens que aparecem na localização.
    - A lista deverá conter um link para a página de perfil do personagem.


- 4️⃣. Criação de rota para exibir o perfil do Episódio:
    - Criar uma nova rota para exibir o perfil do episódio. 
    - A rota deverá ser acessível através do caminho /episode/<id>.
    - A página deverá ser renderizada através do template episode.html.
    - A página deverá conter as seguintes informações: nome, data de lançamento, código e uma lista com os personagens que aparecem no episódio.
    - A lista deverá conter um link para a página de perfil do personagem.

- 5️⃣. Adicionar Infos na página do perfil do Personagem:
    - Na página de perfil do personagem, adicione as seguintes informações: espécie, gênero, origem e localização. 
    - As informações de origem, localização e episódios em que o personagem aparece devem conter um link para a página de perfil da localização


## 👥 SQUAD ENIAC - Integrantes 

- Ana Julia Rauber - [GitHub](https://github.com/anajuliarauber) - [Likedin](https://www.linkedin.com/in/ana-julia-rauber/);
- Angelica Conceição Salvino da Silva - [GitHub](https://github.com/AngelicaSalvino) - [Likedin](https://www.linkedin.com/in/angelica-salvino/);
- Caroline Souza Camargo - [GitHub](https://github.com/Caroline-Camargo) - [Likedin](https://www.linkedin.com/in/caroline-souza-camargo-023b54164/);
- Fabiana Maria Ignácio da Silva - [GitHub](https://github.com/Ignacio-fabianamaria) - [Likedin](https://www.linkedin.com/in/fabianaignacio/);
- Kassia do Espirito Santo - [GitHub](https://github.com/KassiaES) - [Likedin](https://www.linkedin.com/in/kassia-es);
- Laysa Alexia Lima Cipriano - [GitHub](https://github.com/LayCipriano) - [Likedin](https://www.linkedin.com/in/lay-cipriano/);
- Marina Cesconeto dos Santos (líder do squad) - [GitHub](https://github.com/marina6coneto) - [Likedin](https://www.linkedin.com/in/marina-cesconeto-dos-santos-a17563216/);
- Natalia Gomes Vitório - [GitHub]() - [Likedin]();
- Rosana de Souza Brito - [GitHhub](https://github.com/RosanaBrito) - [Likedin](https://www.linkedin.com/in/rosanadesouzabrito/);

### 🤝 Divisão das Tarefas

A divisão foi realizada de forma que cada etapa fosse concluída antes do início da etapa seguinte. Dessa forma, as meninas com mais disponibilidade de tempo no início do projeto começaram pela primeira etapa, e assim por diante.

- 1️⃣. Criação da Rota de Localização: Marina
- 2️⃣. Criação da Rota para listar os Episódios: Kassia
- 3️⃣. Criação de rota para exibir o perfil da Localização:
- 4️⃣. Criação de rota para exibir o perfil do Episódio: Ana Julia e 
- 5️⃣. Adicionar Infos na página do perfil do Personagem:


## 🔧 Como Executar o Projeto

1. **Criar um Ambiente Virtual:**
   - No terminal, navegue até o diretório raiz do projeto.
   - Crie um ambiente virtual com o comando:
     ```bash
     python -m venv venv
     ```

2. **Ativar o Ambiente Virtual:**
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar Dependências:**
   - Com o ambiente virtual ativo, instale as dependências do projeto usando:
     ```bash
     pip install -r requirements.txt
     ```

4. **Executar o Aplicativo:**
   - Para iniciar o servidor Flask, execute o seguinte comando:
     ```bash
     flask --app app run
     ```
