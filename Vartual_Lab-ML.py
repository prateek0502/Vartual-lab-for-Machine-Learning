import tkinter as tk
from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


def open():

    # Changing csv_filename to top.csv_filename
    top.csv_filename = filedialog.askopenfilename(initialdir="machine learning", title="select a train data file",
                                              filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

    # Setting the value in text field
    df_train.set(top.csv_filename)
    # my_label = Label(top,text=csv_filename)

    df = pd.read_csv(top.csv_filename)
    row_count, column_count = df.shape
    # print(row_count)
    # print(column_count)
    total_rows="Total rows - "+str(row_count)
    total_columns = "Total columns - " + str(column_count)
    e3.insert(0, total_rows)
    e3.bind("<FocusIn>", clear_placeholder_e3)
    e5.insert(0, total_columns)
    e5.bind("<FocusIn>", clear_placeholder_e5)

def clear_placeholder_e3(event):
    e3.delete(0, tk.END)

def clear_placeholder_e5(event):
    e5.delete(0, tk.END)


def clear_all():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)
    e6.delete(0, tk.END)


def cluster():

    # Reading input file
    df = pd.read_csv(top.csv_filename)
    s_rows = int(a.get())
    e_rows = int(b.get())
    s_columns = int(c.get())
    e_columns = int(d.get())
    #print(columns)
    X = df.iloc[s_rows:e_rows,s_columns:e_columns]
    #[[rows, columns]]
    print(X)

    wcss = []
    for i in range(1, 12):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 12), wcss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()


def cluster_1():
    df = pd.read_csv(top.csv_filename)
    s_rows = int(a.get())
    e_rows = int(b.get())
    s_columns = int(c.get())
    e_columns = int(d.get())
    # print(columns)
    X = df.iloc[:, [s_columns,e_columns]].values
   # X = df.iloc[a, b].values

    # Applying KMeans to the dataset with the optimal number of cluster
    clusters = int(n.get())
    kmeans = KMeans(n_clusters=clusters, init='k-means++', max_iter=300, n_init=10, random_state=42)
    y_Kmeans = kmeans.fit_predict(X)

    # Visualising the clusters

    plt.scatter(X[y_Kmeans == 0, 0], X[y_Kmeans == 0, 1], s=100, c='red', label='Cluster 1')

    plt.scatter(X[y_Kmeans == 1, 0], X[y_Kmeans == 1, 1], s=100, c='blue', label='Cluster 2')

    plt.scatter(X[y_Kmeans == 2, 0], X[y_Kmeans == 2, 1], s=100, c='green', label='Cluster 3')

    plt.scatter(X[y_Kmeans == 3, 0], X[y_Kmeans == 3, 1], s=100, c='cyan', label='Cluster 4')

    plt.scatter(X[y_Kmeans == 4, 0], X[y_Kmeans == 4, 1], s=100, c='magenta', label='Cluster 5')

    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')

    plt.title('Clusters of clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending score (1-100)')
    plt.legend()
    plt.show()


top = tk.Tk()
top.title("GUI : k-means clustering")
Tops = Frame(top, bg='#000', pady=2, width=2000, height=100, relief="ridge")
Tops.grid(row=0, column=0)
df_train = StringVar()
a = StringVar()
b = StringVar()
c = StringVar()
d = StringVar()
n = IntVar()

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text=' k-means clustering ', bg='#663300', fg='white')
headlabel.grid(row=1, column=0, sticky=W)
La = Label(top, font=('lato black', 27, 'bold'), text='', padx=2, pady=2, bg="#e6e5e5", fg="black")
La.grid(row=1, column=0, sticky=W)

my_btn = Button(top, font=('arial', 10, 'bold'), text="open file", padx=2, pady=2, bg="Blue", fg="white", command=open)
my_btn.grid(row=6, column=10)
Label(top, font=('lato black', 15, 'bold'), text='Starting index for rows :', bg="#e6e5e5", fg="black").grid(row=8)
Label(top, font=('lato black', 15, 'bold'), text='Ending index for rows :', bg="#e6e5e5", fg="black").grid(row=10)
Label(top, font=('lato black', 15, 'bold'), text='Train data :', bg="#e6e5e5", fg="black").grid(row=6)
Label(top, font=('lato black', 15, 'bold'), text='Starting index for columns :', bg="#e6e5e5", fg="black").grid(row=12)
Label(top, font=('lato black', 15, 'bold'), text='Ending index for columns :', bg="#e6e5e5", fg="black").grid(row=14)
e1 = Entry(top, font=('arial', 10, 'bold'), textvariable=df_train)
e2 = Entry(top, font=('arial', 10, 'bold'), textvariable=a)
e3 = Entry(top, font=('arial', 10, 'bold'), textvariable=b)
e4 = Entry(top, font=('arial', 10, 'bold'), textvariable=c)
e5 = Entry(top, font=('arial', 10, 'bold'), textvariable=d)
e1.grid(row=6, column=7)
e2.grid(row=8, column=7)
e3.grid(row=10, column=7)
e4.grid(row=12, column=7)
e5.grid(row=14, column=7)
# open()  

bt = Button(top, font=('arial', 15, 'bold'), text=" process1 ", padx=2, pady=2, bg="green", fg="white", command=cluster)
bt.grid(row=16, column=7)
Label(top, font=('lato black', 15, 'bold'), text='n :', bg="#e6e5e5", fg="black").grid(row=18)
e6 = Entry(top, font=('arial', 10, 'bold'), textvariable=n)
e6.grid(row=18, column=7)
bt1 = Button(top, font=('arial', 15, 'bold'), text=" process2 ", padx=2, pady=2, bg="green", fg="white",
             command=cluster_1)
bt1.grid(row=20, column=7)
bt2 = Button(top, font=('arial', 15, 'bold'), text=" Clear All ", padx=2, pady=2, bg="white", fg="red",
             command=clear_all)
bt2.grid(row=22, column=7)
top.mainloop()
