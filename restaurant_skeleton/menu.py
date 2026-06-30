# menu.py - מחלקת תפריט

from menu_item import MenuItem, Appetizer, MainCourse, Dessert, Beverage


class Menu:
    """
    תפריט המסעדה.

    שדות מופע:
        _items (list): רשימת פריטי התפריט
    """

    def __init__(self):
        """
        אתחול תפריט ריק.

        דרישות:
        - לאתחל _items לרשימה ריקה
        """
        self._items = []

    # --- Properties ---

    @property
    def items(self) -> list:
        """
        מחזיר עותק של רשימת הפריטים.

        דרישות:
        - להחזיר עותק (copy) ולא את הרשימה עצמה
        """
        return self._items.copy()

    # --- Methods ---

    def add_item(self, item: MenuItem) -> bool:
        """
        הוספת פריט לתפריט.

        דרישות:
        - לבדוק שפריט עם אותו שם לא קיים כבר
        - אם קיים: להחזיר False
        - אם לא קיים: להוסיף ולהחזיר True

        Returns:
            True אם נוסף, False אם כבר קיים
        """
        if self.find_item(item.name) is not None:
            return False
        self._items.append(item)
        return True

    def remove_item(self, name: str) -> bool:
        """
        הסרת פריט לפי שם.

        Returns:
            True אם נמצא והוסר, False אחרת
        """
        for item in self._items:
            if item.name == name:
                self._items.remove(item)
                return True
        return False

    def find_item(self, name: str) -> MenuItem:
        """
        חיפוש פריט לפי שם.

        Returns:
            הפריט אם נמצא, None אחרת
        """
        for item in self._items:
            if item.name == name:
                return item
        return None

    def update_price(self, name: str, new_price: float) -> bool:
        """
        עדכון מחיר פריט.

        דרישות:
        - למצוא את הפריט ולעדכן את המחיר שלו

        Returns:
            True אם נמצא ועודכן, False אחרת
        """
        for item in self._items:
            if item.name == name:
                item.price = new_price
                return True
        return False

    def get_by_category(self, category: str) -> list:
        """
        מחזיר את כל הפריטים בקטגוריה מסוימת.

        Returns:
            רשימת פריטים שה-get_category שלהם שווה לקטגוריה
        """
        filtered_items = []
        for item in self._items:
            if item.get_category() == category:
                filtered_items.append(item)
        return filtered_items

    def get_all_categories(self) -> list:
        """
        מחזיר רשימת כל הקטגוריות בתפריט.

        Returns:
            רשימה ללא כפילויות
        """
        categories_list = []
        for item in self._items:
            current_category = item.get_category()
            if current_category not in categories_list:
                categories_list.append(current_category)
        return categories_list

    def get_items_in_price_range(self, min_price: float, max_price: float) -> list:
        """
        מחזיר פריטים בטווח מחירים.

        Returns:
            רשימת פריטים שהמחיר שלהם בין min_price ל-max_price (כולל)
        """
        items_in_range = []
        for item in self._items:
            if min_price <= item.price <= max_price:
                items_in_range.append(item)
        return items_in_range

    # --- Class Methods ---

    @classmethod
    def from_file(cls, filename: str) -> 'Menu':
        """
        יצירת תפריט מקובץ טקסט.

        פורמט הקובץ (כל שורה):
            type,name,price,description

        סוגים: "Appetizer", "MainCourse", "Dessert", "Beverage"

        דרישות:
        - לדלג על שורות ריקות או שמתחילות ב-#
        - ליצור את הפריט המתאים לפי הסוג
        - להוסיף לתפריט
        - אם הקובץ לא נמצא, להדפיס "File {filename} not found" ולהחזיר תפריט ריק

        Returns:
            אובייקט Menu חדש
        """
        menu_obj = cls()
        try:
            with open(filename, 'r') as file:
                for line in file:
                    cleaned_line = line.strip()
                    if not cleaned_line or cleaned_line.startswith('#'):
                        continue
                    parts = cleaned_line.split(',')
                    if len(parts) == 4:
                        item_type = parts[0].strip()
                        name = parts[1].strip()
                        price = float(parts[2].strip())
                        description = parts[3].strip()
                        if item_type == "Appetizer":
                            new_item = Appetizer(name, price, description)
                        elif item_type == "MainCourse":
                            new_item = MainCourse(name, price, description)
                        elif item_type == "Dessert":
                            new_item = Dessert(name, price, description)
                        elif item_type == "Beverage":
                            new_item = Beverage(name, price, description)
                        else:
                            new_item = MenuItem(name, price, description)
                        menu_obj.add_item(new_item)
        except FileNotFoundError:
            print(f"File {filename} not found")
        return menu_obj

    # --- Magic Methods ---

    def __len__(self) -> int:
        """מחזיר כמות פריטים בתפריט"""
        return len(self._items)

    def __contains__(self, name: str) -> bool:
        """
        בדיקה אם פריט קיים בתפריט לפי שם.

        שימוש: "Hummus" in menu
        """
        return self.find_item(name) is not None

    def __iter__(self):
        """
        אפשרות לעבור על הפריטים בלולאה.

        שימוש: for item in menu: ...
        """
        return iter(self._items)

    def __getitem__(self, name: str) -> MenuItem:
        """
        גישה לפריט לפי שם.

        שימוש: menu["Hummus"]

        דרישות:
        - אם לא נמצא, להעלות KeyError עם הודעה "Item 'name' not found in menu"
        """
        item = self.find_item(name)
        if item is None:
            raise KeyError(f"Item '{name}' not found in menu")
        return item
