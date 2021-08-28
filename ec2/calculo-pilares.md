# Cálculo de pilares

O cálculo de pilares de betão armado de acordo com o eurocódigo 2 encontra-se definido para estruturas contraventadas. É assim necessário que as estruturas disponham de paredes ou núcleos capazes de receber as ações horizontais.

## Estimativa da carga de encurvadura global

O cálculo da carga de instabilidade de estruturas pode ser estimado pela expressão:

$$F_{v,BB}=\xi\frac{\sum_{}^{}EI}{L^2}$$
com
$$\xi=7.8\frac{n_s}{n_s+1.6}\frac{1}{1+0.7k}, \quad EI=0.4E_{cd}I_c$$
$n_s=$número de pisos,
$k=0.1$ para um elemento de contraventamento único e $k=0$ para vários elementos de contraventamento. Para $k=0$ obtém-se a expressão: $$F_{v,BB}=3.12\frac{n_s}{n_s+1.6}\frac{\sum_{}^{}E_{cd}I_c}{L^2}$$

## Verificação da estabilidade global

A estrutura não tem esforços de sefunda ordem significativos se
$$F_{v,Ed}\le 0.1F_{v,BB}$$
