# Bibliotecas utilizadas
import pandas as pd
import vector
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
from scipy.optimize import curve_fit
import os
import matplotlib.patches as mpatches
from matplotlib.ticker import MultipleLocator
import seaborn as sns



# Arquivo csv contendo as informações de cada partícula (4 leptons)
pasta_csv = r"C:\Users\venut\Desktop\CSV"
# Lista para armazenar os caminhos completos de todos os arquivos CSV na pasta
arquivos_csv = []
# envia os arquivos da pasta para a lista criada
for arquivo in os.listdir(pasta_csv):
    arquivos_csv.append(os.path.join(pasta_csv, arquivo))
# junta os arquivos em 1 só
df = pd.concat((pd.read_csv(file_path) for file_path in arquivos_csv), axis=0)



def ptmax(row):
    pt_values = [row[f'pt{i}'] for i in range(1, 5)]
    max_pt = max(pt_values)
    return max_pt
df['ptmax1'] = df.apply(ptmax, axis=1)

def second_max_pt(row):
    pt_values = [row[f'pt{i}'] for i in range(1, 5)]
    sorted_pts = sorted(pt_values, reverse=True)
    second_max_pt = sorted_pts[1] if len(sorted_pts) >= 2 else None
    return second_max_pt
df['second_max_pt'] = df.apply(second_max_pt, axis=1)

def third_max_pt(row):
    pt_values = [row[f'pt{i}'] for i in range(1, 5)]
    sorted_pts = sorted(pt_values, reverse=True)
    third_max_pt = sorted_pts[2] if len(sorted_pts) >= 3 else None
    return third_max_pt
df['third_max_pt'] = df.apply(third_max_pt, axis=1)

def min_pt(row):
    pt_values = [row[f'pt{i}'] for i in range(1, 5)]
    min_pt = min(pt_values)
    return min_pt
df['min_pt'] = df.apply(min_pt, axis=1)

# Passando os dados para array
part1=np.array(df['ptmax1'])
part2=np.array(df['second_max_pt'])
part3=np.array(df['third_max_pt'])
part4=np.array(df['min_pt'])
pt_z=np.hstack((part1, part2,part3,part4))


#plots
bins = 21
largura=2
plt.hist(part1, bins, range=(0, 150), histtype='step', color="blue", label='partícula 1',linewidth=largura)
plt.hist(part2, bins, range=(0, 150), histtype='step', color="green", label='partícula 2',linewidth=largura)
plt.hist(part3, bins, range=(0, 150), histtype='step', color="purple", label='partícula 3',linewidth=largura)
plt.hist(part4, bins, range=(0, 150), histtype='step', color="red", label='partícula 4',linewidth=largura)

#legendas
fontsize=20
plt.legend(fontsize=14)
plt.xlabel(r'$P_T$ (GeV)',fontsize=fontsize)
plt.ylabel('Frequência',fontsize=fontsize)
plt.title(r'Distribuição de $P_T$',fontsize=fontsize)



#Massa de referência do bóson Z
massa_z1=np.array(df['mZ1'])
massa_z2=np.array(df['mZ2'])
massa_z= np.hstack((massa_z1, massa_z2))


def compute_pt1(row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])

    if row['Q1'] != row['Q2'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) != abs(row['PID3']):
         return (v1+v2).pt

def compute_pt2(row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])

    if row['Q1'] != row['Q2'] and abs(row['PID1']) == abs(row['PID2']) and abs(row['PID1']) != abs(row['PID3']):
         return (v3+v4).pt

df['pt_12'] = df.apply(compute_pt1, axis=1)
df['pt_34'] = df.apply(compute_pt2, axis=1)

pt_z1=np.array(df['pt_12'])
pt_z2=np.array(df['pt_34'])
pt_zz= np.hstack((pt_z1, pt_z2))




plt.figure(figsize=(7, 6))
plt.hist2d(massa_z, pt_zz, bins=(10,25), cmap=plt.cm.jet)
plt.colorbar(label='Densidade')
plt.ylim(0,150)

#Legendas
fontsize=20
plt.xlabel(r'$M_{ℓ⁺ℓ⁻}$ [$GeV/c^2$]',fontsize=fontsize)
plt.ylabel(r'Distribuição de $P_T$ [GeV]',fontsize=fontsize)
plt.title('Produção do Bóson Z',fontsize=fontsize)
plt.show()
