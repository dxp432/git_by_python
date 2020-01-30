import os
import time


def my_cmd(my_cmd_str):
    res = os.popen(my_cmd_str)
    return res.read()


if __name__ == '__main__':
    my_r = my_cmd(r'D:')
    print(my_r)
    my_r = my_cmd(r'cd D:\dxp\github\2020\github_page')
    print(my_r)
    my_r = my_cmd(r'git init')
    print(my_r)
    print('now git add .')
    my_r = my_cmd(r'git add .')
    print(my_r)

    print('now git commit')
    my_r = my_cmd(r'git commit -m "python commit"')
    print(my_r)

    print('now remote')
    my_cmd(r'git remote add origin https://github.com/dxp4321/dxp4321.github.io.git')
    print(my_r)

    print('now git push')
    my_r = my_cmd(r'git push -u origin master')
    print(my_r)
