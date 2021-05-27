#!/bin/bash

printf "Enter the string to be checked: "
read s
len=${#s}

if [[ $(rev <<< "$s") == "$s" ]];
then
	printf "Given string is a palindrome \n"
else
	printf "Given string is not a palindrome \n"
fi
