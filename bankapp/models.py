import psycopg2
import os

def get_db_connection():
	
	conn_string = os.environ.get("POSTGRESQL_ADDON_URI")	
	# conn_string = os.environ.get("DATABASE_URI")

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

	if param_search.isdigit() and len(param_search) <= 3:
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
	
	cur.execute(sql ,tuple(param_list))
	branches = cur.fetchall()
	cur.close()
	conn.close()

	if len(branches) == 0:
		return {'message': 'No data found'}
	return branches
