import os
import pickle

class data_management:

	default_data = [{'name':'Bhaskar','mobile':8511363202,'id':1}]
	def __init__(self):
		if not os.path.isfile("data"):


	def get_data(self,field_list=[]):
		lst,d = [],{}

		for field in field_list:
			if self.dct.get(field):
				d.update({field:self.dct.get(field)})
		lst.append(d)
		return lst

pickle_with_file_obj = pickle_with_file()

read_data = pickle_with_file_obj.get_data(['name'])

print "The data found is : ",read_data

