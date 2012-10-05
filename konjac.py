import os
import sys
import time
import subprocess

DEBUG = True

def blog(msg, ):
    if DEBUG:
        print msg.rstrip()

def spawn(cmd,):
    blog("SYS: OPENING " + cmd + "...")
    return subprocess.Popen(cmd,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            #env={"PATH": ".:$PATH"},
                            )

def speak(p, cmd, args=[],):
    args = map(str, args)
    p.stdin.write(cmd + "\n")
    p.stdin.write(str(len(args)) + "\n")
    map(lambda x : p.stdin.write(x + "\n"), args)
    blog("CMD: " + cmd)
    blog("ARGS: " + ' '.join(args)) if args else None

def listen(p, ):
    result = p.stdout.readline().rstrip()
    blog("RECV: " + result)
    return result

def kill(p, ):
    blog("SYS: KILLING...")
    speak(p, "exit")
    p.terminate()
    if touch(p) :
        blog("SYS: KILLED")
    else:
        blog("SYS: KILLING FAILED AFTER 1SEC")

def touch(p, ):
    time.sleep(1)
    return p.poll()
