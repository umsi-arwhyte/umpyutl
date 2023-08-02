import sys
import unittest

from pathlib import Path
from src.umpyutl import read, write

project_path = Path.cwd().parent
if project_path not in sys.path:
    sys.path.insert(0, str(project_path))


class UmpyUtlWriteTest(unittest.TestCase):
    """umpyutl functional tests."""

    def setUp(self):
        """Default values."""
        self.fixtures_path = "./fixtures"

    def test_01_to_csv(self):
        """write.to_csv test"""

        fxt_headers = [
            "Date",
            "Week",
            "County",
            "State",
            "Vax_Level",
            "Series_Complete_Pop_Pct",
        ]
        fxt_counties = [
            ["02/19/2022", "7", "Wayne County", "MI", "Moderate", "53.0"],
            ["02/19/2022", "7", "Macomb County", "MI", "Moderate", "55.9"],
            ["02/19/2022", "7", "Oakland County", "MI", "Moderate", "65.4"],
        ]

        filepath = "./output/vax_counties.csv"
        write.to_csv(filepath, fxt_counties, fxt_headers)

        fxt_vax_counties = [
            ["Date", "Week", "County", "State", "Vax_Level", "Series_Complete_Pop_Pct"],
            ["02/19/2022", "7", "Wayne County", "MI", "Moderate", "53.0"],
            ["02/19/2022", "7", "Macomb County", "MI", "Moderate", "55.9"],
            ["02/19/2022", "7", "Oakland County", "MI", "Moderate", "65.4"],
        ]

        # Read file
        vax_counties = read.from_csv(filepath)

        self.assertIsInstance(vax_counties, list, "Error: vax_counties is not a list.")
        self.assertIsInstance(vax_counties[-1], list, "Error: vax_counties[-1] is not a list.")
        self.assertEqual(
            vax_counties,
            fxt_vax_counties,
            "Error: file contents do not match fixture value",
        )

    def test_02_dicts_to_csv(self):
        """write.dicts_to_csv test"""

        fxt_passengers = [
            {
                "url": "https://starwars.fandom.com/wiki/Anakin_Skywalker",
                "name": "Anakin Skywalker",
                "birth_year": "41BBY",
                "height_cm": "188.0",
                "mass_kg": "87.0",
                "homeworld": "https://starwars.fandom.com/wiki/Tatooine",
                "species": "https://swapi.py4e.com/api/species/1/",
            },
            {
                "url": "https://starwars.fandom.com/wiki/Padm%C3%A9_Amidala",
                "name": "Padmé Amidala",
                "birth_year": "46BBY",
                "height_cm": "165.0",
                "mass_kg": "45.0",
                "homeworld": "https://starwars.fandom.com/wiki/Naboo",
                "species": "https://swapi.py4e.com/api/species/1/",
            },
        ]

        filepath = "./output/passengers.csv"
        write.dicts_to_csv(filepath, fxt_passengers, fxt_passengers[0].keys())

        # Read file
        passengers = read.from_csv_to_dicts(filepath)

        self.assertIsInstance(passengers, list, "Error: passengers is not a list.")
        self.assertIsInstance(passengers[-1], dict, "Error: passengers[-1] is not a dict.")
        self.assertEqual(
            passengers,
            fxt_passengers,
            "Error: file contents do not match fixture value",
        )

    def test_03_to_txt(self):
        """write.to_txt test"""

        fxt_opening_crawl = [
            (
                "It is a period of civil war. Rebel spaceships, striking from a hidden base, have won \
                their first victory against the evil Galactic Empire."
            ),
            (
                "During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate \
                weapon, the DEATH STAR, an armored space station with enough power to destroy an \
                entire planet."
            ),
            (
                "Pursued by the Empire's sinister agents, Princess Leia races home aboard her \
                starship, custodian of the stolen plans that can save her people and restore \
                freedom to the galaxy...."
            ),
        ]

        filepath = "./output/episode_iv_opening_crawl.txt"
        write.to_txt(filepath, fxt_opening_crawl)

        # Read file
        opening_crawl = read.from_txt(filepath)

        self.assertIsInstance(opening_crawl, list, "Error: opening_crawl is not a list.")
        self.assertIsInstance(opening_crawl[-1], str, "Error: opening_crawl[-1] is not a str.")
        self.assertEqual(
            opening_crawl,
            fxt_opening_crawl,
            "Error: file contents do not match fixture value",
        )

    def test_04_to_json(self):
        """write.to_json test"""

        fxt_crew_members = {
            "pilot": {
                "url": "https://starwars.fandom.com/wiki/Anakin_Skywalker",
                "name": "Anakin Skywalker",
                "birth_year": "41BBY",
                "height_cm": 188.0,
                "mass_kg": 87.0,
                "homeworld": {
                    "url": "https://starwars.fandom.com/wiki/Tatooine",
                    "name": "Tatooine",
                    "region": "Outer Rim Territories",
                    "sector": "Arkanis sector",
                    "suns": 2,
                    "moons": 3,
                    "orbital_period_days": 304.0,
                    "diameter_km": 10465,
                    "gravity_std": 1.0,
                    "climate": ["Hot", "Arid"],
                    "terrain": ["Canyons", "Desert", "Mountains", "Rocky bluffs"],
                    "population": 200000,
                },
                "species": {
                    "url": "https://swapi.py4e.com/api/species/1/",
                    "name": "Human",
                    "classification": "mammal",
                    "designation": "sentient",
                    "average_lifespan": 120,
                    "average_height_cm": 180.0,
                    "language": "Galactic Basic",
                },
                "force_sensitive": True,
            },
            "copilot": {
                "url": "https://starwars.fandom.com/wiki/Obi-Wan_Kenobi",
                "name": "Obi-Wan Kenobi",
                "birth_year": "57BBY",
                "height_cm": 182.0,
                "mass_kg": 77.0,
                "homeworld": {
                    "url": "https://starwars.fandom.com/wiki/Stewjon",
                    "name": "Stewjon",
                    "region": None,
                    "sector": None,
                    "suns": None,
                    "moons": None,
                    "orbital_period_days": None,
                    "diameter_km": None,
                    "gravity_std": 1.0,
                    "climate": None,
                    "terrain": None,
                    "population": None,
                },
                "species": {
                    "url": "https://swapi.py4e.com/api/species/1/",
                    "name": "Human",
                    "classification": "mammal",
                    "designation": "sentient",
                    "average_lifespan": 120,
                    "average_height_cm": 180.0,
                    "language": "Galactic Basic",
                },
                "force_sensitive": True,
            },
        }

        filepath = "./output/crew_members.json"
        write.to_json(filepath, fxt_crew_members)

        # Read file
        crew_members = read.from_json(filepath)

        self.assertIsInstance(crew_members, dict, "Error: crew_members is not a dict.")
        self.assertIsInstance(
            crew_members["pilot"], dict, "Error: crew_members['pilot'] is not a dict."
        )
        self.assertEqual(
            crew_members,
            fxt_crew_members,
            "Error: file contents do not match fixture value",
        )

    # Deprecated tests 05-08 (remove umpyutl-3.0.0)
    def test_05_write_csv(self):
        """write.write_csv test"""

        fxt_headers = [
            "Date",
            "Week",
            "County",
            "State",
            "Vax_Level",
            "Series_Complete_Pop_Pct",
        ]
        fxt_counties = [
            ["02/19/2022", "7", "Wayne County", "MI", "Moderate", "53.0"],
            ["02/19/2022", "7", "Macomb County", "MI", "Moderate", "55.9"],
            ["02/19/2022", "7", "Oakland County", "MI", "Moderate", "65.4"],
        ]

        filepath = "./output/vax_counties.csv"
        write.write_csv(filepath, fxt_counties, fxt_headers)

        fxt_vax_counties = [
            ["Date", "Week", "County", "State", "Vax_Level", "Series_Complete_Pop_Pct"],
            ["02/19/2022", "7", "Wayne County", "MI", "Moderate", "53.0"],
            ["02/19/2022", "7", "Macomb County", "MI", "Moderate", "55.9"],
            ["02/19/2022", "7", "Oakland County", "MI", "Moderate", "65.4"],
        ]

        # Read file
        vax_counties = read.read_csv(filepath)

        self.assertIsInstance(vax_counties, list, "Error: vax_counties is not a list.")
        self.assertIsInstance(vax_counties[-1], list, "Error: vax_counties[-1] is not a list.")
        self.assertEqual(
            vax_counties,
            fxt_vax_counties,
            "Error: file contents do not match fixture value",
        )

    def test_06_write_dicts_to_csv(self):
        """write.write_dicts_to_csv test"""

        fxt_passengers = [
            {
                "url": "https://starwars.fandom.com/wiki/Anakin_Skywalker",
                "name": "Anakin Skywalker",
                "birth_year": "41BBY",
                "height_cm": "188.0",
                "mass_kg": "87.0",
                "homeworld": "https://starwars.fandom.com/wiki/Tatooine",
                "species": "https://swapi.py4e.com/api/species/1/",
            },
            {
                "url": "https://starwars.fandom.com/wiki/Padm%C3%A9_Amidala",
                "name": "Padmé Amidala",
                "birth_year": "46BBY",
                "height_cm": "165.0",
                "mass_kg": "45.0",
                "homeworld": "https://starwars.fandom.com/wiki/Naboo",
                "species": "https://swapi.py4e.com/api/species/1/",
            },
        ]

        filepath = "./output/passengers.csv"
        write.write_dicts_to_csv(filepath, fxt_passengers, fxt_passengers[0].keys())

        # Read file
        passengers = read.read_csv_to_dicts(filepath)

        self.assertIsInstance(passengers, list, "Error: passengers is not a list.")
        self.assertIsInstance(passengers[-1], dict, "Error: passengers[-1] is not a dict.")
        self.assertEqual(
            passengers,
            fxt_passengers,
            "Error: file contents do not match fixture value",
        )

    def test_07_write_file(self):
        """write.write_file test"""

        fxt_opening_crawl = [
            (
                "It is a period of civil war. Rebel spaceships, striking from a hidden base, have won \
                their first victory against the evil Galactic Empire."
            ),
            (
                "During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate \
                weapon, the DEATH STAR, an armored space station with enough power to destroy an \
                entire planet."
            ),
            (
                "Pursued by the Empire's sinister agents, Princess Leia races home aboard her \
                starship, custodian of the stolen plans that can save her people and restore \
                freedom to the galaxy...."
            ),
        ]

        filepath = "./output/episode_iv_opening_crawl.txt"
        write.write_file(filepath, fxt_opening_crawl)

        # Read file
        opening_crawl = read.read_file(filepath)

        self.assertIsInstance(opening_crawl, list, "Error: opening_crawl is not a list.")
        self.assertIsInstance(opening_crawl[-1], str, "Error: opening_crawl[-1] is not a str.")
        self.assertEqual(
            opening_crawl,
            fxt_opening_crawl,
            "Error: file contents do not match fixture value",
        )

    def test_08_write_json(self):
        """write.write_json test"""

        fxt_crew_members = {
            "pilot": {
                "url": "https://starwars.fandom.com/wiki/Anakin_Skywalker",
                "name": "Anakin Skywalker",
                "birth_year": "41BBY",
                "height_cm": 188.0,
                "mass_kg": 87.0,
                "homeworld": {
                    "url": "https://starwars.fandom.com/wiki/Tatooine",
                    "name": "Tatooine",
                    "region": "Outer Rim Territories",
                    "sector": "Arkanis sector",
                    "suns": 2,
                    "moons": 3,
                    "orbital_period_days": 304.0,
                    "diameter_km": 10465,
                    "gravity_std": 1.0,
                    "climate": ["Hot", "Arid"],
                    "terrain": ["Canyons", "Desert", "Mountains", "Rocky bluffs"],
                    "population": 200000,
                },
                "species": {
                    "url": "https://swapi.py4e.com/api/species/1/",
                    "name": "Human",
                    "classification": "mammal",
                    "designation": "sentient",
                    "average_lifespan": 120,
                    "average_height_cm": 180.0,
                    "language": "Galactic Basic",
                },
                "force_sensitive": True,
            },
            "copilot": {
                "url": "https://starwars.fandom.com/wiki/Obi-Wan_Kenobi",
                "name": "Obi-Wan Kenobi",
                "birth_year": "57BBY",
                "height_cm": 182.0,
                "mass_kg": 77.0,
                "homeworld": {
                    "url": "https://starwars.fandom.com/wiki/Stewjon",
                    "name": "Stewjon",
                    "region": None,
                    "sector": None,
                    "suns": None,
                    "moons": None,
                    "orbital_period_days": None,
                    "diameter_km": None,
                    "gravity_std": 1.0,
                    "climate": None,
                    "terrain": None,
                    "population": None,
                },
                "species": {
                    "url": "https://swapi.py4e.com/api/species/1/",
                    "name": "Human",
                    "classification": "mammal",
                    "designation": "sentient",
                    "average_lifespan": 120,
                    "average_height_cm": 180.0,
                    "language": "Galactic Basic",
                },
                "force_sensitive": True,
            },
        }

        filepath = "./output/crew_members.json"
        write.write_json(filepath, fxt_crew_members)

        # Read file
        crew_members = read.read_json(filepath)

        self.assertIsInstance(crew_members, dict, "Error: crew_members is not a dict.")
        self.assertIsInstance(
            crew_members["pilot"], dict, "Error: crew_members['pilot'] is not a dict."
        )
        self.assertEqual(
            crew_members,
            fxt_crew_members,
            "Error: file contents do not match fixture value",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
