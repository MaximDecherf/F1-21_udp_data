
class PacketEventData:

    EVENT_CODES = {'SSTA' : 'event', 'SEND' : 'event' }

    def __init__(self, body_data):
        self.body_data = body_data
        print( int.from_bytes(body_data[0:4], byteorder='little'))