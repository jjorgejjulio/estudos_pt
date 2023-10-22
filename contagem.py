import pandas as pd
import vector
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
import os



# Arquivo csv contendo as informações de cada partícula (4 leptons)
pasta_csv = r"C:\Users\venut\Desktop\CSV"
# Lista para armazenar os caminhos completos de todos os arquivos CSV na pasta
arquivos_csv = []
# envia os arquivos da pasta para a lista criada
for arquivo in os.listdir(pasta_csv):
    arquivos_csv.append(os.path.join(pasta_csv, arquivo))
# junta os arquivos em 1 só
df = pd.concat((pd.read_csv(file_path) for file_path in arquivos_csv), axis=0)


x1data=np.array(df['mZ1'])
x2data=np.array(df['mZ2'])
x3data= np.hstack((x1data, x2data))

zz_resultados = []


def zz_sabor_oposto (row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])

    if row['PID1'] == - row['PID2'] and row['PID3'] == -row['PID4'] and abs(row['PID1']) != abs(row['PID3']):
        return (v1+v2).mass , (v3+v4).mass
    else:
        return None, None


def zz_candidato1 (row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])

    if row['Q1'] == row['Q2'] and row['Q1'] != row['Q3'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) == abs(row['PID3']):
            return (v1+v3).mass , (v2+v4).mass
    else:
        return None , None


def zz_candidato2 (row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])

    if row['Q1'] == row['Q2'] and row['Q1'] != row['Q3'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) == abs(row['PID3']) :
            return (v1+v4).mass , (v2+v3).mass
    else:
        return None , None


def zz_candidato3 (row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])

    if row['Q1'] != row['Q2'] and row['Q3'] != row['Q4'] and  row['Q1'] == row['Q3'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) == abs(row['PID3']) :
            return (v1+v2).mass , (v3+v4).mass
    else:
        return None , None
    

def zz_candidato4 (row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])

    if row['Q1'] != row['Q2'] and row['Q3'] != row['Q4'] and  row['Q1'] == row['Q3'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) == abs(row['PID3']) :
            return (v1+v4).mass , (v2+v3).mass
    else:
        return None , None


def zz_candidato5 (row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])

    if row['Q1'] != row['Q2'] and row['Q3'] != row['Q4'] and  row['Q1'] == row['Q4'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) == abs(row['PID3']) :
            return (v1+v2).mass , (v3+v4).mass
    else:
        return None , None


def zz_candidato6 (row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])

    if row['Q1'] != row['Q2'] and row['Q3'] != row['Q4'] and  row['Q1'] == row['Q4'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) == abs(row['PID3']) :
            return (v1+v3).mass , (v2+v4).mass
    else:
        return None , None

candidato1 = [item for result in df.apply(zz_candidato1, axis=1) for item in result if item is not None]
candidato2 = [item for result in df.apply(zz_candidato2, axis=1) for item in result if item is not None]

candidato1= [valor for valor in candidato1 if 12 < valor < 103]
candidato2= [valor for valor in candidato2 if 12 < valor < 103]

candidato3 = [item for result in df.apply(zz_candidato3, axis=1) for item in result if item is not None]
candidato4 = [item for result in df.apply(zz_candidato4, axis=1) for item in result if item is not None]

candidato3= [valor for valor in candidato3 if 12 < valor < 103]
candidato4= [valor for valor in candidato4 if 12 < valor < 103]

candidato5 = [item for result in df.apply(zz_candidato5, axis=1) for item in result if item is not None]
candidato6 = [item for result in df.apply(zz_candidato6, axis=1) for item in result if item is not None]

candidato5= [valor for valor in candidato5 if 12 < valor < 103]
candidato6= [valor for valor in candidato6 if 12 < valor < 103]


resultados1 = [item for result in df.apply(zz_sabor_oposto, axis=1) for item in result if item is not None]
zz_resultados.extend(resultados1)
print(len(zz_resultados))





bins = 21
largura=2
plt.figure()
#plt.hist(zz_resultados, bins,  histtype='step', color="blue", label='Calculado',linewidth=largura)
#plt.hist(x3data, bins,  histtype='step', color="green", label='Referência',linewidth=largura)
plt.hist(candidato1, bins,  histtype='step', color="red", label='cand1',linewidth=largura)
plt.hist(candidato2, bins,  histtype='step', color="blue", label='cand2',linewidth=largura)
plt.legend(fontsize=14)

plt.figure()
plt.hist(candidato3, bins,  histtype='step', color="red", label='cand1',linewidth=largura)
plt.hist(candidato4, bins,  histtype='step', color="blue", label='cand2',linewidth=largura)
plt.legend(fontsize=14)

plt.figure()
plt.hist(candidato5, bins,  histtype='step', color="red", label='cand1',linewidth=largura)
plt.hist(candidato6, bins,  histtype='step', color="blue", label='cand2',linewidth=largura)

plt.legend(fontsize=14)
plt.show()