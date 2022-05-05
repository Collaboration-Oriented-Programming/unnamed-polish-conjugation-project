class ConjugatedWord:
	_root: str
	_mianownik: str
	_dopełniacz: str
	_celownik: str
	_biernik: str
	_narzędnik: str
	_miejscownik: str
	_wołacz: str

	def set_conjugations(self, root):
		# Call an api or scrape a website for the other fields
		self._root = root

	def __init__(self, root):
		self.set_conjugations(root)

	def display(self):
		print('Word:', self._root)
		print('!Not yet implemented!')


def main():
	input_string = input('Please enter word to be conjugated\n')
	conjugated = ConjugatedWord(input_string)
	conjugated.display()


if __name__ == '__main__':
	main()
