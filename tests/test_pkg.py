import inspect
import re
import requests
import sys
import unittest

from pathlib import Path

project_path = Path.cwd().parent
if project_path not in sys.path:
    sys.path.insert(0, str(project_path))

from umpyutl import http, read, write

class UmpyUtlTest(unittest.TestCase):
    """umpyutl functional tests."""

    def setUp(self):
        """Default values."""
        self.fixtures_path = './fixtures'

    def test_01_read_csv(self):
        """read.read_csv test"""

        planets = read.read_csv(f"{self.fixtures_path}/wookieepedia_planets.csv")
        self.assertIsInstance(planets, list, 'Error: planets is not a list.')

    def test_02_read_csv_to_dicts(self):
        """read.read_csv_to_dicts test"""

        starships = read.read_csv_to_dicts(f"{self.fixtures_path}/wookieepedia_starships.csv")
        self.assertIsInstance(starships, list, 'Error: starships is not a list.')
        self.assertIsInstance(starships[0], dict, 'Error: starships[0] is not a dict.')

    def test_03_read_file(self):
        """read.read_file test"""

        speech = read.read_file(f"{self.fixtures_path}/mandela-rivonia_trial-verbatim.txt")
        self.assertIsInstance(speech, list, 'Error: speech is not a list.')
        self.assertEqual(speech[2], 'Transcript', "Error: speech[2] does not equal 'Transcript'")

    def test_04_read_json(self):
        """read.read_json test"""

        people = read.read_csv(f"{self.fixtures_path}/wookieepedia_people.json")
        self.assertIsInstance(people, list, 'Error: people is not a list.')

    def test_05_write_csv(self):
        """write.write_csv test"""

        fxt_headers = ['Date', 'Week', 'County', 'State', 'Vax_Level', 'Series_Complete_Pop_Pct']
        fxt_counties = [
            ['02/19/2022', '7', 'Wayne County', 'MI', 'Moderate', '53.0'],
            ['02/19/2022', '7', 'Macomb County', 'MI', 'Moderate', '55.9'],
            ['02/19/2022', '7', 'Oakland County', 'MI', 'Moderate', '65.4']
            ]

        filepath = './output/vax_counties.csv'
        write.write_csv(filepath, fxt_counties, fxt_headers)

        fxt_vax_counties = [
            ['Date', 'Week', 'County', 'State', 'Vax_Level', 'Series_Complete_Pop_Pct'],
            ['02/19/2022', '7', 'Wayne County', 'MI', 'Moderate', '53.0'],
            ['02/19/2022', '7', 'Macomb County', 'MI', 'Moderate', '55.9'],
            ['02/19/2022', '7', 'Oakland County', 'MI', 'Moderate', '65.4']
        ]

        # Read file
        vax_counties = read.read_csv(filepath)

        self.assertIsInstance(
            vax_counties,
            list,
            'Error: vax_counties is not a list.')
        self.assertIsInstance(
            vax_counties[-1],
            list,
            'Error: vax_counties[-1] is not a list.')
        self.assertEqual(
            vax_counties,
            fxt_vax_counties,
            'Error: file contents do not match fixture value')

    def test_06_write_dicts_to_csv(self):
        """write.write_dicts_to_csv test"""

        fxt_passengers = [
            {
                'url': 'https://starwars.fandom.com/wiki/Anakin_Skywalker',
                'name': 'Anakin Skywalker',
                'birth_year': '41BBY',
                'height_cm': '188.0',
                'mass_kg': '87.0',
                'homeworld': 'https://starwars.fandom.com/wiki/Tatooine',
                'species': 'https://swapi.py4e.com/api/species/1/'
                },
            {
                'url': 'https://starwars.fandom.com/wiki/Padm%C3%A9_Amidala',
                'name': 'Padmé Amidala',
                'birth_year': '46BBY',
                'height_cm': '165.0',
                'mass_kg': '45.0',
                'homeworld': 'https://starwars.fandom.com/wiki/Naboo',
                'species': 'https://swapi.py4e.com/api/species/1/'
                }
            ]

        filepath = './output/passengers.csv'
        write.write_dicts_to_csv(filepath, fxt_passengers, fxt_passengers[0].keys())

        # Read file
        passengers = read.read_csv_to_dicts(filepath)

        self.assertIsInstance(
            passengers,
            list,
            'Error: passengers is not a list.')
        self.assertIsInstance(
            passengers[-1],
            dict,
            'Error: passengers[-1] is not a dict.')
        self.assertEqual(
            passengers,
            fxt_passengers,
            'Error: file contents do not match fixture value')

    def test_07_write_file(self):
        """write.write_file test"""

        fxt_opening_crawl = [
            ("It is a period of civil war. Rebel spaceships, striking from a hidden base, have won \
                their first victory against the evil Galactic Empire."),
            ("During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate \
                weapon, the DEATH STAR, an armored space station with enough power to destroy an \
                entire planet."),
            ("Pursued by the Empire's sinister agents, Princess Leia races home aboard her \
                starship, custodian of the stolen plans that can save her people and restore \
                freedom to the galaxy....")
        ]

        filepath = './output/episode_iv_opening_crawl.txt'
        write.write_file(filepath, fxt_opening_crawl)

        # Read file
        opening_crawl = read.read_file(filepath)

        self.assertIsInstance(
            opening_crawl,
            list,
            'Error: opening_crawl is not a list.')
        self.assertIsInstance(
            opening_crawl[-1],
            str,
            'Error: opening_crawl[-1] is not a str.')
        self.assertEqual(
            opening_crawl,
            fxt_opening_crawl,
            'Error: file contents do not match fixture value')

    def test_08_write_json(self):
        """write.write_json test"""

        fxt_crew_members = {
            'pilot': {
                'url': 'https://starwars.fandom.com/wiki/Anakin_Skywalker',
                'name': 'Anakin Skywalker',
                'birth_year': '41BBY',
                'height_cm': 188.0,
                'mass_kg': 87.0,
                'homeworld': {
                    'url': 'https://starwars.fandom.com/wiki/Tatooine',
                    'name': 'Tatooine',
                    'region': 'Outer Rim Territories',
                    'sector': 'Arkanis sector',
                    'suns': 2,
                    'moons': 3,
                    'orbital_period_days': 304.0,
                    'diameter_km': 10465,
                    'gravity_std': 1.0,
                    'climate': [
                    'Hot',
                    'Arid'
                    ],
                    'terrain': [
                    'Canyons',
                    'Desert',
                    'Mountains',
                    'Rocky bluffs'
                    ],
                    'population': 200000
                },
                'species': {
                    'url': 'https://swapi.py4e.com/api/species/1/',
                    'name': 'Human',
                    'classification': 'mammal',
                    'designation': 'sentient',
                    'average_lifespan': 120,
                    'average_height_cm': 180.0,
                    'language': 'Galactic Basic'
                },
                'force_sensitive': True
                },
            'copilot': {
                'url': 'https://starwars.fandom.com/wiki/Obi-Wan_Kenobi',
                'name': 'Obi-Wan Kenobi',
                'birth_year': '57BBY',
                'height_cm': 182.0,
                'mass_kg': 77.0,
                'homeworld': {
                    'url': 'https://starwars.fandom.com/wiki/Stewjon',
                    'name': 'Stewjon',
                    'region': None,
                    'sector': None,
                    'suns': None,
                    'moons': None,
                    'orbital_period_days': None,
                    'diameter_km': None,
                    'gravity_std': 1.0,
                    'climate': None,
                    'terrain': None,
                    'population': None
                },
                'species': {
                    'url': 'https://swapi.py4e.com/api/species/1/',
                    'name': 'Human',
                    'classification': 'mammal',
                    'designation': 'sentient',
                    'average_lifespan': 120,
                    'average_height_cm': 180.0,
                    'language': 'Galactic Basic'
                },
                'force_sensitive': True
                }
            }

        filepath = './output/crew_members.json'
        write.write_json(filepath, fxt_crew_members)

        # Read file
        crew_members = read.read_json(filepath)

        self.assertIsInstance(
            crew_members,
            dict,
            'Error: crew_members is not a dict.')
        self.assertIsInstance(
            crew_members['pilot'],
            dict,
            "Error: crew_members['pilot'] is not a dict.")
        self.assertEqual(
            crew_members,
            fxt_crew_members,
            'Error: file contents do not match fixture value')

    def test_09_get_resource(self):
        """write.get_resource test"""

        fxt_chewie = {
            'name': 'Chewbacca',
            'height': '228',
            'mass': '112',
            'hair_color': 'brown',
            'skin_color': 'unknown',
            'eye_color': 'blue',
            'birth_year': '200BBY',
            'gender': 'male',
            'homeworld': 'https://swapi.py4e.com/api/planets/14/',
            'films': [
                'https://swapi.py4e.com/api/films/1/',
                'https://swapi.py4e.com/api/films/2/',
                'https://swapi.py4e.com/api/films/3/',
                'https://swapi.py4e.com/api/films/6/',
                'https://swapi.py4e.com/api/films/7/'
            ],
            'species': [
                'https://swapi.py4e.com/api/species/3/'
            ],
            'vehicles': [
                'https://swapi.py4e.com/api/vehicles/19/'
            ],
            'starships': [
                'https://swapi.py4e.com/api/starships/10/',
                'https://swapi.py4e.com/api/starships/22/'
            ],
            'created': '2014-12-10T16:42:45.066000Z',
            'edited': '2014-12-20T21:17:50.332000Z',
            'url': 'https://swapi.py4e.com/api/people/13/'
            }

        response = http.get_resource('https://swapi.py4e.com/api/people/13/')

        self.assertIsInstance(
            response,
            requests.Response,
            'Error: response is not an instance of requests.Response')
        self.assertIsInstance(
            response.json(),
            dict, 'Error: response is not a dict.')
        self.assertEqual(
            response.json(),
            fxt_chewie,
            'Error: decoded response does not match fixture dict')

    def test_10_get_resource_params(self):
        """write.get_resource with params test"""

        fxt_response = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'name': 'Han Solo',
                    'height': '180',
                    'mass': '80',
                    'hair_color': 'brown',
                    'skin_color': 'fair',
                    'eye_color': 'brown',
                    'birth_year': '29BBY',
                    'gender': 'male',
                    'homeworld': 'https://swapi.py4e.com/api/planets/22/',
                    'films': [
                        'https://swapi.py4e.com/api/films/1/',
                        'https://swapi.py4e.com/api/films/2/',
                        'https://swapi.py4e.com/api/films/3/',
                        'https://swapi.py4e.com/api/films/7/'
                    ],
                    'species': [
                        'https://swapi.py4e.com/api/species/1/'
                    ],
                    'vehicles': [],
                    'starships': [
                        'https://swapi.py4e.com/api/starships/10/',
                        'https://swapi.py4e.com/api/starships/22/'
                    ],
                    'created': '2014-12-10T16:49:14.582000Z',
                    'edited': '2014-12-20T21:17:50.334000Z',
                    'url': 'https://swapi.py4e.com/api/people/14/'
                }
            ]
        }

        response = http.get_resource('https://swapi.py4e.com/api/people/', {'search': 'han solo'})

        self.assertIsInstance(
            response,
            requests.Response,
            'Error: response is not an instance of requests.Response')
        self.assertIsInstance(
            response.json(),
            dict,
            'Error: response is not a dict.')
        self.assertEqual(
            response.json(),
            fxt_response,
            'Error: decoded response does not match fixture response.')

    def test_11_get_resource_json(self):
        """write.get_resource_json test"""

        fxt_m_falcon = {
            'name': 'Millennium Falcon',
            'model': 'YT-1300 light freighter',
            'manufacturer': 'Corellian Engineering Corporation',
            'cost_in_credits': '100000',
            'length': '34.37',
            'max_atmosphering_speed': '1050',
            'crew': '4',
            'passengers': '6',
            'cargo_capacity': '100000',
            'consumables': '2 months',
            'hyperdrive_rating': '0.5',
            'MGLT': '75',
            'starship_class': 'Light freighter',
            'pilots': [
                'https://swapi.py4e.com/api/people/13/',
                'https://swapi.py4e.com/api/people/14/',
                'https://swapi.py4e.com/api/people/25/',
                'https://swapi.py4e.com/api/people/31/'
            ],
            'films': [
                'https://swapi.py4e.com/api/films/1/',
                'https://swapi.py4e.com/api/films/2/',
                'https://swapi.py4e.com/api/films/3/',
                'https://swapi.py4e.com/api/films/7/'
            ],
            'created': '2014-12-10T16:59:45.094000Z',
            'edited': '2014-12-20T21:23:49.880000Z',
            'url': 'https://swapi.py4e.com/api/starships/10/'
            }

        m_falcon = http.get_resource_json('https://swapi.py4e.com/api/starships/10/')

        self.assertIsInstance(
            m_falcon,
            dict, 'Error: response is not a dict.')
        self.assertEqual(
            m_falcon,
            fxt_m_falcon,
            'Error: decoded response does not match fixture dict')

    def test_12_get_resource_json_params(self):
        """write.get_resource_json with params test"""

        fxt_response = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'name': 'Hoth',
                    'rotation_period': '23',
                    'orbital_period': '549',
                    'diameter': '7200',
                    'climate': 'frozen',
                    'gravity': '1.1 standard',
                    'terrain': 'tundra, ice caves, mountain ranges',
                    'surface_water': '100',
                    'population': 'unknown',
                    'residents': [],
                    'films': [
                        'https://swapi.py4e.com/api/films/2/'
                    ],
                    'created': '2014-12-10T11:39:13.934000Z',
                    'edited': '2014-12-20T20:58:18.423000Z',
                    'url': 'https://swapi.py4e.com/api/planets/4/'
                }
            ]
        }

        response = http.get_resource_json('https://swapi.py4e.com/api/planets/', {'search': 'hoth'})

        self.assertIsInstance(
            response,
            dict,
            'Error: response is not a dict.')
        self.assertEqual(
            response,
            fxt_response,
            'Error: decoded response does not match fixture response.')


if __name__ == "__main__":
    unittest.main(verbosity=2)