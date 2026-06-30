# order.py - מחלקת הזמנה

from datetime import datetime
from menu_item import MenuItem
from order_item import OrderItem
from table import Table


class Order:
    """
    הזמנה שלמה של שולחן.
    
    שדות מחלקה:
        _order_counter (int): מונה הזמנות - עולה ב-1 בכל יצירה (פרטי)
        DEFAULT_TIP_PERCENT (float): אחוז טיפ ברירת מחדל (10.0)
    
    שדות מופע:
        _order_id (int): מזהה ייחודי (נקבע אוטומטית מהמונה)
        _table (Table): אובייקט השולחן
        _items (list): רשימת OrderItem
        _created_at (datetime): זמן פתיחת ההזמנה
        _is_closed (bool): האם ההזמנה נסגרה
    """
    
    _order_counter: int = 0
    DEFAULT_TIP_PERCENT: float = 10.0
    
    def __init__(self, table: Table):
        """
        אתחול הזמנה.
        
        דרישות:
        - להעלות את _order_counter ב-1
        - לשמור את הערך החדש של המונה ב-_order_id
        - לשמור את table ב-_table
        - לאתחל _items לרשימה ריקה
        - לשמור את הזמן הנוכחי ב-_created_at (datetime.now())
        - לאתחל _is_closed ל-False
        
        Args:
            table: אובייקט השולחן
        """
        Order._order_counter += 1
        self._order_id = Order._order_counter
        self._table = table
        self._items =[]
        self._created_at = datetime.now()
        self._isclosed = False


    # --- Properties ---
    
    @property
    def order_id(self) -> int:
        return self._order_id
        """מחזיר את מזהה ההזמנה"""

    @property
    def table(self) -> Table:
        return self._table
        """מחזיר את אובייקט השולחן"""

    @property
    def items(self) -> list:
        return self._items.copy()
        """
        מחזיר עותק של רשימת הפריטים.
        
        דרישות:
        - להחזיר עותק (copy) ולא את הרשימה עצמה
        """

    @property
    def is_closed(self) -> bool:
        return self._isclosed
        """מחזיר האם ההזמנה נסגרה"""

    @property
    def created_at(self) -> datetime:
        return self._created_at
        """מחזיר את זמן יצירת ההזמנה"""

    # --- Methods ---
    
    def add_item(self, menu_item: MenuItem, quantity: int = 1, notes: str = "") -> OrderItem:
        """
        הוספת פריט להזמנה.
        
        דרישות:
        - אם ההזמנה סגורה, להעלות Exception עם הודעה "Cannot add items to closed order"
        - לבדוק אם הפריט כבר קיים (לפי שם ואותן הערות)
          - אם כן: להוסיף לכמות הקיימת
          - אם לא: ליצור OrderItem חדש ולהוסיף לרשימה
        - להחזיר את ה-OrderItem
        
        Args:
            menu_item: הפריט מהתפריט
            quantity: כמות
            notes: הערות
            
        Returns:
            ה-OrderItem שנוסף/עודכן
        """
        if self._isclosed:
            raise Exception("Cannot remove items from closed order")
        for item in self._items:
            if item.menu_item.name == menu_item.name and item.notes == notes:
                item.quantity += quantity
                return item

        new_order_item = OrderItem(menu_item, quantity, notes)
        self._items.append(new_order_item)
        return new_order_item

    def remove_item(self, menu_item: MenuItem) -> bool:
        """
        הסרת פריט מההזמנה.
        
        דרישות:
        - אם ההזמנה סגורה, להעלות Exception עם הודעה "Cannot remove items from closed order"
        - לחפש פריט עם אותו menu_item ולהסיר אותו
        
        Returns:
            True אם נמצא והוסר, False אחרת
        """
        if self._isclosed:
            raise Exception("Cannot remove items from closed order")
        for item in self._items:
            if item.menu_item == menu_item:
                self._items.remove(item)
                return True
        return False

    def get_subtotal(self) -> float:
        """
        מחזיר סכום ביניים (לפני טיפ).
        
        Returns:
            סכום כל ה-subtotal של הפריטים
        """
        total = 0.0
        for item in self._items:
            total += item.subtotal
        return total


    def get_total(self, tip_percent: float = None) -> float:
        """
        מחזיר סכום כולל עם טיפ.
        
        דרישות:
        - אם tip_percent הוא None, להשתמש ב-DEFAULT_TIP_PERCENT
        - לחשב: subtotal + (subtotal × tip_percent / 100)
        
        Args:
            tip_percent: אחוז טיפ (ברירת מחדל: None)
            
        Returns:
            סכום כולל טיפ
        """
        if tip_percent is None:
            tip_percent = Order.DEFAULT_TIP_PERCENT

        subtotal = self.get_subtotal()
        return subtotal + (subtotal * tip_percent / 100)

    def get_bill(self, tip_percent: float = None) -> str:
        """
        מחזיר חשבון מפורט כמחרוזת.
        
        דרישות:
        - כותרת עם מספר הזמנה ושולחן
        - רשימת כל הפריטים
        - סכום ביניים (Subtotal)
        - טיפ (Tip) - סכום ואחוז
        - סכום סופי (Total)
        
        הפורמט:
        ========================================
        Bill - Order #X
        Table: Y
        Time: HH:MM:SS
        ========================================
        (items list)
        ----------------------------------------
        Subtotal: $XX.XX
        Tip (X%): $XX.XX
        ========================================
        Total: $XX.XX
        ========================================
        
        Returns:
            חשבון מפורמט
        """

        if tip_percent is None:
            tip_percent = Order.DEFAULT_TIP_PERCENT

        subtotal = self.get_subtotal()
        total = self.get_total(tip_percent)
        tip_amount = total - subtotal

        time_str = self._created_at.strftime("%H:%M:%S")

        bill_str = "========================================\n"
        bill_str += f"Bill - Order #{self._order_id}\n"
        bill_str += f"Table: {self._table.number}\n"
        bill_str += f"Time: {time_str}\n"
        bill_str += "========================================\n"

        for item in self._items:
            bill_str += f"{item}\n"

        bill_str += "----------------------------------------\n"
        bill_str += f"Subtotal: {MenuItem.format_price(subtotal)}\n"
        bill_str += f"Tip ({tip_percent}%): {MenuItem.format_price(tip_amount)}\n"
        bill_str += "========================================\n"
        bill_str += f"Total: {MenuItem.format_price(total)}\n"
        bill_str += "========================================"

        return bill_str

    def close(self):
        """
        סגירת ההזמנה.
        
        דרישות:
        - לסמן את ההזמנה כסגורה
        - לשחרר את השולחן (לקרוא ל-free)
        """
        self._isclosed = True
        self._table.free()

    # --- Class Methods ---
    
    @classmethod
    def get_total_orders(cls) -> int:
        """מחזיר כמה הזמנות נוצרו בסה"כ"""
        return cls._order_counter

    # --- Magic Methods ---
    
    def __len__(self) -> int:
        """מחזיר כמות פריטים בהזמנה"""
        return len(self._items)

    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "Order #X (Table Y) - Z items - Open/Closed"
        """
        if self._isclosed:
            status = "Closed"
        else:
            status = "Open"
        return f"Order #{self._order_id} (Table {self._table.number}) - {len(self._items)} items - {status}"
