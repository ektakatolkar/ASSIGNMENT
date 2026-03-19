books = []

while True:
    print("\n1.Add Book  2.Show Books  3.Issue  4.Return  5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Book name: ")
        books.append([name, "yes"])

    elif ch == "2":
        for b in books:
            print(b[0], "-", b[1])

    elif ch == "3":
        name = input("Enter book: ")
        for b in books:
            if b[0] == name and b[1] == "yes":
                b[1] = "no"
                print("Issued")

    elif ch == "4":
        name = input("Enter book: ")
        for b in books:
            if b[0] == name:
                b[1] = "yes"
                print("Returned")

    elif ch == "5":
        break