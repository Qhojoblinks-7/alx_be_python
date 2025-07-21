# Identifying auth user

logged_in = True  # Try changing this to False later
is_admin = False  # Try changing this to True later

if logged_in and is_admin:
    print("Show Admin Panel Link")
else:
    print("Access Denied")


is_admin = False
is_premium_subscriber = False

if is_admin == True or is_premium_subscriber == True:
    print("Access granted")
else:
    print("Access Denied")


for num in range(1,6):
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")