#non-color version

import socket
from pyngrok import ngrok
import sys

op = int(input("ROOM\n------\n[0] Host\n[1] Join\nOption> "))

ngrokop = int(input("NGROK SETUP\n-------------\n[0] Port forward\n[1] Don't port forward\nOption> "))
if ngrokop == 0:
    #ngrok
    host = input("[?] Host: ")
    port = int(input("[?] Port: "))
    pf = ngrok.connect(port,"tcp")
    dest_port = int(pf.split(":")[2])
    print("The destination port is {}".format(dest_port))
    username = input("[?] Username: ")
    if op == 0:
        #host
        server = socket.socket()
        try:
            server.bind((host,dest_port))
            server.listen()
            while True:
                client,(ip,port) = server.accept()
                while True:
                    your_msg = input("{}: ".format(username))
                    client.send("{}: {}".format(username,your_msg).encode())
                    msg_rx = client.recv(4096)
                    print(msg_rx.decode())
                    break
        except Exception as e:
            print("Something went wrong while hosting!\n{}".format(e))
    elif op == 1:
        #join
        print("[i] Keep in mind that you won't be port forwarding since you're only joining the room :)")
        host = input("[?] Host: ")
        port = int(input("[?] Port: "))
        username = input("[?] Username: ")
        client = socket.socket()
        try:
            client.connect((host,port))
            while True:
                msg_rx = client.recv(4096)
                print(msg_rx.decode())
                break
            while True:
                your_msg = input("{}: ".format(username))
                client.send("{}: {}".format(username,your_msg).encode())
                break
        except Exception as e:
            print("Something went wrong while joining!\n{}".format(e))
    else:
        print("Hm, next time please select a proper option :) -0x74ngly")
        sys.exit()
elif ngrokop == 1:
    #no ngrok
    if op == 0:
        #host
        print("Hm, good luck hosting then... (unless if you want to join rooms)")
        host = input("[?] Host: ")
        port = int(input("[?] Port: "))
        username = input("[?] Username: ")
        if op == 0:
            server = socket.socket()
            try:
                server.bind((host,port))
                server.listen()
                while True:
                    client,(ip,port) = server.accept()
                    while True:
                        msg_rx = client.recv(4096)
                        print(msg_rx.decode())
                        break
                    while True:
                        your_msg = input("{}: ".format(username))
                        client.send("{}: {}".format(username,your_msg).encode())
                        break
            except Exception as e:
                print("Something went wrong while hosting!\n{}".format(e))
    elif op == 1:
        #join
        host = input("[?] Host: ")
        port = int(input("[?] Port: "))
        username = input("[?] Username: ")
        client = socket.socket()
        try:
            client.connect((host,port))
            while True:
                your_msg = input("{}: ".format(username))
                client.send("{}: {}".format(username,your_msg).encode())
                msg_rx = client.recv(4096)
                print(msg_rx.decode())
        except Exception as e:
            print("Something went wrong while joining!\n{}".format(e))
    else:
        print("Hm, next time please select a proper option :) -0x74ngly")
        sys.exit()
else:
    print("Hm, next time please select a proper option :) -0x74ngly")
    sys.exit()