#!/bin/bash

./mlc > latency.log

L3=$(lscpu | grep L3 | grep -oP '\d+(?=K)')
L2=$(lscpu | grep L2 | grep -oP '\d+(?=K)')
L1=$(lscpu | grep L1d  | grep -oP '\d+(?=K)')

echo "L1d latency" >> latency.log
echo "" >> latency.log
./mlc --idle_latency -b${L1}k--t10 -c0 >> latency.log

echo "L2 latency" >> latency.log
echo "" >> latency.log
./mlc --idle_latency -b${L2}k--t10 -c0 >> latency.log

echo "L3 latency" >> latency.log
echo "" >> latency.log
./mlc --idle_latency -b${L3}k--t10 -c0 >> latency.log