# Buscador de Certificados PUCGO
Script buscador de certificados, criado com o intuito de facilitar a busca no terrível [site de certificados da PUCGO](https://sites.pucgoias.edu.br/certificados/).

# Sumário
* [Instalação](#instalação)
  * [Instalação do Python](#instalação-do-python)
  * [Instalação de módulos](#instalação-de-módulos)
* [Utilização](#utilização)
  * [Download do script](#download-do-script)
    * [Download manual](#download-manual)
    * [Download pelo terminal Linux](#download-pelo-terminal-linux)
  * [Executando o script](#executando-o-script)

# Instalação
Para utilizar o script, é necessários ter o Python 3.10 (ou superior) instalado, assim como os módulos `requests`, `json` e `beautifulsoup4`.

### Instalação do Python
Caso você não tenha o Python instalado, siga as instruções do tutorial:
* https://www.geeksforgeeks.org/how-to-install-python-on-windows/

### Instalação de módulos
A instalação de um módulo pode ser feita por um dos dois comandos a seguir:
```
python -m pip install <nome_do_modulo>
```
ou
```
pip install <nome_do_modulo>
```
Para instalar os módulos necessários para este projeto, use os comandos a seguir:
```
python -m pip install requests
python -m pip install json
python -m pip install beautifulsoup4
```
ou
```
pip install requests
pip install json
pip install beautifulsoup4
```

# Utilização
### Download do script
Primeiramente você deverá fazer o download dos arquivos do repositório. Você pode fazer isso diretamente pelo terminal ou de forma manual:

#### Download manual
* Faça o download pela página do repositório:
<br>![image](https://github.com/Firemanarg/busca-certificados-pucgo/assets/35619327/cc830b37-afc5-416b-a034-0da0c6a12485)
* Clique em _Download ZIP_:
<br>![image](https://github.com/Firemanarg/busca-certificados-pucgo/assets/35619327/907497bf-35ae-48c4-958b-fd8af91f3893)
* Vá para a pasta de Downloads e extraia o arquivo em uma pasta:
<br>![image](https://github.com/Firemanarg/busca-certificados-pucgo/assets/35619327/beb27628-e5e3-4ea8-9119-2dda109407f5)

#### Download pelo terminal Linux
* Abra o terminal no caminho desejado:
<br>![image](https://github.com/Firemanarg/busca-certificados-pucgo/assets/35619327/9a2a95b7-ca0b-4775-a1df-45ca9b3e3632)
* Execute o seguinte comando e aguarde:
```
git clone https://github.com/Firemanarg/busca-certificados-pucgo.git
```
![image](https://github.com/Firemanarg/busca-certificados-pucgo/assets/35619327/1da1600d-4379-4f8f-b523-9699ac5ee240)

#### Pronto!

### Executando o script
Para utilizar o script, você deverá executá-lo no terminal. Para fazer isso, utilize o comando no terminal dentro da pasta:
```
python busca.py
```
* Após executado o script, você deverá o nome do participante. É importante considerar que o nome deve estar escrito exatamente igual ao nome que foi cadastrado no evento.
<br>![image](https://github.com/Firemanarg/busca-certificados-pucgo/assets/35619327/53a8c836-401c-4f9c-91a3-35da2e4ee38e)
* Em seguida, será solicitado que você digite os filtros desejados. Se quiser buscar em todos os certificados, deixe o campo vazio (obs: quanto mais certificados, mais tempo a busca levará).
<br>![image](https://github.com/Firemanarg/busca-certificados-pucgo/assets/35619327/f6ea003c-7bc9-4276-bf57-d12b00b13a56)
* Assim, a busca será iniciada:
<br>![image](https://github.com/Firemanarg/busca-certificados-pucgo/assets/35619327/95bbc927-426b-4443-b22a-435dacb0426a)
* Aguarde até que a busca seja finalizada, e o link para os certificados encontrados será exibido:
<br>![image](https://github.com/Firemanarg/busca-certificados-pucgo/assets/35619327/bb727dbf-c372-4c27-b248-b723d4cc2908)


