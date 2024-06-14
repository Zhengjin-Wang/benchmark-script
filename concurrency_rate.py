import argparse
import subprocess
import csv

parser = argparse.ArgumentParser(description='Collect concurrency rate.')
parser.add_argument('--pid',default="", type=str, help='', required=True)
args = parser.parse_args()
pid = args.pid

ps = subprocess.Popen(('ps', '-efL'), stdout=subprocess.PIPE, text=True)
output = subprocess.check_output(('grep', pid), stdin=ps.stdout, text=True)
ps.wait()

rows = output.split('\n')
rows = rows[:-3]
with open(f'./concurrency_rate.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow([row])
    writer.writerow([f'Total thread(s): {len(rows)}'])

thread_num = len(rows)