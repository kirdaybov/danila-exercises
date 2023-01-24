stock = 2000
stock_purchase_price = 40
share_sale_price = 42.75
# 0.03 - это не магическое число, а процент биржевому брокеру
purchase_commission = (stock * stock_purchase_price) * 0.03
sales_commission = (stock * share_sale_price) * 0.03
sum_stock_purchase_price = stock * stock_purchase_price
sum_share_sale_price = stock * share_sale_price
purchase_amount = sum_stock_purchase_price + purchase_commission
sale_amount = sum_share_sale_price + sales_commission
total_amount = purchase_amount - (sum_share_sale_price + sales_commission)
print('Это сколько Джо отдал за покупку акций -', sum_stock_purchase_price)
print('Это сколько составила комисия брокоре при покупке -', purchase_commission)
print('Это сколько всего Джо потратил на покупку -', purchase_amount )
print('Это сумма, за которую Джо продал акции -', sum_share_sale_price)
print('Это сумма комисси, при продаже - ', sales_commission)
print('Это оставшаяся сумма у Джо, после всех махинаций - ', total_amount)
if total_amount > 0:
    print ('Джо оказался в плюсе на: ', total_amount)
else:
    print('Джо понес убытки в размере: ', total_amount) 
