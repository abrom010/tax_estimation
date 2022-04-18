import json

def load_object(file_name, default_data):
	try:
		with open(file_name, "x") as file:
			json.dump(default_data, file, indent=1)
	except FileExistsError:
		#print("File exists for: " + file_name)
		with open(file_name) as file:
			return json.load(file)

def save_object(file_name, data):
	with open(file_name, "w") as file:
		json.dump(data, file, indent=1)