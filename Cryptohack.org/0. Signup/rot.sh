#!/bin/sh

a="OBGMTZX GBVX LHNE ZBGZXK"

for i in $(seq 25);do
    echo $i $a | tr $(printf %${i}s | tr ' ' '.')\A-Z A-ZA-Z
done
