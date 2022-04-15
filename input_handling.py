import json_handling

def quit(split_input_string, bundle):
	return True

def show(split_input_string, bundle):
	# print("Commands: ", end="")
	print("Commands: " + str(list(commands.keys())))
	print("Self Employment Tax Percentage: " + str(json_handling.get_self_employed_tax_percentage()))
	print("Self Employment Boolean: " + str(json_handling.get_self_employed_boolean()))
	return False

def percent(split_input_string, bundle):
	try:
		new_percent = float(split_input_string[1])
		#bundle["config.json"]
		json_handling.set_self_employed_tax_percentage(new_percent)
	except ValueError:
		print("Percentage must be a float")
	except IndexError:
		print("Must give an argument for the percentage")
	return False

def newline(split_input_string, bundle):
	try:
		json_handling.set_newline_symbol(split_input_string[1])
	except IndexError:
		print("Must give an argument for the symbol")
	return False

def payments(split_input_string, bundle):
	try:
		second_argument = split_input_string[1]
		if second_argument == "add":
			try:
				third_argument = float(split_input_string[2])
				json_handling.add_payment(third_argument)
			except ValueError:
				print("Payment must be a number")
			except IndexError:
				print("Must provide an argument for the payment")
		if second_argument == "delete":
			try:
				third_argument = int(split_input_string[2])
				json_handling.remove_payment(third_argument)
			except ValueError:
				print("Payment index must be an integer")
			except IndexError:
				print("Must provide an argument for the payment index")

	except IndexError:
		pass # print payments

# Must be defined after all command functions are defined
commands = {
	"quit": quit,
	"show": show,
	"percent": percent,
	"newline": newline,
	"payments": payments
}

def handle_input(input_string, bundle):
	split_input_string = input_string.split()
	first_argument = split_input_string[0]
	if first_argument in commands.keys():
		return commands[first_argument](split_input_string, bundle)