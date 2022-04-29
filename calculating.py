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
		income_tax = 0

		# net_addition = payment - deduction
		# for bracket in tax_brackets:
		# 	if net_income + net_addition < float(bracket):
		# 		income_tax = float((payment - deduction)) * float(tax_brackets[bracket])
		# 		net_income += net_addition
		# 		break
		
		net_addition = payment - deduction
		for i, bracket in enumerate(tax_brackets):
			if net_income < float(bracket) and net_income + net_addition >= float(bracket) and bracket != "over":
				money_for_first_bracket = float(bracket) - net_income
				income_tax = float(money_for_first_bracket * float(tax_brackets[bracket]))
				income_tax += float((net_addition - money_for_first_bracket) * float(list(tax_brackets.values())[i + 1]))
				net_income += net_addition
				break
			elif net_income + net_addition < float(bracket):
				income_tax = float((payment - deduction)) * float(tax_brackets[bracket])
				net_income += net_addition
				break			
		
		tax_for_payment = self_employed_tax + income_tax
		total_tax += tax_for_payment
		print("Payment: $" + str(payment) + "\t\tTax: $" + str(round(tax_for_payment, 2)))

	print()
	print("Gross income: $" + str(gross_income))
	print("Net income: $" + str(round(net_income, 2)))
	print()
	print("Total tax owed: $" + str(round(total_tax, 2)))