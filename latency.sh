#!/bin/bash

./mlc > mlc.log

L3=$(lscpu | grep L3 | grep -oP '\d+(?=K)')
L2=$(lscpu | grep L2 | grep -oP '\d+(?=K)')
L1=$(lscpu | grep L1d  | grep -oP '\d+(?=K)')

echo "L1d latency" >> mlc.log
echo "" >> mlc.log
./mlc --idle_latency -b${L1}k--t10 -c0 >> mlc.log

echo "L2 latency" >> mlc.log
echo "" >> mlc.log
./mlc --idle_latency -b${L2}k--t10 -c0 >> mlc.log

echo "L3 latency" >> mlc.log
echo "" >> mlc.log
./mlc --idle_latency -b${L3}k--t10 -c0 >> mlc.log