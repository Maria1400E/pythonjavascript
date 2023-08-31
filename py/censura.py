"""
import re
frasecompleta='Mi amigo es muy mamón, y la vez su primo, al que llaman mamónides, es un mendrugo bastante zopenco.'

censuradas=['mamón', 'mendrugo', 'zopenco']
regex = "|".join(censuradas)
frasecompleta = re.sub(f"\\b({regex})\\b", "***", frasecompleta)
print(frasecompleta)
"""

import re

def censurado(texto=None, busqueda=None):
    resultado = ""

    if not texto and not busqueda:
        resultado = "No puedes leer el texto y la busqueda"
    elif not texto and busqueda:
        resultado = "No puedes leer el texto"
    elif texto and not busqueda:
        resultado = "No puedes hacer la busqueda"
    elif texto and busqueda:
        resultado = re.sub(re.escape(busqueda), "[-CENSURADO-]", texto, flags=re.IGNORECASE)

    return resultado

print(censurado("hola hola hola", "hola"))