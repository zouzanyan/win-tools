import os
import re

str = 'netstat -aon|findstr "8887"'
res = os.popen(cmd=str).read()  # 查看被占用端口对应的 PID
print(res)
res = res.strip()
pattern = re.compile('LISTENING(.*)$')
data = re.findall(pattern, res)[0]
print(data.strip())

# str2 = 'taskkill /T /F /PID 839924'
# print(os.popen(cmd=str2).read())

input()
