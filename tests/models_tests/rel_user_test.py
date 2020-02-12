from tests import OhmTestCase
from models import RelUser

class RelUserTest(OhmTestCase):
    ####################################################################################
    #
    #   Lookup Attributes
    #
    ####################################################################################
    def test_find_by_lookup_attribute(self):
        row = RelUser.find_by_lookup_attribute("LOCATION", "USA")
        assert row.user_id == 2

        row = RelUser.find_by_lookup_attribute("LOCATION", "EUROPE")
        assert row.user_id == 1

    def test_find_all_by_rel_lookup(self):
        results = RelUser.find_all_by_rel_lookup("LOCATION")
        assert results[0].user_id == 1
        assert results[1].user_id == 2
        assert results[2].user_id == 3
