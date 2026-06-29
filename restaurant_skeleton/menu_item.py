# menu_item.py - מחלקת פריט תפריט ותתי-מחלקות


class MenuItem:
    """
    מחלקת בסיס לפריט בתפריט.
    
    שדות:
        _name (str): שם המנה (פרטי)
        _price (float): מחיר המנה (פרטי)
        _description (str): תיאור קצר (פרטי)
    """
    
    def __init__(self, name: str, price: float, description: str = ""):
        self._name = name
        self.price = price
        self._description = description



        """
        אתחול פריט תפריט.
        
        דרישות:
        - לשמור את name ב-_name
        - לשמור את description ב-_description  
        - להשתמש ב-setter של price (לצורך ולידציה)
        
        Args:
            name: שם הפריט
            price: מחיר (חייב להיות אי-שלילי)
            description: תיאור (ברירת מחדל: מחרוזת ריקה)
        """

    # --- Properties ---
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price
        """מחזיר את מחיר הפריט"""

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value

        """
        קובע את מחיר הפריט.
        
        דרישות:
        - אם המחיר שלילי, להעלות ValueError עם הודעה "Price cannot be negative"
        - אחרת, לשמור את הערך ב-_price
        """

    
    @property
    def description(self) -> str:
        return self._description
        """מחזיר את תיאור הפריט"""
    
    @description.setter
    def description(self, value: str):
        self._description = value
        """קובע את תיאור הפריט"""

    
    # --- Methods ---
    
    def get_category(self) -> str:
        return "General"
        """
        מחזיר את קטגוריית הפריט.
        
        דרישות:
        - במחלקת הבסיס, להחזיר "General"
        - בתתי-מחלקות, לדרוס ולהחזיר קטגוריה מתאימה
        
        Returns:
            שם הקטגוריה כמחרוזת
        """

    @staticmethod
    def format_price(price: float) -> str:
        return f"${price:.2f}"
        """
        מחזיר מחיר מפורמט עם סימן $.
        
        דרישות:
        - להחזיר מחרוזת בפורמט "$XX.XX" (שתי ספרות אחרי הנקודה)
        
        Args:
            price: המחיר לפרמוט
            
        Returns:
            מחרוזת מפורמטת, לדוגמה: "$32.00"
        """

    # --- Magic Methods ---
    
    def __str__(self) -> str:
        return f"{self._name} - {MenuItem.format_price(self.price)}"
        """
        מחזיר ייצוג מחרוזת ידידותי.
        
        דרישות:
        - להחזיר: "name - $price"
        - להשתמש ב-format_price
        
        Returns:
            לדוגמה: "Hummus - $32.00"
        """

    def __repr__(self) -> str:
        return f"MenuItem(name='{self._name}', price={self._price}, description='{self._description}')"
        """
        מחזיר ייצוג טכני.
        
        Returns:
            לדוגמה: "MenuItem(name='Hummus', price=32.0, description='desc')"
        """

    def __eq__(self, other) -> bool:
        if isinstance(other , MenuItem):
            return self._name == other._name
        return False
        """
        השוואה בין פריטים לפי שם.
        
        דרישות:
        - אם other הוא MenuItem, להשוות לפי name
        - אחרת, להחזיר False
        """


