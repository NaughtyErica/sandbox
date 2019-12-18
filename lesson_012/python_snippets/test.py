# Базовый привет на ассинхоронность с помощью итераторов по видео-лекциям Олега Молчанова

import socket
from select import select

tasks = []
to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()
    while True:
        yield ('read', server_socket)
        client_socket, addr = server_socket.accept() # серверный сокет читает
        print('Connection from', addr)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield ('read', client_socket)
        request = client_socket.recv(4096) # клиентский сокет читает
        if not request:
            break
        else:
            responce = 'Hello world\n'.encode()
            yield ('write', client_socket)
            client_socket.send(responce) # клиентский сокет пишет
    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):
        # из словарей to_read и  to_write мы извлекаем генераторы и добавляем их в список задач tasks
        while not tasks: # входим в цикл если tasks не пустой
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
            # Селект делает выборку сокетов, кторые уже готовы что-то проичтать из буфера или записать в него
            # (отфильтровывает функции по готовкности)(если буфер наполнился - из него можно прочитать и наоборот)
            for sock in ready_to_read:
                tasks.append(to_read.pop(sock)) # извлекается из словаря значение ключа sock,
                # которым является генератор
            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))
        try:
            task = tasks.pop(0)
            reason, sock = next(task) # вызываем next и передаем туда генератор, кторый лежит в task
            if reason == 'read':
                to_read[sock] = task # заполнятем соответствующике (для чтения или для записи)словари,
                # создававая ключ sock со значением соответствующего объекта генератора
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('Done')


tasks.append(server())
event_loop()
