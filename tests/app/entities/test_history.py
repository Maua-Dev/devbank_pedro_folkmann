import pytest
from src.app.entities.history import History
from src.app.enums.user_trans_type_enum import UserTransTypeEnum
from src.app.errors.entity_errors import ParamNotValidated


class Test_History:
    def test_history(self):
        history = History(UserTransTypeEnum.WITHDRAW, "1000", 2000.0, 11111)
        assert history.type_transaction.value == "WITHDRAW"
        assert history.value == "1000"
        assert history.current_balance == 2000.0
        assert history.timestamp == 11111

    #type_transaction
    def test_type_transction_none(self):
        with pytest.raises(ParamNotValidated):
            history = History(None, "1000", 2000.0, 11111)
    def test_type_transction_not_enum(self):
        with pytest.raises(ParamNotValidated):
            history = History("None", "1000", 2000.0, 11111)

    #value
    def test_value_none(self):
        with pytest.raises(ParamNotValidated):
            history = History(UserTransTypeEnum.WITHDRAW, None, 2000.0, 11111)
    def test_value_not_string(self):
        with pytest.raises(ParamNotValidated):
            history = History(UserTransTypeEnum.WITHDRAW, 1000 , 2000.0, 11111)
    
    #current_balance
    def test_user_current_none(self):
        with pytest.raises(ParamNotValidated):
            history = History(UserTransTypeEnum.WITHDRAW, "1000", None, 11111)
    def test_user_current_not_float(self):
        with pytest.raises(ParamNotValidated):
            history = History(UserTransTypeEnum.WITHDRAW, "1000", "2000.0", 11111)
    def test_user_current_is_negative(self):
        with pytest.raises(ParamNotValidated):
            history = History(UserTransTypeEnum.WITHDRAW, "1000", -2000.0, 11111)

    #timestamp
    def test_timestamp_none(self):
        with pytest.raises(ParamNotValidated):
            history = History(UserTransTypeEnum.WITHDRAW, "1000", 2000.0, None)
    def test_timestamp_not_int(self):
        with pytest.raises(ParamNotValidated):
            history = History(UserTransTypeEnum.WITHDRAW, "1000", 2000.0, "1111")
    
