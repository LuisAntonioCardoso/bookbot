from stats import get_word_count, get_char_count, sort_on
import sys

def get_book_text(path):
	text=''
	with open(path) as file:
		text =file.read()
	return text

def main():

	if not len(sys.argv) == 2:
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)
	path = sys.argv[1]

	print('============ BOOKBOT ============')
	print('Analyzing book found at books/frankenstein.txt...')
	text = get_book_text(path)
	word_count = get_word_count(text)
	char_count = get_char_count(text)
	print('----------- Word Count ----------')
	print(f'Found {word_count} total words')
	print('--------- Character Count -------')
	
	char_list = []
	for key in char_count:
		item = {'key':key, 'num':char_count[key]}
		char_list.append(item)

	char_list.sort(reverse=True, key=sort_on)
	
	for item in char_list:
		if item['key'].isalpha():
			print(f"{item['key']}: {item['num']}")

	print('============= END ===============')

main()