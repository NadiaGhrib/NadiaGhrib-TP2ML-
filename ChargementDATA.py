import pandas as pd
import numpy as np


#Produit
#Lecture des données + on garde les données qui nous interesse

produit = pd.read_csv("/Users/nadiaghrib/Desktop/git/Data/products.csv")

#print(produit.columns)

df_produit = produit[["department_id", "product_id"]]

#print(df_produit)



#Commande : pour chaque client on a juste besoint du panier (order_id)
#Lecture des données

df_commande = pd.read_csv("/Users/nadiaghrib/Desktop/git/Data/orders.csv")

#On garde que les deux variables qui nous interesse
df_commande = df_commande [["order_id", "user_id"]]

N=100  #On commence à tester pour 100 clients

def commande(n_clients):
   return df_commande[df_commande['user_id'].isin(range(N+1))]

commande_df = commande(N)


#Order products prior
#Lecture des données + on garde les données qui nous interesse

commande_produit = pd.read_csv("/Users/nadiaghrib/Desktop/git/Data/order_products__prior.csv")

#print(commande_produit .columns)

df_commande_produit =commande_produit [['order_id', 'product_id']]

#print(df_commande_produit)






