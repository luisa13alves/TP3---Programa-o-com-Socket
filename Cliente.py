from socket import *
import time 
from datetime import datetime
import random 

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
sensor_id = 'sensor1' # Identificação do sensor 
clientSocket.connect((serverName,serverPort)) 

while True:
 temperatura = round(random.uniform(10,40)) # Gerar temperatura variadas

# Exibir data e hora exata que a temperatura foi registrada
data = datetime.now().strftime("%D/%M/%Y")
hora = datetime.now().strftime("%H:%M:%S") 

# Gera o texto com os dados 
texto = f"{sensor_id},{temperatura},{data},{hora}"

clientSocket.send(texto.encode()) # Envia a mensagem para o servidor
resposta = clientSocket.recv(1024).decode() # Recebe a resposta
time.sleep(5)
print (f"[{data} {hora}] Temperatura: {temperatura}°C | Resposta: {resposta}")



clientSocket.close()
