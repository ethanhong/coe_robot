
import subprocess

import parameters
from helper import log


# Constants
TAP_DELAY = parameters.delay_between_taps


def run(cmd, timeout=30, retry=3):
    for _ in range(retry):
        try:
            process = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, timeout=timeout)
            out = process.stdout
            return out
        except subprocess.TimeoutExpired:
            log('[adb command timeout]:', cmd)
            # subprocess.run('adb disconnect {}'.format(cur_serial_no))
            # subprocess.run('adb connect {}'.format(cur_serial_no))
            continue
    else:
        raise subprocess.TimeoutExpired


def reset():
    run('adb kill-server')


def connect(addr):
    out = run(f'adb connect {addr}')
    if f'connected to {addr}' not in out:
        raise RuntimeError(f'cannot connect to device: {addr}')
