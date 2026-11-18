from stats import book_string, get_book_text,  book_count_text

def main():
	text = get_book_text("./books/frankenstein.txt")
	
	print(book_string(text))
	
	counts = book_count_text(text)

	for char, count in counts.items():
		print(f"'{char}': {count}")

main()
