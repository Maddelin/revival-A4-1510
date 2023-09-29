"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase

from character_information import leveling


class TestDisplayLevelChart(TestCase):
    def test_display_level_chart(self):
        expected = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500,
                    6: 600, 7: 700, 8: 800, 9: 900, 10: 1000}
        actual = leveling.display_level_chart()
        self.assertEqual(expected, actual)
