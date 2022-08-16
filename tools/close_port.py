import os
import re


def closeport():
    port = input("请输入将禁用的端口号")
    searchpid = f'netstat -aon|findstr "{port}"'
    res = os.popen(cmd=searchpid).read().strip()  # 查看被占用端口对应的 PID
    pattern = re.compile('LISTENING(.*)$')
    data = re.findall(pattern, res)
    if not data:
        print('该端口未被占用')
        return
    pid = data[0].strip()
    usercheck = input('该端口的进程为 ' + pid + ' ,确定将其杀死?(y/n)')
    if usercheck == 'y':
        killpid = f'taskkill /T /F /PID {pid}'
        print(os.popen(cmd=killpid).read())
    else:
        print('已撤销操作')
        return
