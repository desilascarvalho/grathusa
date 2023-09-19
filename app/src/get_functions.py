import subprocess
import time
import logging
import datetime

def run_command(command):
    subprocess.run(command, shell=True)

def run_refresh_command():
    # Obtém a data atual
    today = datetime.date.today()

    # Calcula a data do dia anterior
    yesterday = today - datetime.timedelta(days=1)

    # Formata a data do dia anterior no formato 'YYYY-MM-DD'
    yesterday_formatted = yesterday.strftime('%Y-%m-%d')

    # Constrói o comando com a data do dia anterior
    command = f"deemon refresh --time-machine {yesterday_formatted}"

    # Executa o comando
    run_command(command)

def run_import_command():
    import_command = "deemon monitor --import /downloads"
    run_command(import_command)

def wait_seconds(seconds):
    logging.info(f"Aguardando {seconds} segundos...")
    time.sleep(seconds)
