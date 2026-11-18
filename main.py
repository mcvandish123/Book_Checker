from stats import book_string, get_book_text, book_count_text, chars_dict_to_sorted_list
import sys

def main():
	
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	text_path = sys.argv[1]
	text = get_book_text(text_path)
	
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
