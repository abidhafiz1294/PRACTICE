from mobile_tech import  Mobile
from laptop_tech import Laptop
from tech_product import  Tech
from sales_person import SalesPerson
from  datetime import date

phone_1= Mobile('iphone_11', 60000,500, 'Black', '1920-1080',10)
phone_2= Mobile('iphone_12', 60000,500, 'Black', '1920-1080',11)
phone_3= Mobile('iphone_13', 60000,500, 'Black', '1920-1080',12)

laptop_1= Laptop('Asus', 60000, 700, 'Black', 4, 'core i7', 256)
laptop_2= Laptop('leanvo', 60000, 700, 'Black', 4, 'core i7', 256)
laptop_3= Laptop('Acer', 60000, 700, 'Black', 4, 'core i7', 256)




#Test Methods
print(laptop_1)
print(phone_1)

#Applying the discount upon the product
phone_1.apply_discount()
print(f'With apply discount:{phone_1.price}')

#Total Number of products
print(Tech.get_total_products())

#shipping Cost
print(laptop_3.calculate_shipping_cost(10))

#Setting the double price for the 1st laptop
print(laptop_3)
laptop_3.change_speces(32, 1000)
print(laptop_3)

sales_person_1 = SalesPerson(
    'Majed',
    'Ali',
    40000,
    date(2020, 1, 5)
)

#adding the products
sales_person_1.sell_product(phone_1)
sales_person_1.sell_product(phone_2)
sales_person_1.sell_product(laptop_1)
sales_person_1.sell_product(laptop_2)

#total products sold
print(sales_person_1.total_products_sold())

#Products sold
sales_person_1.display_sales()

#Calculate Commission
print(sales_person_1.calculate_commission(0.2))

#sort the sold products by price
sales_person_1.sort_by_price()
sales_person_1.display_sales()



