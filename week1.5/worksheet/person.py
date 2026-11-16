# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """Create a person with the given name and date of birth."""
        if not isinstance(name, str):
            raise TypeError
        if name == '':
            raise ValueError
        if not isinstance(birth, date):
            raise TypeError

        self.name = name
        self.birth = birth

    def initials(self):
        """Return the uppercased initials of each part of the name."""
        return ''.join(part[0].upper() for part in self.name.split())

    def is_birthday(self):
        """Return True if today is the person's birthday."""
        today = date.today()
        return self.birth.month == today.month and self.birth.day == today.day
