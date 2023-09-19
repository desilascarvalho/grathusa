import os
import datetime
import logging
import sys
from get_functions import run_refresh_command, run_import_command, wait_seconds

# Configurar logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    today = datetime.datetime.today().date()

    while True:
        # Importe o que os artistas existentes
        run_import_command()
        wait_seconds(10)

        # Verifique novos albums
        run_refresh_command()
        wait_seconds(86400)

        logging.info("Próximo ciclo de execução.")

if __name__ == "__main__":
    main()
