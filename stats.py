
def get_word_count(text):
	return len(text.split())

def get_char_count(text):
	char_counts = {}
	for c in text:
		letter = c.lower()
		if letter not in char_counts:
			char_counts[letter]=0
		char_counts[letter]+=1
	return char_counts

def sort_on(item):
	return item['num']