import pytest

from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated

class Test_User:
    
    def test_user(self):
        user = User("Pedro", "0001", "22002-3", 999.9)
        assert user.name == "Pedro"
        assert user.agency == "0001"
        assert user.account == "22002-3"
        assert user.current_balance == 999.9

    #name
    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(None, "0001", "22002-3", 999.9)

    def test_user_name_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            user = User(21312, "0001", "22002-3", 999.9)
               
    def test_user_name_is_len_less_3(self):
        with pytest.raises(ParamNotValidated):
            user = User("aa", "0001", "22002-3", 999.9)
            

    #agency            
    def test_user_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", None, "22002-3", 999.9) 

    def test_user_agency_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", 1000, "22002-3", 999.9) 

    def test_user_agency_is_len_not_4(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", "00012", "22002-3", 999.9) 

    def test_user_agency_is_not_digit(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", "22a2", "22002-3", 999.9) 


    #account
    def test_user_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", "0001", None, 999.9)

    def test_user_account_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", "0001", 22002, 999.9)

    def test_user_account_is_not_len_7(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", "0001", "22002-33", 999.9)

    def test_user_account_dont_have_minus(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", "0001", "2200233", 999.9)

    def test_user_account_is_digit(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", "0001", "220x2-3", 999.9)

    #current_balance
    def test_user_current_none(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", "0001", "22002-3", None)
    def test_user_current_not_float(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", "0001", "22002-3", "999.9")
    def test_user_current_is_negative(self):
        with pytest.raises(ParamNotValidated):
            user = User("Pedro", "0001", "22002-3", -999.9)
