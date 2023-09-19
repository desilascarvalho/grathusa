import os
import json
import time

# Diretório onde o arquivo 'config_arl' será verificado
diretorio_arquivo_config = '/opt/grathusa'

# Define o intervalo de verificação em segundos
intervalo_verificacao = 5

# Função para verificar a existência do arquivo 'config_arl'
def verificar_arquivo_config_arl():
    while not os.path.exists(os.path.join(diretorio_arquivo_config, 'config_arl')):
        print("Aguardando a existência do arquivo 'config_arl'...")
        time.sleep(intervalo_verificacao)

# Verifica se o arquivo 'config_arl' existe
verificar_arquivo_config_arl()

# Leitura da ARL do arquivo 'config_arl'
with open(os.path.join(diretorio_arquivo_config, 'config_arl'), 'r') as arquivo_arl:
    arl = arquivo_arl.read().strip()

# Caminho para o arquivo config_deemon.json
config_file_path = '/root/.config/deemon/config.json'

try:
    # Lê o arquivo de configuração
    with open(config_file_path, 'r') as config_file:
        config_data = json.load(config_file)

    # Preenche a ARL no arquivo de configuração
    config_data['deemix']['arl'] = arl

    # Escreve as alterações de volta no arquivo
    with open(config_file_path, 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

    print("ARL configurada com sucesso no config_deemon.json.")

except Exception as e:
    print(f"Erro ao configurar a ARL no arquivo de configuração: {str(e)}")
