#!/bin/bash

for i in {1..21}
do
    file="Ex2/ex$i.py"
    echo -e "\n--- Executando $file ---"
    python3 "$file"
done
