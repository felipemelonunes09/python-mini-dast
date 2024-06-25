# Mais sobre a API

Dependencias utilizadas no projeto 

```jsx
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
gunicorn==22.0.0
mysqlclient==2.2.4
websockets==12.0
```

# Bibliotecas

### 1. Flask

A API foi construída utilizando o framework Flask, que é conhecido por sua simplicidade e flexibilidade no desenvolvimento de aplicações web. Flask permite criar endpoints de forma rápida e eficiente, facilitando a gestão de rotas, requisições e respostas dentro da aplicação. Além disso, sua integração com SQLAlchemy facilita a manipulação do banco de dados, permitindo que as operações sejam realizadas de maneira mais estruturada e eficiente.

### 2. SQLAlchemy

Para facilitar a interação e estruturação das tabelas no banco de dados, foi escolhido o SQLAlchemy como ORM (Object-Relational Mapping). O SQLAlchemy oferece uma maneira flexível de mapear classes Python para tabelas do banco de dados, permitindo operações CRUD (Create, Read, Update, Delete) de maneira mais intuitiva e eficiente. Além disso, ele suporta uma ampla gama de funcionalidades avançadas, como consultas complexas, mapeamento de relacionamentos e transações, proporcionando uma camada de abstração robusta entre a aplicação e o banco de dados.

### 3. Gunicorn

Gunicorn é uma biblioteca de servidor web que facilita a escalabilidade horizontal da nossa aplicação através do uso de workers. Ele é um servidor WSGI (Web Server Gateway Interface) compatível com uma variedade de frameworks web em Python, incluindo Flask. Gunicorn é projetado para ser leve, simples de usar e altamente eficiente, permitindo que a aplicação gerencie múltiplas requisições simultaneamente de forma eficaz. Isso é especialmente útil em ambientes de produção onde a carga de trabalho pode variar significativamente, garantindo que a aplicação mantenha um desempenho estável e responsivo mesmo sob alta demanda.

### 4. Websockets

WebSockets foram utilizados para estabelecer uma conexão de socket facilitada com o serviço `api-celery`. Esta biblioteca permite uma comunicação bidirecional em tempo real entre o cliente e o servidor, garantindo que as atualizações e notificações sejam transmitidas de forma rápida e eficiente. 

Após a criação de cada scan, é estabelecida uma conexão WebSocket com o serviço `api-celery`. Essa conexão permite o envio dos dados do scan para que o `celery` possa processá-lo

# Diretórios

### 1. db

Este diretório contém os arquivos relacionados às conexões com o banco de dados. Caso sejam necessárias outras tipos de conexões ou se o banco de dados for trocado, basta criar uma nova classe e estender as funcionalidades da classe `DatabaseConnection.py`. Ao fazer isso, é necessário implementar os métodos abstratos definidos na classe base. Lembre-se de que o ORM utilizado é o SQLAlchemy.

### 2. models

No diretório específico, encontram-se os arquivos que definem as classes do ORM SQLAlchemy. Essas classes facilitam o processo de interação com o banco de dados, permitindo a criação, alteração, deleção e consulta das tabelas de forma simplificada e orientada a objetos.

As classes definidas nos arquivos seguem a estrutura padrão do SQLAlchemy, onde cada classe representa uma tabela do banco de dados. Cada classe mapeia os campos da tabela e define métodos que permitem realizar operações CRUD (Create, Read, Update, Delete) de maneira eficiente.

Essa abordagem facilita a manutenção do código e melhora a legibilidade, tornando mais claro o funcionamento e a estrutura do banco de dados da aplicação.

### 3. scan

Este diretório contém os arquivos relacionados aos controllers e services relacionados aos scans da aplicação. Os controllers são responsáveis por receber as requisições HTTP relacionadas aos scans e direcioná-las para as funções adequadas. Já os services são responsáveis por implementar a lógica de negócio relacionada aos scans, como a criação, atualização, consulta e exclusão de scans no banco de dados.

### 4. test

Este diretório contém os testes da aplicação. Esses testes são executados automaticamente antes do Docker Compose iniciar os serviços da aplicação. A execução dos testes garante que todas as funcionalidades estão operando corretamente e que eventuais problemas são identificados antes que a aplicação seja iniciada em um ambiente de produção.