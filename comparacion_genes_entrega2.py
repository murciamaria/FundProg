# archivos formato genebank de las secuencias

prochloro_sec = 'Prochlorococcus.gb'
synecho_sec = 'Synechococcus.gb'

# definimos los archivos como sets y demás variables

prochloro_sec_set = set()
synecho_sec_set = set()

interseccion = set()
diferencia_prochloro = set()
diferencia_synecho = set()


#extracción genes Prochlorococcus

with open(prochloro_sec) as file:
    for line in file:
        if "/gene=" in line:
            line = line.strip()
            gen1 = line[7:-1]
            #print(gen1)
            prochloro_sec_set.add(gen1)

#extracción genes Synechococcus

with open(synecho_sec) as file:
    for line in file:
        if "/gene=" in line:
            line = line.strip()
            gen2 = line[7:-1]
            #print(gen2)
            synecho_sec_set.add(gen2)

            interseccion = prochloro_sec_set.intersection(synecho_sec_set)
            num_interseccion = len(interseccion)

            diferencia_synecho = synecho_sec_set.difference(prochloro_sec_set)
            num_diferencia_synecho = len(diferencia_synecho)

            diferencia_prochloro = prochloro_sec_set.difference(synecho_sec_set)
            num_diferencia_prochloro = len(diferencia_prochloro)

num_prochloro = len(prochloro_sec_set)
num_synecho = len(synecho_sec_set)

print('Genes totales Synechococcus sp. PCC 7002: ')
print(num_synecho)

print('Genes totales Prochlorococcus marinus subsp. marinus str. CCMP1375:')
print(num_prochloro)

print('La cantidad de genes que comparten ambos organismos es:')
print(num_interseccion)

print('La cantidad de genes presentes solo en Synechococcus sp. PCC 7002 es:')
print(num_diferencia_synecho)

print('La cantidad de genes presentes solo en Prochlorococcus '
      'marinus subsp. marinus str. CCMP1375 es:')
print(num_diferencia_prochloro)
