from scipy.stats import norm
import numpy as np

'''
Uma amostra aleatória simples de 1976 itens de uma população normalmente distribuída, com desvio padrão populacional igual a 11, resultou em uma média amostral de 28.

Qual o intervalo de confiança de 90% para a média populacional?
'''

media_amostral = 28
desvio_padrao = 11
n = 1976

norm.interval(confidence = 0.90, 
                loc = media_amostral, 
                scale = desvio_padrao / np.sqrt(n))

# saida 27,59 a 28,41


