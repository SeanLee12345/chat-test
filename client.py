import socket
import time
import threading

PORT = 5050
SERVER = "173.255.245.184"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
nameU = ""


def connect():
    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.connect(ADDR)
    return client1


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)

def start1():
    connection1 = connect()
    while True:
        msg1 = (connection1.recv(1024).decode(FORMAT)).split(" ")
        name = msg1[2].strip()
        if name != nameU.strip():
            print((" ".join(msg1[2:]))) #Gets rid of numbers and brackets from msg1(previous line)



def start():
    # answer = input('Would you like to connect (yes/no)? ')
    # if answer.lower() != 'yes':
    #     return
    global nameU 
    nameU = input('What is your name? ') + ': '
    if input("Message (q for quit): ")== 'q':
        return
    thread = threading.Thread(target=start1, args=())
    thread.start()
    connection = connect()
    while True:
        msg = nameU + input("Me: ")
        if msg == "q":
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')


start()
