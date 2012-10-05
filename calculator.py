#!/usr/bin/python
import sys
import os
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

while(True) :
    cmd = raw_input()
    if (cmd == "exit"):
        break
    elif (cmd == "sum"):
        count = int(raw_input())
        _sum = 0
        def add_to_sum(num):
            global _sum
            _sum += num
        map(add_to_sum,
            [int(raw_input()) for i in range(0, count)])
        print _sum
    else:
        sys.stderr.write("unknown command! %s \n" % (cmd,))
        break;
