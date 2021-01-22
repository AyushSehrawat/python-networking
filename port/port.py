import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print(f'[+] Scanning Target - {target}')
    for ports in range(1,100):
        scan_port(converted_ip,ports)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress,port))
        try:
            banner = get_banner(sock)
            data = banner.decode().strip('\n')
            print(f'{port} - {data}')
        except:
            print(f'[+] Port {port} : Open')
    except:
        pass

if __name__ == '__main__':

    targets = input('[+] Enter Target/s (for multiple separate with ,) ADDRESS: ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
