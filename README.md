# helio-2.0

Uma empresa de táxi aéreo precisa controlar as viagens de seus pilotos e helicópteros, e saber como estão as reservas e os vôos realizados para fins de manutenção e pagamento de salários. A empresa possui uma frota de variados modelos de helicópteros, sendo que cada modelo possui um valor base de hora de voo.

Os pilotos são comissionados e recebem 20% do valor de hora de voo, sendo que possuem um acréscimo de 3% de bônus a 10.000 horas de voo em seu registro oficial, limitados a 15% de acréscimo total.

A empresa possui uma tabela de destinos atendidos, organizados por heliportos com as informações: código do heliporto, cidade, distância da origem e tempo médio de viagem para um trecho origem-destino. Uma cidade pode ter mais de um heliporto atendido.

Os clientes realizam reservas para os voos informando o destino (heliporto), data, hora e o modelo. A empresa consulta os helicópteros e os pilotos disponíveis para a data e hora solicitada, levando em consideração o tempo estimado de liberação de um voo para este par, pois é necessário calcular o tempo de uma viagem como origem->destino->origem. Por exemplo, se o destino escolhido for Curitiba, e o tempo de viagem médio considerado for de 1h, piloto e helicóptero somente estarão disponíveis em 2:30h após a saída (é necessário considerar 30 min para limpeza e reabastecimento).

O programa deve possibilitar a consulta de reservas por período, uma listagem dos helicópteros que precisam parar para manutenção e o valor a ser pago de salário para um piloto.

O cálculo de parada para manutenção está relacionado ao modelo, idade do helicóptero e horas de voo. Por padrão um helicóptero de determinado modelo deve parar para manutenção quando a quantidade de horas de voo desde sua última parada seja igual ou maior ao valor determinado pelo seu modelo, porém, este valor sofre alteração em relação à idade do helicóptero, com uma depreciação de 1% para cada ano de vida do veículo. Isto significa que um helicóptero com 5 anos de idade deve voar 5% menos horas em relação ao valor de referência indicado para seu modelo.

Escreva seu programa para atender às regras descritas, neste trabalho não será exigida interface de interação com o programa, portanto, se não o fizer, para simular seu uso escreva uma lógica que simule as entradas de dados e manipulação do programa, como criação dos helicópteros, modelos, pilotos e tabela de destinos, realização de reservas, listagem de reservas, voos realizados, listagem de manutenção, marcação de manutenção realizada e listagem de pagamento de salários.

