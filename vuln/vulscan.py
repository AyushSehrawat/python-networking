import ports

targets_ip = input('[+] Ip: ')
port_number = int(input('[+] Port: '))
vul_file = input('Path: ')
print('\n')

target = ports.PortScan(targets_ip,port_number)
target.scan()

with open(vul_file,'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for  line in file.readlines():
            if line.strip() in banner:
                print(f'[!!] Vulnerable Banner {banner} : {target.open_ports[count]}')

        count +=1