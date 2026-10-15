product_list=['tomato','brinjal','cabbage','milk','bread','cheese']
cart_list=[]
user_list=[]
order_list=[]
user_carts={}
while True:
 ch=input('enter 1.admin 2.user 3.exit\n')
 if ch=='1':
    menu=('enter your choice:\n'
                '1.Add product \n'
                '2.Update product \n'
                '3.remove product \n'
                '4.view products \n'
                '5.view users \n'
                '6.exit \n')
    while True:
        admin=input(menu)
        if admin=='1':
           item=input('enter product')
           product_list.append(item)
           print('new product added to the list')
           print(product_list)
        elif admin=='2':
           for i in range (len(product_list)):
             print(product_list[i],i)
           upd=int(input('which product do you want to update/enter the number beside the product'))
           new_pro=input('enter the new product name')
           if upd>=0 and upd<len(product_list):
              product_list[old_pro]=new_pro
              print('new product added succesfully')
              print(product_list)
           else:
               print('Ivalid product number')
        elif admin=='3':
           for i in range (len(product_list)):
             print(product_list[i],i)
           rm=int(input('enter the product number which you want to remove'))
           if rm>=0 and rm<len(product_list):
              product_list.pop(rm)
              print('Removed successfully')
              print(product_list)
           else:
               print('invalid product number')
        elif admin=='4':
           if product_list==[]:
                print('empty!no products are there in the shop')
           else:
                print(product_list)
        elif admin=='5':
            if user_list==[]:
                print('no users are registered')
            else:
                print(user_list)
        elif admin=='6':
            print('exit sucessful')
            break
        else:
            print('Invalid Choice,choose correct option')
 elif ch=='2':
      reg=input('if you registered or not:1 registerd \n 2 Not registerd ')
      if reg=='1':
        name=input('enter your registerd name')
        if name in user_list:
          print('login successful')
          cart_list=user_carts[name]
          while True:
           menu=('1.view product\n 2.Add to cart\n 3.remove from cart\n 4.view cart\n 5.checkout\n 6.exit\n')
           user=input(menu)
           if user=='1':
             print(product_list)
           elif user=='2':
             if name in user_list:
                 if name not in user_carts:
                     user_carts[name]=[]
                 cart_list=user_carts[name]
             for i in range (len(product_list)):
              print(product_list[i],i)
             cart=int(input('enter the product number you want to buy'))
             if cart>=0 and cart<len(product_list):
                cart_list.append(product_list[cart])
                print('your item is added to cart')
             else:
                 print('invalid product number')
           elif user=='3':
             for i in range (len(cart_list)):
              print(cart_list[i],i)
             rem=int(input('enter the product number you want to remove'))
             if rem>=0 and rem<len(cart_list):
                 cart_list.pop(rem)
                 print('item is removed')
             else:
                print('invalid product number')
           elif user=='4':
             if cart_list==[]:
                 print('your cart is empty')
             else:
                 print(cart_list)
           elif user=='5':
             if cart_list==[]:
                 print('cannot checkout ! your cart is empty')
             else:
                 print('your cart items:',cart_list)
                 cnf=input('do you want to confirm 1.yes/2.no')
                 if cnf=='1':
                     for item in cart_list:
                      order_list.append(item)
                     print('order placed successfully')
                     cart_list.clear()
                 else:
                     print('order cancelled')
           elif user=='6':
             print('exit')
             break
        else:
             print('your not registerd')
             continue
      elif reg=='2':
           name=input('enter your name')
           if name not in user_list:
             user_list.append(name)
             user_carts[name]=[]
             print('you are registerd successfully')
      else:
           print('invalid choice')
         
 elif ch=='3':
     print('exit sucessfull')
     break
 else:
    print('Invalid choice/choose 1 ,2 ,3')
    
