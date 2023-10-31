class Ebook():
    def __init__(self, title, author, number_of_pages):
        self.is_open = False
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page_no = 0
    
    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False
    
    def show_status(self):
        print(f'Title: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.number_of_pages}\nCurrent page: {self.current_page_no}')
        if self.is_open == True:
            print("Book is open")
        else:
            print("Book is closed")


    def next_page(self):
        if self.is_open and self.current_page_no < self.number_of_pages:
            self.current_page_no += 1
        else:
            print("Must open book before")

    def previous_page(self):
        if self.is_open:
            if self.current_page_no > 0:
                self.current_page_no -= 1
            else:
                print("You are on the title page, cannot turn")
        else:
            print("Must open book before")



# book1 = Ebook("Crime and punishment", "Fyodor Dostoevsky", 374)

# # book1.show_status()
# book1.open()
# # book1.show_status()
# book1.next_page()
# book1.next_page()
# book1.next_page()
# book1.next_page()
# # book1.show_status()
# book1.close()
# book1.show_status()
# book1.next_page()

  



