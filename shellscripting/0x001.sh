#!/bin/bash

name="Name"
age=30

echo "Name: $name"
echo "Age: $age"

if [ $name ]; then
    echo "Your name is $name"
else
    echo "What is your name?"
fi