class Appetizer(MenuItem):

    """
    מנה ראשונה - עם אפשרות להוסיף לחם.
    
    שדות מחלקה:
        _bread_inventory (dict): מילון {סוג_לחם: כמות} - משותף לכל המופעים
        BREAD_PRICE (float): מחיר תוספת לחם (קבוע: 5.0)
    
    שדות מופע:
        _selected_bread (str או None): סוג הלחם שנבחר
    """
    
    # משתני מחלקה
    _bread_inventory: dict = {}
    BREAD_PRICE: float = 5.0
    
    def __init__(self, name: str, price: float, description: str = ""):
        super().__init__(name, price , description)
        self._selected_bread = None


        """
        אתחול מנה ראשונה.
        
        דרישות:
        - לקרוא ל-__init__ של מחלקת האב
        - לאתחל _selected_bread ל-None
        """

    # --- Properties ---
    
    @property
    def selected_bread(self) -> str:
        return self._selected_bread
        """מחזיר את סוג הלחם שנבחר (או None)"""

    # --- Instance Methods ---
    
    def add_bread(self, bread_type: str) -> bool:
        if bread_type in Appetizer._bread_inventory and Appetizer._bread_inventory[bread_type] > 0:
            self._selected_bread = bread_type
            Appetizer._bread_inventory[bread_type] -= 1
            return True
        return False
        """
        בחירת סוג לחם מהמלאי.
        
        דרישות:
        - לבדוק שסוג הלחם קיים במלאי וכמותו > 0
        - אם כן: לעדכן _selected_bread, להוריד 1 מהמלאי, להחזיר True
        - אם לא: להחזיר False
        
        Args:
            bread_type: סוג הלחם המבוקש
            
        Returns:
            True אם הצליח, False אחרת
        """

    def remove_bread(self):
        if self._selected_bread is not None:
            Appetizer._bread_inventory[self._selected_bread] += 1
            self._selected_bread = None
        """
        ביטול בחירת לחם.
        
        דרישות:
        - אם יש לחם נבחר: להחזיר 1 למלאי ולאפס את _selected_bread
        """

    def get_total_price(self) -> float:
        if self._selected_bread is not None:
            return self._price + Appetizer.BREAD_PRICE
        return self._price
        """
        מחזיר מחיר כולל לחם.
        
        Returns:
            מחיר + BREAD_PRICE אם נבחר לחם, אחרת רק המחיר
        """

    def get_category(self)-> str:
        return "Appetizer"

        """מחזיר 'Appetizers'"""

    # --- Class Methods ---
    
    @classmethod
    def get_available_breads(cls) -> list:
        return [bread for bread, count in cls._bread_inventory.items() if count > 0]
        """
        מחזיר רשימת סוגי לחמים זמינים.
        
        Returns:
            רשימה של סוגי לחם שהכמות שלהם > 0
        """
        raise NotImplementedError("Implement this method")
    
    @classmethod
    def add_bread_to_inventory(cls, bread_type: str, quantity: int):
        if bread_type in cls._bread_inventory:
            cls._bread_inventory[bread_type] += quantity
        else:
            cls._bread_inventory[bread_type] = quantity
        """
        הוספת לחמים למלאי.
        
        דרישות:
        - אם סוג הלחם קיים: להוסיף לכמות הקיימת
        - אם לא קיים: להוסיף מפתח חדש עם הכמות
        
        Args:
            bread_type: סוג הלחם
            quantity: כמות להוספה
        """

    @classmethod
    def remove_bread_from_inventory(cls, bread_type: str, quantity: int) -> bool:
        """
        הורדת לחמים מהמלאי.

        דרישות:
        - לבדוק שיש מספיק במלאי
        - אם כן: להוריד ולהחזיר True
        - אם לא: להחזיר False
        """
        # בודקים קודם שהלחם קיים, ואז שהכמות שלו גדולה או שווה לכמות המבוקשת
        if bread_type in cls._bread_inventory and cls._bread_inventory[bread_type] >= quantity:
            cls._bread_inventory[bread_type] -= quantity
            return True
        return False

    @classmethod
    def get_bread_quantity(cls, bread_type: str) -> int:
        if bread_type in cls._bread_inventory and cls._bread_inventory[bread_type] > 0:
            return cls._bread_inventory[bread_type]
        return 0
        """
        מחזיר כמות מסוג לחם מסוים.
        
        Returns:
            הכמות במלאי, או 0 אם לא קיים
        """
        raise NotImplementedError("Implement this method")
    
    @classmethod
    def get_bread_inventory(cls) -> dict:
        return cls._bread_inventory.copy()

        """מחזיר עותק של מילון המלאי"""
    # --- Magic Methods ---
    
    def __str__(self) -> str:
        return f"{self._name} - ${self._price} (with bread_type +{Appetizer.BREAD_PRICE})"
        """
        ייצוג מחרוזת כולל פרטי לחם.
        
        Returns:
            "name - $price" או "name - $price (with bread_type +$5.00)"
        """


