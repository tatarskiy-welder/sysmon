import matplotlib.pyplot as plt
import pandas as pd
import csv
import os

def create_plot(name, number_of_client, first_try):
    append = str(number_of_client) + ".csv"

    if first_try and os.path.isfile(append):
        os.remove(append)

    with open(name,'r') as new_file:
        csv_reader=csv.reader(new_file)
        with open(append,'a', newline='') as csv_file:
            csv_writer=csv.writer(csv_file)
            if not first_try:
                next(csv_reader)
            for line in csv_reader:
                csv_writer.writerow(line) 
    if not first_try:
        plt.style.use('ggplot')  # Красивые графики
        plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок
        fixed_df = pd.read_csv(append,  # Это то, куда вы скачали файл
                                sep=',')
        print(fixed_df)

        fixed_df['mem_load'].plot()
        plt.show()

    

