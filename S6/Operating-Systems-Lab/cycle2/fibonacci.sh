#!/bin/bash

x=0
y=1
printf "Enter the number of terms required in the series: "
read n

if [ $n -lt 1 ]
then
	printf "Invalid value entered!"
elif [ $n -eq 1 ]
then
	printf "${x}"
elif [ $n -eq 2 ]
then
	printf "${x}"
	printf "${y}"
else
	printf $x
	printf " $y"
	i=2
	while [ $i -lt $n ]
	do
		y=`expr $x + $y`
		x=`expr $y - $x`
		printf " $y"
		i=`expr $i + 1`
	done
fi	
printf "\n"
