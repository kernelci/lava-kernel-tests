import subprocess
import re

proc = subprocess.Popen(['./cpufreq-ljt-stress-test'], stdout=subprocess.PIPE)

cpu = -1
for line in iter(proc.stdout.readline, ''):
    current_line = line.rstrip()
    if 'Testing CPU' in current_line:
        cpu += 1
    match = re.match(u'\s+\d+\sMHz', current_line)
    if match:
        test_case = match.group().replace(" ", "")
        if 'OK' in current_line:
            test_result = 'cpu' + str(cpu) + '_' + test_case + ' : ' + 'pass'
            print test_result
        elif 'SKIPPED' in current_line:
            test_result = 'cpu' + str(cpu) + '_' + test_case + ' : ' + 'skip'
            print test_result
        else:
            test_result = 'cpu' + str(cpu) + '_' + test_case + ' : ' + 'fail'
            print test_result
