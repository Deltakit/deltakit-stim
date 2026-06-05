import sys

import deltakit_stim


def main_argv():
    deltakit_stim.main(command_line_args=sys.argv[1:])


if __name__ == '__main__':
    main_argv()
