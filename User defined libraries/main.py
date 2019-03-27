from palindrome_reb import get_df
# from substring_reb import is_substring

import numpy as np
from chartjs.views.lines import BaseLineChartView
from . import db



class LineChartJSONView(BaseLineChartView):
	def get_labels(self):
		return db.ngos

	def get_providers(self):
		return db.category['NGO']

	def get_data(self):
		data = []


		df = db.get_df()
		df = df[df['recipient_type'] == 'NGO']

		for waste in db.category['NGO']:
			dict_waste = {db.ngos,[0 for _ in db.ngos]}
			df_waste = df[df['type'] == waste]

			for ngo in db.ngos:
				dict_waste[ngo] = df_waste[df_waste['recipient_name'] == ngo]['quantity'].sum()
			data.append(list(dict_waste.values()))

		print(data)

		return [list(np.random.rand(7,)),
				list(np.random.rand(7,)),
				list(np.random.rand(7,)),]

def json1():
	line_chart_json = LineChartJSONView.as_view()
	return line_chart_json
