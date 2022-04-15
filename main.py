import json_handling
import input_handling

def main():
	default_data_object = json_handling.load_object("default_data.json", {})
	config_object = json_handling.load_object("config.json", default_data_object["config.json"])
	tax_brackets_object = json_handling.load_object("tax_brackets.json", default_data_object["tax_brackets.json"])
	payments_object = json_handling.load_object("payments.json", [])

	bundle = [default_data_object, config_object, tax_brackets_object, payments_object]

	while True:
		config_object = json_handling.load_object("config.json", default_data_object["config.json"])
		newline_symbol = config_object["newline_symbol"] + " "
		input_string = input(newline_symbol)
		quit = input_handling.handle_input(input_string, bundle)
		if quit: return


if __name__ == "__main__":
	main()