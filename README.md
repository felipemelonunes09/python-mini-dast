# Minidast Doc

## 1. Desafio

O projeto Minidast foi desenvolvido utilizando uma arquitetura de microserviços e as seguintes tecnologias: Python, Redis, MySQL e Zaproxy. Na estrutura do projeto, é possível ver duas diretivas principais: "api" e "minidast".

## 2. API

O diretório chamado "api" contém todo o código da API responsável pela interação com o banco de dados. Qualquer outro serviço que precise interagir com o banco de dados utilizará esta API para consultar, criar ou alterar os registros permitidos.

[Mais sobre a API](Minidast%20Doc%20bebcf028e4e742acb07c178cd96f8570/Mais%20sobre%20a%20API%20d2c5f6038c6344ee9cf0ae2deb6a1ce8.md)

[Endpoints](Minidast%20Doc%20bebcf028e4e742acb07c178cd96f8570/Endpoints%201600a8da930346b6938f33c45c8f5fba.md)

## 3. Minidast

O diretório "minidast" contém a lógica de negócio do scanner. Dentro deste diretório, dois serviços são responsáveis pelo funcionamento do sistema: "celery-api" e "celery".

O serviço "celery" lida com a execução de tarefas de forma independente, permitindo que vários scanners sejam executados simultaneamente. Este serviço garante que as tarefas sejam gerenciadas e processadas de maneira eficiente.

Já o serviço "celery-api" é uma API que permite a criação de novas tarefas para o gerenciador de filas de tarefas executar. Ele atua como uma interface que facilita a interação com o sistema de filas, assegurando que novas tarefas sejam adicionadas e gerenciadas corretamente.

[Mais sobre o minidast](Minidast%20Doc%20bebcf028e4e742acb07c178cd96f8570/Mais%20sobre%20o%20minidast%20ff30e0e8d8f54bfca1a0cfb3196bdfc1.md)

## **4.  Serviços**

- **mysql**: Responsável pelo armazenamento de dados e informações que precisam ser persistidas.
- **api**: API que manipula o banco de dados MySQL, permitindo consultas, criações e alterações de registros.
- **celery**: Gerenciador de filas de tarefas que permite a execução de várias tarefas de forma independente.
- **celery-api**: API que possibilita a criação de tarefas e a interação com o gerenciador de filas Celery.
- **redis**: Utilizado para a persistência dos dados das tarefas de scans e das filas.
- **zaproxy**: Serviço de scan que é acionado pelas tarefas gerenciadas pelo Celery.
- **juice-shop**: Aplicação vulnerável utilizada para testes de segurança.

### 4.1. Conceito

![Screenshot 2024-06-24 at 20.53.50.png](Minidast%20Doc%20bebcf028e4e742acb07c178cd96f8570/Screenshot_2024-06-24_at_20.53.50.png)

## 5. Executando

Para subir os containers, basta acessar o diretório do projeto no terminal e verificar se todas as variáveis de ambiente estão corretamente configuradas de acordo com o seu ambiente. Em seguida, execute o comando abaixo para iniciar os serviços:

```powershell
docker-compose build --no-cache && docker-compose up
```

## 6. Considerações finais

Este projeto é um teste desenvolvido para um desafio e, como tal, suas configurações não são ideais para um ambiente de produção. O objetivo principal é permitir testes, criação de um ambiente sandbox e o aprimoramento de conceitos. Para facilitar esse processo, algumas configurações de segurança e boas práticas foram deliberadamente omitidas. Por exemplo, não há definição de chave da API, endereços que podem acessar os serviços não estão restritos, e a autenticação não foi implementada. Essas omissões permitem um ambiente mais flexível e fácil de usar para fins de teste e aprendizado.

É importante entender que essas escolhas foram feitas intencionalmente para simplificar o desenvolvimento e o uso do projeto em um contexto de teste. Em um ambiente de produção, seria essencial implementar todas as medidas de segurança adequadas.

## 7. Próximos passos

- **Implementação de um Sistema de Logs**: Um sistema de logs pode ser útil para monitorar erros e eventos importantes na aplicação. Isso pode ajudar a identificar problemas e melhorar a estabilidade e confiabilidade do sistema.
- **Autenticação entre Serviços**: Implementar um sistema de autenticação entre os serviços pode aumentar a segurança da aplicação, garantindo que apenas serviços autorizados possam se comunicar entre si.
- **Melhor Divisão de Pastas**: Uma melhor organização de pastas e módulos pode facilitar o crescimento ordenado da aplicação. Isso inclui separar claramente as responsabilidades de cada parte da aplicação e garantir que os componentes sejam facilmente escaláveis e mantidos.
- **Criação de Mais Testes**: A criação de testes adicionais, como testes de unidade, integração e ponta a ponta, pode garantir uma cobertura mais abrangente da aplicação e ajudar a evitar regressões e bugs.
- **Aprimoramento do Modelo de Banco de Dados**: Avaliar e aprimorar o modelo de banco de dados e seus relacionamentos pode melhorar a eficiência, a escalabilidade e a manutenção do sistema a longo prazo.
