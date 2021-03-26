import time
def	equality(sim_1, sim_2):
	if sim_1 == sim_2:
		return 'OK'

	if '*' in sim_2:
		n = sim_2.find('*')
		s = sim_1[:n]
		s2 = sim_2[:n]
		if s == s2:
			return 'OK'

	return 'KO'

a, b = input('Введите первую строку: '), input('Введите вторую строку: ')
print(equality(a, b))


print('Консоль закроется через 20 секунд...')
time.sleep(20)