#!/bin/bash

for i in {1..15}
do
    file="ex$i.py"
    echo -e "\n--- Executando $file ---"
    python3 "$file"
done

