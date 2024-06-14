# benchmark-script

## 并发效率
通过`ps -efL | grep <pid>` 查看进程中的线程。

输入: 进程pid

输出: 进程的线程列表

## perf相关(访存效率、缓存效率、分支效率、不同层次缓存访问缺失率)
`perf stat -e events_name [-p <pid> | -G <cgroup_name>]`

输入: 进程pid或者cgroup name

进程应当可以结束

输出: 运行期间PMC数据，每秒数据，某些PMC有缺失率等信息