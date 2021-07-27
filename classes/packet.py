from .packetHeader import PacketHeader

class Packet():
    HEADER_SIZE = 24


    def __init__(self, data):
        self.packet_header = PacketHeader(data[:self.HEADER_SIZE])
        self.packet_body = data[self.HEADER_SIZE:]
        self.packet_size = len(self.packet_header) +len(self.packet_body) 

    def get_packet_size(self):
        return self.packet_size