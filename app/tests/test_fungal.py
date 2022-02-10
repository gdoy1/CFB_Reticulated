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

    def test_get_fungal(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(len(self.db_mod.get_fungal()), 2973, 'Checks correct number is shown')

    def test_get_fungal_p(self):
        """Return all the data for a given PCT."""
        self.assertEquals(self.db_mod.get_fungal_p(), 9.44, 'Tests that the percentage is the correct value')


if __name__ == "__main__":
    unittest.main()
