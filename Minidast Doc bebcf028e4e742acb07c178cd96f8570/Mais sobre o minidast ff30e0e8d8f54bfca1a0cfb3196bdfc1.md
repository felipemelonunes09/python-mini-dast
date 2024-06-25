# Mais sobre o minidast

# Bibliotecas

```jsx
celery==5.4.0
redis==5.0.6
websockets==12.0
zaproxy
```

### 1. Celery

Esta biblioteca permite registrar uma task no gerenciador de filas de tarefas e iniciar sua execução. Ela facilita a comunicação com o sistema de gerenciamento de filas, assegurando que as tasks sejam corretamente enfileiradas e processadas conforme necessário.

### 2. websockets

A biblioteca de WebSockets é responsável por abrir o servidor WebSocket e monitorar atualizações. Ela fica aguardando a criação de novos scans e, quando um novo scan é criado, a biblioteca facilita a comunicação e o processamento do.

### 3. zaproxy

A biblioteca API do ZAPROXY permite a comunicação com o serviço `zaproxy` e a requisição de scans. Ela facilita a integração, permitindo iniciar, monitorar e gerenciar scans diretamente através da aplicação.

# Arquivos

### 1. run.py

Este arquivo é responsável por iniciar o servidor WebSocket e mantê-lo em modo de escuta. Ele monitora a criação de novos registros de scan e, ao detectar um novo scan, inicia o processo de scan correspondente.

### 2. task.py

Este arquivo contém a task de execução, incluindo a função que o Celery irá iniciar de forma independente. A função definida neste arquivo é responsável por executar as tarefas de processamento de scans, permitindo que elas sejam gerenciadas e executadas de maneira assíncrona e paralela, aproveitando a capacidade do Celery para lidar com múltiplas tarefas simultaneamente.

## Diretórios

### 1. scanner

Este diretório contém a definição da interface do scanner e a lógica de negócio para o scanner do ZAPROXY. Caso seja necessário criar outro scanner, deve-se herdar a classe `Scanner.py` e implementar os métodos abstratos definidos. Isso garante que todos os scanners sigam uma estrutura consistente e possam ser integrados facilmente com o restante do sistema.