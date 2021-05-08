import pandas as pd
import os

years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020']

for year in years:
    # przejście do folderu z danymi
    os.chdir(r"D:\data-visualisation\data")

    # wczytanie danych z pliku excel
    df = "df_{}".format(year)
    df = pd.read_excel("Pojazdy_wg_województw_{}.xlsx".format(year))

    # usunięcie kolumny z oznaczeniem terytorium:
    df.drop('TERYT', axis=1, inplace=True)

    # tworzenie nowej kolumny z roczną ilością rejestracji:
    df['{}'.format(year)] = df.sum(axis=1)

    # tworzenie kopii tabeli z danymi do wykresu:
    df_final = "df_final_{}".format(year)
    df_final = df[['WOJEWÓDZTWO', '{}'.format(year)]].copy()

    # zapisywanie pliku do pliku csv
    df_final.to_csv('pojazdy_wg_woj_{}.csv'.format(year))

merged_df = pd.concat([pd.read_csv(filename) for filename in os.listdir("D:\data-visualisation\data") if filename.endswith(".csv")])

merged_df.to_csv('clean.csv')
