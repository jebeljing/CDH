def getYear(post):
	dt = datetime.strptime(post, '%Y-%m-%dT%H:%M:%S.%f')
	return dt.year

def getMonth(post):
	dt = datetime.strptime(post, '%Y-%m-%dT%H:%M:%S.%f')
	if (dt.day >= 29):
		return dt.month + 1
	return dt.month




	
