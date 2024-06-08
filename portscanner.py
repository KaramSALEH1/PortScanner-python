import socket 
from IPy import IP

def scan(target):
    ip_address = ip_converter(target)
    print ('\n' + '[-_0 Scanning target] ' + str(target))
    for port in range (20,100):
        port_scanner(ip_address , port)    

def ip_converter(ip):
    try :
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip) 

def getbanner(s):
    return s.recv(1024)

def port_scanner(ipad , port):
    try :
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipad , port))
        try:
            banner = getbanner(sock)
            print ('[+] port ' + str(port) +' is open : ' + str(banner.decode().strip('\n')))
        except:
            print ('[+] port ' + str(port) +' is open' )
    except: 
            pass

targets = input ("[+] Enter The IP Addresses (put ',' between them) :")
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)
