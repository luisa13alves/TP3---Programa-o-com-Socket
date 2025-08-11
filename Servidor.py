from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('O servidor esta pronto!')
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	sensor_id, temperatura, data, hora = sentence.split(',')
     
temperatura = float(temperatura)
     
print(f"{data} {hora} | {sensor_id} | {temperatura}°C")

# Verifica se a temperatura está fora de um intervalo aceitável (ex: <15°C ou >35°C). 
if temperatura < 15 or temperatura > 35:
    alerta = f" A temperatura ({temperatura}°C) está fora do intervalo permitido."
    connectionSocket.send(alerta.encode())
else:
    connectionSocket.send("Temperatura permitida!".encode())
    

  
    connectionSocket.close()
