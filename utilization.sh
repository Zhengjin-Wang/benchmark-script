#!/bin/bash

# 启动子脚本
./log_mem.sh > mem_utilization.log &
pid1=$!
mpstat 1 > mpstat.log &
pid2=$!
pqos -r 1 > pqos.log &
pid3=$!

# 定义信号处理器
trap 'kill -SIGTERM $pid1 $pid2 $pid3' SIGINT SIGTERM

# 等待子脚本结束
wait $pid1
wait $pid2
wait $pid3