class MainCourse(MenuItem):
    """
    מנה עיקרית - עם בחירת תוספת.
    
    שדות מחלקה:
        _side_options (list): רשימת תוספות אפשריות
    
    שדות מופע:
        _selected_side (str או None): התוספת שנבחרה
    """

    _side_options: list = []
    
    def __init__(self, name: str, price: float, description: str = ""):
        super().__init__(name, price, description)
        self._selected_side = None



        """
        אתחול מנה עיקרית.
        
        דרישות:
        - לקרוא ל-__init__ של מחלקת האב
        - לאתחל _selected_side ל-None
        """

    @property
    def selected_side(self) -> str:
        return self._selected_side
        """מחזיר את התוספת שנבחרה (או None)"""

    def select_side(self, side: str) -> bool:
        if side in MainCourse._side_options:
            self._selected_side = side
            return True
        return False

        """
        בחירת תוספת.
        
        דרישות:
        - לבדוק שהתוספת קיימת ברשימת האפשרויות
        - אם כן: לעדכן _selected_side ולהחזיר True
        - אם לא: להחזיר False
        """

    def get_category(self) -> str:
        return "Main Courses"
        """מחזיר 'Main Courses'"""

    @classmethod
    def get_side_options(cls) -> list:
        return cls._side_options.copy()

        """מחזיר עותק של רשימת התוספות"""

    @classmethod
    def add_side_option(cls, side: str):
        if side not in cls._side_options:
            cls._side_options.append(side)
        """
        הוספת תוספת חדשה לרשימה.
        
        דרישות:
        - להוסיף רק אם לא קיימת כבר
        """

    @classmethod
    def remove_side_option(cls, side: str):
        if side in cls._side_options:
            cls._side_options.remove(side)

        """הסרת תוספת מהרשימה (אם קיימת)"""

    def __str__(self) -> str:
        return f"{self._name} - ${self._price} (with side)"
        """
        ייצוג מחרוזת כולל תוספת.
        
        Returns:
            "name - $price" או "name - $price (with side)"
        """


class Dessert(MenuItem):

    """
    קינוח - עם אפשרות לסימון ללא סוכר.
    
    שדות מופע:
        _is_sugar_free (bool): האם ללא סוכר
    """
    
    def __init__(self, name: str, price: float, description: str = "", is_sugar_free: bool = False):
        super().__init__(name, price, description)
        self._is_sugar_free = is_sugar_free

        """
        אתחול קינוח.
        
        דרישות:
        - לקרוא ל-__init__ של מחלקת האב
        - לשמור את is_sugar_free ב-_is_sugar_free
        """

    @property
    def is_sugar_free(self) -> bool:
        return self._is_sugar_free
        """מחזיר האם הקינוח ללא סוכר"""
        raise NotImplementedError("Implement this method")
    
    def get_category(self) -> str:
        return "Desserts"
        """מחזיר 'Desserts'"""

    def __str__(self) -> str:
        return f"{self._name} - ${self._price} (sugar-free)"
        """
        ייצוג מחרוזת.
        
        Returns:
            "name - $price" או "name - $price (sugar-free)"
        """


class Beverage(MenuItem):
    """
    משקה - עם גודל ומצב חם/קר.
    
    שדות מחלקה:
        SIZES (list): גדלים אפשריים ["S", "M", "L"]
    
    שדות מופע:
        _size (str): גודל המשקה
        _is_cold (bool): האם קר
    """
    
    SIZES = ["S", "M", "L"]
    
    def __init__(self, name: str, price: float, description: str = "", 
                 size: str = "M", is_cold: bool = True):
        super().__init__(name, price, description)
        self._is_cold = is_cold
        self.size = size



        """
        אתחול משקה.
        
        דרישות:
        - לקרוא ל-__init__ של מחלקת האב
        - להשתמש ב-setter של size (לולידציה)
        - לשמור את is_cold ב-_is_cold
        """

    @property
    def size(self) -> str:
        return self._size
        """מחזיר את גודל המשקה"""

    @size.setter
    def size(self, value: str):
        if value not in Beverage.SIZES:
            raise ValueError("Size must be one of: ['S', 'M', 'L']")
        self._size = value

        """
        קובע את גודל המשקה.
        
        דרישות:
        - אם הגודל לא ברשימת SIZES, להעלות ValueError עם הודעה "Size must be one of: ['S', 'M', 'L']"
        """

    @property
    def is_cold(self) -> bool:
        return self._is_cold
        """מחזיר האם המשקה קר"""

    def get_category(self) -> str:
        return "Beverages"
        """מחזיר 'Beverages'"""

    @staticmethod
    def get_size_multiplier(size: str) -> float:
        multipliers = {
            "S": 0.8,
            "M": 1.0,
            "L": 1.3
        }
        return multipliers.get(size.upper(), 1.0)

        """
        מחזיר מכפיל מחיר לפי גודל.
        
        Returns:
            S -> 0.8, M -> 1.0, L -> 1.3
        """

    def get_total_price(self) -> float:
        """
        מחזיר מחיר לפי גודל.
        
        Returns:
            מחיר בסיס כפול מכפיל הגודל
        """
        multiplier = Beverage.get_size_multiplier(self.size)
        return self._price * multiplier

    def __str__(self) -> str:
        return f"{self.name}  ({self.size}, {self._is_cold}) - ${self._price}"
        """
        ייצוג מחרוזת כולל גודל וטמפרטורה.
        
        Returns:
            "name (size, cold/hot) - $price"
        """


























































