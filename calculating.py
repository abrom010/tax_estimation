import data_handling

def calculate_tax(bundle):
	payments = data_handling.get_payments(bundle)
	self_employed_boolean = data_handling.get_self_employed_boolean(bundle)
	self_employed_percentage = data_handling.get_self_employed_tax_percentage(bundle)
	tax_brackets = data_handling.get_tax_brackets(bundle)

	if not self_employed_boolean:
		print("Non self employed tax not implemented")
		return

	gross_income = 0
	net_income = 0
	total_tax = 0

	for payment in payments:
		gross_income += payment
		self_employed_tax = payment * self_employed_percentage
		#print("Self employed tax: " + str(self_employed_tax))
		deduction = self_employed_tax / 2
		net_income += payment - deduction
		income_tax = 0
		for bracket in tax_brackets:
			if net_income < float(bracket):
				# temporarily simple
				income_tax = float((payment - deduction)) * float(tax_brackets[bracket])
				break
		#print("Income tax: " + str(income_tax))
		tax_for_payment = self_employed_tax + income_tax
		total_tax += tax_for_payment
		print("Payment: $" + str(payment) + "\t\tTax: $" + str(round(tax_for_payment, 2)))

	print("Gross income: $" + str(gross_income))
	print("Total tax owed: $" + str(round(total_tax, 2)))