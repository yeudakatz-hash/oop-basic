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
        return "Appetizers"

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