# tests.py - Tests for your implementation
# Run this file to check your implementation
# python tests.py

import sys

# Colors for output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

passed = 0
failed = 0


def test(name, condition):
    """Helper function for tests"""
    global passed, failed
    if condition:
        print(f"{GREEN}PASS:{RESET} {name}")
        passed += 1
    else:
        print(f"{RED}FAIL:{RESET} {name}")
        failed += 1


def test_exception(name, exception_type, func):
    """Test that a function raises an exception"""
    global passed, failed
    try:
        func()
        print(f"{RED}FAIL:{RESET} {name} (no exception raised)")
        failed += 1
    except exception_type:
        print(f"{GREEN}PASS:{RESET} {name}")
        passed += 1
    except Exception as e:
        print(f"{RED}FAIL:{RESET} {name} (wrong exception: {type(e).__name__})")
        failed += 1


print("=" * 60)
print("  Restaurant Management System Tests")
print("=" * 60)
print()

# ==========================================
# MenuItem Tests
# ==========================================
print(f"{YELLOW}--- MenuItem Tests ---{RESET}")

try:
    from menu_item import MenuItem, Appetizer, MainCourse, Dessert, Beverage

    # Basic item creation
    item = MenuItem("Test", 50, "Description")
    test("MenuItem.__init__ - creation", item.name == "Test" and item.price == 50)
    test("MenuItem.description", item.description == "Description")
    test("MenuItem.get_category", item.get_category() == "General")
    test("MenuItem.format_price", MenuItem.format_price(32.5) == "$32.50")
    test("MenuItem.__str__", "Test" in str(item) and "50" in str(item))
    test("MenuItem.__eq__", MenuItem("a", 10, "") == MenuItem("a", 20, "x"))

    # Price validation
    test_exception("MenuItem.price negative", ValueError, lambda: MenuItem("x", -5, ""))

    # Price setter
    item.price = 60
    test("MenuItem.price setter", item.price == 60)

except Exception as e:
    print(f"{RED}Error in MenuItem tests: {e}{RESET}")

print()

# ==========================================
# Appetizer Tests
# ==========================================
print(f"{YELLOW}--- Appetizer Tests ---{RESET}")

try:
    # Reset bread inventory
    Appetizer._bread_inventory = {}

    Appetizer.add_bread_to_inventory("Pita", 10)
    test("Appetizer.add_bread_to_inventory", Appetizer.get_bread_quantity("Pita") == 10)

    Appetizer.add_bread_to_inventory("Pita", 5)
    test("Appetizer add to existing", Appetizer.get_bread_quantity("Pita") == 15)

    test("Appetizer.get_available_breads", "Pita" in Appetizer.get_available_breads())

    app = Appetizer("Hummus", 30, "")
    test("Appetizer.get_category", app.get_category() == "Appetizers")
    test("Appetizer.selected_bread initial", app.selected_bread is None)

    result = app.add_bread("Pita")
    test("Appetizer.add_bread success", result == True and app.selected_bread == "Pita")
    test("Appetizer inventory decreased", Appetizer.get_bread_quantity("Pita") == 14)
    test("Appetizer.get_total_price with bread", app.get_total_price() == 35)

    app.remove_bread()
    test("Appetizer.remove_bread", app.selected_bread is None)
    test("Appetizer inventory increased", Appetizer.get_bread_quantity("Pita") == 15)

    test("Appetizer.add_bread non-existent", app.add_bread("Baguette") == False)

