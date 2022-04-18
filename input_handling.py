import data_handling
import calculating

def quit(split_input_string, bundle):
	return True

def show(split_input_string, bundle):
	print("Commands: " + str(list(commands.keys())))
	print("Self Employment Tax Percentage: " + str(data_handling.get_self_employed_tax_percentage(bundle)))
	print("Self Employment Boolean: " + str(data_handling.get_self_employed_boolean(bundle)))
	return False

def percent(split_input_string, bundle):
	try:
		new_percent = float(split_input_string[1])
		data_handling.set_self_employed_tax_percentage(new_percent, bundle)
	except ValueError:
		print("Percentage must be a float")
	except IndexError:
		print("Must give an argument for the percentage")
	return False

def newline(split_input_string, bundle):
	try:
		data_handling.set_newline_symbol(split_input_string[1], bundle)
	except IndexError:
		print("Must give an argument for the symbol")
	return False

def payments(split_input_string, bundle):
	try:
		second_argument = split_input_string[1]
		if second_argument == "add":
			try:
				third_argument = float(split_input_string[2])
				data_handling.add_payment(third_argument, bundle)
			except ValueError:
				print("Payment must be a number")
			except IndexError:
				print("Must provide an argument for the payment")
		elif second_argument == "remove":
			try:
				third_argument = int(split_input_string[2])
				data_handling.remove_payment(third_argument, bundle)
			except ValueError:
				print("Payment index must be an integer")
			except IndexError:
				print("Must provide an argument for the payment index")

	except IndexError:
		payments = data_handling.get_payments(bundle)
		i = 0
		for payment in payments:
			print("[" + str(i) + "]\t" + str(payment))
			i += 1

def calculate(split_input_string, bundle):
	calculating.calculate_tax(bundle)

# Must be defined after all command functions are defined
commands = {
	"quit": quit,
	"show": show,
	"percent": percent,
	"newline": newline,
	"payments": payments,
	"calculate": calculate
}

def handle_input(input_string, bundle):
	if input_string == "": return
	split_input_string = input_string.split()
	first_argument = split_input_string[0]
	if first_argument in commands.keys():
		return commands[first_argument](split_input_string, bundle)
	print("Invalid command")