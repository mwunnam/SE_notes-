#!/bin/bash

read -p "Enter a letter: " letter

case $letter in 
    [aA])
    echo "You entered $letter"
    ;;

    [bB])
    echo "You enter $letter"
    ;;
    
    *)
    echo "Enter something else"
esac