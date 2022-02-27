import json
import pandas as pd
import os
data = {'name': [], 'payment_modes': [], 'locality':[]}
pre = 'jsonFiles'
files = os.listdir(pre)
def parse(filename):
	content = open(filename).read()
	jdict = json.loads(content)
	data['name'].append(jdict["basic-info"]['name'])
	data['locality'].append(jdict['contact']['locality_verbose'])
	try:
		data['payment_modes'].append(jdict['details']['CFT_DETAILS']['accepted_payments'])
	except:
		data['payment_modes'].append(None)
for each in files:
	parse(pre+'/'+each)
	
df = pd.DataFrame(data)
df.to_csv('new_data.csv')