except Exception as e:
    print(f"{RED}Error in Appetizer tests: {e}{RESET}")

print()

# ==========================================
# MainCourse Tests
# ==========================================
print(f"{YELLOW}--- MainCourse Tests ---{RESET}")

try:
    MainCourse._side_options = []

    MainCourse.add_side_option("Rice")
    MainCourse.add_side_option("Fries")
    test("MainCourse.add_side_option", "Rice" in MainCourse.get_side_options())

    mc = MainCourse("Schnitzel", 60, "")
    test("MainCourse.get_category", mc.get_category() == "Main Courses")

    result = mc.select_side("Rice")
    test("MainCourse.select_side success", result == True and mc.selected_side == "Rice")
    test("MainCourse.select_side non-existent", mc.select_side("Pasta") == False)

except Exception as e:
    print(f"{RED}Error in MainCourse tests: {e}{RESET}")

print()

# ==========================================
# Dessert Tests
# ==========================================
print(f"{YELLOW}--- Dessert Tests ---{RESET}")

try:
    d1 = Dessert("Cake", 40, "", is_sugar_free=False)
    d2 = Dessert("Fruit", 30, "", is_sugar_free=True)

    test("Dessert.get_category", d1.get_category() == "Desserts")
    test("Dessert.is_sugar_free False", d1.is_sugar_free == False)
    test("Dessert.is_sugar_free True", d2.is_sugar_free == True)
    test("Dessert.__str__ sugar-free", "sugar-free" in str(d2))

except Exception as e:
    print(f"{RED}Error in Dessert tests: {e}{RESET}")

print()

# ==========================================
# Beverage Tests
# ==========================================
print(f"{YELLOW}--- Beverage Tests ---{RESET}")

try:
    b = Beverage("Cola", 10, "", "M", True)

    test("Beverage.get_category", b.get_category() == "Beverages")
    test("Beverage.size", b.size == "M")
    test("Beverage.is_cold", b.is_cold == True)
    test("Beverage.get_size_multiplier S", Beverage.get_size_multiplier("S") == 0.8)
    test("Beverage.get_size_multiplier L", Beverage.get_size_multiplier("L") == 1.3)
    test("Beverage.get_total_price M", b.get_total_price() == 10)

    b.size = "L"
    test("Beverage.get_total_price L", b.get_total_price() == 13)

    test_exception("Beverage.size invalid", ValueError, lambda: setattr(b, 'size', 'XL'))

except Exception as e:
    print(f"{RED}Error in Beverage tests: {e}{RESET}")

print()

# ==========================================
# Table Tests
# ==========================================
print(f"{YELLOW}--- Table Tests ---{RESET}")

try:
    from table import Table

    Table.total_tables = 0

    t = Table(1, 4)
    test("Table.__init__", t.number == 1 and t.seats == 4)
    test("Table.is_occupied initial", t.is_occupied == False)
    test("Table.total_tables", Table.total_tables == 1)

    result = t.occupy()
    test("Table.occupy success", result == True and t.is_occupied == True)
    test("Table.occupy already occupied", t.occupy() == False)

    t.free()
    test("Table.free", t.is_occupied == False)

except Exception as e:
    print(f"{RED}Error in Table tests: {e}{RESET}")

print()

# ==========================================
# OrderItem Tests
# ==========================================
print(f"{YELLOW}--- OrderItem Tests ---{RESET}")

try:
    from order_item import OrderItem

    item = MenuItem("Test", 25, "")
    oi = OrderItem(item, 2, "Note")

    test("OrderItem.__init__", oi.quantity == 2 and oi.notes == "Note")
    test("OrderItem.menu_item", oi.menu_item == item)
    test("OrderItem.subtotal", oi.subtotal == 50)

    oi.quantity = 3
    test("OrderItem.quantity setter", oi.quantity == 3 and oi.subtotal == 75)

    test_exception("OrderItem.quantity < 1", ValueError, lambda: setattr(oi, 'quantity', 0))

except Exception as e:
    print(f"{RED}Error in OrderItem tests: {e}{RESET}")

print()

# ==========================================
# Order Tests
# ==========================================
print(f"{YELLOW}--- Order Tests ---{RESET}")

