import sys
import unittest

from pathlib import Path
from src.umpyutl import read

# project_path = Path.cwd().parent
# if project_path not in sys.path:
#     sys.path.insert(0, str(project_path))

PARENT_PATH = Path(__file__).parent.resolve()


class UmpyUtlReadTest(unittest.TestCase):
    """umpyutl functional tests."""

    def setUp(self):
        """Default values."""
        self.fixtures_path = PARENT_PATH.joinpath("fixtures")

    def test_01_from_csv(self):
        """read.from_csv test"""

        filepath = self.fixtures_path.joinpath("wookieepedia_planets").with_suffix(".csv")
        planets = read.from_csv(filepath)
        self.assertIsInstance(planets, list, "Error: planets is not a list.")

    def test_02_from_csv_to_dicts(self):
        """read.from_csv_to_dicts test"""

        filepath = self.fixtures_path.joinpath("wookieepedia_starships").with_suffix(".csv")
        starships = read.from_csv_to_dicts(filepath)
        self.assertIsInstance(starships, list, "Error: starships is not a list.")
        self.assertIsInstance(starships[0], dict, "Error: starships[0] is not a dict.")

    def test_03_from_txt(self):
        """read.from_txt test"""

        filepath = self.fixtures_path.joinpath("mandela-rivonia_trial-verbatim").with_suffix(".txt")
        speech = read.from_txt(filepath)
        self.assertIsInstance(speech, list, "Error: speech is not a list.")
        self.assertEqual(speech[2], "Transcript", "Error: speech[2] does not equal 'Transcript'")

    def test_04_read_json(self):
        """read.read_json test"""

        filepath = self.fixtures_path.joinpath("wookieepedia_people").with_suffix(".json")
        people = read.from_json(filepath)
        self.assertIsInstance(people, list, "Error: people is not a list.")

    def test_05_from_yaml(self):
        """read.from_yaml test"""

        filepath = self.fixtures_path.joinpath("loc").with_suffix(".yml")
        config = read.from_yaml(filepath)
        self.assertIsInstance(config, dict, "Error: config is not a dict.")
        self.assertIsInstance(config["maps"], dict, "Error: config['maps'] is not a dict.")
        self.assertEqual(
            config["maps"]["ann_arbor_mi_1925"]["digital_id"],
            "http://hdl.loc.gov/loc.gmd/g4114am.g039091925",
            "Error: config['maps']['ann_arbor_mi_1925']['digital_id'] != 'http://hdl.loc.gov/loc.gmd/g4114am.g039091925'",
        )

    # Deprecated tests 06-10 (Remove umpyutl 3.0.0)
    def test_06_read_csv(self):
        """read.read_csv test"""

        filepath = self.fixtures_path.joinpath("wookieepedia_planets").with_suffix(".csv")
        planets = read.read_csv(filepath)
        self.assertIsInstance(planets, list, "Error: planets is not a list.")

    def test_07_read_csv_to_dicts(self):
        """read.read_csv_to_dicts test"""

        filepath = self.fixtures_path.joinpath("wookieepedia_starships").with_suffix(".csv")
        starships = read.read_csv_to_dicts(filepath)

        self.assertIsInstance(starships, list, "Error: starships is not a list.")
        self.assertIsInstance(starships[0], dict, "Error: starships[0] is not a dict.")

    def test_08_read_file(self):
        """read.read_file test"""

        filepath = self.fixtures_path.joinpath("mandela-rivonia_trial-verbatim").with_suffix(".txt")
        speech = read.from_txt(filepath)
        self.assertIsInstance(speech, list, "Error: speech is not a list.")
        self.assertEqual(speech[2], "Transcript", "Error: speech[2] does not equal 'Transcript'")

    def test_09_read_json(self):
        """read.read_json test"""

        filepath = self.fixtures_path.joinpath("wookieepedia_people").with_suffix(".json")
        people = read.read_csv(filepath)
        self.assertIsInstance(people, list, "Error: people is not a list.")

    def test_10_read_yaml(self):
        """read.read_yaml test"""

        filepath = self.fixtures_path.joinpath("loc").with_suffix(".yml")
        config = read.from_yaml(filepath)
        self.assertIsInstance(config, dict, "Error: config is not a dict.")
        self.assertIsInstance(config["maps"], dict, "Error: config['maps'] is not a dict.")
        self.assertEqual(
            config["maps"]["ann_arbor_mi_1925"]["digital_id"],
            "http://hdl.loc.gov/loc.gmd/g4114am.g039091925",
            "Error: config['maps']['ann_arbor_mi_1925']['digital_id'] != 'http://hdl.loc.gov/loc.gmd/g4114am.g039091925'",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
