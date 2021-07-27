import socket
from classes.packet import Packet


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
        print(packet.packet_header.get_game_version())
        print(len(packet.packet_header))
        print(packet.get_packet_size())

        # print(len(bytearray(data)))
        # print(bytearray(data))
        # packet_header = PacketHeader(data[:2], data[2:3], data[3:4], data[4:5], data[5:6], data[6:14], data[14:18], data[18:22], data[22:23], data[23:24])
        # print(packet_header)



if __name__ == '__main__':
  main()