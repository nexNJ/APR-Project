Fare_table =['phaya thai','ratchaprarop','makkasan','ramkhamhaeng','hua mak','ban thap chang','lat krabang','suvarnabhumi']
origin = input().lower()
destination = input().lower()
distance_abs = abs(Fare_table.index(origin) - Fare_table.index(destination))
cost = 0
for i in range(1,distance_abs+1,1):
    print(i)
    if i == 1:
        cost +=15
    else:
        cost +=5
