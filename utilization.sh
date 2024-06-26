#!/bin/bash

# 启动子脚本
./log_mem.sh > utilization_mem.log &
pid1=$!
mpstat 1 > utilization_cpu.log &
pid2=$!
pqos -r 1 > utilization_bw.log &
pid3=$!

# 定义信号处理器
trap 'kill -SIGTERM $pid1 $pid2 $pid3' SIGINT SIGTERM

# 等待子脚本结束
wait $pid1
wait $pid2
wait $pid3