import sys

import robot


def main():
    if robot.game_prepare() != 0: return -1
    robot.surge_routine()


if __name__ == '__main__':
    sys.exit(main())
    