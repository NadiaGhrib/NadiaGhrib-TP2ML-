from ChargementDATA import *

#On va chercher à faire un groupe par client :
#for order in commande_df.groupby("user_id"):
    #print(order)

#On va créer un seul data set
#Pour cela on va joindre les trois qui sont dans ChargementDATA

jointure1 = pd.merge (commande_df, df_commande_produit, on="order_id")
jointure2 = pd.merge (jointure1, df_produit, on="product_id")

#on a un Data set avec : le client (user_id) , le panier (order_id) , le product_id et la catégorie (department_id)
Data = jointure2
#print(Data)



#On met le Data avec les variables qui nous interesse dans un csv
Data.to_csv("/Users/nadiaghrib/Desktop/git/Data/data.csv")

