
from helper import log
import parameters
import adb


def connect_device():
    adb.reset()
    try:
        addr = parameters.device_addr
        adb.connect(addr)
    except RuntimeError as e:
        log(e)
        return -1

    log(f'connect to {addr} successfully!')
    return 0


def game_prepare():
    # connect to device
    if connect_device() != 0: return -1

    # launth the game
    return 0

def surge_routine():
    return


def normal_routine():
    return
