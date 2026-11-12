path_name = "./books/frankenstein.txt"

def get_book_text(path):
	with open(path) as f:
		return f.read()

def book_string() -> str:
	path = get_book_text(path_name)
	num_words = len(path.split())

	return f"Found {num_words} total words"
