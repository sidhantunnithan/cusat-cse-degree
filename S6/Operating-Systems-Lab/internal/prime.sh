# Sidhant Unnithan
# CSE B     89
# OS Lab Internal

#!/bin/bash

printf "Enter a number: "
read n

if [ $n -lt 2 ]
then
    printf "Number is not prime\n"
else
    i=2
    while [ `expr $n % $i ` != 0 ]
    do
        i=`expr $i + 1`
    done

    if [ $n = $i ]
    then
        printf "Number is prime\n"
    else 
        printf "Number is not prime\n"
    fi
fi


