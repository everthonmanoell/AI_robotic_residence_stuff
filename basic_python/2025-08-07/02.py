texto = 'a a Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vehicula mauris ac bibendum euismod. Aliquam sapien felis, luctus vitae lacus at, elementum tempor neque. Donec at nisl lectus. Sed ultrices pellentesque odio non vulputate. Nam eu est euismod, viverra metus rutrum, luctus quam. Nunc hendrerit elit at vestibulum porta. Quisque porttitor justo vel odio volutpat blandit. Cras non elit ligula. Proin et luctus tellus. Nam lacinia tincidunt justo a gravida. Vestibulum efficitur et odio rhoncus faucibus.'

# print(texto)
texto = texto.replace(',', '').replace('.', '')
# print(texto)

palavras = texto.split()

# print(palavras)

# frequencia em que cada palavra ocorre


def frequencia_palavra(palvaras):
    frequencia = {}
    
    for p in palavras:
        p = p.lower()
        if p not in frequencia:
            frequencia[p] = 0
        
        frequencia[p] = frequencia[p] + 1
    
    return frequencia 

print(frequencia_palavra(palavras))

#quantas palavras começam com determinada letra inicial




