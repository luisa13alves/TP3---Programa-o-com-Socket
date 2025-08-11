# TP3 - Programação com Socket
**TRABALHO PRÁTICO III**  
O objetivo deste trabalho é desenvolver uma aplicação cliente-servidor usando Python e sockets, simulando 
um sistema distribuído de monitoramento de temperatura, como se fosse usado em data centers, estufas, 
ou cidades inteligentes. Não é necessário implementar interface gráfica. O trabalho poderá ser realizado em dupla. 
**Descrição do Trabalho:** 
Vocês deverão implementar um sistema onde cada cliente representa um sensor remoto de temperatura 
(ex: um servidor ou uma sala), e o servidor central coleta os dados, armazena, analisa e responde com 
alertas. 
**Funcionamento da Plataforma:** <br>
1. Cliente (sensor):<br> 
    a. Se conecta ao servidor e envia periodicamente: <br>
       i. Identificação do sensor (ID ou nome) <br>
       ii. Temperatura atual  <br>
       iii. Timestamp da leitura <br>
Pode simular o envio com random.uniform() para gerar temperaturas variadas. <br>
Pode permitir o envio contínuo ou em ciclos (ex: a cada 1 minuto. Você escolhe como fazer). <br>
2. Servidor (central de monitoramento): <br>
a. Recebe dados de múltiplos sensores. <br>
b. Armazena os dados em um log ou estrutura de dados (pode ser um arquivo CSV ou lista). <br>
c. Verifica se a temperatura está fora de um intervalo aceitável (ex: <15°C ou >35°C). <br>
    i. Se estiver, envia uma mensagem de alerta ao cliente (sensor). <br>
d. Pode exibir no console ou salvar em arquivo: <br> 
    i. Os dados de sensores e alertas emitidos. <br>
   ii. Um resumo com a temperatura média de cada sensor.<br>
  iii. Implementar um gráfico simples com matplotlib.<br>
