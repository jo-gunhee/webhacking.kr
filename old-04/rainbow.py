# -*- coding:utf-8 -*-
#!/usr/bin/env python3

from hashlib import sha1

with open("file_index", "w") as f:
    for i in range(10000000, 100000000):
        '''
        범위를 전체 범위로 하면 굉장히 오랜시간이 걸리기 때문에 
        1/4 정도로 범위를 줄여서 찾는걸 추천한다.
        '''
        k = 0
        res = (str(i)+"salt_for_you")
        while k < 500:
            res = sha1(res.encode('utf-8')).hexdigest()
            k = k+1

        f.write(res + ':' + str(i) + '\n')

print("it's over")
