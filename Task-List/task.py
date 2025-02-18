# task.py

class Task:
    def __init__(self, description, date, time):
        self.description = description
        self.date = date
        self.time = time

    def get_description(self):
        """returns the task’s description string"""
        return self.description

    def __str__(self):
        """returns a string used to display the task’s information to the user"""
        return f"{self.description} - \nDue: {self.date} at {self.time}"

    def __repr__(self):
        """ returns a string used to write the task’s information to the file"""
        return f"{self.description},{self.date},{self.time}"

    def __lt__(self, other):
        """returns true if the self task is less than the other task"""

        # Splitting date and time to get individual components for comparison
        self_year, self_month, self_day = map(int, self.date.split('/'))
        other_year, other_month, other_day = map(int, other.date.split('/'))
        self_hour, self_minute = map(int, self.time.split(':'))
        other_hour, other_minute = map(int, other.time.split(':'))

        # Compare by year, then month, day, hour, minute, and then description
        return (self_year, self_month, self_day, self_hour, self_minute, self.description) < \
            (other_year, other_month, other_day, other_hour, other_minute, other.description)
