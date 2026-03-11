import csv

field_names = ["Name", "Author", "Publisher", "Price", "Category"]
bool1 = ["Computer Programming Part 1", "Tamim Shahriar Subeen", "Onnorokom Prokashoni", "240.00"
         , "Programming"]
bool2 = ["Computer Programming Part 2", "Tamim Shahriar Subeen", "Dimik Prokashoni", "250.00"
         , "Programming"]
bool3 = ["Learn Programming with Python", "Tamim Shahriar Subeen", "Dimik Prokashoni", "200.00"
         , "Programming"]

book_list = [bool1, bool2, bool3]

with open("books.csv", "w") as csvf:
    csv_writer = csv.writer(csvf, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(field_names)
    for book in book_list:
        csv_writer.writerow(book)