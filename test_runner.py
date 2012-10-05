#!/usr/bin/python
import konjac
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("USAGE: konjac.py <NAME_OF_CHILD_PROGRAM>")
    child = konjac.spawn(sys.argv[1])
    konjac.speak(child, "sum", [1, 2, 3, 4])
    assert(int(konjac.listen(child)) == 10)
    konjac.kill(child)
