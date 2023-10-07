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


# Arquivo csv contendo as informações de cada partícula (4 leptons)
pasta_csv = r"C:\Users\venut\Desktop\CSV"
# Lista para armazenar os caminhos completos de todos os arquivos CSV na pasta
arquivos_csv = []
# envia os arquivos da pasta para a lista criada
for arquivo in os.listdir(pasta_csv):
    arquivos_csv.append(os.path.join(pasta_csv, arquivo))
# junta os arquivos em 1 só
df = pd.concat((pd.read_csv(file_path) for file_path in arquivos_csv), axis=0)



def ptmax1(row):
    v1 = vector.obj(px=row['px1'], py=row['py1'], pz=row['pz1'], E=row['E1'])
    v2 = vector.obj(px=row['px2'], py=row['py2'], pz=row['pz2'], E=row['E2'])
    v3 = vector.obj(px=row['px3'], py=row['py3'], pz=row['pz3'], E=row['E3'])
    v4 = vector.obj(px=row['px4'], py=row['py4'], pz=row['pz4'], E=row['E4'])
    pt1 = v1.pt
    pt2 = v2.pt
    pt3 = v3.pt
    pt4 = v4.pt
    lista = [pt1, pt2, pt3, pt4]
    max_pt = max(lista)   
    return max_pt
df['ptmax1'] = df.apply(ptmax1, axis=1)


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

# Aplique a função à coluna 'df' e armazene o resultado em uma nova coluna 'min_pt'
df['min_pt'] = df.apply(min_pt, axis=1)


part1=np.array(df['ptmax1'])

part2=np.array(df['second_max_pt'])

part3=np.array(df['third_max_pt'])

part4=np.array(df['min_pt'])



bins = 21
largura=2

plt.hist(part1, bins, range=(0, 150), histtype='step', color="blue", label='partícula 1',linewidth=largura)
plt.hist(part2, bins, range=(0, 150), histtype='step', color="green", label='partícula 2',linewidth=largura)
plt.hist(part3, bins, range=(0, 150), histtype='step', color="purple", label='partícula 3',linewidth=largura)
plt.hist(part4, bins, range=(0, 150), histtype='step', color="red", label='partícula 4',linewidth=largura)

fontsize=20

plt.legend(fontsize=14)
plt.xlabel(r'$P_T$ (GeV)',fontsize=fontsize)
plt.ylabel('Frequência',fontsize=fontsize)
plt.title(r'Distribuição de $p_T$',fontsize=fontsize)
