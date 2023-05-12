import unittest
from unittest.mock import patch
from on_call_developer import OnCallDeveloperList
import excel_writer


class OnCallDeveloperTest(unittest.TestCase):
    def setUp(self):
        self.list = OnCallDeveloperList(
            ['Lynx Lockwood', 'Rex Sharp', 'Nova Frost'], 3)

    @patch.object(excel_writer.ExcelWriter, 'print_row')
    @patch.object(excel_writer.ExcelWriter, 'write')
    def test_generate(self, write_mock, print_row_mock):
        self.list.generate()
        write_mock.assert_called_once_with()
        self.assertEqual(print_row_mock.call_count, 3)


if __name__ == '__main__':
    unittest.main()
