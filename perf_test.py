import argparse
import subprocess
import re
import csv
    
def get_pmc_string(pmc_file):
    pmc_string = ""
    with open(pmc_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            pmc_string += ' -e '
            pmc_string += line
    return pmc_string

def get_pmc_list(pmc_file):
    return get_pmc_string(pmc_file).split(' -e ')[1:]

def benchmark(cmd, pmc_list):

    benchmark = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    _, output = benchmark.communicate()    # 等待runner停止

    csv_data = []
    time_elapsed = re.findall("(\d+\.\d+) seconds time elapsed", output)[0]
    time_elapsed = float(time_elapsed)
    csv_data.append(['time_elapsed', time_elapsed])

    for pmc in pmc_list:
        
        data = [pmc]
        val = int(re.findall(f'(\d+)\s+{pmc}', output)[0])
        data.append(val)
        data.append(val/time_elapsed)
        
        match = re.search(f"{pmc}\s+#\s+([^\(]+)\(", output)

        if match:
            data.append(match.group(1))
        
        csv_data.append(data)

    return csv_data

parser = argparse.ArgumentParser(description='Collect perf-related data.')
parser.add_argument('--pid',default="", type=str, help='')
parser.add_argument('--cgroup',default="", type=str, help='')
args = parser.parse_args()
pid = args.pid
cgroup = args.cgroup
if pid and cgroup or pid is None and cgroup is None:
    print("Incorrect argument input!")
    exit()

pmc_file = "pmc.txt"
pmc_string = get_pmc_string(pmc_file)
pmc_list = get_pmc_list(pmc_file)

header = ['PMC', 'data', "data per second", "rate"]
csv_data = [header]

if pid:
    target = f'-p {pid}'
elif cgroup:
    target = f'-G {cgroup}'
cmd = 'perf stat --no-big-num ' + pmc_string + " " + target
csv_data += benchmark(cmd, pmc_list)

with open(f'./perf_test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)