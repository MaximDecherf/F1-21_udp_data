from .packetHeader import PacketHeader
from .packetBody import PacketBody

class Packet():
    HEADER_SIZE = 24
    

    def __init__(self, data):
        self.packet_header = PacketHeader(data[:self.HEADER_SIZE])
        self.packet_body = PacketBody(data[self.HEADER_SIZE:], self.packet_header.packet_id)
        self.packet_size = len(self.packet_header) +len(self.packet_body)

    #TODO make filter for different packet ids so it wont do al the computations if u dont want the packet info 

    def __len__(self):
        return self.packet_size