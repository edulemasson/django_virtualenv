#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

    from django.core.management import execute_from_command_line

    os.system('clear')

    print " _                 __  _     _   _   _ ___ __"
    print "| \   |  /\  |\ | /__ / \   |_) / \ / \ | (_"
    print "|_/ \_| /--\ | \| \_| \_/   |_) \_/ \_/ | __)"
    print "                         by Eduardo Le Masson"

    execute_from_command_line(sys.argv)
