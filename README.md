# Servidor Http Conversor de Inteiros

O projeto consiste num servidor que recebe uma requisição http com um valor inteiro passado no path e retorna um json com o valor por extenso. O inteiro deve estar entre -99999 e 99999.

## Início

As instruções contidas nesse documento tem como finalidade auxiliar a implantação da aplicação na máquina local do usuário.

### Pré-requisitos

Docker para Desktop

### Instalação e Execução

1 - Faça o download e instalação do Docker para Desktop através do link https://hub.docker.com/search/?type=edition&offering=community

2 - Crie um diretório e faça o download dos três arquivos contidos nesse repositório para o novo diretório

3 - Execute os seguintes comandos através da linha de comando:
	
	3.1 - docker build -t python-servidor-http .
	
	3.2 - docker run -p 8181:8181 python-servidor-http
	
4 - Por fim, execute uma requisição http através da linha de comando ou algum software específico (Ex.: Postman)

	4.1 - curl http://localhost:8181/99999

## Autor

* **Lucas Raphael Leão Martins** 
