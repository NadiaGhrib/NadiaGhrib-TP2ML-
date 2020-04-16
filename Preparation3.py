from ChargementDATA import *
from Preparation1 import *

#On va chercher à faire un groupe par client avec le nouveau Data Set :
for order in Data.groupby("user_id"):
    print(order)

#Pour chaque ligne on a le nméros du client (user_id), le panier (order id) et la catégorie (department_id) :

for user in Data.groupby("user_id"):
    user_id = user[0]
    user_data = user[1]
    for order in user_data.groupby("order_id"):
        order_id = order[0]
        order_data = order[1]
        departement_ids = list(order_data["department_id"])
        print(user_id,order_id,departement_ids)