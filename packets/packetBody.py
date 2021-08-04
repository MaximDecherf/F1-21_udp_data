from .packetData.PacketMotionData import PacketMotionData
from .packetData.PacketSessionData import PacketSessionData
from .packetData.PacketLapData import PacketLapData
from .packetData.PacketEventData import PacketEventData
from .packetData.PacketParticipantsData import PacketParticipantsData
from .packetData.PacketCarSetupData import PacketCarSetupData
from .packetData.PacketCarTelemetryData import PacketCarTelemetryData

class PacketBody:
    SWITCHER = [PacketMotionData, PacketSessionData, PacketLapData, PacketEventData, PacketParticipantsData, PacketCarSetupData, PacketCarTelemetryData, None, None, None, None, None] 
    # the index of the list is equal to the packet_id
    # Packet Name	 Value/packet_id	Description
    # Motion	            0	    Contains all motion data for player’s car – only sent while player is in control
    # Session	            1	    Data about the session – track, time left
    # Lap Data	            2	    Data about all the lap times of cars in the session
    # Event	                3	    Various notable events that happen during a session
    # Participants	        4	    List of participants in the session, mostly relevant for multiplayer
    # Car Setups	        5	    Packet detailing car setups for cars in the race
    # Car Telemetry	        6	    Telemetry data for all cars
    # Car Status	        7	    Status data for all cars
    # Final Classification	8	    Final classification confirmation at the end of a race
    # Lobby Info	        9	    Information about players in a multiplayer lobby
    # Car Damage	        10	    Damage status for all cars
    # Session History	    11	    Lap and tyre data for session
    # source :  https://forums.codemasters.com/topic/80231-f1-2021-udp-specification/


    def __init__(self, body_data, packet_id, *args, **kwargs):
        self.body_data = self.packet_id_class(body_data, packet_id)
        self.packet_id = packet_id
        self.body_length = len(body_data)

    
    def packet_id_class(self, data, packet_id):
        if self.SWITCHER[packet_id] != None:
            packet_class = self.SWITCHER[packet_id]
            
            return packet_class(data)

    def __len__(self):
        return self.body_length

    def __eq__(self, other):
        return self.body_data == other.body_data 
    
    
    def __str__(self):
        return str({'body_data':self.body_data, 'packet_id':self.packet_id})