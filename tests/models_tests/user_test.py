from tests import OhmTestCase
from models import User

class UserTest(OhmTestCase):
    ####################################################################################
    #
    #   Lookup Attributes
    #
    ####################################################################################
    def test_get_attribute(self):
        pass

    def test_get_rel_user_attribute(self):
        pass

    def test_delete_attribute(self):
        pass

    def test_add_multi(self):
        pass

    def test_get_multi(self):
        assert self.chuck.get_multi("PHONE") == ['+14086441234', '+14086445678']
        assert self.elvis.get_multi("PHONE") == ['+14086551234']
        assert self.justin.get_multi("PHONE") == []

    def test_delete_multi(self):
        pass

    def test_replace_multi(self):
        pass

    def test_get_text_record(self):
        pass

    def test_get_text(self):
        pass

    def test_put_text(self):
        pass

    ####################################################################################
    #
    #   Ohm Account Test
    #
    ####################################################################################
    def test_full_name(self):
        assert self.chuck.full_name() == "Chuck Norris"
        assert self.elvis.full_name() == "Elvis Presley"
        assert self.justin.full_name() == "Justin Bieber"

    def test_set_display_name(self):
        pass

    def test_short_name(self):
        assert self.chuck.short_name() == "Chuck Norris"
        assert self.elvis.short_name() == "Elvis Presley"
        assert self.justin.short_name() == "Justin Bieber"

    def test_get_email(self):
        assert self.chuck.get_email() == "test@test.com"
        assert self.elvis.get_email() == "test2@test.com"
        assert self.justin.get_email() == "test3@test.com"

    def test_get_points_and_dollars(self):
        assert self.chuck.get_points_and_dollars() == {"points": 5000, "dollars" : 5000/100}
        assert self.elvis.get_points_and_dollars() ==  {"points": 0, "dollars" : 0/100}
        assert self.justin.get_points_and_dollars() == {"points": 0, "dollars" : 0/100}

    def test_get_tier(self):
        assert self.chuck.get_tier() == "Carbon"
        assert self.elvis.get_tier() == "Carbon"
        assert self.justin.get_tier() == "Silver"

    def test_is_below_tier(self):
        assert self.chuck.is_below_tier("Bronze") == True
        assert self.chuck.is_below_tier("Silver") == True
        assert self.chuck.is_below_tier("Gold") == True
        assert self.chuck.is_below_tier("Gold") == True
        assert self.chuck.is_below_tier("") == False

        assert self.elvis.is_below_tier("Bronze") == True
        assert self.elvis.is_below_tier("Silver") == True
        assert self.elvis.is_below_tier("Gold") == True
        assert self.elvis.is_below_tier("Platinum") == True
        assert self.elvis.is_below_tier("") == False

        assert self.justin.is_below_tier("Bronze") == False
        assert self.justin.is_below_tier("Silver") == False
        assert self.justin.is_below_tier("Gold") == True
        assert self.justin.is_below_tier("Platinum") == True
        assert self.justin.is_below_tier("") == False

    def test_is_active(self):
        assert self.chuck.is_active() == True
        assert self.elvis.is_active() == True
        assert self.justin.is_active() == True

    def test_is_authenticated(self):
        assert self.chuck.is_authenticated() == True
        assert self.elvis.is_authenticated() == True
        assert self.justin.is_authenticated() == True

    def test_is_anonymonus(self):
        assert self.chuck.is_anonymous() == False
        assert self.elvis.is_anonymous() == False
        assert self.justin.is_anonymous() == False

    def test_get_id(self):
        assert self.chuck.get_id() == 1
        assert self.elvis.get_id() == 2
        assert self.justin.get_id() == 3

    def test_equality(self):
        assert self.chuck == self.chuck
        assert self.elvis == self.elvis
        assert self.justin == self.justin

        assert not self.chuck == self.elvis
        assert self.chuck != self.justin


    ####################################################################################
    #
    # Class methods Tests
    #
    ####################################################################################
    def test_last(self):
        last = User.last()
        assert last.user_id == 3

    '''
    get_by_email invokes a function, is_deleted(),
    which is not defined, once defined, uncomment
    def test_get_by_email(self):
        user = User.get_by_email("test@test.com")
        assert user.user_id == 1
        assert user.user_name == "tester1"
        assert user.display_name == "Chuck Norris"

        user = User.get_by_email("test2@test.com")
        assert user.user_id == 2
        assert user.user_name == "tester2"
        assert user.display_name == "Elvis Presley"

        user = User.get_by_email("test3@test.com")
        assert user.user_id == 3
        assert user.user_name == "tester3"
        assert user.display_name == "Justin Bieber"

        user = User.get_by_email("")
        assert user == None
    '''

    '''
    get_by_phone invokes a function, is_deleted(),
    which is not defined, once defined, uncomment
    def test_get_by_phone(self):
        user = User.get_by_phone('+14086441234')
        assert user.user_id == 1
        assert user.user_name == "tester1"
        assert user.display_name == "Chuck Norris"

        user = User.get_by_phone('+1408644567')
        assert user.user_id == 1
        assert user.user_name == "tester1"
        assert user.display_name == "Chuck Norris"

        user = User.get_by_phone('+14086551234')
        assert user.user_id == 3
        assert user.user_name == "tester3"
        assert user.display_name == "Justin Bieber"

        user = User.get_by_phone('+')
        assert user == None
    '''

    def test_find_by_attribute(self):
        row = User.find_by_attribute("LOCATION", "USA")
        assert row.user_id == 2

        row = User.find_by_attribute("LOCATION", "EUROPE")
        assert row.user_id == 1
