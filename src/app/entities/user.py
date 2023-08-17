from typing import Tuple
from ..errors.entity_errors import ParamNotValidated


class User:
    name:str
    agency:str
    account:str
    current_balance:float

    def __init__(self, name=None, agency=None, account=None,current_balance=None):

        validation_name = self.validate_name(name) 
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency) 
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account) 
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance
        

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True, "")

    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return (False, "Agency is required")
        if type(agency) != str:
            return (False, "Agency must be a string")
        if len(agency) != 4 :
            return (False, "Agency must be 4 characters long")
        if(agency.isdigit() == False):
            return (False, "Agency must be a number")
        return (True, "")

    @staticmethod
    def validate_account(account:str) -> Tuple[bool,str]:
        if account is None:
            return (False, "Account is required")
        if type(account) != str:
            return (False, "Account must be a string")
        if len(account) != 7 :
            return (False, "Account must be 7 characters long")
        if account[5] != '-':
            return (False, "Account text must be in the format of XXXXX-X") 
        if not account[:5].isdigit() or not account[6:].isdigit():
            return (False, "Account text must be in the format of 00000-0")
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

    def to_dict(self):
        return{
            "name" : self.name,
            "agency" : self.agency,
            "account" : self.account,
            "current_balance" : self.current_balance
        }




