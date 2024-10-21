import socket, threading, time, ipaddress
def TCP_connect(ip, port_number, delay, output):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(delay)
    try:
        sock.connect((ip, port_number))
        output [port_number] = 'is listening'
    except:
        output[port_number] = ''



def scan_ports(host_ip, delay):

    threads = []
    output = {}
    try:
        for i in range(10000):
         t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
         threads.append(t)

        for i in range(10000):
         threads[i].start()

        for i in range(10000):
         threads[i].join()

        for i in range(10000):
            if output[i] == 'is listening':
             print(str(i) + ': ' + output[i])
        print("\n Scan completed (^人^)\n")
        time.sleep(3)
    except KeyboardInterrupt:
        print("\nScan stopped by user\n")
        for t in threads:
            t.join()
        return
    except:
        TimeoutError
        print("Timeout error （＞人＜；\n")


        

def main():
    while True:
        print("""     ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓████████▓▒░  ░▒▓███████▓▒░ ░▒▓████████▓▒░  ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓███████▓▒░  ░▒▓████████▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
    ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
    ░▒▓█▓▒░        ░▒▓████████▓▒░    ░▒▓█▓▒░      ░▒▓██████▓▒░  ░▒▓██████▓▒░   ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓███████▓▒░  ░▒▓██████▓▒░   
    ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░            ░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░            ░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
     ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓███████▓▒░  ░▒▓████████▓▒░  ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ 
                                                                                                                                       
      """)
        print("****************************************************************************************************************************************************************")
        print("Developed on the CTP CIT")
        print("Authors: Andres B.A., Santiago S.C. and Isaac F.G.")
        print("2024")
        print("****************************************************************************************************************************************************************")
        print("")
        print("Select and option ᓚᘏᗢ")
        try:
            opt = int(input("1. Port Scanner \n2. DOS Pen Tester\n3. Antivirus (STILL IN DEVELOPMENT X﹏X)\nYour input: "))
            if opt == 1:
                host_ip = input("Enter host IP: ")
                try:
                    ip_address_obj = ipaddress.ip_address(host_ip)
                    print("You entered a valid ip address.")
                except:
                    print("You entered an invalid ip address")
                    break
                delay = int(input("How many seconds the socket is going to wait until timeout: "))
                scan_ports(host_ip, delay)
            elif opt == 2:
                print("This option is still in development.")
            elif opt == 3:
                print("This option is still in development.")
        except opt>3:
            print("Invalid input (っ °Д °;)っ. Please try again .")
            main()




if __name__ == "__main__":
    main()