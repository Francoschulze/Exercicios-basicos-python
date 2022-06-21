"""
Utilize o módulo datetime e mostre na tela a data e hora atual do sistema
de acordo com o formato: DD/MM/AAAA - HH:MM:SS
"""

# Importando o método datetime
from datetime import datetime

# Aqui é o seguinte:
# datetime.today() informa o dia atual
# para formatar a hora use o método strftime()
data_hora_atual = datetime.today().strftime('%d-%m-%y %H:%M')

print(data_hora_atual)
