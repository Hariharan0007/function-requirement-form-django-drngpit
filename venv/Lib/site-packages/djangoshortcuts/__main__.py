import os
import sys


current_path = os.path.dirname(__file__)
sys.path.insert(0, os.path.dirname(current_path))


from djangoshortcuts import print_help

def main():
    print_help()

if __name__ == '__main__':
    main()
