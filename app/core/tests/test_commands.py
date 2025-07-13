from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError

from django.core.management import call_command
from django.test import SimpleTestCase

@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandTest(SimpleTestCase):
    
    def test_wait_for_db(self, patched_getitem):
        patched_getitem.return_value = True

        call_command('wait_for_db')
        self.assertEqual(patched_getitem.call_count, 1)

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_get_item):
        patched_get_item.side_effect = [Psycopg2OpError] + [OperationalError] * 5 + [True]
        call_command('wait_for_db')
        self.assertEqual(patched_get_item.call_count, 6)
