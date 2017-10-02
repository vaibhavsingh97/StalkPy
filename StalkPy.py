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
# @Last Modified Date: 2017-08-30
# @License: MIT License
# you can find your copy of the License
# https://vaibhavsingh97.mit-license.org/
#-----------------------------------------------------------------------------
import json
import requests
import os
import webbrowser
import threading
import argparse
from clint.textui import colored, puts
from time import time as timer


class StalkPy():
    """class for StalkPy tool"""

    def __init__(self):
        with open('config.json') as data_file:
            self.data = json.loads(data_file.read())

    @classmethod
    def clear(self):
        """for removing the clutter from the screen when necessary"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def space(self):
        """ for adding one linespace in the console"""
        print("")

    @classmethod
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

    @classmethod
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

    @classmethod
    def notification(self, flag):
        """messages for StalkPy tool which will be printed according to the flags"""
        if flag == 1:
            flag = 0
            return "Success: "

        elif flag == 2:
            flag = 0
            self.space()
            return " account found. :)"

        elif flag == 3:
            flag = 0
            self.space()
            return " account not found. :("

    @classmethod
    def CleanedLink(self, url, username):
        return "https://www." + url + username

    def OpenLinks(self, user):
        for social_account_name in self.data:
            try:
                r = requests.get(self.CleanedLink(
                    self.data[social_account_name], user))
                if r.status_code == 200:
                    puts(colored.green(self.notification(1) +
                                       social_account_name + self.notification(2)))
                    webbrowser.open(self.CleanedLink(
                        self.data[social_account_name], user), new=1)
                    puts(colored.green(social_account_name + ": ") +
                         colored.blue(self.CleanedLink(self.data[social_account_name], user)))
                elif r.status_code == 404:
                    puts(colored.red(social_account_name + self.notification
                                     (3)))
                r.close()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    StalkPy().head()
    StalkPy().showDoc()
    start = timer()
    parser = argparse.ArgumentParser(
        description="StalkPy help you to stalk anyone ;)")
    parser.add_argument('-u', '--username', type=str,
                        help='Usename you want to stalk', nargs='+')
    parser.add_argument('-a', '--add', type=str,
                        help='Add social media account, pattern [account:link] e.g. spotify:spotify.com/user', nargs="+")
    args = parser.parse_args()

    if args.add is not None:
        social_media_accounts = args.add
        with open("config.json", "r+") as config_file:
            existing_acconts = json.load(config_file)
            config_file.seek(0);
            config_file.truncate()
            for account in social_media_accounts:
                try:
                    account_name, account = account.split(':')
                    existing_acconts[account_name] = account
                except ValueError:
                    print("Please enter account in the pattern [name:link] e.g. spotify:spotify.com/user")
            json.dump(existing_acconts, config_file, indent=2)

    if args.username is not None:
        username_list = args.username[0].split(",")
        for n in username_list:
            StalkPy().space()
            puts(colored.magenta("User: %s" % n))
            t = threading.Thread(target=StalkPy().OpenLinks(n))
            t.start()
            t.join()
        print("Elapsed Time: %s" % (timer() - start,))
