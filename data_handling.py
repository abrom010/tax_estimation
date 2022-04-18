def set_self_employed_tax_percentage(percentage, bundle):
	bundle["config_object"]["self_employed_tax_percentage"] = percentage

def get_self_employed_tax_percentage(bundle):
	return bundle["config_object"]["self_employed_tax_percentage"]

def set_self_employed_boolean(enabled, bundle):
	bundle["config_object"]["self_employed_boolean"] = enabled

def get_self_employed_boolean(bundle):
	return bundle["config_object"]["self_employed_boolean"]

def set_newline_symbol(symbol, bundle):
	bundle["config_object"]["newline_symbol"] = symbol

def get_newline_symbol(bundle):
	return bundle["config_object"]["newline_symbol"]

def add_payment(payment, bundle):
	payments_object = bundle["payments_object"]
	payments_object.append(payment)

def remove_payment(index, bundle):
	payments_object = bundle["payments_object"]
	payments_object.pop(index)

def get_payments(bundle):
	return bundle["payments_object"]

def get_tax_brackets(bundle):
	return bundle["tax_brackets_object"]