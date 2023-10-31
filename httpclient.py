#!/usr/bin/env python3

import socket

def send_msg(sock, msg):
    sock.sendall(msg)

def recv_msg(sock, chunk_len=1024):
    while True:
        received_chunk = sock.recv(chunk_len)
        if not received_chunk:
            break
        yield received_chunk

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 80))
    request_text = 'GET / HTTP/1.0\r\n\r\n'
    send_msg(client_socket, request_text.encode('ASCII'))
    received_bytes = b''.join(recv_msg(client_socket))
    print(received_bytes.decode('ASCII'))
    client_socket.close()

if __name__ == '__main__':
    main()
