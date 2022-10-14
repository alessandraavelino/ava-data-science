# ava-data-science
Análise de Rede
Um professor do IFPB campus Guarabira está fazendo uma análise do desempenho de uma
server farm para determinar o melhor local para armazenar um site de manipulação de arquivos
.pdf (https://pdfmania.com.br). O objetivo da análise é descobrir a máquina que tem o menor
tempo de resposta para acesso externo (a partir da máquina de fronteira) e mover o site para
ela. Para isto, o professor executou o comando ping(8) a partir da máquina de fronteira para
saber o tempo de resposta de cada uma das máquinas da server farm e gerou arquivos de log
para cada uma delas (exemplo na listagem 1): azul_64b.ping, azul_1428b.ping, verde_64b.ping,
verde_1428b.ping, boca_64b.ping e boca_1428b.ping.
PING azul.vpn.laced.com.br (10.8.0.42): 56 data bytes
64 bytes from 10.8.0.42: icmp_seq=0 ttl=64 time=83.542 ms
64 bytes from 10.8.0.42: icmp_seq=1 ttl=64 time=84.254 ms
64 bytes from 10.8.0.42: icmp_seq=2 ttl=64 time=83.377 ms
64 bytes from 10.8.0.42: icmp_seq=3 ttl=64 time=82.264 ms
64 bytes from 10.8.0.42: icmp_seq=4 ttl=64 time=82.333 ms
64 bytes from 10.8.0.42: icmp_seq=5 ttl=64 time=83.293 ms
64 bytes from 10.8.0.42: icmp_seq=6 ttl=64 time=83.851 ms
Exemplo 1: Parte da listagem do comando ping para a máquina azul.
Escreva um programa capaz de analisar o tempo de resposta do comando ping no conjunto de
dados obtidos nas listagens. Seu programa deve calcular as métricas: média, mediana, o valor
do quantil para 25% e 75%, moda, amplitude, variância e dispersão. Liste a quantidade e os
valores dos outliers presentes nos dados. Considere como outliers os valores maiores ou iguais a
6 vezes a variância.
Para cada um dos pares de arquivos (exemplo: azul_64b.ping e azul_1428b.ping) calcule a
correlação entre as medidas para a variável “tamanho dos pacotes”.
Apresente um texto argumentativo indicando qual a máquina mais adequada para hospedar
o site. Utilize como justificativa os valores d
