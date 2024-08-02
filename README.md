# Delicious-Kitchen-System
Delicious Kitchen System is a food ordering website build using Django Framework.

## How to use the website?
1. User registration and login:
To create an account click on register. Fill in the details and  create and accoun. Then navigate back to login page and login using the email id and the password that has been created while registering.

2. Home Page:
The home page consists of the menu, search bar, and the navbar containing few options like view profile, contact us and logout.
In order to add the item into cart, click on Add button given on the right side of each item, after that confirm the quantity and proceed with viewing cart or checkout.

3. Cart:
On cart page the items can be seen that has been added by the user, they can proceed to checkout or make payment or they can delete the item.

4. Make Payment:
To make a payment user need to fill in the details like name address and pincode. The payment can be proceeded only if the entered pin is valid and comes within the range set by the admin.
With the help of "razorpay" API the payment module has been created. After successful payment the user will be directed to the succesfull payment page, from there user can navigate to order details or to the menu page.

5. Admin Page:
To access the admin page, first create django superuser using the following command:
    "python manage.py createsuperuser"
After creating the superuser account go back to login page and login with the credentials that  have been created. On admin page we have dashboars containing pending orders,orders in line and many options on the sidebar like manage orders, pending orders, completed orders.
The admin manages the order for the user by updating the delivery progress like order received, order prepared, order out for delivery and order delivered.
