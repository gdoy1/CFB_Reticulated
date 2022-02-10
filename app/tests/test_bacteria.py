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

    def test_get_bacteria(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(len(self.db_mod.get_bacteria()), 24668, 'Checks correct number is shown')

    def test_get_bacteria_p(self):
        """Return all the data for a given PCT."""
        self.assertEquals(self.db_mod.get_bacteria_p(), 78.32, 'Tests that the percentage is the correct value')


if __name__ == "__main__":
    unittest.main()
