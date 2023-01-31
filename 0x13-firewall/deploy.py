#!/usr/bin/python3
"""Distribute an archve to the web servers"""

from fabric.api import local, put, run, env
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['54.160.126.209', '54.208.232.134', '18.233.62.177']

def do_run():
    put("0-block_all_incoming_traffic_but")
    run("chmod a+x 0-block_all_incoming_traffic_but")
    run("sudo ./0-block_all_incoming_traffic_but")
