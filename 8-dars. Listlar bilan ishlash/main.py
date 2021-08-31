# states = ['Uzbekistan', 'Poland', 'USA', 'Russia', 'Afghanistan', 'Turkmenistan']
# lenght = len(states)
# print(lenght)

# print(sorted(states))
# print(sorted(states, reverse=True))
# print(states)
# states.reverse()
# states.sort()
# states.sort(reverse=True)
# print(states)

# sonlar = list(range(120,1200))
# yigindi = sum(sonlar)
# ayirma = max(sonlar)-min(sonlar)
# print(yigindi)
# print(ayirma)
# print(len(sonlar))
# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar[530:550])

taomlar = ['palov', 'saryog\'', 'lag\'mon', 'manti', 'sut']
nonushta = taomlar[:]
# print(nonushta)
nonushta.remove('palov')
nonushta.remove('lag\'mon')
nonushta.remove('manti')

# print(nonushta)

nonushta.append('choy')
nonushta.append('shakar')
# print(taomlar)
# print(nonushta)
nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"