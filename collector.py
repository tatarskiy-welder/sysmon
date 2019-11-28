import psutil
import platform
import json
import os
import socket
import pandas as pd
import time


def collector():
    if platform.system() == 'Windows':
        path = "C:\\"
    else:
        path = "/"

    info = {'hostname': socket.gethostname(),
            'IP': socket.gethostbyname(socket.gethostname()),
            'cpu_version': platform.processor(),
            'cpu_load': psutil.cpu_percent(interval=1, percpu=False),
            'cpu_cores': psutil.cpu_count(),
            'mem_total': psutil.virtual_memory().total / 1024 ** 2,
            'mem_load': psutil.virtual_memory().available / 1024 ** 2,
            'pids_number': len(psutil.pids()),
            'user': os.getlogin(),
            'OS': platform.system(),
            'disk_free': psutil.disk_usage(path).free / 1024 ** 2
            }

    df = pd.DataFrame(info, index=[0])
    name = str(time.clock()) + "data.csv"
    df.to_csv(name)
    return name


if __name__ == "__main__":
    collector()
