def get_book_text(path):
	with open(path) as f:
		return f.read()

def book_string(text) -> str:
	num_words = len(text.split())
	return f"Found {num_words} total words"

def book_count_text(text) -> dict[str, int]:
	words = {}
	
	for char in text.lower():
		if char in words:
			words[char] += 1
		else:
			words[char] = 1
	return words
