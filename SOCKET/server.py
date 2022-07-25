import socket
import sys


def create_socket():
    try:
        global host, port, s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 9999
    except socket.error as error:
        print("Socket creation error: " + str(error))


def bind_socket():
    try:
        global host, port
        s.bind((host, port))
        s.listen(5)
        print(f"Binding the PORT {str(port)}")

    except socket.error as error:
        print(f"Binding error: {error}\nReconnecting......")
        bind_socket()


def accept_connection():
    client, address = s.accept()
    print(
        f"Connection established with IP [{address[0]}] PORT [{str(address[1])}]")
    send_command(client)
    client.close()


def send_command(connection):
    while True:
        cmd = input()
        if cmd == "quit":
            s.close()
            sys.exit()
        if len(cmd.encode("utf-8")) > 0:
            connection.send(str.encode(cmd))
            client_response = str(connection.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    accept_connection()


main()
