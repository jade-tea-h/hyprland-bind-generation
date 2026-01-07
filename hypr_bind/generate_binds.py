#!/usr/bin/python

import argparse as ap
import sys

MODKEYS = 'CTRL', 'ALT', 'SUPER', 'SHIFT'

parser = ap.ArgumentParser(
    prog='generate_binds',
    description='Generates a hyprland configuration file of keybinds'
)

parser.add_argument('filename', default='')
parser.add_argument('-m', '--mouse-modkey', dest='mouse_modkey', metavar='MODKEY', default='SUPER')
parser.add_argument('-k', '--keyboard-modkey', dest='keyboard_modkey', metavar='MODKEY', default='ALT')

args = parser.parse_args()

if args.filename == '':
    pass

binds: list[str] = []

def get_bind(*args: Sequence[str]):
    string = "bind="
    for arg in args:
        string += arg + ', '
    string = string[:-2]
    return string

# Quick keybinds for default programs, $PROGRAM for programs set as environment variables
programs: dict[str,str] = {'q': "$TERMINAL", 'a': "$BROWSER", 'r': "$RUNNER"}

for key, program in programs.keys():
    binds.append(get_bind(args.mouse_modkey, key, 'exec', program))
binds.append('')

# Keybinds for navigating between windows
motion: dict[str,str] = {'h': LEFT, 'j': DOWN, 'k': UP, 'l': RIGHT,
                         'left': LEFT, 'right': RIGHT, 'up': UP, 'down': DOWN}

for key, direction in motion.keys():
    binds.append(get_bind(args.mouse_modkey, key, 'movefocus', direction))
    binds.append(get_bind(args.keyboard_modkey, key, 'movefocus', direction))
binds.append('')


f = open()
