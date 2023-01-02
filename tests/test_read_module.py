import sys
import unittest

from pathlib import Path

project_path = Path.cwd().parent
if project_path not in sys.path:
    sys.path.insert(0, str(project_path))

from umpyutl import read


class UmpyUtlReadTest(unittest.TestCase):
    """umpyutl functional tests."""

    def setUp(self):
        """Default values."""
        self.fixtures_path = "./fixtures"

    def test_01_from_csv(self):
        """read.from_csv test"""

        planets = read.from_csv(f"{self.fixtures_path}/wookieepedia_planets.csv")
        self.assertIsInstance(planets, list, "Error: planets is not a list.")

    def test_02_from_csv_to_dicts(self):
        """read.from_csv_to_dicts test"""

        starships = read.from_csv_to_dicts(
            f"{self.fixtures_path}/wookieepedia_starships.csv"
        )
        self.assertIsInstance(starships, list, "Error: starships is not a list.")
        self.assertIsInstance(starships[0], dict, "Error: starships[0] is not a dict.")

    def test_03_from_txt(self):
        """read.from_txt test"""

        speech = read.from_txt(
            f"{self.fixtures_path}/mandela-rivonia_trial-verbatim.txt"
        )
        self.assertIsInstance(speech, list, "Error: speech is not a list.")
        self.assertEqual(
            speech[2], "Transcript", "Error: speech[2] does not equal 'Transcript'"
        )

    def test_04_read_json(self):
        """read.read_json test"""

        people = read.from_json(f"{self.fixtures_path}/wookieepedia_people.json")
        self.assertIsInstance(people, list, "Error: people is not a list.")

    def test_05_from_yaml(self):
        """read.from_yaml test"""

        config = read.from_yaml(f"{self.fixtures_path}/loc.yml")
        self.assertIsInstance(config, dict, "Error: config is not a dict.")
        self.assertIsInstance(
            config["maps"], dict, "Error: config['maps'] is not a dict."
        )
        self.assertEqual(
            config["maps"]["ann_arbor_mi_1925"]["digital_id"],
            "http://hdl.loc.gov/loc.gmd/g4114am.g039091925",
            "Error: config['maps']['ann_arbor_mi_1925']['digital_id'] != 'http://hdl.loc.gov/loc.gmd/g4114am.g039091925'",
        )

    # Deprecated tests 06-10 (Remove umpyutl 3.0.0)
    def test_06_read_csv(self):
        """read.read_csv test"""

        planets = read.read_csv(f"{self.fixtures_path}/wookieepedia_planets.csv")
        self.assertIsInstance(planets, list, "Error: planets is not a list.")

    def test_07_read_csv_to_dicts(self):
        """read.read_csv_to_dicts test"""

        starships = read.read_csv_to_dicts(
            f"{self.fixtures_path}/wookieepedia_starships.csv"
        )
        self.assertIsInstance(starships, list, "Error: starships is not a list.")
        self.assertIsInstance(starships[0], dict, "Error: starships[0] is not a dict.")

    def test_08_read_file(self):
        """read.read_file test"""

        speech = read.read_file(
            f"{self.fixtures_path}/mandela-rivonia_trial-verbatim.txt"
        )
        self.assertIsInstance(speech, list, "Error: speech is not a list.")
        self.assertEqual(
            speech[2], "Transcript", "Error: speech[2] does not equal 'Transcript'"
        )

    def test_09_read_json(self):
        """read.read_json test"""

        people = read.read_csv(f"{self.fixtures_path}/wookieepedia_people.json")
        self.assertIsInstance(people, list, "Error: people is not a list.")

    def test_10_read_yaml(self):
        """read.read_yaml test"""

        config = read.read_yaml(f"{self.fixtures_path}/loc.yml")
        self.assertIsInstance(config, dict, "Error: config is not a dict.")
        self.assertIsInstance(
            config["maps"], dict, "Error: config['maps'] is not a dict."
        )
        self.assertEqual(
            config["maps"]["ann_arbor_mi_1925"]["digital_id"],
            "http://hdl.loc.gov/loc.gmd/g4114am.g039091925",
            "Error: config['maps']['ann_arbor_mi_1925']['digital_id'] != 'http://hdl.loc.gov/loc.gmd/g4114am.g039091925'",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
