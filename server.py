import socket
import pandas as pd
import time
import plot
import os
import threading
from _thread import *

def client_input(conn, addr, number_of_client, first_try):
    while True:
        try:
            conn.send(bytes('1', 'utf-8'))
            name = str(str(number_of_client) + '_' + str(time.clock()) + '.csv')
            f = open(name, "w")
            data = conn.recv(8192).decode('utf-8')
            f.write(data)
            if not data:
                conn.close()
                break
            f.close()
            plot.create_plot(name, number_of_client, first_try)
            first_try = False
            print("---Data recieved---" + str(conn))
            os.remove(name)
            time.sleep(5)
        except Exception as e:
            print(str(e))
            conn.close()
            print('---Connection closed---' + str(conn))
            break

def main():
    sock = socket.socket()
    sock.bind(('', 7777))
    print('---Finding client---')

    number_of_client = 0

    while True:
        first_connection = True
        number_of_client +=1
        sock.listen(1)
        print("---Socket is listening---") 
        conn, addr = sock.accept()
        print('---Connection established---' + str(conn))
        start_new_thread(client_input, (conn, addr, number_of_client, first_connection))
        #client_input(conn, addr, number_of_client, first_connection)
    print('---Connection end---')

    sock.close()

if __name__ == "__main__":
    main()