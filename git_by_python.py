import os
import time

def my_cmd(my_cmd):
    res = os.popen(my_cmd)
    return res.read()

if __name__ == '__main__':
    my_r = my_cmd(r'D:')
    print(my_r)
    my_r = my_cmd(r'cd D:\myPython\20200130_git_by_python')
    print(my_r)
    my_r = my_cmd(r'git status')
    print(my_r)
    print('now git add .')
    my_r = my_cmd(r'git add .')
    print(my_r)
    print('now git commit')
    my_r = my_cmd(r'git commit -m "python commit"')
    print(my_r)
    print('now git push')
    my_r = my_cmd(r'git push -u origin master')
    print(my_r)
