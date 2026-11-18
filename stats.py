def get_book_text(path):
	with open(path) as f:
		return f.read()

def book_string(text) -> str:
	return len(text.split())

def book_count_text(text) -> dict[str, int]:
	words = {}
	
	for char in text.lower():
		if char in words:
			words[char] += 1
		else:
			words[char] = 1
	return words

def sort_on(counted: tuple[str, int]) -> int:
	return counted[1]

def chars_dict_to_sorted_list(value: dict[str, int]) -> list[tuple[str, int]]:
	list = []

	for chars in value:
		count = value[chars]
		list.append((chars, count))

	sort_highest = sorted(list, key=sort_on, reverse=True)
	
	return sort_highest 
