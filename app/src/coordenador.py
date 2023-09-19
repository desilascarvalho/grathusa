import subprocess
import threading

# Função para executar daily_script.py
def run_daily_script():
    subprocess.run(["python", "daily_script.py"])

# Função para executar new_artists.py com o Watchdog
def run_new_artists_with_watchdog():
    subprocess.run(["python", "new_artists.py"])

# Crie threads para executar ambos os scripts em paralelo
daily_script_thread = threading.Thread(target=run_daily_script)
new_artists_thread = threading.Thread(target=run_new_artists_with_watchdog)

# Inicie as threads
daily_script_thread.start()
new_artists_thread.start()

# Aguarde que ambas as threads terminem
daily_script_thread.join()
new_artists_thread.join()
