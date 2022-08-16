from tools import close_port
import os
import time


def showmenu():
    print('****    windows小工具v1.0    ****')
    print('         1.关闭端口占用')
    print('')


if __name__ == '__main__':
    while 1:
        showmenu()
        userin = input('请在此选择$')
        if userin == '1':
            close_port.closeport()
            time.sleep(1)
            i = os.system('cls')
            continue
        else:
            i = os.system('cls')
            continue
