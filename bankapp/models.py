import psycopg2


def get_db_connection():
	# db_con = psycopg2.connect(host="localhost", 
	#                  port="5432", 
	#                  user="postgres", 
	#                  password="asb266", 
	#                  database="darkhorse", 
	#                  options="-c search_path=bankdata")
	# return db_con
	conn_string = 'postgresql://ufazqe5ru1fnd974uhrv:n1Bq3tI1IUb3nVN7LjTz@bsvjhovusoysfhtsoiec-postgresql.services.clever-cloud.com:5432/bsvjhovusoysfhtsoiec'
	try:
		return psycopg2.connect(conn_string)
	except Exception as e:
		print(e)

def bank_model():
	conn = get_db_connection()
	cur = conn.cursor()
	cur.execute('SELECT * FROM bankdata.banks;')
	banks = cur.fetchall()
	cur.close()
	conn.close()
	return banks


def branch_autocomplete_model(param_search, param_limit, param_offset):
	conn = get_db_connection()
	cur = conn.cursor()

	sql = '''select * from bankdata.branches where branch like %s order by ifsc limit %s offset %s;'''
	param_list = ['%'+param_search.upper()+'%', param_limit, param_offset]

	cur.execute(sql ,tuple(param_list))
	autocomplete_branches = cur.fetchall()
	cur.close()
	conn.close()

	return autocomplete_branches


def branches_model(param_search, param_limit, param_offset):
	conn = get_db_connection()
	cur = conn.cursor()
	# print(param_search.is_numeric())
	if param_search.isdigit() and len(param_search) <= 3:
		# print(param_search)
		sql = '''select b1.ifsc, b1.bank_id, b1.branch, b1.address, b1.city, b1.district, b1.state, b2.name 
		from bankdata.branches b1 left join bankdata.banks b2
		on b1.bank_id = b2.id 
		where b1.bank_id = %s order by ifsc limit %s offset %s;'''
		param_list = [param_search, param_limit, param_offset]

	else: 
		param_search = '%'+param_search.upper()+'%'
		sql = '''select b1.ifsc, b1.bank_id, b1.branch, b1.address, b1.city, b1.district, b1.state, b2.name 
		from bankdata.branches b1 left join bankdata.banks b2
		on b1.bank_id = b2.id 
		where b1.branch like %s or
		b1.address like %s or
		b1.city like %s or
		b1.district like %s or
		b1.state like %s or
		b1.ifsc like %s order by ifsc limit %s offset %s;'''
	
		param_list = [param_search] * 6 + [param_limit, param_offset]
		# print(param_list)
	
	cur.execute(sql ,tuple(param_list))
	branches = cur.fetchall()
	cur.close()
	conn.close()

	if len(branches) == 0:
		return {'message': 'No data found'}
	# print(branches, type(branches), len(branches))
	return branches
