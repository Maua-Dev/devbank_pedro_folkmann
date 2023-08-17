from enum import Enum

class UserTransTypeEnum(Enum):
    WITHDRAW='WITHDRAW'
    DEPOSIT='DEPOSIT'

input = "WITHDRAW"
if(type(input) != str):
    print("Error, necessita ser uma string")
elif(input not in [type.value for type in UserTransTypeEnum]):
    print("Não é uma string valida")
else:
    print("Tudo certo")