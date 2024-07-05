#RESTAURANT MANAGEMENT
class MenuItem:
    def __init__(mine,name,price):    #MINE IS REFERENCE/OBECT 
        mine.name=name 
        mine.price=price

# Defining Menu
class Menu:
    def __init__(mine):
        mine.items=[]
        
    def add_item(mine,item):
        mine.items.append(item)
        
    def display_menu(mine):
        print("\nsnacks")
        for i, item in enumerate(mine.items[0:17],1):
            print(f"{i}.{item.name} - Rs.{item.price:.2f}")
        print("\nmain course")
        for i, item in enumerate(mine.items[17:21],18):
            print(f"{i}.{item.name} - Rs.{item.price:.2f}")
        print("\nbeverages")
        for i, item in enumerate(mine.items[21:],22):
            print(f"{i}.{item.name} - Rs.{item.price:.2f}")

#Defining Order
class Order:
    def __init__(mine):
        mine.items = []

    def add_item(mine, item):
        mine.items.append(item)

    def calculate_total(mine):
        return sum(item.price for item in mine.items)
    def Payment(mine):
        print("\nPayment via: ")
        print("1. Cash")
        print("2. Card")
        print("3. UPI/Scanner\n")
        ch=int(input("Enter your choice for payment: "))
        if ch==1:
            print("Payment via Cash")
        elif ch==2:
            print("Payment via Card")
        else:
            print("Payment via UPI")

