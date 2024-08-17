#!/bin/bash

#INput & output do user
echo "Por favor, coloque um número : "
read a
echo "Por favor, coloque um segundo número : "
read b

#Selecionando uma operação
echo "Por favor, selecione uma opção: "
echo "1. Adição"
echo "2. Subtração"
echo "3. Multiplicação"
echo "4. Divisão"
read operacao

#Inicializando uma operação
c=$(( $a + $b))
d=$(( $a - $b))
e=$(( $a * $b))
f=$(( $a / $b))

#Swith case para inicializar a operação
case $operacao in
1)resultado="$a + $b = $c"
;;
2)resultado="$a - $b = $d"
;;
3)resultado="$a * $b = $e"
;;
4)resultado="$a / $b = $f"
;;
esac
echo "Sua resposta é : $resultado"
