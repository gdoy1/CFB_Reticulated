import unittest
from app import app
from app.database.controllers import Database

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_infection(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(len(self.db_mod.get_infection()), 31497, 'Checks correct number is shown')

if __name__ == "__main__":
    unittest.main()

