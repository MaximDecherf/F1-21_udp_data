from .classes.CarDamageData import CarDamageData

class PacketCarDamageData:
    
    BYTES_SPLITS = {'car_damage_data' : [False, 39 , CarDamageData ,858]}

    def __init__(self, body_data):
        self.body_data = body_data
        end_prev = 0
        for key, value in self.BYTES_SPLITS.items():
            if not value[0]:
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