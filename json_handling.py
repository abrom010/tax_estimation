import json

def set_self_employed_tax_percentage(percentage):
	set_json_var("config.json", "self_employed_tax_percentage", percentage)

def get_self_employed_tax_percentage():
	return get_json_var("config.json", "self_employed_tax_percentage")

def set_self_employed_boolean(enabled):
	set_json_var("config.json", "self_employed_boolean", enabled)

def get_self_employed_boolean():
	get_json_var("config.json", "self_employed_boolean")

def set_newline_symbol(symbol):
	set_json_var("config.json", "newline_symbol", symbol)

def get_newline_symbol():
	get_json_var("config.json", "newline_symbol")

def add_payment():
	pass

def remove_payment():
	pass

# write a general function for every variable by passing a set of variables (object, filename?, value)
def set_json_var(file_name, var_name, new_value):
	file = open(file_name, "r")
	data = json.load(file)
	data[var_name] = new_value
	file.close()

	file = open("config.json", "w")
	json.dump(data, file)
	file.close()

def get_json_var(file_name, var_name):
	file = open(file_name, "r")
	data = json.load(file)
	value = data[var_name]
	file.close()
	return value

def load_object(file_name, default_data):
	try:
		with open(file_name, "x") as file:
			json.dump(default_data, file, indent=1)
	except FileExistsError:
		pass
	with open(file_name, "r") as file:
		return json.load(file)