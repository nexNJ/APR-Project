thai_baht = float(input())
currency_type = str(input())
usd = 34.20
eur = 38.47
gbp = 44.73
hundren_jpy = 24.76

if currency_type == "USD":
    amount_in_thai = thai_baht // usd
    print(round(amount_in_thai))
    print(round(thai_baht % usd,2))

elif currency_type == "EUR":
    amount_in_thai = thai_baht // eur
    print(round(amount_in_thai))
    print(round(thai_baht % eur,2))
    
elif currency_type == "GBP":
    amount_in_thai = thai_baht // gbp
    print(round(amount_in_thai))
    print(round(thai_baht % gbp,2))

elif currency_type == "JPY":
    amount_in_thai = thai_baht // (hundren_jpy/100)
    print(round(amount_in_thai))
    print(round(thai_baht % (hundren_jpy/100),2))