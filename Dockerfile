# Use a imagem base do Python 3.8-slim
FROM python:3.8-slim

# Instale o módulo requests
RUN pip install requests

# Instale o deemon
RUN pip install --upgrade deemon

# Instale o watchdog
RUN pip install watchdog

# Configuração do diretório de trabalho no contêiner
WORKDIR /opt/grathusa

# Copie os arquivos de config para o diretório /app/config/
COPY app/config/config_deemon.json /root/.config/deemon/config.json
COPY app/config/config_deemix.json /root/.config/deemix/config.json

# Copie o script para a pasta /app/
COPY app/src/* /opt/grathusa/

# Execute o script Python como comando de entrada
CMD ["python", "coordenador.py"]
