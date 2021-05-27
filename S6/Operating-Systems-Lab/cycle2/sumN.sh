#!/bin/bash

printf "Enter the value of 'n': "
read n

i=1
sum=0
while [ "$i" != `expr $n + 1` ]
do
	printf "Enter number $i : "
	read num
	sum=`expr $num + $sum`
	i=`expr $i + 1`
done

printf "Sum of ${n} numbers : $sum \n"

