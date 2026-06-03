import pandas as pd


data = pd.read_csv('orders.csv')

# aggregate functions: sum avg, mean 
delivery = data["total_amount"].agg(["mean"])


print(delivery)

# mean: avg of the data
# median: middle value
# mode: kon si 



# Appcount = 0
# MobileWeb = 0
# Website = 0

# for i in data["channel"]:
#     if i == "App":
#         Appcount = Appcount+1
#     if i=="Mobile Web":
#         MobileWeb +=1
#     if i=="Website":
#         Website += 1



# print(Appcount)
# print(MobileWeb)
# print(Website)

# print(Appcount+MobileWeb+Website)



# learning github

git add .
git commit -m "adding comment"
git push -u origin main
