#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   _____   _             _   _      _____             __      __    __            ___
#  / ____| | |           | | | |    |  __ \            \ \    / /   /_ |          / _ \
# | (___   | |_    __ _  | | | | __ | |__) |  _   _     \ \  / /     | |         | | | |
#  \___ \  | __|  / _` | | | | |/ / |  ___/  | | | |     \ \/ /      | |         | | | |
#  ____) | | |_  | (_| | | | |   <  | |      | |_| |      \  /       | |    _    | |_| |
# |_____/   \__|  \__,_| |_| |_|\_\ |_|       \__, |       \/        |_|   (_)    \___/
#                                              __/ |
#                                             |___/
#-----------------------------------------------------------------------------
# @Author: Vaibhav Singh
# @Date: 2017-08-27
# @Email: vaibhav.singh.14cse@bml.edu.in
# @Github username: vaibhavsingh97
# @Website: https://vaibhavsingh97.me
# @Last Modified by: Vaibhav Singh
# @Last Modified Date: 2017-08-28
# @License: MIT License
# you can find your copy of the License
# https://vaibhavsingh97.mit-license.org/
#-----------------------------------------------------------------------------
import sys
import json
import requests
import os
import webbrowser
import threading
from clint.textui import colored, puts
from time import time as timer


class StalkPy():
    """class for StalkPy tool"""

    def __init__(self):
        with open('config.json') as data_file:
            self.data = json.loads(data_file.read())

    def clear(self):
        """for removing the clutter from the screen when necessary"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def space(self):
        """ for adding one linespace in the console"""
        print("")

    def head(self):
        """official banner for StalkPy printed in green color"""
        self.clear()
        stalkPyBanner = """
               _____   _             _   _      _____
              / ____| | |           | | | |    |  __ \\
             | (___   | |_    __ _  | | | | __ | |__) |  _   _
              \___ \  | __|  / _` | | | | |/ / |  ___/  | | | |
              ____) | | |_  | (_| | | | |   <  | |      | |_| |
             |_____/   \__|  \__,_| |_| |_|\_\ |_|       \__, |
                                                          __/ |
                                                         |___/

                                        - Vaibhav Singh (@ vaibhavsingh97)
                                        - Version 1.0
        """
        puts(colored.green(stalkPyBanner))

    def showDoc(self):
        documentation = """
        A simple python script to open the major social accounts connected to the
        specfic handle. Inspired from [HandleStalker](https://github.com/samanthakem/HandleStalker)

        - Simple to use: Built with love so it's easy to use.
        - single command will query any number of usernames
        - Text Highlighting is cross platform - Supports Linux, MAC, Windows for the terminal based highlighting.
        """
        puts(colored.cyan(documentation))
        self.space()

    def notification(self, flag):
        """messages for StalkPy tool which will be printed according to the flags"""
        if flag == 1:
            puts(colored.red("Error: wrong value entered! Please enter correct value."))
            space()
            flag = 0
        elif flag == 2:
            puts(colored.green("Success: Social account found. :)"))
            flag = 0
        elif flag == 3:
            puts(colored.red("No Social accounts found. :("))
            flag = 0

    def CleanedLink(self, url, username):
        return "https://www." + url + username

    def OpenLinks(self, user):
        for social_account_name in self.data:
            try:
                r = requests.get(self.CleanedLink(
                    self.data[social_account_name], user))
                if r.status_code == 200:
                    self.notification(2)
                    webbrowser.open(self.CleanedLink(
                        self.data[social_account_name], user), new=1)
                    puts(colored.green(social_account_name + ": ") +
                         colored.blue(self.CleanedLink(self.data[social_account_name], user)))
                r.close()
            except Exception as e:
                return e


if __name__ == '__main__':
    StalkPy().head()
    StalkPy().showDoc()
    start = timer()
    if (len(sys.argv) < 2):
        print("usage: \n python StalkPy.py [username1] [username2]...")
        StalkPy().space()
        puts(colored.red("Exiting..."))
    else:
        for i in range(1, len(sys.argv)):
            StalkPy().space()
            puts(colored.magenta("User: %s" % sys.argv[i]))
            t = threading.Thread(target=StalkPy().OpenLinks(sys.argv[i]))
            t.start()
            t.join()
    print("Elapsed Time: %s" % (timer() - start,))
