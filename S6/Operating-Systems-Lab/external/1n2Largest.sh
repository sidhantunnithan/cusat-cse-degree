#!/bin/bash

printf "Enter the value of 'n': "
read n

if [ $n -lt 2 ]
then
    printf "minimum value of n has to be 2\n"
    exit 1
fi

read first
read second

if [ $second -gt $first ]
then
    temp=$second
    second=$first
    first=$temp
fi

i=2
while [ $i != $n ]
do
	read num
	if [ $num -gt $first ]
    then
        second=$first
        first=$num
    elif [ $num -gt $second ]
    then
        second=$num
    fi
    i=`expr $i + 1`
done
printf "largest : $first\nsecond largest : $second\n"
