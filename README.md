# benchmark-script

## 并发效率

concurrency.py

通过`ps -efL | grep <pid>` 查看进程中的线程。

输入: 进程pid

输出: 进程的线程列表

## perf相关(访存效率、缓存效率、分支效率、不同层次缓存访问缺失率)

perf_test.py

`perf stat -e events_name [-p <pid> | -G <cgroup_name>]`

在进程启动后运行脚本，原进程运行结束后脚本会输出统计信息

输入: 进程pid或者cgroup name

输出: 运行期间PMC数据，每秒数据，某些PMC有缺失率等信息

## 算力/缓存/内存/带宽资源利用率

utilization.sh
    - log_mem.sh

`mpstat 1`

`pqos`

`free -h`

输入: 无

输出: CPU资源利用率，带宽利用率，内存占用，分别保存在三个文件中(mpstat.log, pqos.log, mem_utilization.log)

## 硬件信息

device_info.sh

`lscpu`

`sudo dmidecode -t memory`

输入: 无

输出: 硬件信息(device.log) 内存信息(mem_info.log)

## 内存时延

latency.sh

输入: 无

输出: 内存带宽、跨Numa延迟、缓存带宽、缓存时延(L1d L2 L3)