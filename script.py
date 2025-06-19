import utils
import sorts

# Load small dataset of books
books_small = utils.load_books('books_small.csv')

# Sort by title (ascending)
def compare_by_title_asc(book_a, book_b):
  return book_a["title_lower"] > book_b["title_lower"]

sorted_by_title = sorts.bubble_sort(books_small[:], compare_by_title_asc)

# Sort by author (ascending)
def compare_by_author_asc(book_a, book_b):
  return book_a["author_lower"] > book_b["author_lower"]

sorted_by_author_bubble = sorts.bubble_sort(books_small[:], compare_by_author_asc)
sorted_by_author_quick = books_small[:]  # Copy to sort in-place
sorts.quicksort(sorted_by_author_quick, 0, len(sorted_by_author_quick) - 1, compare_by_author_asc)

# Sort by total length of author + title
def compare_by_total_length(book_a, book_b):
  sum_a = len(book_a["author"]) + len(book_a["title"])
  sum_b = len(book_b["author"]) + len(book_b["title"])
  return sum_a > sum_b

# Load large dataset of books
books_large = utils.load_books('books_large.csv')

# Sort large list using both sorting algorithms
sorted_by_length_bubble = sorts.bubble_sort(books_large[:], compare_by_total_length)
sorted_by_length_quick = books_large[:]  # In-place sort
sorts.quicksort(sorted_by_length_quick, 0, len(sorted_by_length_quick) - 1, compare_by_total_length)

# Output results
print("\nSorted by title (bubble sort):")
for book in sorted_by_title:
  print(book["author"])

print("\nSorted by author (bubble sort):")
for book in sorted_by_author_bubble:
  print(book["author"])

print("\nSorted by author (quicksort):")
for book in sorted_by_author_quick:
  print(book["author"])

print("\nSorted by total length (bubble sort):")
for book in sorted_by_length_bubble:
  print(len(book["author"]) + len(book["title"]))

print("\nSorted by total length (quicksort):")
for book in sorted_by_length_quick:
  print(len(book["author"]) + len(book["title"]))
