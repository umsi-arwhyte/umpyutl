import sys
import unittest

from pathlib import Path
from src.umpyutl import convert

# project_path = Path.cwd().parent
# if project_path not in sys.path:
#     sys.path.insert(0, str(project_path))

PARENT_PATH = Path(__file__).parent.resolve()


class UmpyUtlConvertTest(unittest.TestCase):
    def setUp(self):
        """Default values."""
        self.fixtures_path = PARENT_PATH.joinpath("fixtures")
        self.output_path = PARENT_PATH.joinpath("output")

    def test_01_to_float_str_num(self):
        """to_float string number"""

        try:
            getattr(convert, "to_float")
        except AttributeError:
            raise AttributeError("< convert.to_float > function not found.")
        else:
            self.assertEqual(
                convert.to_float("4.98"),
                4.98,
                """\nError: calling < convert.to_float > and passing it the string '4.98' did not
                return the expected float value.
                """,
            )

    def test_02_to_float_na(self):
        """to_float n/a"""

        try:
            getattr(convert, "to_float")
        except AttributeError:
            raise AttributeError("< convert.to_float > function not found.")
        else:
            self.assertEqual(
                convert.to_float("N/A"),
                "N/A",
                """\nError: calling < convert.to_float > and passing it the string 'N/A' did
                not return the vaule unchanged.
                """,
            )

    def test_03_to_float_tuple(self):
        """to_float tuple"""

        try:
            getattr(convert, "to_float")
        except AttributeError:
            raise AttributeError("< convert.to_float > function not found.")
        else:
            self.assertEqual(
                convert.to_float(("C-3PO", "R2-D2", "BB-8")),
                ("C-3PO", "R2-D2", "BB-8"),
                """\nError: calling < convert.to_float > and passing it the tuple
                ('C-3PO', 'R2-D2', 'BB-8') did not return the expected value ('C-3PO', 'R2-D2', 'BB-8')
                unchanged.
                """,
            )

    def test_04_to_int_str_num_commas(self):
        """to_int string number with commas"""

        try:
            getattr(convert, "to_int")
        except AttributeError:
            raise AttributeError("< convert.to_int > function not found.")
        else:
            self.assertEqual(
                convert.to_int("1,000,000"),
                1000000,
                """\nError: calling < convert.to_int > and passing it the string '1,000,000'
                did not return the expected integer value. Make sure you handle the thousands
                separator commas in the string.
                """,
            )

    def test_05_to_int_str_unknown(self):
        """to_int string unknown"""

        try:
            getattr(convert, "to_int")
        except AttributeError:
            raise AttributeError("< convert.to_int > function not found.")
        else:
            self.assertEqual(
                convert.to_int("unknown"),
                "unknown",
                """\nError: calling < convert.to_int > and passing it the string 'unknown' did
                not return the value unchanged. Recheck your implementation of the function's
                < try > / < except > blocks.
                """,
            )

    def test_06_to_int_list(self):
        """to_int list"""

        try:
            getattr(convert, "to_int")
        except AttributeError:
            raise AttributeError("< convert.to_int > function not found.")
        else:
            self.assertEqual(
                convert.to_int(["C-3PO", "R2-D2", "BB-8"]),
                ["C-3PO", "R2-D2", "BB-8"],
                """\nError: calling < convert.to_int > and passing it the list
                ['C-3PO', 'R2-D2', 'BB-8'] did not return the list unchanged.
                """,
            )

    def test_07_to_list_str_delimiter(self):
        """to_list string with delimiter"""

        try:
            getattr(convert, "to_list")
        except AttributeError:
            raise AttributeError("< convert.to_list > function not found.")
        else:
            self.assertEqual(
                convert.to_list("C-3PO, R2-D2, BB-8", ", "),
                ["C-3PO", "R2-D2", "BB-8"],
                """\nError: calling < convert.to_list > and passing it the string
                'C-3PO, R2-D2, BB-8' did not return the expected list.
                """,
            )

    def test_08_to_list_str_no_delimiter(self):
        """to_list no delimiter"""

        try:
            getattr(convert, "to_list")
        except AttributeError:
            raise AttributeError("< convert.to_list > function not found.")
        else:
            self.assertEqual(
                convert.to_list("C-3PO R2-D2 BB-8"),
                ["C-3PO", "R2-D2", "BB-8"],
                """\nError: calling < convert.to_list > and passing it the string
                'C-3PO R2-D2 BB-8' did not return the expected list.
                """,
            )

    def test_09_to_list_int(self):
        """to_list integer"""

        try:
            getattr(convert, "to_list")
        except AttributeError:
            raise AttributeError("< convert.to_list > function not found.")
        else:
            self.assertEqual(
                convert.to_list(506),
                506,
                """\nError: calling < convert.to_list > and passing it the integer 506 did
                not return the integer value unchanged.
                """,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
