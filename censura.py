import re
frasecompleta='Mi amigo es muy mamón, y la vez su primo, al que llaman mamónides, es un mendrugo bastante zopenco.'

censuradas=['mamón', 'mendrugo', 'zopenco']
regex = "|".join(censuradas)
frasecompleta = re.sub(f"\\b({regex})\\b", "***", frasecompleta)
print(frasecompleta)


