# -*- coding:utf-8 -*-
#!/usr/bin/env python3

'''
rainbow.py파일보다 프로세스를 더욱 많이 사용함으로써 더욱 빨리 생성된다.
'''

from hashlib import *
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def worker(arg):
    with open(f"C:\\Users\\hackcatml\\Desktop\\sha1dict_{arg}.txt", "w") as f:
        for i in range(arg * 10000000, (arg + 1) * 10000000):
            k = 0
            res = (str(i) + "salt_for_you")
            while k < 500:
                res = sha1(res.encode('utf-8')).hexdigest()
                k = k + 1

            f.write(res + ': ' + str(i) + '\n')


def main():
    with ProcessPoolExecutor(max_workers=10) as executor:
        for arg in range(1, 10):
            executor.submit(worker, arg)


if __name__ == '__main__':
    main()

# 출처: https://hackcatml.tistory.com/18
