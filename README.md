# Servidor Http Conversor de Inteiros para Valor por Extenso

O projeto consiste num servidor http que recebe uma requisição http com um valor inteiro passado no path, e retorna um json com o valor por extenso. O inteiro deve estar entre -99999 e 99999.

## Início

As instruções contidas nesse documento tem como finalidade auxiliar a implantação da aplicação na máquina local do usuário.

### Pré-requisitos

Python 3
Docker para Desktop

### Instalação e Execução

1 - Faça o download e instalação do Python 3.x através do link https://www.python.org/downloads/

2 - Faça o download e instalação do Docker para Desktop através do link https://hub.docker.com/search/?type=edition&offering=community

3 - Crie um diretório e faça o download dos três arquivos contidos nesse repositório para o novo diretório

4 - Execute os seguintes comandos através da linha de comando:
	
	4.1 - docker build -t python-servidor-http .
	
	4.2 - docker run -p 8181:8181 python-servidor-http
	
5 - Por fim, execute uma requisição http através da linha de comando ou algum software específico (Ex.: Postman)

	5.1 - curl http://localhost:8181/99999

## Autor

* **Lucas Raphael Leão Martins** 
