# Author: Lucas S. Queiroz [Firemanarg]
# Creation Date: 13/07/2023 00:42

import requests
import json
from bs4 import BeautifulSoup


MAIN_URL = "https://sites.pucgoias.edu.br/certificados/"
CONTENT_URL = MAIN_URL + "participantes/"
NAME = "LUCAS SILVA QUEIROZ"
FILTERS = ["CIRCUITO", "CASA"]

download_links = []


def list_events():
    page = requests.get(MAIN_URL)
    events = []
    for line in page.text.split('\n'):
        if line.startswith("eventos.push"):
            raw_event = line.replace("eventos.push(", "")[0:-2]
            event = json.loads(raw_event)
            for filter_ in FILTERS:
                if filter_ in event["titulo"]:
                    events.append(event)
    return events


def find_name_on_page(id, name):
    URL = CONTENT_URL + str(id)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="lista-eventos")
    name_elements = results.find_all("a", string = name)
    if len(name_elements) == 0:
        return None
    return name_elements[0]


def main():
    print("Carregando eventos...")
    events = list_events()
    print("Iniciando a busca...")
    EVENTS_COUNT_STR = str(len(events))
    count = 1
    for event in events:
        download_link = find_name_on_page(event["id"], NAME)
        print("Buscando... (" + str(count), "/", EVENTS_COUNT_STR + ")")
        if download_link:
            download_links.append(download_link)
        count += 1
    print("Busca finalizada! Links encontrados:")
    print()
    for link in download_links:
        print("  >", link["href"])

        
main()
