import subprocess
import time
import logging

def run_command(command):
    subprocess.run(command, shell=True)

def run_refresh_command(date):
    command = f"deemon refresh --time-machine {date.strftime('%Y-%m-%d')}"
    run_command(command)

def run_import_command():
    import_command = "deemon monitor --import /downloads"
    run_command(import_command)

def wait_seconds(seconds):
    logging.info(f"Aguardando {seconds} segundos...")
    time.sleep(seconds)
