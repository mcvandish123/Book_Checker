from stats import book_string, get_book_text, book_count_text, chars_dict_to_sorted_list

def main():
	text_path = "./books/frankenstein.txt"
	text = get_book_text("./books/frankenstein.txt")
	
	how_many = book_string(text)
	
	counts = book_count_text(text)
	
	sorted_value = chars_dict_to_sorted_list(counts)
	
	print_report(text_path, how_many, sorted_value)	

def print_report(text_path, how_many, sorted_value):
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {text_path}")
	print("----------- Word Count -----------")
	print(f"Found {how_many} total words")
	print("--------- Character Count ---------")
	for char, count in sorted_value:
		text = char.isalpha()
		
		if text == True:
			print(f"{char}: {count}")
	print("============= END =============")

main()
