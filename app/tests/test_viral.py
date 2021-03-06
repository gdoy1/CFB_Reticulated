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

    def test_get_virus(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(len(self.db_mod.get_virus()), 1949, 'Checks correct number is shown')

    def test_get_virus_p(self):
        """Checks that correct percentage relative to all infection drugs is correct."""
        self.assertEquals(self.db_mod.get_virus_p(), 6.19, 'Tests that the percentage is the correct value')


if __name__ == "__main__":
    unittest.main()