#Restaurant
class Restaurant:
    def __init__(mine):
        mine.Menu = Menu()
        
        mine.Order = Order()
    def display_options(mine):
        print("\nOptions:")
        print("1. Display Menu")
        print("2. Add Item to Order")
        print("3. View Order")
        print("4. Calculate Total")
        print("5. Payment")
        print("6. Exit\n")

    def run(mine):
        print("\nHeLlo")
        print("WeLCoMe To OuR REsTaUraNt\n")
        while True:
            mine.display_options()
            choice=input("enter your choice (1-5): ")
            if choice== '1':
                mine.Menu.display_menu()
            elif choice == '2':
                item_number = int(input("Enter the item number to add to the order: "))
                if 1 <= item_number <= len(mine.Menu.items):
                    selected_item = mine.Menu.items[item_number - 1]
                    mine.Order.add_item(selected_item)
                    print(f"{selected_item.name} added to the order.")
                else:
                    print("Invalid item number.")
            elif choice == '3':
                print("\nCurrent Order:")
                for item in mine.Order.items:
                    print(f"{item.name} - Rs.{item.price:.2f}")
            elif choice == '4':
                total = mine.Order.calculate_total()
                print(f"\nTotal Order Amount: Rs.{total:.2f}")
            elif choice == '5':
                print("\nHere is  Your Bill\n")
                for item in mine.Order.items:
                    print(f"{item.name} - Rs.{item.price:.2f}")
                mine.Order.Payment()
                total = mine.Order.calculate_total()
                print(f"Total Order Amount: Rs.{total:.2f}")
                print("\nThanks for Payment")
            elif choice == '6':
                print("\nThankYoU FoR VisiTIng OUr ReSTauRaNt")
                print("PleaSe Do ViSiT OuR ReSTAuraNt NeXT TimE")
                print("Exiting the restaurant management system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

#MAIN PROGRAM
if __name__== "__main__":
    restaurant=Restaurant()

    #Snacks
    menu_item1 = MenuItem("Veg Burger", 80)
    menu_item2 = MenuItem("cheese Veg Burger", 90)
    menu_item3 = MenuItem("French Fries", 50)
    menu_item4 = MenuItem("Samosa", 30)
    menu_item5 = MenuItem("kachoori", 30)
    menu_item6 = MenuItem("Vada Pav", 50)
    menu_item7 = MenuItem("Pav Bhaji", 50)
    menu_item8 = MenuItem("Masala Pav", 50)
    menu_item9 = MenuItem("Pani Puri", 30)
    menu_item10 = MenuItem("Dahi Puri", 50)
    menu_item11 = MenuItem("Sev Puri", 50)
    menu_item12 = MenuItem("Bhel", 30)
    menu_item13 = MenuItem("Pasta", 80)
    menu_item14 = MenuItem("Maggie", 60)
    menu_item15 = MenuItem("Bread Pakoda", 40)
    menu_item16 = MenuItem("Bread Pattis", 40)
    menu_item17 = MenuItem("Dahi Vada", 50)

    #Main Course
    menu_item18 = MenuItem("Dal & Rice", 80)
    menu_item19 = MenuItem("Chapatti & Bhaji", 70)
    menu_item20 = MenuItem("Mini thali(roti,bhaji,dal,rice,salad)", 150)
    menu_item21 = MenuItem("Full thali (roti/chapatti, bhaji-2,rice, dal tadka, raita,papad,salad)", 250)

    #Beverages
    menu_item22 = MenuItem("Butter milk", 40)
    menu_item23 = MenuItem("Hot coffee", 40)
    menu_item24 = MenuItem("Cold coffee", 40)
    menu_item25 = MenuItem("Thik Cold coffee", 60)
    menu_item26 = MenuItem("Special Cold coffee", 80)
    menu_item27 = MenuItem("Masala chai", 40)
    menu_item28 = MenuItem("Elaichi chai", 30)
    menu_item29 = MenuItem("Ginger chai", 30)
    menu_item30 = MenuItem("Chocolate chai", 40)
    menu_item31 = MenuItem("Juice(seasonal)", 30)
    menu_item32 = MenuItem("Juice(Pineapple)", 50)
    menu_item33 = MenuItem("Juice(watermelon)", 50)
    menu_item34 = MenuItem("Juice(sweet lime)", 40)
    menu_item35 = MenuItem("Juice(orange)", 40)
    menu_item36 = MenuItem("Juice(grapes)", 80)
    menu_item37 = MenuItem("Juice(kiwi)", 50)
    menu_item38 = MenuItem("Juice(strawberry)", 60)
    menu_item39 = MenuItem("Juice(lichi)", 40)
    menu_item40 = MenuItem("Juice(pomogranate)", 60)
    menu_item41 = MenuItem("Juice(apple)", 50)
    menu_item42 = MenuItem("Juice(mango)", 80)
    menu_item43 = MenuItem("Milk shake(chocolate)", 60)
    menu_item44= MenuItem("Milk shake(butter scotch)", 80)
    menu_item45 = MenuItem("Milk shake(orio)",80)
    menu_item46 = MenuItem("Milk shake(hazelnutt)",80)
    menu_item47 = MenuItem("Milk shake(caramell)",70)
    menu_item48 = MenuItem("Milk shake(vanilla)",50)
    menu_item49 = MenuItem("Milk shake(strawberry)",50)
    menu_item50 = MenuItem("Milk shake(banana)",50) 

    # Appending elements into list
    restaurant.Menu.add_item(menu_item1)
    restaurant.Menu.add_item(menu_item2)
    restaurant.Menu.add_item(menu_item3)
    restaurant.Menu.add_item(menu_item4)
    restaurant.Menu.add_item(menu_item5)
    restaurant.Menu.add_item(menu_item6)
    restaurant.Menu.add_item(menu_item7)
    restaurant.Menu.add_item(menu_item8)
    restaurant.Menu.add_item(menu_item9)
    restaurant.Menu.add_item(menu_item10)
    restaurant.Menu.add_item(menu_item11)
    restaurant.Menu.add_item(menu_item12)
    restaurant.Menu.add_item(menu_item13)
    restaurant.Menu.add_item(menu_item14)
    restaurant.Menu.add_item(menu_item15)
    restaurant.Menu.add_item(menu_item16)
    restaurant.Menu.add_item(menu_item17)

    restaurant.Menu.add_item(menu_item18)
    restaurant.Menu.add_item(menu_item19)
    restaurant.Menu.add_item(menu_item20)
    restaurant.Menu.add_item(menu_item21)
    
    restaurant.Menu.add_item(menu_item22)
    restaurant.Menu.add_item(menu_item23)
    restaurant.Menu.add_item(menu_item24)
    restaurant.Menu.add_item(menu_item25)
    restaurant.Menu.add_item(menu_item26)
    restaurant.Menu.add_item(menu_item27)
    restaurant.Menu.add_item(menu_item28)
    restaurant.Menu.add_item(menu_item29)
    restaurant.Menu.add_item(menu_item30)
    restaurant.Menu.add_item(menu_item31)
    restaurant.Menu.add_item(menu_item32)
    restaurant.Menu.add_item(menu_item33)
    restaurant.Menu.add_item(menu_item34)
    restaurant.Menu.add_item(menu_item35)
    restaurant.Menu.add_item(menu_item36)
    restaurant.Menu.add_item(menu_item37)
    restaurant.Menu.add_item(menu_item38)
    restaurant.Menu.add_item(menu_item39)
    restaurant.Menu.add_item(menu_item40)
    restaurant.Menu.add_item(menu_item41)
    restaurant.Menu.add_item(menu_item42)
    restaurant.Menu.add_item(menu_item43)
    restaurant.Menu.add_item(menu_item44)
    restaurant.Menu.add_item(menu_item45)
    restaurant.Menu.add_item(menu_item46)
    restaurant.Menu.add_item(menu_item47)
    restaurant.Menu.add_item(menu_item48)
    restaurant.Menu.add_item(menu_item49)
    restaurant.Menu.add_item(menu_item50)

    #Running Program
    restaurant.run()   
