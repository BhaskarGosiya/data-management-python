import os
import pickle

data_file_name = "data"

class data_management:

    default_data = [{'name':'Bhaskar','mobile':8511363202,'id':1}]
    data_obj = None
    
    def __init__(self):
        if not os.path.isfile(data_file_name):
            data_file_obj = open(data_file_name,'wb')
            pickle.dump(self.default_data,data_file_obj)
            data_file_obj.close()
            self.set_data()
        else:
            self.set_data()

    def set_data(self):
        data_file_obj = open(data_file_name,'r')
        self.data_obj = pickle.load(data_file_obj)
        return True

    def read_data(self,field_list=[]):
        lst,dct = [],{}
        for d in self.data_obj:
            for field in field_list:
                if d.get(field,False):
                    dct.update({field:d.get(field)})
            lst.append(dct)
        return lst

data_management_obj = data_management()

read_data = data_management_obj.read_data(['name','id','mobile'])

print "The data found is : ",read_data

