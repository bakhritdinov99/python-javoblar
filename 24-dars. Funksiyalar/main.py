
mevalar = ['olma', 'anor', 'anjir', 'asal']
x = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(x)