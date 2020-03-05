
import socket
from datetime import datetime


class SocketWriter(object):

    def __init__(self, ip, port):
        self._socket = socket.socket(socket.AF_INET,
                                     socket.SOCK_DGRAM)
        self._ip = ip
        self._port = port

    def write(self, message):
        self._socket.send(message, (self._ip, self._port))


def log(message, destination):
    destination.write('[{}] - {}'.format(datetime.now(), message))


upd_logger = SocketWriter('1.2.3.4', '9999')
log('Something happened', udp_destination)

