class PhoneBook:
    """
    A class representing a phone book with phone numbers.

    Attributes:
        numbers (dict): A dictionary containing phone numbers indexed by name and surname of a person.
    
    Methods:
        add_number: Adds a phone number for a given person to the phone book.
        any_number: Retrieves any phone number associated with a given person from the phone book.
        delete_number: Deletes a specific phone number associated with a given person from the phone book.
        all_numbers: Retrieves all phone numbers associated with a given person from the phone book.
    """

    def __init__(self) -> None:
        """
        Initializes the phone book with an empty dictionary to store phone numbers.
        """
        self.numbers = dict()

    def __repr__(self) -> str:
        return self.numbers.__repr__()

    def add_number(self, person, number):
        """
        Adds a phone number for a given person to the phone book.

        Args:
            person (str): The name of the person.
            number (str): The phone number to be added.
        """
        if person not in self.numbers.keys():
            self.numbers[person] = set()
        self.numbers[person].add(number)

    def any_number(self, person):
        """
        Retrieves any phone number associated with a given person from the phone book.

        Args:
            person (str): The name and surname of the person.

        Returns:
            str: A phone number associated with the person.
        """
        it = iter(self.numbers[person])
        return next(it)

    def delete_number(self, person, number):
        """
        Deletes a specific phone number associated with a given person from the phone book.

        Args:
            person (str): The name of the person.
            number (str): The phone number to be deleted.
        """
        self.numbers[person].remove(number)
        if self.numbers[person] == []:
            del self.numbers[person]

    def all_numbers(self, person):
        """
        Retrieves set of all phone numbers associated with a given person from the phone book.

        Args:
            person (str): The name of the person.

        Returns:
            set: A set containing all phone numbers associated with the person.
        """
        return self.numbers[person].copy()
 