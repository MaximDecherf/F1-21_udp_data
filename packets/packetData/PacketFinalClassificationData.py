from .classes.FinalClassificationData import FinalClassificationData

class PacketFinalClassificationData:

    BYTES_SPLITS = {'num_cars' : [True, int, 1], 'final_classification_data' : [False, 37, FinalClassificationData ,815]}

    def __init__(self, body_data):
        self.body_data = body_data
        end_prev = 0
        for key, value in self.BYTES_SPLITS.items():
            if value[0]:
                if value[1] == int:
                    setattr(self, key, int.from_bytes(body_data[end_prev:value[2]], byteorder='little'))
                    end_prev = value[2]
            else:
                data_list = []
                while value[3] > end_prev:
                    data_list.append(value[2](body_data[end_prev:end_prev+value[1]]))
                    end_prev = end_prev+value[1]
                setattr(self, key, data_list)
                end_prev = value[3]
        self.data_lenhgt = len(body_data)
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        del full_dict['body_data']
        return str(self.__class__) + " : " + str(full_dict)
    