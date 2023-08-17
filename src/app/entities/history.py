from typing import Tuple

from src.app.enums.user_trans_type_enum import UserTransTypeEnum
from ..errors.entity_errors import ParamNotValidated


class History:
    type_transaction: UserTransTypeEnum
    value:str
    current_balance:float
    timestamp: int

    def __init__(self, type_transaction: UserTransTypeEnum=None, value=None, current_balance=None, timestamp=None):
        
        validation_type_transaction = self.validate_type_transaction(type_transaction)
        if validation_type_transaction[0] is False:
            raise ParamNotValidated("type", validation_type_transaction[1])
        self.type_transaction = type_transaction

        validation_value = self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("type", validation_value[1])
        self.value = value

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("type", validation_timestamp[1])
        self.timestamp = timestamp

    @staticmethod
    def validate_type_transaction(type_transaction: UserTransTypeEnum) -> Tuple[bool, str]:
        if type_transaction is None:
            return (False, "Type is required")
        if type(type_transaction) != UserTransTypeEnum:
            return (False, "Type must be a enum")
        return (True, "")
    
    @staticmethod
    def validate_value(value: str) -> Tuple[bool, str]:
        if value is None:
            return (False, "Value is required")
        if type(value) != str:
            return (False, "Value must be a String")
        return (True, "")
   
    @staticmethod
    def validate_current_balance(current_balance:float) -> Tuple[bool,str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        if current_balance < 0:
            return (False, "Current balance can't negative")
        return (True, "")
    
    @staticmethod
    def validate_timestamp(timestamp: int) -> Tuple[bool,str]:
        if timestamp is None:
            return (False, "Timestamp is required")
        if type(timestamp) != int:
            return(False, "Timestamp must be a float")
        return (True,"")
    
    def to_dict(self):
        return{
            "type_transaction" : self.type_transaction,
            "value" : self.value,
            "current_balance" : self.current_balance,
            "timestamp" : self.timestamp
        }   
    