import socket
from .packets.packet import Packet


class F1Data:

    PACKET_SIZE_MAPPER = {'MOTION': 1464, 'SESSION': 625, 'LAP_DATA': 970, 'EVENT': 36, 'PARTICIPANTS': 1257, 'CAR_SETUPS': 1102,
                          'CAR_TELEMETRY': 1347, 'CAR_STATUS': 1058, 'FINAL_CLASSIFICATION': 839, 'LOBBY_INFO': 1191, 'CAR_DAMAGE': 882, 'SESSION_HISTORY': 1155}

    def __init__(self, port=20777, ip="127.0.0.1", filter_packets=None):
        self.udp_ip = ip
        self.udp_port = port
        self.filter_packets = filter_packets
        if type(filter_packets) == list:
            allowed_packets = []
            for packet in filter_packets:
                allowed_packets.append(self.PACKET_SIZE_MAPPER[packet])
            self.filter_packets = allowed_packets

    def run(self, sock):
        return self.incoming_data(sock)

    def setup_udp_con(self, ip=None, port=None):
        if ip == None and port == None:
            ip = self.udp_ip
            port = self.udp_port
        sock = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP
        sock.bind((ip, port))
        return sock

    def incoming_data(self, sock):
        data, addr = sock.recvfrom(2048)  # buffer size is 2048 bytes
        if type(self.filter_packets) == list:
            if len(data) in self.filter_packets:
                packet = Packet(data)
                return packet.packet_body.body_data
        else:
            packet = Packet(data)
            return packet.packet_body.body_data
