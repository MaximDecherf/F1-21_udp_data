from .classes.LapData import LapData
import struct

class PacketLapData:

    BYTES_SPLITS = {'lap_data' : [False, 43, LapData, 946]}

    def __init__(self, body_data):
        self.body_data = body_data
        end_prev = 0
        for key, value in self.BYTES_SPLITS.items():
            if value[0]:
                if value[1] == int:
                        setattr(self, key, int.from_bytes(body_data[end_prev:value[2]], byteorder='little'))
                        end_prev = value[2]
                elif value[1] == float:
                        setattr(self, key, struct.unpack('<f', body_data[end_prev:value[2]]))
                        end_prev = value[2]
            else:
                #The following code is for items in a list 
                #It starts a while loop that checks if the prev end value of the byte array is not larger than de end of the list items ,if it larger we know we are at the end of the byte array for this item
                # next we fill the list with 1 item at a time, the item is from the end prev value until the prev value + the lenhgt of 1 item in the list and at the end we will set the field eq to the data_list
                data_list = []
                while value[3] > end_prev:
                    data_list.append(value[2](body_data[end_prev:end_prev+value[1]])) 
                    end_prev = end_prev+value[1]
                setattr(self, key, data_list)
                end_prev = value[3]


    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        del full_dict['body_data']
        return str(self.__class__) + " : " + str(full_dict)
