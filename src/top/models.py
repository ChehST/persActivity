""" Объектное представление сети
"""

import subprocess


class Host:
    """ Класс описывающий объект Host
    """
    def __init__(self, hostname, ip_address, mac_address):
        self.hostname = hostname
        self.ip_address = ip_address
        self.mac_address = mac_address

    def ping(self):
        """ Проверяем доступность хоста """
        try:
            output = subprocess.check_output("ping -c 1 " + self.ip_address, shell=True)
            return "Host is up "
        except subprocess.CalledProcessError as e:
            return "Host is down"

class Network(Host):
    """ Класс описывающий объект Network
        Принимает объекты класса Host
    """

    def __init__(self, net_mask):
        self.net_mask = net_mask
        self.hosts = []

    def add_host(self, host):
        self.hosts.append(host)

    def ping_hosts(self):
        for host in self.hosts:
            print(host.ping())

    def list_hosts(self):
        for host in self.hosts:
            print(host.ip_address)
