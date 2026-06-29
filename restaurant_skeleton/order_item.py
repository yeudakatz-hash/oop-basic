# order_item.py - מחלקת פריט בהזמנה

from menu_item import MenuItem


class OrderItem:
    """
    פריט בודד בהזמנה - מכיל MenuItem + כמות + הערות.
    
    שדות מופע:
        _menu_item (MenuItem): הפריט מהתפריט (פרטי)
        _quantity (int): כמות (פרטי)
        _notes (str): הערות מיוחדות (פרטי)
    """
    
    def __init__(self, menu_item: MenuItem, quantity: int = 1, notes: str = ""):
        """
        אתחול פריט בהזמנה.
        
        דרישות:
        - לשמור את menu_item ב-_menu_item
        - להשתמש ב-setter של quantity (לולידציה)
        - לשמור את notes ב-_notes
        
        Args:
            menu_item: הפריט מהתפריט
            quantity: כמות (ברירת מחדל: 1)
            notes: הערות (ברירת מחדל: מחרוזת ריקה)
        """
        self._menu_item = menu_item
        self._quantity = quantity
        self._notes = notes

    # --- Properties ---
    
    @property
    def menu_item(self) -> MenuItem:
        return self._menu_item
        """מחזיר את הפריט מהתפריט"""

    @property
    def quantity(self) -> int:
        return self._quantity
        """מחזיר את הכמות"""

    @quantity.setter
    def quantity(self, value: int):
        """
        קובע את הכמות.
        
        דרישות:
        - אם הכמות קטנה מ-1, להעלות ValueError עם הודעה "Quantity must be at least 1"
        """
        if value < 1:
            raise ValueError("Quantity must be at least 1")
        self._quantity = value

    @property
    def notes(self) -> str:
        return self._notes
        """מחזיר את ההערות"""

    @notes.setter
    def notes(self, value: str):
        self._notes = value
        """קובע את ההערות"""

    @property
    def subtotal(self) -> float:
        """
        מחזיר סכום ביניים (מחיר × כמות).
        
        דרישות:
        - אם לפריט יש מתודת get_total_price (כמו Appetizer, Beverage), להשתמש בה
        - אחרת, להשתמש ב-price רגיל
        - להכפיל בכמות
        
        Returns:
            מחיר × כמות
        """
        if hasattr(self._menu_item, "get_total_price"):
            price = self._menu_item.get_total_price()
        else:
            price = self._menu_item.price
        return price * self._quantity

    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "quantity x name = $subtotal" או "quantity x name = $subtotal (notes)"
        """
        # מפרמטים את סכום הביניים בצורה יפה עם הפונקציה של מחלקת הבסיס
        formatted_price = MenuItem.format_price(self.subtotal)

        if self._notes:
            return f"{self._quantity} x {self._menu_item.name} = {formatted_price} ({self._notes})"
        return f"{self._quantity} x {self._menu_item.name} = {formatted_price}"
