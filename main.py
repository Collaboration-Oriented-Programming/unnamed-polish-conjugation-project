class ConjugatedWord:
	_root_word: str
	_mianownik: str
	_dopełniacz: str
	_celownik: str
	_biernik: str
	_narzędnik: str
	_miejscownik: str
	_wołacz: str

	def set_conjugations(self, root_word):
		# Call an api or scrape a website for the other fields
		self._root_word = root_word

	def __init__(self, root_word):
		self.set_conjugations(root_word)

	def display(self):
		print('Word:', self._root_word)
		print('!Not yet implemented!')


def main():
	input_string = input('Please enter word to be conjugated:\n')
	conjugated = ConjugatedWord(input_string)
	conjugated.display()


if __name__ == '__main__':
	main()
