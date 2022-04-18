import serialization
import input_handling

def main():
	default_data_object = serialization.load_object("data/default_data_object.json", {})
	config_object = serialization.load_object("data/config_object.json", default_data_object["config.json"])
	tax_brackets_object = serialization.load_object("data/tax_brackets_object.json", default_data_object["tax_brackets.json"])
	payments_object = serialization.load_object("data/payments_object.json", [])

	print("Payments object loaded: " + str(payments_object))

	bundle = {
		"default_data_object": default_data_object,
		"config_object": config_object,
		"tax_brackets_object": tax_brackets_object,
		"payments_object": payments_object
	}

	while True:
		newline_symbol = config_object["newline_symbol"] + " "
		input_string = input(newline_symbol)
		quit = input_handling.handle_input(input_string, bundle)
		if quit:
			print("Payments object: " + str(bundle["payments_object"]))
			for obj in bundle:
				serialization.save_object("data/" + obj + ".json", bundle[obj])
				print("Saved " + obj)
			return


if __name__ == "__main__":
	main()