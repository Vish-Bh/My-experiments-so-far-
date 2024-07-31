import time
def countdown(start):
    while True:
        sec=(start%60)
        mint=(start//60)%60
        hrs=(start//360)%24
        print(f'\r {mint:0} mint and sec{sec:} and hr {hrs}')
        time.sleep(1)
        start-=1
countdown(86400)
#2*60 180*60    10800\\
24*60*60
