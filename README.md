# Busca Certificados PUCGO
Script criado com o intuito de encontrar certificados no terrível site de certificados da PUCGO. Para utilizar basta modificar o nome e os filtros.

# Instalação
Para utilizar o script, são necessários os módulos `requests`, `json` e `beautifulsoup4`

### Instalação de módulos
A instalação de um módulo pode ser feita por um dos dois comandos a seguir:
```
python -m pip install <nome_do_modulo>
```
ou
```
pip install <nome_do_modulo>
```

# Utilização
Para utilizar o script, basta alterar o valor das variáveis `NAME` e `FILTERS` para os valores desejados:
* `NAME` -> indica o nome do participante (o nome deve estar idêntico ao da inscrição)
* `FILTERS` -> indica os filtros para refinar e reduzir a quantidade de páginas durante a busca
Depois é só executar o script em algum terminal que tenha o Python 3.10+ instalado (não testei em versões anteriores).

### Executando o script pelo terminal
Comando de execução do script (obs: o caminho do terminal deve ser o mesmo do script):
```
python busca.py
```
