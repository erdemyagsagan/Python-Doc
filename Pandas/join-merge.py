import pandas as pd

customers = {
    'CustomerID' : [3,4,5,6],
    'Name' : ['Ahmet','Kemal','Adil','Asli'],
    'Surname' : ['Aslan','Tam','Peker','Yildirim']
}
orders = {
    'OrderID' : [11,22,32,43],
    'CustomerID' : [3,4,5,6],
    'Date' : ['2023','2022','2021','2020']
}

df_customers = pd.DataFrame(customers, columns = ['CustomerID','Name','Surname'])
df_orders = pd.DataFrame(orders, columns = ['OrderID','CustomerID','Date'])

# print(df_customers)
# print(df_orders)

result = pd.merge(df_customers,df_orders,how='inner')
# result = pd.merge(df_customers,df_orders,how='left')
result = pd.merge(df_customers,df_orders,how='right')

print(result)