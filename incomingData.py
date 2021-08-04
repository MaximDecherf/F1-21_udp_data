import socket
from packets.packet import Packet


def main():
    sock = setup_udp_con()
    incoming_data(sock)

def setup_udp_con(UDP_IP = None, UDP_PORT = None):
    UDP_IP = "127.0.0.1"
    UDP_PORT = 20777

    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    return sock



    
def incoming_data(sock):
    while True:
        data, addr = sock.recvfrom(2048) # buffer size is 2048 bytes
        packet = Packet(data)
        
        
        if packet.packet_body.packet_id == 5:
            print(packet.packet_body.body_data)

            #if you are only intrested in certain types of packets for example Lap data,
            #you can set the packet.packetbody == 2 and you will only get the lapdata
        

   



if __name__ == '__main__':
  main()