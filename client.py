import socket

cs = socket.socket()

cs.connect(("localhost", 9999))
cs.send(bytes("hello server", "utf-8"))
print(cs.recv(1024).decode())
