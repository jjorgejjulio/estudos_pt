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

#referência
x1data=np.array(df['mZ1'])
x2data=np.array(df['mZ2'])
Referencia= np.hstack((x1data, x2data))

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

#Essa maneira que as funções foram determinadas estão erradas, seria possível realizar apenas uma única função.

#Dessa forma que foi realizada a separação das possíveis combinações das partículas com o mesmo sabor, não é possível determinar qual é a correta.

# Agora, as combinações das partículas com mesmo sabor serão escolhidas utilizando o Pt.

#==================================================================================================================

#calculo da massa zz
def massa_zz (row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])
    vetores_com_pt = [(v1.pt, v1), (v2.pt, v2), (v3.pt, v3), (v4.pt, v4)]
    vetores_ordenados = sorted(vetores_com_pt, key=lambda x: x[0], reverse=True)
    candidato = [vetor for _, vetor in vetores_ordenados]

    if row['PID1'] == - row['PID2'] and row['PID3'] == -row['PID4'] and abs(row['PID1']) != abs(row['PID3']):
        return (v1+v2).mass , (v3+v4).mass
    
    if row['Q1'] == row['Q2'] and row['Q1'] != row['Q3'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) == abs(row['PID3']):
        return (candidato[0]+candidato[1]).mass , (candidato[2]+candidato[3]).mass

    if row['Q1'] != row['Q2'] and row['Q3'] != row['Q4'] and  row['Q1'] == row['Q3'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) == abs(row['PID3']):
        return (candidato[0]+candidato[1]).mass , (candidato[2]+candidato[3]).mass
    
    if row['Q1'] != row['Q2'] and row['Q3'] != row['Q4'] and  row['Q1'] == row['Q4'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) == abs(row['PID3']):
         return (candidato[0]+candidato[1]).mass , (candidato[2]+candidato[3]).mass
    else:
         return None, None


#Distribuição do pt
def distribuiçao_pt(row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])  
    vetores_com_pt = [(v1.pt, v1), (v2.pt, v2), (v3.pt, v3), (v4.pt, v4)]
    vetores_ordenados = sorted(vetores_com_pt, key=lambda x: x[0], reverse=True)
    pt_partículas_ordenadas = [pt for pt, _ in vetores_ordenados]
    return pt_partículas_ordenadas




#plot das massas
zz_resultados = [item for result in df.apply(massa_zz, axis=1) for item in result if item is not None]
print(len(zz_resultados))

plt.figure()
bins = 25
largura=2
plt.hist(zz_resultados, bins, range=(0, 150), histtype='step', color="blue", label='calculo',linewidth=largura)
plt.hist(Referencia, bins, range=(0, 150), histtype='step', color="green", label='referência',linewidth=largura)
fontsize=20
plt.xlabel(r'$M_{ℓ⁺ℓ⁻}$ [$GeV/c^2$]',fontsize=fontsize)
plt.ylabel(r'Eventos',fontsize=fontsize)
plt.title('Distribuição da massa do bóson Z',fontsize=fontsize)
plt.legend()


#plot do pt
pt_distribuido = df.apply(distribuiçao_pt, axis=1)
part1, part2, part3, part4 = zip(*pt_distribuido)

plt.figure()
bins = 25
largura=2
plt.hist(part1, bins, range=(0, 150), histtype='step', color="blue", label='partícula 1',linewidth=largura)
plt.hist(part2, bins, range=(0, 150), histtype='step', color="green", label='partícula 2',linewidth=largura)
plt.hist(part3, bins, range=(0, 150), histtype='step', color="purple", label='partícula 3',linewidth=largura)
plt.hist(part4, bins, range=(0, 150), histtype='step', color="red", label='partícula 4',linewidth=largura)
fontsize=20
plt.xlabel(r'Distribuição de $P_T$ [GeV]',fontsize=fontsize)
plt.ylabel(r'Eventos',fontsize=fontsize)
plt.title('Distribuição do Pt',fontsize=fontsize)
plt.legend()

#==================================================================================================================
#Fazendo o plot da massa do Higgs
def massa_H(row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])
    return (v1 + v2 + v3 + v4).mass

# Aplicando a função à coluna e criando uma nova coluna no DataFrame
df['massa_H'] = df.apply(massa_H, axis=1)

#referência do Higgs

ref_higgs=np.array(df['M'])

# Plotando o histograma
plt.figure()
bins = 25
largura = 2
plt.hist(df['massa_H'], bins, range=(0, 150), histtype='step', color="blue", label='calculo', linewidth=largura)
plt.hist(ref_higgs, bins, range=(0, 150), histtype='step', color="red", label='referência', linewidth=largura)
fontsize = 20
plt.xlabel(r'$M_{ℓ⁺ℓ⁻}$ [$GeV/c^2$]', fontsize=fontsize)
plt.ylabel(r'Eventos', fontsize=fontsize)
plt.title('Distribuição da massa do Higgs', fontsize=fontsize)
plt.legend()

plt.show()
