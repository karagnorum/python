import unittest

from phone_book import PhoneBook

class TestPhoneBook(unittest.TestCase):

    def test_add_number(self):
        phone_book = PhoneBook()
        phone_book.add_number("Ala", "123456789")
        phone_book.add_number("Ala", "987654321") 
        self.assertEqual(phone_book.all_numbers("Ala"), {"123456789", "987654321"})

    def test_any_number(self):
        phone_book = PhoneBook()
        phone_book.add_number("Ala", "123456789")
        number = phone_book.any_number("Ala")
        self.assertTrue(number == "123456789")
        phone_book.add_number("Ala", "987654321")
        number = phone_book.any_number("Ala")
        self.assertTrue(number == "123456789" or number == "987654321")

    def test_delete_number(self):
        phone_book = PhoneBook()
        phone_book.add_number("Ala", "123456789")
        phone_book.add_number("Ala", "123456789")
        phone_book.add_number("Ala", "987654321")
        phone_book.delete_number("Ala", "123456789")
        number = phone_book.any_number("Ala")
        self.assertTrue(number == "987654321")


if __name__ == '__main__':
    unittest.main()