# table.py - מחלקת שולחן


class Table:
    """
    שולחן במסעדה.
    
    שדות מחלקה:
        total_tables (int): סה"כ שולחנות שנוצרו (מתעדכן בכל יצירה)
    
    שדות מופע:
        _number (int): מספר השולחן (פרטי)
        _seats (int): כמות מקומות ישיבה (פרטי)
        _is_occupied (bool): האם תפוס (פרטי)
    """
    
    total_tables: int = 0
    
    def __init__(self, number: int, seats: int = 4):
        self._number = number
        self._seats = seats
        self._is_occupied = False
        Table.total_tables += 1

        """
        אתחול שולחן.
        
        דרישות:
        - לשמור את number ב-_number
        - לשמור את seats ב-_seats
        - לאתחל _is_occupied ל-False
        - להעלות את total_tables ב-1
        
        Args:
            number: מספר השולחן
            seats: כמות מקומות (ברירת מחדל: 4)
        """

    # --- Properties ---
    
    @property
    def number(self) -> int:
        return self._number
        """מחזיר את מספר השולחן"""

    @property
    def seats(self) -> int:
        return self._seats
        """מחזיר את כמות המקומות"""

    @property
    def is_occupied(self) -> bool:
        return self._is_occupied
        """מחזיר האם השולחן תפוס"""

    # --- Methods ---
    
    def occupy(self) -> bool:

        """
        סימון השולחן כתפוס.
        
        דרישות:
        - אם כבר תפוס: להחזיר False
        - אחרת: לסמן כתפוס ולהחזיר True
        
        Returns:
            True אם הצליח, False אם כבר היה תפוס
        """
        if self._is_occupied:
            return False
        self._is_occupied = True
        return True


    def free(self):
        """סימון השולחן כפנוי"""
        self._is_occupied = False


    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "Table X (Y seats) - Free/Occupied"
        """
        status = "Occupied" if self._is_occupied else "Free"
        return f"Table {self._number} ({self._seats} seats) - {status}"
