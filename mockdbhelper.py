class MockDBHelper:
    def connect(self, database='crimemap'):
        pass
    def get_all_inputs(self):
        return []
    def add_input(self, data):
        pass
    def clear_all(self):
        pass
    def add_crime(self, category, date, latitude, longitude, description):
    	pass
    def get_all_crimes(self):
    	return [{'latitude': -33.33,
    			'longitude': 26.26,
    			'date': '2018-01-01',
    			'category': 'mugging',
    			'description': 'mock description',
    			}]
