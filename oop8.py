# class User:
#     _user_count = 0
#     _users_list = []
#     def __init__(self, username, email, password_hash):
#         self.username = username
#         self.email = email
#         self._password_hash = User.hash_password(password_hash)
#
#         User._user_count += 1
#         User._users_list.append(self)
#
#     @staticmethod
#     def hash_password(password_hash):
#         return str(hash(password_hash))
#
#     @staticmethod
#     def is_valid_email(email):
#         if "@" in email:
#             parts = email.split("@")
#             if "." in parts[1]:
#                 return True
#             else:
#                 return False
#
#     @staticmethod
#     def validate_password(password):
#         if len(password) < 8:
#             return False
#         has_upper = False
#         has_lower = False
#         has_digit = False
#
#         for char in password:
#             if char.isupper():
#                 has_upper = True
#             elif char.islower():
#                 has_lower = True
#             elif char.isdigit():
#                 has_digit = True
#
#         if has_upper and has_lower and has_digit:
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def create_user_safely(username, email, password):
#         if User.is_valid_email(email) and User.validate_password(password):
#             new_user = User(username, email, password)
#             print("המשתמש נוצר בהצלחה")
#             return new_user
#         else:
#             print("שגיאה בנתונים")
#             return None
#
#     @classmethod
#     def get_user_count(cls):
#         return cls._user_count
#
#     @classmethod
#     def find_user_by_username(cls, username):
#         for user in cls._users_list:
#             if user.username == username:
#                 return user
#         return None
#
#
# user1 = User.create_user_safely("moshe123", "moshe@gmail", "123")
# user2 = User.create_user_safely("yossi", "yossi@gmail.com", "Abc12345")
# user3 = User.create_user_safely("arav", "dana@yahoo.com", "Secret99")
#
# print(f"Total users: {User.get_user_count()}")
#
# found_user = User.find_user_by_username("dana_smart")
# if found_user:
#     print(f"Found: {found_user.email}")
# else:
#     print("Not found")
#
# ghost_user = User.find_user_by_username("david")
# if ghost_user:
#     print("Found")
# else:
#     print("Not found")




# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         if value > 0:
#             self.__width = value
#         else:
#             print("שגיאה")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, value):
#         if value > 0:
#             self.__height = value
#         else:
#             print("שגיאה")
#
#     @property
#     def area(self):
#         return self.__width * self.__height
#
#     @property
#     def perimeter(self):
#         return 2 * (self.__width + self.__height)
#
#     @property
#     def is_square(self):
#         if self.__width == self.__height:
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def create_square(side):
#         return Rectangle(side, side)
#
#     @staticmethod
#     def compare_areas(rect1, rect2):
#         if rect1.area > rect2.area:
#             return "המלבן הראשון גדול יותר"
#         elif rect2.area > rect1.area:
#             return "המלבן השני גדול יותר"
#         else:
#             return "השטחים של שני המלבנים שווים"
#
# r1 = Rectangle(5, 4)
# r2 = Rectangle(3, 3)
#
# print(f"Rectangle 1 - Area: {r1.area}, Perimeter: {r1.perimeter}, Is Square: {r1.is_square}")
# print(f"Rectangle 2 - Area: {r2.area}, Perimeter: {r2.perimeter}, Is Square: {r2.is_square}")
#
# r1.width = 6
# r1.height = 6
# print(f"After change - Area: {r1.area}, Perimeter: {r1.perimeter}, Is Square: {r1.is_square}")
#
# square = Rectangle.create_square(5)
# print(f"Created Square - Area: {square.area}, Is Square: {square.is_square}")
#
# comparison = Rectangle.compare_areas(r1, square)
# print(comparison)


class Product:
    TAX_RATES = {
        "food": 0.0,
        "books": 0.0,
        "electronics": 0.17,
        "clothing": 0.17,
        "other": 0.17
    }
    def __init__(self, name, base_price, category = "other", discount_percent = 0):
        self.__name = name
        self.__base_price = base_price
        self.__category = category
        self.__discount_percent = discount_percent

    @property
    def name(self):
        return self.__name

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, value):
        if value >= 0:
            self.__base_price = value
        else:
            print("שגיאה: המחער אינו יכול להית שלילי")

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if value in Product.TAX_RATES:
            self.__category = value
        else:
            print("שגיאה: קטגוריה לא חוקית")

    @property
    def discount_percent(self):
        return self.__discount_percent

    @discount_percent.setter
    def discount_percent(self, value):
        if 0 <= value <= 100:
            self.__discount_percent = value
        else:
            print("שגיאה: אחוז הנחה חייב להיות בין 0 ל-100")

    @property
    def price_after_discount(self):
        return self.__base_price * (1 - self.__discount_percent / 100)

    @property
    def tax_amount(self):
        # 1. שולפים את אחוז המס המתאים לקטגוריה של המוצר מהמילון
        tax_rate = Product.TAX_RATES[self.__category]
        # 2. מכפילים אותו במחיר של המוצר אחרי הנחה (משתמשים ב-property שכתבנו שורה מעל!)
        return self.price_after_discount * tax_rate

    @property
    def final_price(self):
        return self.price_after_discount + self.tax_amount

    @staticmethod
    def get_tax_rate(category):
        if category in Product.TAX_RATES:
            return Product.TAX_RATES[category]
        else:
            return Product.TAX_RATES["other"]

    @staticmethod
    def calculate_bulk_discount(quantity, unit_price):
        if quantity >= 100:
            discount_rate = 0.15
        elif quantity >= 50:
            discount_rate = 0.10
        elif quantity >= 10:
            discount_rate = 0.05
        else:
            discount_rate = 0.0

        total_before_discount = quantity * unit_price
        return total_before_discount * discount_rate

p1 = Product("Laptop", 3000, "electronics")
p2 = Product("Bread", 10, "food", 10)
p3 = Product("Shirt", 100, "clothing")

print(f"Product 1 - Name: {p1.name}, Base Price: {p1.base_price}, Category: {p1.category}")
print(f"Product 1 Final Price: {p1.final_price}")
print(f"Product 2 Final Price: {p2.final_price}")

p3.discount_percent = 20
p3.base_price = 80
print(f"Product 3 Updated - Base Price: {p3.base_price}, Discount: {p3.discount_percent}%, Final Price: {p3.final_price}")

p3.category = "invalid_category"
p3.base_price = -50
p3.discount_percent = 150

print(f"Tax rate for books: {Product.get_tax_rate('books')}")
print(f"Tax rate for unknown: {Product.get_tax_rate('toys')}")

bulk_discount = Product.calculate_bulk_discount(60, 100)
print(f"Bulk discount for 60 units of 100 NIS: {bulk_discount} NIS")
