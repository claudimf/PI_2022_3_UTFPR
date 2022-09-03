# Projeto Integrador 5 módulo "Python para negócios" UTFPR(Universidade Tecnológica Federal do Paraná).

## Requisitos das disciplinas ##

### Python para WEB (PWEB)

O trabalho consiste em desenvolver uma aplicação WEB utilizando Python para o backend. A aplicação WEB pode ser tanto o produto principal como uma parte ou módulo complementar do seu projeto principal. 

### Engenharia de Software para Projetos em Python (ESPP)

Arquivos solicitados para entrega. No relatório (Item i) descrever:  
[● Cinco problemas do produto;](https://github.com/claudimf/PI_2022_1_UTFPR/blob/main/ESPP%20-%20Requisitos%20da%20disciplina%20Engenharia%20de%20Software.pdf)  
[● Cinco expectativas (benefícios) do produto;](https://github.com/claudimf/PI_2022_1_UTFPR/blob/main/ESPP%20-%20Requisitos%20da%20disciplina%20Engenharia%20de%20Software.pdf)  
[● Duas personas que representam os usuários do produto, identificando duas atividades que ela faz e dois objetivos que ela espera alcançar; ](https://github.com/claudimf/PI_2022_1_UTFPR/blob/main/ESPP%20-%20Requisitos%20da%20disciplina%20Engenharia%20de%20Software.pdf)  
[● Oito requisitos, no formato de histórias do usuário, do seu projeto identificando o que já foi implementado neste PI ou nos anteriores. ](https://github.com/claudimf/PI_2022_1_UTFPR/blob/main/ESPP%20-%20Requisitos%20da%20disciplina%20Engenharia%20de%20Software.pdf)  

### Processamento de Sinais e Imagens com Python (PSIP)

Descrição. O trabalho deve conter pelo menos [três funcionalidades](https://github.com/claudimf/PI_2022_1_UTFPR/blob/main/crypto_games/utils.py) para edição de imagens
utilizando técnicas apresentadas na disciplina.
Arquivos solicitados para entrega. No relatório (Item i) descrever as funcionalidades para edição
de imagem utilizadas e sua relação com o projeto. (ii) Entregar todo o código do projeto, que deve
incluir o código das funcionalidades utilizadas.

### Material para Entregar

Arquivo compactado. Deve-se preparar o arquivo compactado contendo todos os arquivos
mencionados em cada requisito descrito anteriormente. Somente um membro do grupo faz a
entrega deste arquivo compactado, entretanto, todos os membros do grupo devem entregar o
vídeo de explicação (de 3 a 5 minutos, e mostrando um documento oficial para fins de
identificação).

## Como utilizar? ##

**:warning: Warning:** É necessário ter o Docker instalado:
- 🐳 [Docker Engine Installation](https://docs.docker.com/engine/install/ubuntu/)  
- 🐳 [Docker Compose Installation](https://docs.docker.com/compose/install/)  
- **💡 Tip:** [For any doubts please use Docker documentation](https://docs.docker.com/)  

### Utilizando a aplicação

Após instalar o Docker e o Docker-compose, abar um terminal e execute:

```sh
sudo docker-compose up
```
Para acessar a aplicação, abra uma nova aba no seu terminal e execute:

```sh
sudo docker-compose run --rm postgres bash
```

Para resetar a aplicação, execute:

```sh
docker-compose down && docker-compose up
```

#### Testando a conexão com o banco de dados

```sh
sudo docker-compose run --rm aplicacao python3 app/test-postgres.py
```

#### Rodar o banco de dados

```sh
sudo docker-compose run -d postgres
```

#### Criar fixtures
```sh
sudo docker-compose run --rm web ./create_fixtures
```

#### Recriar e Popular banco
```sh
sudo docker-compose run --rm web ./populate_db
```

### Permissões de arquivos ###
Quando se cria arquivos dentro de um contâiner Docker eles irão pertencer ao contâiner, para mudar a permissão rode o seguinte comando:

```sh
sudo chown -R $USER:$USER .
```

## Referências ##
[1° Django + Docker](https://github.com/claudimf/django-docker)  
[2° Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)  


Relatório para assinantes:

__ preencha a crypto


Opções:
() Tudo () Personalizado
[ ] GoogleTrends
[ ] BSCscan
[ ] CoinGecko


https://github.com/sodamodo/geospatial_docker_tutorial
https://medium.com/@zack.noah/creating-a-geospatial-web-app-using-docker-django-and-postgis-975bc24e7a6b
https://github.com/tlubenov/geodjango-postgis-nginx-docker
https://github.com/ernestone/docker-compose_geodjango_postgres_nginx/blob/master/docker-compose.yml
https://medium.com/geekculture/easily-gather-google-trends-data-in-python-22219cecd6fc
https://github.com/GeneralMills/pytrends
https://pypi.org/project/pytrends/
https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/