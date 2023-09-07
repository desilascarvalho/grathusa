import os
import csv
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def get_new_artist_titles(pasta, arquivo_csv):
    try:
        arquivos_na_pasta = os.listdir(pasta)
        artistas_existentes = set()

        # Verifique se o arquivo CSV existe e carregue títulos de artistas existentes
        if os.path.exists(arquivo_csv):
            with open(arquivo_csv, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                artistas_existentes = set(row[0] for row in csv_reader)

        # Encontre novos títulos de artistas
        novos_artist_titles = set()
        for arquivo in arquivos_na_pasta:
            nome_artista = arquivo.strip()
            if nome_artista not in artistas_existentes:
                novos_artist_titles.add(nome_artista)

        # Escreva novos títulos no arquivo CSV
        if novos_artist_titles:
            with open(arquivo_csv, 'a') as csv_file:
                csv_writer = csv.writer(csv_file)
                for artista in novos_artist_titles:
                    csv_writer.writerow([artista])

        return novos_artist_titles

    except Exception as e:
        print(f"Erro ao detectar novos títulos de artistas: {str(e)}")
        return None

class FolderEventHandler(FileSystemEventHandler):
    def __init__(self, pasta, arquivo_csv):
        self.pasta = pasta
        self.arquivo_csv = arquivo_csv

    def on_created(self, event):
        if not event.is_directory:
            print(f"Novo arquivo criado: {event.src_path}")
            novos_artist_titles = get_new_artist_titles(self.pasta, self.arquivo_csv)

            if novos_artist_titles:
                print(f"Novos títulos de artistas detectados: {novos_artist_titles}")

                # Execute o comando deemon
                subprocess.run(["deemon", "monitor", "--download", "--import", self.arquivo_csv])

if __name__ == "__main__":
    pasta_artist_titles = "/grathusa/news_id"
    arquivo_csv = "new_artists.csv"

    event_handler = FolderEventHandler(pasta_artist_titles, arquivo_csv)
    observer = Observer()
    observer.schedule(event_handler, path=pasta_artist_titles, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
