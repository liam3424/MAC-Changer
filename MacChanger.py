#!/usr/bin/env python



import subprocess

import optparse

import re

praser = optparse.OptionParser()

praser.add_option('-i', '--interface', dest="interface", help="Interface to change its MAC address")

praser.add_option('-m', '--mac_address', dest='mac', help="What MAC address you want")

(options, arguments) = praser.parse_args()



class bcolors:

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'

    OKGREEN = '\033[92m'

    WARNING = '\033[93m'

    FAIL = '\033[91m'

    ENDC = '\033[0m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'

print()

print()

print()

print(bcolors.FAIL + r'         ______  ____    ')

print(bcolors.FAIL + r"/'\_/`\/\  _  \/\  _`\ ")

print(bcolors.FAIL + r'/\      \ \ \L\ \ \ \/\_\ ')

print(bcolors.FAIL + r'\ \ \__\ \ \  __ \ \ \/_/_')

print(bcolors.FAIL + r" \ \ \_/\ \ \ \/\ \ \ \L\ \ ")

print(bcolors.FAIL + r'  \ \_\\ \_\ \_\ \_\ \____/')

print(bcolors.FAIL + r'   \/_/ \/_/\/_/\/_/\/___/ ')

print()









mac_address = options.mac

specify_the_inter = options.interface



if not options.interface:

    praser.error(bcolors.WARNING + "[-] ERROR: Enter interface !")

elif not options.mac:

    print(bcolors.WARNING + "[-] ERROR: Enter interface !")



subprocess.call(f'ifconfig {specify_the_inter} down', shell=True)

subprocess.call(f'ifconfig {specify_the_inter} hw ether {mac_address}', shell=True)

subprocess.call(f'ifconfig {specify_the_inter} up', shell=True)

print()

print()

print()

subprocess.call('ifconfig', shell=True)



ifconfig_result = subprocess.check_output(['ifconfig', options.interface])

print(ifconfig_result)

mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

print()

print()

print()



print(bcolors.WARNING + f'[+] Succesfuly changed the MAC address, {mac_address_result.group(0)}')