try:
    from order import Order

    Order._order_counter = 0
    Table.total_tables = 0

    t = Table(1, 4)
    o = Order(t)

    test("Order.__init__", o.order_id == 1 and o.table == t)
    test("Order.is_closed initial", o.is_closed == False)
    test("Order.__len__ empty", len(o) == 0)
    test("Order.get_total_orders", Order.get_total_orders() == 1)

    item1 = MenuItem("Item1", 30, "")
    item2 = MenuItem("Item2", 20, "")

    o.add_item(item1, 2)
    test("Order.add_item", len(o) == 1)
    test("Order.get_subtotal", o.get_subtotal() == 60)

    o.add_item(item2, 1)
    test("Order.get_subtotal two items", o.get_subtotal() == 80)

    total = o.get_total(10)
    test("Order.get_total with tip", total == 88)

    o.remove_item(item1)
    test("Order.remove_item", len(o) == 1 and o.get_subtotal() == 20)

    t.occupy()
    o.close()
    test("Order.close", o.is_closed == True and t.is_occupied == False)

    test_exception("Order.add_item to closed", Exception, lambda: o.add_item(item1, 1))

except Exception as e:
    print(f"{RED}Error in Order tests: {e}{RESET}")

print()

# ==========================================
# Menu Tests
# ==========================================
print(f"{YELLOW}--- Menu Tests ---{RESET}")

try:
    from menu import Menu

    m = Menu()
    test("Menu.__init__", len(m) == 0)

    item1 = MenuItem("Item1", 30, "")
    item2 = MenuItem("Item2", 20, "")

    test("Menu.add_item success", m.add_item(item1) == True)
    test("Menu.add_item duplicate", m.add_item(MenuItem("Item1", 50, "")) == False)
    test("Menu.__len__", len(m) == 1)
    test("Menu.__contains__", "Item1" in m)

    m.add_item(item2)
    test("Menu.find_item exists", m.find_item("Item1") == item1)
    test("Menu.find_item not exists", m.find_item("None") is None)
    test("Menu.__getitem__", m["Item1"] == item1)

    m.update_price("Item1", 40)
    test("Menu.update_price", m["Item1"].price == 40)

    test("Menu.remove_item", m.remove_item("Item1") == True and len(m) == 1)

    # Test __iter__
    m.add_item(MenuItem("A", 10, ""))
    count = sum(1 for _ in m)
    test("Menu.__iter__", count == 2)

except Exception as e:
    print(f"{RED}Error in Menu tests: {e}{RESET}")

print()

# ==========================================
# Restaurant Tests
# ==========================================
print(f"{YELLOW}--- Restaurant Tests ---{RESET}")

try:
    from restaurant import Restaurant

    Table.total_tables = 0
    Order._order_counter = 0

    r = Restaurant("Test")
    test("Restaurant.__init__", r.name == "Test")

    t1 = Table(1, 4)
    t2 = Table(2, 6)
    r.add_table(t1)
    r.add_table(t2)

    test("Restaurant.get_all_tables", len(r.get_all_tables()) == 2)
    test("Restaurant.get_free_tables", len(r.get_free_tables()) == 2)
    test("Restaurant.get_table", r.get_table(1) == t1)

    order = r.open_order(1)
    test("Restaurant.open_order", order is not None)
    test("Restaurant table occupied", len(r.get_free_tables()) == 1)
    test("Restaurant.get_order_by_table", r.get_order_by_table(1) == order)

    test_exception("Restaurant.open_order occupied", ValueError, lambda: r.open_order(1))
    test_exception("Restaurant.open_order not exist", ValueError, lambda: r.open_order(99))

    item = MenuItem("Item", 100, "")
    r.menu.add_item(item)
    order.add_item(item, 1)

    total = r.close_order(order, 10)
    test("Restaurant.close_order", total == 110)
    test("Restaurant.get_total_revenue", r.get_total_revenue() == 110)
    test("Restaurant.get_orders_count", r.get_orders_count() == 1)

except Exception as e:
    print(f"{RED}Error in Restaurant tests: {e}{RESET}")

print()

# ==========================================
# Summary
# ==========================================
print("=" * 60)
total = passed + failed
print(f"  Summary: {passed}/{total} tests passed")
if failed == 0:
    print(f"  {GREEN}Excellent! All tests passed!{RESET}")
else:
    print(f"  {RED}{failed} tests failed - keep working!{RESET}")
print("=" * 60)

sys.exit(0 if failed == 0 else 1)
