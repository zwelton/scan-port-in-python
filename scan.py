import socket

print("""
[1] - insert ip
[X] - insert specific port
[X] - range 100 ports
[X] - range 1000 ports
[X] - common ports
[X] - all ports

[0] - exit
""")

loop = True
while loop:
    op = str(input('choose an option above: '))

    if op == '1':
        host = input("insert ip: ")

        print("""
[X] - insert ip
[2] - insert specific port
[3] - range 100 ports
[4] - range 1000 ports
[5] - common ports
[6] - all ports

[0] - exit
""")

    elif op == '2':
        port = input("enter the port: ")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.7)
        code = client.connect_ex((host, int(port)))
        if code == 0:
            print("[+] {} open".format(port))
        else:
            print("[+] {} closed".format(port))
        loop = False

    elif op == '3':
        ports = range(100)
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.4)
            code = client.connect_ex((host, port))
            if code == 0:
                print("[+] {} open".format(port))
            else:
                print("[+] {} closed".format(port))
            loop = False

    elif op == '4':
        ports = range(1000)
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.4)
            code = client.connect_ex((host, port))
            if code == 0:
                print("[+] {} open".format(port))
            else:
                print("[+] {} closed".format(port))
            loop = False

    elif op == '5':
        ports = [21, 22, 23, 25, 53, 80, 135, 139, 443, 445, 3306, 8080, 8081, 8443]
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.4)
            code = client.connect_ex((host, port))
            if code == 0:
                print("[+] {} open".format(port))
            else:
                print("[+] {} closed".format(port))
            loop = False

    elif op == '6':
        ports = range(65536)
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.4)
            code = client.connect_ex((host, port))
            if code == 0:
                print("[+] {} open".format(port))
            else:
                print("[+] {} closed".format(port))
            loop = False

    elif op == '0':
        loop = False
        break

    else:
        print('invalid option. going out...')
        break
