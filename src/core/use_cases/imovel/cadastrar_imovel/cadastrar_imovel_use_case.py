from core.use_cases.imovel.cadastrar_imovel.cadastrar_imovel_input import CadastrarImovelInput
from core.use_cases.imovel.cadastrar_imovel.cadastrar_imovel_validation import CadastrarImovelValidation
from lib.use_case.output.output import Output



def handle(input: CadastrarImovelInput):
    validation = CadastrarImovelValidation()
    validation_output = validation.validate(input)

    if validation_output.get_isvalid() != True:
        return Output(validation_output.get_error_messages(), isvalid = False)
    
    """ 
     Executa regra de negocio...
    """

    return True