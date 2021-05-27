#!/bin/bash

printf "Enter a number: "
read n

fact=1

if [ $n = 0 ]
then
	fact=1
elif [ $n = 1 ]
then
	fact=1
else
	i=2
	n=`expr $n + 1`
	while [ "$i" != "$n" ]
	do
		fact=`expr "$fact * $i" | bc` 
		i=`expr $i + 1`
	done
fi

printf "The factorial of `expr $n - 1` is : $fact \n"
