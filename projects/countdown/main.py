import time,subprocess

x=10
for i in range(1,x+1,1):
    time.sleep(1)
    print(i)
    if i==x:
        subprocess.Popen(['vlc','-vvv','./stan.mp4'])