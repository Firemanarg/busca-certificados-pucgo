# Author: Lucas S. Queiroz [Firemanarg]
# Creation Date: 13/07/2023 00:42

import requests
import json
from bs4 import BeautifulSoup
import sys


MAIN_URL = "https://sites.pucgoias.edu.br/certificados/"
CONTENT_URL = MAIN_URL + "participantes/"
name = ""
filters = []
download_links = []
progress_x = 0
search_began = False


def list_events():
    global MAIN_URL
    global filters

    page = requests.get(MAIN_URL)
    events = []
    lines = page.text.split('\n')
    LINES_COUNT = len(lines)
    count = 1
    for line in lines:
        progress(count / LINES_COUNT * 100)
        count += 1
        if line.startswith("eventos.push"):
            raw_event = line.replace("eventos.push(", "")[0:-2]
            event = json.loads(raw_event)
            for filter_ in filters:
                if filter_.lower() in event["titulo"].lower():
                    events.append(event)
    return events


def find_name_on_page(page_id):
    global CONTENT_URL
    global name

    URL = CONTENT_URL + str(page_id)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="lista-eventos")
    name_elements = results.find_all("a", string = name.upper())
    if len(name_elements) == 0:
        return None
    return name_elements[0]


def start_progress(title):
    global progress_x

    sys.stdout.write(title + ": [" + "-"*40 + "]" + chr(8)*41)
    sys.stdout.flush()
    progress_x = 0

def progress(x):
    global progress_x

    x = int(x * 40 // 100)
    sys.stdout.write("#" * (x - progress_x))
    sys.stdout.flush()
    progress_x = x

def end_progress():
    sys.stdout.write("#" * (40 - progress_x) + "]\n")
    sys.stdout.flush()


def load_events():
    print("Carregando eventos...")
    start_progress("Progresso")
    events = list_events()
    end_progress()
    print("Eventos carregados!")
    print("Foram encontrados", len(events), "eventos com os filtros informados.")
    return events


def search_in_events(events):
    global name
    global filters
    global download_links

    EVENTS_COUNT = len(events)
    count = 1
    print("Buscando certificados...")
    start_progress("Progresso")
    for event in events:
        download_link = find_name_on_page(event["id"])
        progress(count / EVENTS_COUNT * 100)
        if download_link:
            download_links.append(download_link)
        count += 1
    end_progress()


def print_header():
    print()
    print(" /@@@@@@@@@@@@@@@@@@**==~oOo~==**@@@@@@@@@@@@@@@@@@\ ")
    print("@@@@@====================~*~====================@@@@@")
    print("@@-------------------------------------------------@@")
    print("@- B U S C A D O R   D E   C E R T I F I C A D O S -@")
    print("@---------------- P U C   G O I Á S ----------------@")
    print("@@@-----------------------------------------------@@@")
    print("@========================~*~========================@")
    print("@@@@*** Autor: Lucas S. Queiroz  [Firemanarg] ***@@@@")
    print("@@@@@@@=======================================@@@@@@@")
    print("@@@| Facilitando sua vida nesse site horrível... |@@@")
    print(" \@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/ ")
    print()


def get_inputs():
    global name
    global filters

    print("Para começar digite os seguintes dados:")
    print()
    name = input("\t> Nome da pessoa: ")
    filters = input("\t> Filtros (separados por vírgula): ").split(",")
    print()


def display_results():
    global download_links

    if len(download_links) == 0:
        print("\tNenhum certificado foi encontrado.")
        return
    print("Foram encontrados", len(download_links), "certificados com o nome", name + ":")
    print()
    for link in download_links:
        print("\t>", link["href"])
    print()


def main():
    global name
    global download_links
    global search_began

    try:
        print_header()
        get_inputs()
        search_began = True
        events = load_events()
        search_in_events(events)
    except KeyboardInterrupt:
        if search_began:
            end_progress()
            print("Busca interrompida pelo usuário.")
        else:
            print()
            print()
            print("Programa interrompido pelo usuário.")
    except Exception as e:
        if search_began:
            end_progress()
            print("Ocorreu um erro durante a busca:", e)
        else:
            print("Ocorreu um erro:", e)
    if search_began:
        print("Busca finalizada!")
        print()
        display_results()
    else:
        print("Programa finalizado!")

        
main()
