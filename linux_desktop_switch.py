#!/usr/bin/python3

# Firewall rule:
# ufw allow from 192.168.66.0/24 to any port 48484 proto udp

import dbus
import os
import socket

DIR_MAP = [ "UP", "RIGHT", "DOWN", "LEFT" ]

UDP_IP = '' # == INADDR_ANY
UDP_PORT = 48484

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    direction = DIR_MAP[data[0]]
    print("Switch desktop", direction)
    print(os.system(f"dbus-send --session --type=method_call --dest=org.gnome.Shell /org/gnome/Shell org.gnome.Shell.Eval string:'global.workspace_manager.get_active_workspace().get_neighbor(Meta.MotionDirection.{direction}).activate(global.get_current_time());'"))
