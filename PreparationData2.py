from ChargementDATA import *
from Preparation1 import *
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

def Data_final ():

    L=[]

    for user in Data.groupby ("user_id") :
        user_id = user [0]
        user_data = user [1]
        seq_user=[]
        for order in user_data.groupby("order_id"):
            order_id = order[0]
            order_data = order[1]
            departement_ids = list(order_data["department_id"])
            seq_user.append(departement_ids)
        L.append(seq_user)

    return L

L= final(Data)
X1=np.zeros((100,3,5)) #100 = le nombre de client ; 4 = le nombre de panier ; 5 = le nombre d'achat /catégories

#On va prendre les 5 premier achats par client (maxlen)
#Timestep - On commence avec 3 panier par client


for i in range(len(L)):
  panier =pad_sequences(L[i], maxlen=5, dtype="int32", padding="post", truncating='pre', value=0.0)
  panier = panier [:3]
  X1[i]=panier

#print(panier)
#print(X1)

X = X1[:,:-1,:] # Tous les achats sauf le dernier
Y = X1[:,-1,:] #Le dernier achat

#print(X)
#print(Y)

#On split nos données

x_train, x_test, y_train, y_test = train_test_split(X, Y)