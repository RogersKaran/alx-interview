#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    status_codes = [200] * 50 + [301] * 25 + [400] * 15 + [401] * 20 + [403] * 20 + [404] * 25 + [405] * 15 + [500] * 35
    status_code = random.choice(status_codes)
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        status_code,
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

