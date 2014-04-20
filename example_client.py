import socket
from req_resp_maker import randomHttp

f = randomHttp()

RESPIP = '127.69.69.69'
RESPPORT = 80
BUFFER_SIZE = 2048

# req
req_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
req_s.connect((RESPIP, RESPPORT))
while True:
    req_s.send(f.request())
    who_cares_req = req_s.recv(BUFFER_SIZE)

