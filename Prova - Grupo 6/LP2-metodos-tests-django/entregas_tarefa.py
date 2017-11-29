from datetime import datetime

def verifica_prazo(prazo_questao_dia, prazo_questao_mes):
    now = datetime.now()
    if now.month < prazo_questao_mes:
            return True
    elif now.month == prazo_questao_mes:
        if now.day <= prazo_questao_dia:
            return True
        else:
            return False
    else:
        return False