import ebook


book1 = ebook.Ebook("Crime and punishment", "Fyodor Dostoevsky", 374)

# book1.show_status()
book1.open()
book1.show_status()
book1.next_page()
book1.next_page()
book1.show_status()
# book1.close()
book1.previous_page()
book1.previous_page()
book1.previous_page()
book1.show_status()
