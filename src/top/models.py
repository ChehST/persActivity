""" Объектное представление сети
"""

import subprocess


class Host:

    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address

    def ping(self):
        """ Проверяем доступность хоста """
        try:
            output = subprocess.check_output("ping -c 1 " + self.ip_address, shell=True)
            return "Host is up"
        except subprocess.CalledProcessError as e:
            return "Host is down"
