import socket

s = socket.socket()
print("socket created")
s.bind(("localhost", 9999))
s.listen()

while True:
    c, add = s.accept()
    print("one more client connected with address: ", add)
    c.send(bytes("connection sucessfull", "utf-8"))
    print(c.recv(1024).decode())
