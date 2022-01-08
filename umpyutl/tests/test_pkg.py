import csv
import json
import inspect
import re
import unittest

# Testing
# import swapi_solution as swapi
# import sw_utils_solution as utl

import swapi as swapi
import sw_utils as utl

class UmpyUtlTest(unittest.TestCase):
    """umpyutl functional tests."""

    def setUp(self):
        """Default values."""

        self.endpoint = 'https://swapi.py4e.com/api'
        self.endpoint_people = f"{self.endpoint}/people/"
        self.endpoint_planets = f"{self.endpoint}/planets/"
        self.endpoint_species = f"{self.endpoint}/species/"
        self.endpoint_starships = f"{self.endpoint}/starships/"
        self.fixtures_path = './tests/fixtures'

        self.stu_func_main = inspect.getsource(swapi.main)
        self.stu_func_convert_episode_values = inspect.getsource(swapi.convert_episode_values)
        self.stu_func_create_droid = inspect.getsource(swapi.create_droid)
        self.stu_func_create_person = inspect.getsource(swapi.create_person)
        self.stu_func_create_planet = inspect.getsource(swapi.create_planet)
        self.stu_func_create_starship = inspect.getsource(swapi.create_starship)
        self.stu_func_get_least_viewed_episode = inspect.getsource(swapi.get_least_viewed_episode)
        self.stu_func_get_most_viewed_episode = inspect.getsource(swapi.get_most_viewed_episode)

        self.stu_func_convert_gravity_value = inspect.getsource(utl.convert_gravity_value)
        self.stu_func_convert_to_float = inspect.getsource(utl.convert_to_float)
        self.stu_func_convert_to_int = inspect.getsource(utl.convert_to_int)
        self.stu_func_convert_to_list = inspect.getsource(utl.convert_to_list)
        self.stu_func_convert_to_none = inspect.getsource(utl.convert_to_none)

        self.fxt_episodes_viewer_data_count = 24
        self.fxt_most_viewed_episode = {
            'series_title': 'Star Wars: The Clone Wars',
            'series_season_num': 1,
            'series_episode_num': 2,
            'season_episode_num': 2,
            'episode_title': 'Rising Malevolence',
            'episode_director': 'Dave Filoni',
            'episode_writers': ['Steven Melching'],
            'episode_release_date': 'October 3, 2008',
            'episode_prod_code': 1.07,
            'episode_us_viewers_mm': 4.92
            }
        self.fxt_least_viewed_episode = {
            'series_title': 'Star Wars: The Clone Wars',
            'series_season_num': 1,
            'series_episode_num': 9,
            'season_episode_num': 9,
            'episode_title': 'Cloak of Darkness',
            'episode_director': 'Dave Filoni',
            'episode_writers': ['Paul Dini'],
            'episode_release_date': 'December 5, 2008',
            'episode_prod_code': 1.1,
            'episode_us_viewers_mm': 1.95
            }
        self.fxt_director_episode_counts = {
            'Dave Bullock': 1,
            'Dave Filoni': 3,
            "Brian Kalin O'Connell": 9,
            'Justin Ridge': 4,
            'Rob Coleman': 5,
            'Jesse Yeh': 3,
            'Atsushi Takeuchi': 1,
            'Steward Lee': 8,
            'Giancarlo Volpe': 7,
            'Robert Dalva': 1,
            'Kyle Dunlevy': 2
            }
        self.fxt_tatooine_data_updated = {
            'name': 'Tatooine',
            'rotation_period': '34',
            'orbital_period': '304',
            'diameter': '10465',
            'climate': 'Hot, Arid',
            'gravity': '1 standard',
            'terrain': 'Canyons, Desert, Mountains, Rocky bluffs',
            'surface_water': '1',
            'population': '200000',
            'residents': [
                'https://swapi.py4e.com/api/people/1/',
                'https://swapi.py4e.com/api/people/2/',
                'https://swapi.py4e.com/api/people/4/',
                'https://swapi.py4e.com/api/people/6/',
                'https://swapi.py4e.com/api/people/7/',
                'https://swapi.py4e.com/api/people/8/',
                'https://swapi.py4e.com/api/people/9/',
                'https://swapi.py4e.com/api/people/11/',
                'https://swapi.py4e.com/api/people/43/',
                'https://swapi.py4e.com/api/people/62/'],
            'films': [
                'https://swapi.py4e.com/api/films/1/',
                'https://swapi.py4e.com/api/films/3/',
                'https://swapi.py4e.com/api/films/4/',
                'https://swapi.py4e.com/api/films/5/',
                'https://swapi.py4e.com/api/films/6/'],
                'created': '2014-12-09T13:50:49.641000Z',
                'edited': '2014-12-20T20:58:18.411000Z',
                'url': 'https://starwars.fandom.com/wiki/Tatooine',
                'region': 'Outer Rim Territories',
                'sector': 'Arkanis sector',
                'system': 'Tatoo system',
                'grid_coordinates': 'R-16',
                'suns': '2',
                'moons': '3',
                'atmosphere': 'Type 1 (breathable)',
                'primary_languages': 'Bocce, Galactic Basic, Huttese, Jawaese, Tusken'
            }
        self.fxt_tatooine_jsonable = {
            'url': 'https://starwars.fandom.com/wiki/Tatooine',
            'name': 'Tatooine',
            'region': 'Outer Rim Territories',
            'sector': 'Arkanis sector',
            'suns': 2,
            'moons': 3,
            'orbital_period_days': 304.0,
            'diameter_km': 10465,
            'gravity_std': 1.0,
            'climate': ['Hot', 'Arid'],
            'terrain': ['Canyons', 'Desert', 'Mountains', 'Rocky bluffs'],
            'population': 200000
            }
        self.fxt_r2_d2_data_updated = {
            'name': 'R2-D2',
            'height': '108',
            'mass': '32',
            'hair_color': 'n/a',
            'skin_color': 'white, blue',
            'eye_color': 'red',
            'birth_year': '33BBY',
            'gender': 'n/a',
            'homeworld': 'https://swapi.py4e.com/api/planets/8/',
            'films': [
                'https://swapi.py4e.com/api/films/1/',
                'https://swapi.py4e.com/api/films/2/',
                'https://swapi.py4e.com/api/films/3/',
                'https://swapi.py4e.com/api/films/4/',
                'https://swapi.py4e.com/api/films/5/',
                'https://swapi.py4e.com/api/films/6/',
                'https://swapi.py4e.com/api/films/7/'
                ],
            'species': ['https://swapi.py4e.com/api/species/2/'],
            'vehicles': [],
            'starships': [],
            'created': '2014-12-10T15:11:50.376000Z',
            'edited': '2014-12-20T21:17:50.311000Z',
            'url': 'https://starwars.fandom.com/wiki/R2-D2',
            'model': 'R2-series astromech droid',
            'manufacturer': 'Industrial Automaton',
            'create_year': '32 BBY',
            'equipment': 'Ascension cable|Buzz saw|Data probe|Electric pike|Fusion welder|Holoprojector|Power recharge coupler|Rocket booster|Water spout'
            }
        self.fxt_r2_d2_jsonable = {
            'url': 'https://starwars.fandom.com/wiki/R2-D2',
            'name': 'R2-D2',
            'model': 'R2-series astromech droid',
            'manufacturer': 'Industrial Automaton',
            'create_year': '32 BBY',
            'height_m': 108.0,
            'mass_kg': 32.0,
            'equipment': [
                'Ascension cable',
                'Buzz saw',
                'Data probe',
                'Electric pike',
                'Fusion welder',
                'Holoprojector',
                'Power recharge coupler',
                'Rocket booster',
                'Water spout'
                ]
            }
        self.fxt_anakin_data_updated = {
            'name': 'Anakin Skywalker',
            'height': '188',
            'mass': '87',
            'hair_color': 'blond',
            'skin_color': 'fair',
            'eye_color': 'blue',
            'birth_year': '41BBY',
            'gender': 'male',
            'homeworld': 'Tatooine',
            'films': [
                'https://swapi.py4e.com/api/films/4/',
                'https://swapi.py4e.com/api/films/5/',
                'https://swapi.py4e.com/api/films/6/'
                ],
            'species': 'Human',
            'vehicles': [
                'https://swapi.py4e.com/api/vehicles/44/',
                'https://swapi.py4e.com/api/vehicles/46/'
                ],
            'starships': [
                'https://swapi.py4e.com/api/starships/39/',
                'https://swapi.py4e.com/api/starships/59/',
                'https://swapi.py4e.com/api/starships/65/'
                ],
            'created': '2014-12-10T16:20:44.310000Z',
            'edited': '2014-12-20T21:17:50.327000Z',
            'url': 'https://starwars.fandom.com/wiki/Anakin_Skywalker',
            'force_sensitive': True
            }
        self.fxt_anakin_jsonable = {
            'url': 'https://starwars.fandom.com/wiki/Anakin_Skywalker',
            'name': 'Anakin Skywalker',
            'birth_year': '41BBY',
            'height_m': 188.0,
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
                'climate': ['Hot', 'Arid'],
                'terrain': ['Canyons', 'Desert', 'Mountains', 'Rocky bluffs'],
                'population': 200000
                },
            'force_sensitive': True}
        self.fxt_twilight_data = {
            'url': 'https://starwars.fandom.com/wiki/Twilight',
            'manufacturer': 'Corellian Engineering Corporation',
            'starship_class': 'Light freighter',
            'name': 'Twilight',
            'model': 'G9 Rigger-class light freighter',
            'length': '34.1',
            'max_atmosphering_speed': '700',
            'hyperdrive_rating': '3.0',
            'MGLT': '',
            'armament': '3 x heavy blasters,1 x Rotating blaster cannon,Concussion missile launchers', 'crew': '2', 'passengers': '6', 'cargo_capacity': '70000', 'consumables': '1 month'
            }
        self.fxt_twilight_no_crew_passengers_jsonable = {
            'url': 'https://starwars.fandom.com/wiki/Twilight',
            'name': 'Twilight',
            'model': 'G9 Rigger-class light freighter',
            'starship_class': 'Light freighter',
            'manufacturer': 'Corellian Engineering Corporation',
            'length_m': 34.1,
            'max_atmosphering_speed': 700,
            'hyperdrive_rating': 3.0,
            'MGLT': None,
            'armament': [
                '3 x heavy blasters',
                '1 x Rotating blaster cannon',
                'Concussion missile launchers'
                ],
            'crew_members': None,
            'passengers_on_board': None,
            'cargo_capacity_kg': 70000,
            'consumables': '1 month'
            }
        self.fxt_obi_wan_data_updated = {
            'name': 'Obi-Wan Kenobi',
            'height': 182,
            'mass': 77,
            'hair_color': 'auburn, white',
            'skin_color': 'fair',
            'eye_color': 'blue-gray',
            'birth_year': '57BBY',
            'gender': 'male',
            'homeworld': 'Stewjon',
            'films': [
                'https://swapi.py4e.com/api/films/1/',
                'https://swapi.py4e.com/api/films/2/',
                'https://swapi.py4e.com/api/films/3/',
                'https://swapi.py4e.com/api/films/4/',
                'https://swapi.py4e.com/api/films/5/',
                'https://swapi.py4e.com/api/films/6/'
                ],
            'species': 'Human',
            'vehicles': ['https://swapi.py4e.com/api/vehicles/38/'],
            'starships': [
                'https://swapi.py4e.com/api/starships/48/',
                'https://swapi.py4e.com/api/starships/59/',
                'https://swapi.py4e.com/api/starships/64/',
                'https://swapi.py4e.com/api/starships/65/',
                'https://swapi.py4e.com/api/starships/74/'
                ],
            'created': '2014-12-10T16:16:29.192000Z',
            'edited': '2014-12-20T21:17:50.325000Z',
            'url': 'https://starwars.fandom.com/wiki/Obi-Wan_Kenobi',
            'force_sensitive': True
            }
        self.fxt_obi_wan_jsonable = {
            'url': 'https://starwars.fandom.com/wiki/Obi-Wan_Kenobi',
            'name': 'Obi-Wan Kenobi',
            'birth_year': '57BBY',
            'height_m': 182.0,
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
            'force_sensitive': True
            }
        self.fxt_twilight_crew_members_jsonable = {
            'pilot': {
                'url': 'https://starwars.fandom.com/wiki/Anakin_Skywalker',
                'name': 'Anakin Skywalker',
                'birth_year': '41BBY',
                'height_m': 188.0,
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
                    'climate': ['Hot', 'Arid'],
                    'terrain': ['Canyons', 'Desert', 'Mountains', 'Rocky bluffs'],
                    'population': 200000
                    },
                'force_sensitive': True
                },
            'copilot': {
                'url': 'https://starwars.fandom.com/wiki/Obi-Wan_Kenobi',
                'name': 'Obi-Wan Kenobi',
                'birth_year': '57BBY',
                'height_m': 182.0,
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
                'force_sensitive': True
                }
            }
        self.fxt_padme_data_updated = {
            'name': 'Padme Amidala',
            'height': 165,
            'mass': 45,
            'hair_color': 'brown',
            'skin_color': 'light',
            'eye_color': 'brown',
            'birth_year': '46BBY',
            'gender': 'female',
            'homeworld': 'Naboo',
            'films': [
                'https://swapi.py4e.com/api/films/4/',
                'https://swapi.py4e.com/api/films/5/',
                'https://swapi.py4e.com/api/films/6/'
                ],
            'species': 'Human',
            'vehicles': [],
            'starships': [
                'https://swapi.py4e.com/api/starships/39/',
                'https://swapi.py4e.com/api/starships/49/',
                'https://swapi.py4e.com/api/starships/64/'
                ],
            'created': '2014-12-19T17:28:26.926000Z',
            'edited': '2014-12-20T21:17:50.381000Z',
            'url': 'https://starwars.fandom.com/wiki/Padm%C3%A9_Amidala',
            'force_sensitive': False
            }
        self.fxt_padme_jsonable = {
            'url': 'https://starwars.fandom.com/wiki/Padm%C3%A9_Amidala',
            'name': 'Padme Amidala',
            'birth_year': '46BBY',
            'height_m': 165.0,
            'mass_kg': 45.0,
            'homeworld': {
                'url': 'https://starwars.fandom.com/wiki/Naboo',
                'name': 'Naboo',
                'region': 'Mid Rim Territories',
                'sector': 'Chommell sector',
                'suns': 1,
                'moons': 3,
                'orbital_period_days': 312.0,
                'diameter_km': 12120,
                'gravity_std': 1.0,
                'climate': ['Temperate'],
                'terrain': ['Swamps', 'Hills', 'Plains', 'Cities', 'Mountains'],
                'population': 4500000000},
            'force_sensitive': False
            }
        self.fxt_c_3po_data_updated = {
            'name': 'C-3PO',
            'height': '177',
            'mass': '75',
            'hair_color': 'n/a',
            'skin_color': 'gold',
            'eye_color': 'yellow',
            'birth_year': '112BBY',
            'gender': 'n/a',
            'homeworld': 'https://swapi.py4e.com/api/planets/1/',
            'films': [
                'https://swapi.py4e.com/api/films/1/',
                'https://swapi.py4e.com/api/films/2/',
                'https://swapi.py4e.com/api/films/3/',
                'https://swapi.py4e.com/api/films/4/',
                'https://swapi.py4e.com/api/films/5/',
                'https://swapi.py4e.com/api/films/6/'
                ],
            'species': ['https://swapi.py4e.com/api/species/2/'],
            'vehicles': [],
            'starships': [],
            'created': '2014-12-10T15:10:51.357000Z',
            'edited': '2014-12-20T21:17:50.309000Z',
            'url': 'https://starwars.fandom.com/wiki/C-3PO',
            'model': '3PO-series protocol droid',
            'manufacturer': 'Cybot Galactica',
            'create_year': '32 BBY',
            'equipment': 'TranLang III communication module'
            }
        self.fxt_c_3po_jsonable = {
            'url': 'https://starwars.fandom.com/wiki/C-3PO',
            'name': 'C-3PO',
            'model': '3PO-series protocol droid',
            'manufacturer': 'Cybot Galactica',
            'create_year': '32 BBY',
            'height_m': 177.0,
            'mass_kg': 75.0,
            'equipment': ['TranLang III communication module']
            }
        self.fxt_twilight_passengers_on_board_jsonable = [
            {
                'url': 'https://starwars.fandom.com/wiki/Padm%C3%A9_Amidala',
                'name': 'Padme Amidala',
                'birth_year': '46BBY',
                'height_m': 165.0,
                'mass_kg': 45.0,
                'homeworld': {
                    'url': 'https://starwars.fandom.com/wiki/Naboo',
                    'name': 'Naboo',
                    'region': 'Mid Rim Territories',
                    'sector': 'Chommell sector',
                    'suns': 1,
                    'moons': 3,
                    'orbital_period_days': 312.0,
                    'diameter_km': 12120,
                    'gravity_std': 1.0,
                    'climate': ['Temperate'],
                    'terrain': ['Swamps', 'Hills', 'Plains', 'Cities', 'Mountains'],
                    'population': 4500000000
                    },
                'force_sensitive': False
                },
            {
                'url': 'https://starwars.fandom.com/wiki/C-3PO',
                'name': 'C-3PO',
                'model': '3PO-series protocol droid',
                'manufacturer': 'Cybot Galactica',
                'create_year': '32 BBY',
                'height_m': 177.0,
                'mass_kg': 75.0,
                'equipment': ['TranLang III communication module']
                },
            {
                'url': 'https://starwars.fandom.com/wiki/R2-D2',
                'name': 'R2-D2',
                'model': 'R2-series astromech droid',
                'manufacturer': 'Industrial Automaton',
                'create_year': '32 BBY',
                'height_m': 108.0,
                'mass_kg': 32.0,
                'equipment': [
                    'Ascension cable',
                    'Buzz saw',
                    'Data probe',
                    'Electric pike',
                    'Fusion welder',
                    'Holoprojector',
                    'Power recharge coupler',
                    'Rocket booster',
                    'Water spout'
                    ]
                }
            ]


    @weight(20)
    def test_01_clone_wars_22_slice(self):
        """8.1.2.1: clone_wars_22 slice"""

        self.assertTrue(
            re.search(r"clone_wars_22\s=\sclone_wars\[(1:5|-7:-3)\]", self.stu_func_main),
            """\nError: Unable to locate a < clone_wars_22 > variable assignment that employs
            the correct slicing notation. This could be due to one or more of the following reasons:
            1. The variable assignment has yet to be made.
            2. The variable is misspelled.
            3. The expression assigned to the variable employs incorrect slicing notation.
            4. The variable assignment styling is incorrect.
            """
            )

    @weight(20)
    def test_02_clone_wars_2012_slice(self):
        """8.1.2.2: clone_wars_2012 slice"""

        self.assertTrue(
            re.search(r"clone_wars_2012\s=\sclone_wars\[(4:6|-4:-2)\]", self.stu_func_main),
            """\nError: Unable to locate a < clone_wars_2012 > variable assignment that employs
            the correct slicing notation. This could be due to one or more of the following reasons:
            1. The variable assignment has yet to be made.
            2. The variable is misspelled.
            3. The expression assigned to the variable employs incorrect slicing notation.
            4. The variable assignment styling is incorrect.
            """
            )

    @weight(20)
    def test_03_clone_wars_url_index(self):
        """8.1.2.3: clone_wars_url indexing"""

        self.assertTrue(
            re.search(r"clone_wars_url\s=\sclone_wars(\[-2\]\[-1\]|\[-2\]\[6\]|\[6\]\[6\]|\[6\]\[-1\])", self.stu_func_main),
            """\nError: Unable to locate a < clone_wars_url > variable assignment that employs
            correct indexing. This could be due to one or more of the following reasons:
            1. The variable assignment has yet to be made.
            2. The variable is misspelled.
            3. The expression assigned to the variable employs incorrect indexing notation.
            4. The indexing employed returns the wrong nested list element.
            5. The variable assignment styling is incorrect.
            """
            )

    @weight(25)
    def test_04_clone_wars_even_num_seasons(self):
        """8.1.2.4: clone_wars_even_num_seasons slice"""

        self.assertTrue(
            re.search(r"clone_wars_even_num_seasons\s=\sclone_wars\[(2::2|-6::2)\]", self.stu_func_main),
            """\nError: Unable to locate a < clone_wars_even_num_seasons > variable assignment that employs
            the correct slicing notation. This could be due to one or more of the following reasons:
            1. The variable assignment has yet to be made.
            2. The variable is misspelled.
            3. The expression assigned to the variable employs incorrect slicing notation.
            4. The variable assignment styling is incorrect.
            """
            )

    @weight(50)
    def test_05_has_viewer_data(self):
        """8.2.2: has_viewer_data()"""

        try:
            getattr(swapi, 'has_viewer_data')
        except AttributeError:
            raise AttributeError("< has_viewer_data > function not found.")
        else:

            filepath = f"{self.fixtures_path}/fxt-clone_wars_episodes.csv"
            fxt_episodes = fxt_read_csv_to_dicts(filepath)

            stu_count = 0
            for episode in fxt_episodes:
                if swapi.has_viewer_data(episode):
                    stu_count += 1

        self.assertEqual(
            stu_count,
            self.fxt_episodes_viewer_data_count,
            """\nError: Looping over the episodes and calling < has_viewer_data > in order to
            accumulate a count of the number of episodes with viewership data did not return the
            expected count.

            Recheck your implementation of the function. Review the Docstring and make sure you are
            checking the value's truth value correctly.
            """
        )

    @weight(15)
    def test_06_convert_to_int(self):
        """8.3.1.1: convert_to_int()"""

        try:
            getattr(utl, 'convert_to_int')
        except AttributeError:
            raise AttributeError("< convert_to_int > function not found.")
        else:
            stu_converted = utl.convert_to_int('10')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_int),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_converted,
            10,
            """\nError: calling < convert_to_int > and passing it the string '10' did not
            return the expected integer value. Recheck your implementation of the function.
            """
        )

    @weight(15)
    def test_07_convert_to_int(self):
        """8.3.1.2: convert_to_int()"""

        try:
            getattr(utl, 'convert_to_int')
        except AttributeError:
            raise AttributeError("< convert_to_int > function not found.")
        else:
            stu_no_change = utl.convert_to_int('unknown')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_int),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_no_change,
            'unknown',
            """\nError: calling < convert_to_int > and passing it the string 'unknown' did not
            return the expected value ('unknown' unchanged). Recheck your implementation of the
            function's try / except blocks.
            """
        )

    @weight(15)
    def test_08_convert_to_int(self):
        """8.3.1.3: convert_to_int()"""

        try:
            getattr(utl, 'convert_to_int')
        except AttributeError:
            raise AttributeError("< convert_to_int > function not found.")
        else:
            stu_no_change = utl.convert_to_int(['C-3PO', 'R2-D2', 'BB-8'])

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_int),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_no_change,
            ['C-3PO', 'R2-D2', 'BB-8'],
            """\nError: calling < convert_to_int > and passing it the list ['C-3PO', 'R2-D2', 'BB-8']
            did not return the expected value (['C-3PO', 'R2-D2', 'BB-8'] unchanged). Recheck your
            implementation of the function's try / except blocks.
            """
        )

    @weight(15)
    def test_09_convert_to_float(self):
        """8.3.2.1: convert_to_float()"""

        try:
            getattr(utl, 'convert_to_float')
        except AttributeError:
            raise AttributeError("< convert_to_float > function not found.")
        else:
            stu_converted = utl.convert_to_float('4.98')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_float),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_converted,
            4.98,
            """\nError: calling < convert_to_float > and passing it the string '4.98' did not
            return the expected float value. Recheck your implementation of the function.
            """
        )

    @weight(15)
    def test_10_convert_to_float(self):
        """8.3.2.2: convert_to_float()"""

        try:
            getattr(utl, 'convert_to_float')
        except AttributeError:
            raise AttributeError("< convert_to_float > function not found.")
        else:
            stu_no_change = utl.convert_to_float('N/A')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_float),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_no_change,
            'N/A',
            """\nError: calling < convert_to_float > and passing it the string 'N/A' did not
            return the expected value ('N/A' unchanged). Recheck your implementation of the
            function's try / except blocks.
            """
        )

    @weight(15)
    def test_11_convert_to_float(self):
        """8.3.2.3: convert_to_float()"""

        try:
            getattr(utl, 'convert_to_float')
        except AttributeError:
            raise AttributeError("< convert_to_float > function not found.")
        else:
            stu_no_change = utl.convert_to_float(('C-3PO', 'R2-D2', 'BB-8'))

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_float),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_no_change,
            ('C-3PO', 'R2-D2', 'BB-8'),
            """\nError: calling < convert_to_float > and passing it the tuple ('C-3PO', 'R2-D2', 'BB-8')
            did not return the expected value (('C-3PO', 'R2-D2', 'BB-8') unchanged). Recheck your
            implementation of the function's try / except blocks.
            """
        )

    @weight(25)
    def test_12_convert_to_list(self):
        """8.3.3.1: convert_to_list()"""

        try:
            getattr(utl, 'convert_to_list')
        except AttributeError:
            raise AttributeError("< convert_to_list > function not found.")
        else:
            stu_converted = utl.convert_to_list('C-3PO, R2-D2, BB-8', ', ')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_list),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_converted,
            ['C-3PO', 'R2-D2', 'BB-8'],
            """\nError: calling < convert_to_list > and passing it the string 'C-3PO, R2-D2, BB-8'
            did not return the expected list. Recheck your implementation of the function including
            the handling of specified delimiter argument.
            """
        )

    @weight(25)
    def test_13_convert_to_list(self):
        """8.3.3.2: convert_to_list()"""

        try:
            getattr(utl, 'convert_to_list')
        except AttributeError:
            raise AttributeError("< convert_to_list > function not found.")
        else:
            stu_converted = utl.convert_to_list('C-3PO R2-D2 BB-8')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_list),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_converted,
            ['C-3PO', 'R2-D2', 'BB-8'],
            """\nError: calling < convert_to_list > and passing it the string 'C-3PO R2-D2 BB-8'
            did not return the expected list. Recheck your implementation of the function including
            the handling of unspecified delimiters (e.g., rely on the str method's default
            delimiter).
            """
        )

    @weight(25)
    def test_14_convert_to_list(self):
        """8.3.3.3: convert_to_list()"""

        try:
            getattr(utl, 'convert_to_list')
        except AttributeError:
            raise AttributeError("< convert_to_list > function not found.")
        else:
            stu_no_change = utl.convert_to_list(506)

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_list),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_no_change,
            506,
            """\nError: calling < convert_to_list > and passing it the integer 506 did not return
            the integer value unchanged. Recheck your implementation of the function's try / except
            blocks.
            """
        )

    @weight(125)
    def test_15_convert_episode_values(self):
        """8.4.2: convert_episode_values()"""

        try:
            getattr(swapi, 'convert_episode_values')
        except AttributeError:
            raise AttributeError("< convert_episode_values > function not found.")
        else:
            filepath = f"{self.fixtures_path}/fxt-clone_wars_episodes.csv"
            fxt_episodes = fxt_read_csv_to_dicts(filepath) # unconverted

            stu_episodes_converted = swapi.convert_episode_values(fxt_episodes)

            filepath = f"{self.fixtures_path}/fxt-clone_wars-episodes_converted.json"
            fxt_episodes_converted = fxt_read_json(filepath)

        self.assertTrue(
            re.search(r"convert_to_float\(", self.stu_func_convert_episode_values),
            """\nError: Unable to locate call to < convert_to_float > in function block. Review
            instructions and delegate task of converting strings to floats to
            < convert_to_float >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_int\(", self.stu_func_convert_episode_values),
            """\nError: Unable to locate call to < convert_to_int > in function block. Review
            instructions and delegate task of converting strings to integers to
            < convert_to_int >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_list\(", self.stu_func_convert_episode_values),
            """\nError: Unable to locate call to < convert_to_list > in function block. Review
            instructions and delegate task of converting strings to lists to
            < convert_to_list >.
            """
            )

        self.assertEqual(
            stu_episodes_converted,
            fxt_episodes_converted,
            """\nError: Calling < convert_episode_values > in order to convert specified values to
            an appropriate type did not return the expected mutated list of dictionaries. This
            could be due to one or more of the following reasons:
            1. Conditional logic is insufficient or incorrect.
            2. < convert_to_* > functions are not used or called incorrectly.
            3. Values that must be converted to < None > are handled incorrectly.
            4. List delimiters are handled incorrectly.
            """
        )

    @weight(120)
    def test_16_get_most_viewed_episode(self):
        """8.5.2: get_most_viewed_episode()"""

        try:
            getattr(swapi, 'get_most_viewed_episode')
        except AttributeError:
            raise AttributeError("< get_most_viewed_episode > function not found.")
        else:
            filepath = f"{self.fixtures_path}/fxt-clone_wars-episodes_converted.json"
            fxt_episodes_converted = fxt_read_json(filepath)

            stu_most_viewed_episode = swapi.get_most_viewed_episode(fxt_episodes_converted)

        self.assertTrue(
            re.search(r"has_viewer_data\(", self.stu_func_get_most_viewed_episode),
            """\nError: Unable to locate call to < has_viewer_data > in function block. Review
            instructions and delegate task of checking if an episode has viewership info to
            < has_viewer_data >.
            """
            )

        self.assertEqual(
            stu_most_viewed_episode,
            self.fxt_most_viewed_episode,
            """\nError: Calling < get_most_viewed_episode > in order to retrieve the most
            watched episode did not return the expected dictionary. This
            could be due to one or more of the following reasons:
            1. Failed to check if the episode has a viewership value
            2. Conditional logic is insufficient or incorrect.
            3. Incrementing the viewer "count" is handling incorrectly.
            4. Assigning/updating the most viewed episode is handled incorrectly.
            """
        )

    @weight(120)
    def test_17_get_least_viewed_episode(self):
        """8.5.4: get_least_viewed_episode()"""

        try:
            getattr(swapi, 'get_least_viewed_episode')
        except AttributeError:
            raise AttributeError("< get_least_viewed_episode > function not found.")
        else:
            filepath = f"{self.fixtures_path}/fxt-clone_wars-episodes_converted.json"
            fxt_episodes_converted = fxt_read_json(filepath)

            stu_least_viewed_episode = swapi.get_least_viewed_episode(fxt_episodes_converted)

        self.assertTrue(
            re.search(r"has_viewer_data\(", self.stu_func_get_least_viewed_episode),
            """\nError: Unable to locate call to < has_viewer_data > in function block. Review
            instructions and delegate task of checking if an episode has viewership info to
            < has_viewer_data >.
            """
            )

        self.assertEqual(
            stu_least_viewed_episode,
            self.fxt_least_viewed_episode,
            """\nError: Calling < get_least_viewed_episode > in order to retrieve the most
            watched episode did not return the expected dictionary. This
            could be due to one or more of the following reasons:
            1. Failed to check if the episode has a viewership value
            2. Conditional logic is insufficient or incorrect.
            3. Decrementing the viewer "count" is handling incorrectly.
            4. Assigning/updating the least viewed episode is handled incorrectly.
            """
        )

    @weight(120)
    def test_18_count_episodes_by_director(self):
        """8.6.2: count_episodes_by_director()"""

        try:
            getattr(swapi, 'count_episodes_by_director')
        except AttributeError:
            raise AttributeError("< count_episodes_by_director > function not found.")
        else:
            filepath = f"{self.fixtures_path}/fxt-clone_wars-episodes_converted.json"
            fxt_episodes_converted = fxt_read_json(filepath)

            stu_director_episode_counts = swapi.count_episodes_by_director(fxt_episodes_converted)

        self.assertEqual(
            stu_director_episode_counts,
            self.fxt_director_episode_counts,
            """\nError: Calling < count_episodes_by_director > in order to return a dictionary
            containing episode counts by director did return the expected dictionary. This
            could be due to one or more of the following reasons:
            1. Conditional logic is insufficient or incorrect.
            2. Incrementing the episode counts incorrectly.
            3. Assigning new key-value pairs to the accumulator dictionary incorrectly.
            """
        )

    @weight(135)
    def test_19_group_episodes_by_writer(self):
        """8.7.2: group_episodes_by_writer()"""

        try:
            getattr(swapi, 'group_episodes_by_writer')
        except AttributeError:
            raise AttributeError("< group_episodes_by_writer > function not found.")
        else:
            filepath = f"{self.fixtures_path}/fxt-clone_wars-episodes_converted.json"
            fxt_episodes_converted = fxt_read_json(filepath)

            stu_writer_episodes = swapi.group_episodes_by_writer(fxt_episodes_converted)

            filepath = f"{self.fixtures_path}/fxt-clone_wars-writer_episodes.json"
            fxt_writer_episodes = fxt_read_json(filepath)

        self.assertEqual(
            stu_writer_episodes,
            fxt_writer_episodes,
            """\nError: Calling < group_episodes_by_writer > in order to return a list of
            dictionaries that group episodes by a contributing writer did not return the expected
            list. This could be due to one or more of the following reasons:
            1. Conditional logic is insufficient or incorrect.
            2. Incrementing the episode counts incorrectly.
            3. Assigning new key-value pairs to the accumulator dictionary incorrectly.
            """
        )

    @weight(25)
    def test_20_convert_to_none(self):
        """8.8.2.1: convert_to_none()"""

        try:
            getattr(utl, 'convert_to_none')
        except AttributeError:
            raise AttributeError("< convert_to_none > function not found.")
        else:
            stu_converted = utl.convert_to_none('Unknown')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_none),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertIsNone(
            stu_converted,
            """\nError: calling < convert_to_none > and passing it the capitalized string 'Unknown'
            did not return < None > as the value. Recheck your implementation of the function.
            """
        )

    @weight(25)
    def test_21_convert_to_none(self):
        """8.8.2.2: convert_to_none()"""

        try:
            getattr(utl, 'convert_to_none')
        except AttributeError:
            raise AttributeError("< convert_to_none > function not found.")
        else:
            stu_no_change = utl.convert_to_none('Ahsoka Tano')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_none),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_no_change,
            'Ahsoka Tano',
            """\nError: calling < convert_to_none > and passing it the string 'Ahsoka Tano' did not
            return the expected value ('Ahsoka Tano' unchanged). Recheck your implementation of the
            function's try / except blocks.
            """
        )

    @weight(25)
    def test_22_convert_to_none(self):
        """8.8.2.3: convert_to_none()"""

        try:
            getattr(utl, 'convert_to_none')
        except AttributeError:
            raise AttributeError("< convert_to_none > function not found.")
        else:
            stu_no_change = utl.convert_to_none(['C-3PO', 'R2-D2', 'BB-8'])

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_to_none),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_no_change,
            ['C-3PO', 'R2-D2', 'BB-8'],
            """\nError: calling < convert_to_none > and passing it the list ['C-3PO', 'R2-D2', 'BB-8']
            did not return the expected value (['C-3PO', 'R2-D2', 'BB-8'] unchanged). Recheck your
            implementation of the function's try / except blocks.
            """
        )


    @weight(25)
    def test_23_convert_gravity_value(self):
        """8.8.4.1: convert_gravity_value()"""

        try:
            getattr(utl, 'convert_gravity_value')
        except AttributeError:
            raise AttributeError("< convert_gravity_value > function not found.")
        else:
            stu_converted = utl.convert_gravity_value('1 standard')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_gravity_value),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_converted,
            1.0,
            """\nError: calling < convert_gravity_value > and passing it the string '1 standard'
            did not return the expected float value 1.0. Recheck your implementation of the
            function's try / except blocks.
            """
        )

    @weight(25)
    def test_24_convert_gravity_value(self):
        """8.8.4.2: convert_gravity_value()"""

        try:
            getattr(utl, 'convert_gravity_value')
        except AttributeError:
            raise AttributeError("< convert_gravity_value > function not found.")
        else:
            stu_converted = utl.convert_gravity_value('1.56')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_gravity_value),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_converted,
            1.56,
            """\nError: calling < convert_gravity_value > and passing it the string '1.56' did not
            return the expected float value 1.56. Recheck your implementation of the function's
            try / except blocks.
            """
        )

    @weight(25)
    def test_25_convert_gravity_value(self):
        """8.8.4.3: convert_gravity_value()"""

        try:
            getattr(utl, 'convert_gravity_value')
        except AttributeError:
            raise AttributeError("< convert_gravity_value > function not found.")
        else:
            stu_no_change = utl.convert_gravity_value('unknown')

        self.assertTrue(
            re.search(r"try\:", self.stu_func_convert_gravity_value),
            """\nError: Unable to locate <try> statement in function block.
            Review instructions. Function must be implemented using < try > and < except >
            statements.
            """
            )

        self.assertEqual(
            stu_no_change,
            'unknown',
            """\nError: calling < convert_gravity_value > and passing it the string 'unknown'
            did not return the expected value ('unknown' unchanged). Recheck your implementation
            of the function's try / except blocks.
            """
        )

    @weight(100)
    def test_26_create_planet_jsonable(self):
        """8.9.3: create_planet()"""

        try:
            getattr(swapi, 'Planet')
        except AttributeError:
            raise AttributeError("< Planet > instance not found.")

        try:
            getattr(swapi, 'create_planet')
        except AttributeError:
            raise AttributeError("< create_planet > function not found.")
        else:
            stu_tatooine = swapi.create_planet(self.fxt_tatooine_data_updated)

        self.assertTrue(
            re.search(r"convert_gravity_value\(", self.stu_func_create_planet),
            """\nError: Unable to locate call to < convert_gravity_value > in function block.
            Review instructions and delegate task of converting the gravity value to
            < convert_gravity_value >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_float\(", self.stu_func_create_planet),
            """\nError: Unable to locate call to < convert_to_float > in function block. Review
            instructions and delegate task of converting strings to floats to
            < convert_to_float >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_int\(", self.stu_func_create_planet),
            """\nError: Unable to locate call to < convert_to_int > in function block. Review
            instructions and delegate task of converting strings to integers to
            < convert_to_int >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_list\(", self.stu_func_create_planet),
            """\nError: Unable to locate call to < convert_to_list > in function block. Review
            instructions and delegate task of converting strings to lists to
            < convert_to_list >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_none\(", self.stu_func_create_planet),
            """\nError: Unable to locate call to < convert_to_none > in function block. Review
            instructions and delegate task of converting certain string values to < None > to
            < convert_to_none >.
            """
            )

        self.assertIsInstance(
            stu_tatooine,
            swapi.Planet,
            """\nError: Calling < create_planet > did not return a < Planet > instance. Review
            the function's Docstring and correct your implementation.
            """
            )

        try:
            getattr(swapi.Planet, 'jsonable')
        except AttributeError:
            raise AttributeError("< Planet.jsonable > method not found.")
        else:
            stu_tatooine_jsonable = stu_tatooine.jsonable()


        self.assertEqual(
            stu_tatooine_jsonable,
            self.fxt_tatooine_jsonable,
            """\nError: Calling < create_planet > in order to return an instance of the planet
            Tatooine that could then be compared to a test fixture Tatooine dictionary by calling
            the < Planet > instance's < jsonable > method did not return the expected value.

            This could be due to one or more of the following reasons:
            1. SWAPI Tatooine data not updated with Wookieepedia data.
            2. < Planet.__init__ > and/or, < Planet.jsonable > methods are implemented
               incorrectly.
            3. < create_planet > function not checking the truth values of < data > values before
               attempting to assign values to < Planet > instance variables.
            4. < create_planet > function not utilizing < convert_to_* > functions correctly
               in order to convert targeted values.
            """
        )

    @weight(100)
    def test_27_create_droid_jsonable(self):
        """8.10.3: create_droid()"""

        try:
            getattr(swapi, 'Droid')
        except AttributeError:
            raise AttributeError("< Droid > instance not found.")

        try:
            getattr(swapi, 'create_droid')
        except AttributeError:
            raise AttributeError("< create_droid > function not found.")
        else:
            stu_r2_d2 = swapi.create_droid(self.fxt_r2_d2_data_updated)

        self.assertTrue(
            re.search(r"convert_to_float\(", self.stu_func_create_droid),
            """\nError: Unable to locate call to < convert_to_float > in function block. Review
            instructions and delegate task of converting strings to floats to
            < convert_to_float >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_list\(", self.stu_func_create_droid),
            """\nError: Unable to locate call to < convert_to_list > in function block. Review
            instructions and delegate task of converting strings to lists to
            < convert_to_list >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_none\(", self.stu_func_create_droid),
            """\nError: Unable to locate call to < convert_to_none > in function block. Review
            instructions and delegate task of converting certain string values to < None > to
            < convert_to_none >.
            """
            )

        self.assertIsInstance(
            stu_r2_d2,
            swapi.Droid,
            """\nError: Calling < create_droid > did not return a < Droid > instance. Review
            the function's Docstring and correct your implementation.
            """
            )

        try:
            getattr(swapi.Droid, 'jsonable')
        except AttributeError:
            raise AttributeError("< Droid.jsonable > method not found.")
        else:
            stu_r2_d2_jsonable = stu_r2_d2.jsonable()

        self.assertEqual(
            stu_r2_d2_jsonable,
            self.fxt_r2_d2_jsonable,
            """\nError: Calling < create_droid > in order to return an instance of the droid
            R2-D2 that could then be compared to a test fixture R2-D2 dictionary by calling
            the < Droid > instance's < jsonable > method did not return the expected value.

            This could be due to one or more of the following reasons:
            1. SWAPI R2-D2 data not updated with Wookieepedia data.
            2. < Droid.__init__ > and/or, < Droid.jsonable > methods are implemented
               incorrectly.
            3. < create_droid > function not checking the truth values of < data > values before
               attempting to assign values to < Droid > instance variables.
            4. < create_droid > function not utilizing < convert_to_* > functions correctly
               in order to convert targeted values.
            """
        )

    @weight(150)
    def test_28_create_person_jsonable(self):
        """8.11.3: create_person()"""

        try:
            getattr(swapi, 'Person')
        except AttributeError:
            raise AttributeError("< Person > instance not found.")

        # Person.homeworld is assigned a Planet instance
        try:
            getattr(swapi, 'Planet')
        except AttributeError:
            raise AttributeError("< Planet > instance not found.")

        try:
            getattr(swapi, 'create_person')
        except AttributeError:
            raise AttributeError("< create_person > function not found.")
        else:
            filepath = f"{self.fixtures_path}/fxt-wookieepedia_planets.csv"
            fxt_wookiee_planets = fxt_read_csv_to_dicts(filepath)

            stu_anakin = swapi.create_person(self.fxt_anakin_data_updated, fxt_wookiee_planets)

        self.assertTrue(
            re.search(r"convert_to_float\(", self.stu_func_create_person),
            """\nError: Unable to locate call to < convert_to_float > in function block. Review
            instructions and delegate task of converting strings to floats to
            < convert_to_float >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_none\(", self.stu_func_create_person),
            """\nError: Unable to locate call to < convert_to_none > in function block. Review
            instructions and delegate task of converting certain string values to < None > to
            < convert_to_none >.
            """
            )

        self.assertTrue(
            re.search(r"get_swapi_resource\(", self.stu_func_create_person),
            """\nError: Unable to locate call to < get_swapi_resource > in function block. Review
            instructions and delegate task of retrieving SWAPI resources to < get_swapi_resource >.
            """
            )

        self.assertIsInstance(
            stu_anakin,
            swapi.Person,
            """\nError: Calling < create_person > did not return a < Person > instance. Review
            the function's Docstring and correct your implementation.
            """
            )

        try:
            getattr(swapi.Person, 'jsonable')
        except AttributeError:
            raise AttributeError("< Person.jsonable > method not found.")
        else:
            stu_anakin_jsonable = stu_anakin.jsonable()

        self.assertEqual(
            stu_anakin_jsonable,
            self.fxt_anakin_jsonable,
            """\nError: Calling < create_person > in order to return an instance of the person
            Anakin Skywalker that could then be compared to a test fixture Anakin Skywalker
            dictionary by calling the < Person > instance's < jsonable > method did not return
            the expected value.

            This could be due to one or more of the following reasons:
            1. SWAPI Anakin Skywalker data not updated with Wookieepedia data.
            2. < Person.__init__ > and/or, < Person.jsonable > methods are implemented
               incorrectly. Check that < Person.jsonable() > converts the < Planet > instance
               correctly.
            3. < create_person > function not checking the truth values of < data > values before
               attempting to assign values to < Person > instance variables.
            4. < create_person > function not utilizing < convert_to_* > functions correctly
               in order to convert targeted values.
            5. < create_person > function not handling the conversion of the "homeworld" value
               to a < Planet > instance.
            6. < create_person > function not handling 2nd < planets > argument correctly.
            """
        )

    @weight(100)
    def test_29_create_starship_no_crew_passengers_jsonable(self):
        """8.12.3: create_starship_no_crew_passengers_jsonable"""

        try:
            getattr(swapi, 'create_starship')
        except AttributeError:
            raise AttributeError("< create_starship > function not found.")
        else:
            stu_twilight = swapi.create_starship(self.fxt_twilight_data)

        self.assertTrue(
            re.search(r"convert_to_float\(", self.stu_func_create_starship),
            """\nError: Unable to locate call to < convert_to_float > in function block. Review
            instructions and delegate task of converting strings to floats to
            < convert_to_float >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_int\(", self.stu_func_create_starship),
            """\nError: Unable to locate call to < convert_to_int > in function block. Review
            instructions and delegate task of converting strings to integers to
            < convert_to_int >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_list\(", self.stu_func_create_starship),
            """\nError: Unable to locate call to < convert_to_list > in function block. Review
            instructions and delegate task of converting strings to lists to
            < convert_to_list >.
            """
            )

        self.assertTrue(
            re.search(r"convert_to_none\(", self.stu_func_create_starship),
            """\nError: Unable to locate call to < convert_to_none > in function block. Review
            instructions and delegate task of converting certain string values to < None > to
            < convert_to_none >.
            """
            )

        self.assertIsInstance(
            stu_twilight,
            swapi.Starship,
            """\nError: Calling < create_starship > did not return a < Starship > instance. Review
            the function's Docstring and correct your implementation.
            """
            )

        try:
            getattr(swapi.Starship, 'jsonable')
        except AttributeError:
            raise AttributeError("< Starship.jsonable > method not found.")
        else:
            stu_twilight_jsonable = stu_twilight.jsonable()

            # Test without crew members and passengers (if exist)
            if hasattr(stu_twilight_jsonable, 'crew_members'):
                delattr(stu_twilight_jsonable, 'crew_members')

            if hasattr(stu_twilight_jsonable, 'passengers_on_board'):
                delattr(stu_twilight_jsonable, 'passengers_on_board')

        self.assertEqual(
            stu_twilight_jsonable,
            self.fxt_twilight_no_crew_passengers_jsonable,
            """\nError: Calling < create_starship > in order to return an instance of the light
            freighter Twilight that could then be compared to a test fixture Twilight dictionary by
            calling the < Starship > instance's < jsonable > method did not return the expected
            value.

            This could be due to one or more of the following reasons:
            1. Wookieepedia Twilight data not accessed.
            2. < Starship.__init__ > and/or, < Starship.jsonable > methods are implemented
               incorrectly.
            3. < create_starship > function not checking the truth values of < data > values before
               attempting to assign values to < Starship > instance variables.
            4. < create_starship > function not utilizing < convert_to_* > functions correctly
               in order to convert targeted values.
            5. < Starship.jsonable > method not handling < crew_members > and/or
               < passengers_on_board > instance variable values correctly.
            """
        )

    @weight(50)
    def test_30_crew_members_jsonable(self):
        """8.13.2: crew_members_jsonable"""

        # Person.homeworld is assigned a Planet instance
        try:
            getattr(swapi, 'Planet')
        except AttributeError:
            raise AttributeError("< Planet > instance not found.")

        try:
            getattr(swapi, 'create_planet')
        except AttributeError:
            raise AttributeError("< create_planet > function not found.")

        try:
            getattr(swapi, 'Person')
        except AttributeError:
            raise AttributeError("< Person > instance not found.")

        try:
            getattr(swapi, 'create_person')
        except AttributeError:
            raise AttributeError("< create_person > function not found.")

        try:
            getattr(swapi, 'Crew')
        except AttributeError:
            raise AttributeError("< Crew > instance not found.")

        try:
            getattr(swapi, 'Starship')
        except AttributeError:
            raise AttributeError("< Starship > instance not found.")

        try:
            getattr(swapi.Starship, 'assign_crew_members')
        except AttributeError:
            raise AttributeError("< Starship.assign_crew_members > method not found.")
        else:

            filepath = f"{self.fixtures_path}/fxt-wookieepedia_planets.csv"
            fxt_wookiee_planets = fxt_read_csv_to_dicts(filepath)

            # Twilight crew
            stu_twilight = swapi.create_starship(self.fxt_twilight_data)
            stu_anakin = swapi.create_person(self.fxt_anakin_data_updated, fxt_wookiee_planets)
            stu_obi_wan = swapi.create_person(self.fxt_obi_wan_data_updated, fxt_wookiee_planets)
            stu_crew = swapi.Crew({'pilot': stu_anakin, 'copilot': stu_obi_wan})
            stu_twilight.assign_crew_members(stu_crew)

        try:
            getattr(swapi.Crew, 'jsonable')
        except AttributeError:
            raise AttributeError("< Crew.jsonable > method not found.")
        else:
            stu_twilight_crew_jsonable = stu_twilight.crew_members.jsonable()

        self.assertEqual(
            stu_twilight_crew_jsonable,
            self.fxt_twilight_crew_members_jsonable,
            """\nError: Created a < Starship > instance and then called the < assign_crew_members >
            method in order to assign a < Crew > instance comprising Anakin Skywalker as pilot and
            Obi-Wan Kenobi as copilot. Retrieved a JSON-friendly representation of the
            starship's < crew_members > but did not return the expected dictionary. Recheck the
            your implementation of the < Starship.assign_crew_members > method.
            """
        )

    @weight(110)
    def test_31_passengers_on_board_jsonable(self):
        """8.14.3: passengers_on_board_jsonable"""

        # Person.homeworld is assigned a Planet instance
        try:
            getattr(swapi, 'Planet')
        except AttributeError:
            raise AttributeError("< Planet > instance not found.")

        try:
            getattr(swapi, 'create_planet')
        except AttributeError:
            raise AttributeError("< create_planet > function not found.")

        try:
            getattr(swapi, 'Person')
        except AttributeError:
            raise AttributeError("< Person > instance not found.")

        try:
            getattr(swapi, 'create_person')
        except AttributeError:
            raise AttributeError("< create_person > function not found.")

        try:
            getattr(swapi, 'Droid')
        except AttributeError:
            raise AttributeError("< Droid > instance not found.")

        try:
            getattr(swapi, 'create_droid')
        except AttributeError:
            raise AttributeError("< create_droid > function not found.")

        try:
            getattr(swapi, 'Passengers')
        except AttributeError:
            raise AttributeError("< Passengers > instance not found.")

        try:
            getattr(swapi, 'Starship')
        except AttributeError:
            raise AttributeError("< Starship > instance not found.")

        try:
            getattr(swapi.Starship, 'add_passengers')
        except AttributeError:
            raise AttributeError("< Starship.add_passengers > method not found.")
        else:

            filepath = f"{self.fixtures_path}/fxt-wookieepedia_planets.csv"
            fxt_wookiee_planets = fxt_read_csv_to_dicts(filepath)

            # Twilight Passengers
            stu_twilight = swapi.create_starship(self.fxt_twilight_data)
            stu_padme = swapi.create_person(self.fxt_padme_data_updated, fxt_wookiee_planets)
            stu_c_3po = swapi.create_droid(self.fxt_c_3po_data_updated)
            stu_r2_d2 = swapi.create_droid(self.fxt_r2_d2_data_updated)
            stu_passengers = swapi.Passengers([stu_padme, stu_c_3po, stu_r2_d2])
            stu_twilight.add_passengers(stu_passengers)

        try:
            getattr(swapi.Passengers, 'jsonable')
        except AttributeError:
            raise AttributeError("< Passengers.jsonable > method not found.")
        else:
            stu_twilight_passengers_on_board_jsonable = stu_twilight.passengers_on_board.jsonable()

        self.assertEqual(
            stu_twilight_passengers_on_board_jsonable,
            self.fxt_twilight_passengers_on_board_jsonable,
            """\nError: Created a < Starship > instance and then called the < add_passengers >
            method in order to assign a < Passengers > instance comprising Senator Padmé Amidala
            and the droids C-3PO and R2-D2. Retrieved a JSON-friendly representation of the
            starship's < passengers_on_board > but did not return the expected dictionary. Recheck
            the your implementation of the < Starship.add_passengers > method.
            """
        )

    @weight(120)
    def test_32_twilight_departs_json(self):
        """8.14.4 Encode departing starship as JSON and write to file"""

        try:
            swapi.main() # run main()
            filepath = 'stu-twilight_departs.json'
            stu_twilight_departs = fxt_read_json(filepath)
        except:
            stu_twilight_departs = None

        # Read in fixture JSON
        fxt_twilight_departs = fxt_read_json(f"{self.fixtures_path}/fxt-twilight_departs.json")

        self.assertEqual(
            stu_twilight_departs,
            fxt_twilight_departs,
            """
            \nERROR: Calling the function main() failed to generate a version of the file named
            < stu-twilight_departs.json > that matches line for line and character
            for character the test fixture JSON file < fxt-twilight_departs.json >. Make sure that
            the Twilight light freighter crewed by Anakin Skywalker and Obi-Wan Kenobi (with Padmé
            Amidala, C-3PO, and R2-D2 as passengers) has been encoded as JSON correctly. Note that
            the key names, associated values and order of the key-value pairs in the JSON document
            must match the fixture test file < fxt-twilight_departs.json >. Use VS Code to compare
            the differences between the file generated by your script and the fixture test file in
            order to identify mismatches then revise your code accordingly.\n
            """
            )


def fxt_read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of dictionaries that
    represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


def fxt_read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


def fxt_write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


if __name__ == "__main__":
    unittest.main(verbosity=2)