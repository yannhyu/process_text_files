import unittest
from parse_csv import read_data, get_min_difference_on_scoretest

class ParseCSVTest(unittest.TestCase):

    def setUp(self):
        self.data = 'football.csv'

    def test_csv_read_data_headers(self):
        print(read_data(self.data)[0])
        self.assertEqual(
            read_data(self.data)[0],
            ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points']
        )

    def test_csv_read_data_team_name(self):
        self.assertEqual(read_data(self.data)[1][0], 'Arsenal')

    def test_csv_read_data_points(self):
        self.assertEqual(read_data(self.data)[1][7], '87')

    def test_get_min_difference_on_score(self):
        parsed_data = [
            ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'],
            ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
            ['Liverpool', '38', '24', '8', '6', '67', '30', '80']
        ]
        self.assertEqual(get_min_difference_on_score(parsed_data), ('Liverpool', 37))

    def test_get_team(self):
        data = [
            ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'],
            ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
            ['Liverpool', '38', '24', '8', '6', '67', '30', '80']
        ]
        team, min_diff = get_min_difference_on_score(data)
        self.assertEqual(team, 'Liverpool')

if __name__ == '__main__':
    unittest.main()
