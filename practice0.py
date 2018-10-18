def paymentParser(line_list):
	fee_percentage = .029
	flat_fee = .3
	fee_formula = lambda x : x - (x * fee_percentage + flat_fee)
	results = []
	balances = {}

	for command in line_list:
		if command[0:3] == 'API': 
			parameters = command.split('&')
			merchant = parameters[0].split('=')[1]
			merchant_payment = int(parameters[1].split('=')[1])
			destination_account = parameters[2].split('=')[1]
			destination_payment = int(parameters[3].split('=')[1])

			merchant_profit = fee_formula(merchant_payment) - destination_payment

			if merchant in balances.keys:
				balances[merchant] += merchant_profit
			else:
				balances[merchant] = merchant_profit

			if destination_account in balances.keys:
				balances[destination_account] += destination_payment 
			else:
				balances[destination_account] = destination_payment
		else:
			merchant = command.split('=')[1]
			results.append(balances[merchant])
