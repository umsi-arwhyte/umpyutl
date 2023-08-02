import requests
import unittest

from src.umpyutl import http

# project_path = Path.cwd().parent
# if project_path not in sys.path:
#     sys.path.insert(0, str(project_path))


class UmpyUtlHttpTest(unittest.TestCase):
    """umpyutl functional tests."""

    def setUp(self):
        """Default values."""
        self.base_url = "https://swapi.py4e.com/api"

    def test_01_get_resource(self):
        """write.get_resource test"""

        fxt_chewie = {
            "name": "Chewbacca",
            "height": "228",
            "mass": "112",
            "hair_color": "brown",
            "skin_color": "unknown",
            "eye_color": "blue",
            "birth_year": "200BBY",
            "gender": "male",
            "homeworld": "https://swapi.py4e.com/api/planets/14/",
            "films": [
                "https://swapi.py4e.com/api/films/1/",
                "https://swapi.py4e.com/api/films/2/",
                "https://swapi.py4e.com/api/films/3/",
                "https://swapi.py4e.com/api/films/6/",
                "https://swapi.py4e.com/api/films/7/",
            ],
            "species": ["https://swapi.py4e.com/api/species/3/"],
            "vehicles": ["https://swapi.py4e.com/api/vehicles/19/"],
            "starships": [
                "https://swapi.py4e.com/api/starships/10/",
                "https://swapi.py4e.com/api/starships/22/",
            ],
            "created": "2014-12-10T16:42:45.066000Z",
            "edited": "2014-12-20T21:17:50.332000Z",
            "url": "https://swapi.py4e.com/api/people/13/",
        }

        response = http.get_resource(f"{self.base_url}/people/13/")

        self.assertIsInstance(
            response,
            requests.Response,
            "Error: response is not an instance of requests.Response",
        )
        self.assertIsInstance(response.json(), dict, "Error: response is not a dict.")
        self.assertEqual(
            response.json(),
            fxt_chewie,
            "Error: decoded response does not match fixture dict",
        )

    def test_02_get_resource_params(self):
        """write.get_resource with params test"""

        fxt_response = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "name": "Han Solo",
                    "height": "180",
                    "mass": "80",
                    "hair_color": "brown",
                    "skin_color": "fair",
                    "eye_color": "brown",
                    "birth_year": "29BBY",
                    "gender": "male",
                    "homeworld": "https://swapi.py4e.com/api/planets/22/",
                    "films": [
                        "https://swapi.py4e.com/api/films/1/",
                        "https://swapi.py4e.com/api/films/2/",
                        "https://swapi.py4e.com/api/films/3/",
                        "https://swapi.py4e.com/api/films/7/",
                    ],
                    "species": ["https://swapi.py4e.com/api/species/1/"],
                    "vehicles": [],
                    "starships": [
                        "https://swapi.py4e.com/api/starships/10/",
                        "https://swapi.py4e.com/api/starships/22/",
                    ],
                    "created": "2014-12-10T16:49:14.582000Z",
                    "edited": "2014-12-20T21:17:50.334000Z",
                    "url": "https://swapi.py4e.com/api/people/14/",
                }
            ],
        }

        response = http.get_resource(f"{self.base_url}/people/", {"search": "han solo"})

        self.assertIsInstance(
            response,
            requests.Response,
            "Error: response is not an instance of requests.Response",
        )
        self.assertIsInstance(response.json(), dict, "Error: response is not a dict.")
        self.assertEqual(
            response.json(),
            fxt_response,
            "Error: decoded response does not match fixture response.",
        )

    def test_03_get_resource_json(self):
        """write.get_resource_json test"""

        fxt_m_falcon = {
            "name": "Millennium Falcon",
            "model": "YT-1300 light freighter",
            "manufacturer": "Corellian Engineering Corporation",
            "cost_in_credits": "100000",
            "length": "34.37",
            "max_atmosphering_speed": "1050",
            "crew": "4",
            "passengers": "6",
            "cargo_capacity": "100000",
            "consumables": "2 months",
            "hyperdrive_rating": "0.5",
            "MGLT": "75",
            "starship_class": "Light freighter",
            "pilots": [
                "https://swapi.py4e.com/api/people/13/",
                "https://swapi.py4e.com/api/people/14/",
                "https://swapi.py4e.com/api/people/25/",
                "https://swapi.py4e.com/api/people/31/",
            ],
            "films": [
                "https://swapi.py4e.com/api/films/1/",
                "https://swapi.py4e.com/api/films/2/",
                "https://swapi.py4e.com/api/films/3/",
                "https://swapi.py4e.com/api/films/7/",
            ],
            "created": "2014-12-10T16:59:45.094000Z",
            "edited": "2014-12-20T21:23:49.880000Z",
            "url": "https://swapi.py4e.com/api/starships/10/",
        }

        m_falcon = http.get_resource_json(f"{self.base_url}/starships/10/")

        self.assertIsInstance(m_falcon, dict, "Error: response is not a dict.")
        self.assertEqual(
            m_falcon,
            fxt_m_falcon,
            "Error: decoded response does not match fixture dict",
        )

    def test_04_get_resource_json_params(self):
        """write.get_resource_json with params test"""

        fxt_response = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "name": "Hoth",
                    "rotation_period": "23",
                    "orbital_period": "549",
                    "diameter": "7200",
                    "climate": "frozen",
                    "gravity": "1.1 standard",
                    "terrain": "tundra, ice caves, mountain ranges",
                    "surface_water": "100",
                    "population": "unknown",
                    "residents": [],
                    "films": ["https://swapi.py4e.com/api/films/2/"],
                    "created": "2014-12-10T11:39:13.934000Z",
                    "edited": "2014-12-20T20:58:18.423000Z",
                    "url": "https://swapi.py4e.com/api/planets/4/",
                }
            ],
        }

        response = http.get_resource_json(f"{self.base_url}/planets/", {"search": "hoth"})

        self.assertIsInstance(response, dict, "Error: response is not a dict.")
        self.assertEqual(
            response,
            fxt_response,
            "Error: decoded response does not match fixture response.",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
