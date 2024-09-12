#the array of books
books = ["poobook", "book", "the best book", "not good book", "new book"]

print("books available: ")
for book in books:
    print(f"- {book}")

borrowed_book = input("\n write the name of the book you wish to borrow: ")

if borrowed_book in books:
    borrow_time = int(input("how many days to borrow the book for?")) 
    print(f"\n'{borrowed_book}' has been borrowed for {borrow_time} days")
else:
    print(f"'{borrowed_book}' is not available")

points = borrow_time * 10 

print(f"\nyou have earnt '{points}' points")