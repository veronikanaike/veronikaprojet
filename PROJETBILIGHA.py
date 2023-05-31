#pip3 install python-nmap

import nmap
import os 
scanner = nmap.PortScanner()

def main():
    n = input("a- Network scanner\nb- Vulnerabilities Detection\nc- Exploit\nplease enter a letter : ")
    if n == 'a':
        nmap()
    if n == 'b':
        vuln()
    if n == 'c':
        os.system('msfconsole')
    else : 
        print("please choose between a and c")

def nmap():
    ip = input("\nplease enter the IP adress: ") 
    scanner.scan(ip , '1-1024')
    print(scanner.scaninfo())
    print(scanner[ip]['tcp'].keys())

def vuln():
   ip = input("\nplease enter the IP adress: ") 
   print(os.system('nmap -sv --script=vulscan.nse' +ip)) 



if __name__ == "__main__":
    main()
