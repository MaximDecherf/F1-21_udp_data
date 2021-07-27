class PacketBody:


    def __init__(self, body_data, packet_id):
        self.body_data = body_data
        self.packet_id = packet_id
        self.body_length = len(body_data)

    
    def __len__(self):
        return self.body_length

    def __eq__(self, other):
        return self.body_data == other.body_data 
    
    
    def __str__(self):
        return str({'body_data':self.body_data, 'packet_id':self.packet_id})