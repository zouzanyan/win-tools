import os


str = 'netstat -aon|findstr "8887"'
print(os.popen(cmd=str).read())  # 查看被占用端口对应的 PID


str2 = 'taskkill /T /F /PID 839924'
print(os.popen(cmd=str2).read())

input()