import time

with open('../Data/portfolio.csv') as fh:
    while True:
        line = fh.readline()    # readline does not throw error at EOF
        if not line:
            print('EOF. Reading empty line...')
            time.sleep(1)
        print(line, end='')
        time.sleep(.1)
