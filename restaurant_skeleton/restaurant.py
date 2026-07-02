# restaurant.py - מחלקת המסעדה הראשית

from menu import Menu
from table import Table
from order import Order
from menu_item import MenuItem


class Restaurant:
    """
    המחלקה הראשית - מנהלת את כל המסעדה.

    שדות מופע:
        _name (str): שם המסעדה
        _menu (Menu): אובייקט התפריט
        _tables (list): רשימת השולחנות
        _active_orders (list): רשימת הזמנות פעילות
        _closed_orders (list): רשימת הזמנות שנסגרו
        _total_revenue (float): סה"כ הכנסות
    """

    def __init__(self, name: str):
        """
        אתחול מסעדה.

        דרישות:
        - לשמור את name ב-_name
        - ליצור Menu חדש ולשמור ב-_menu
        - לאתחל _tables, _active_orders, _closed_orders לרשימות ריקות
        - לאתחל _total_revenue ל-0.0

        Args:
            name: שם המסעדה
        """
        self._name = name
        self._menu = Menu()
        self._tables = []
        self._active_orders = []
        self._closed_orders = []
        self._total_revenue = 0.0

    # --- Properties ---

    @property
    def name(self) -> str:
        """מחזיר את שם המסעדה"""
        return self._name

    @property
    def menu(self) -> Menu:
        """מחזיר את אובייקט התפריט"""
        return self._menu

    # --- Table Management ---

    def add_table(self, table: Table):
        """הוספת שולחן למסעדה"""
        self._tables.append(table)

    def get_table(self, number: int) -> Table:
        """
        שליפת שולחן לפי מספר.

        Returns:
            השולחן אם נמצא, None אחרת
        """
        for table in self._tables:
            if table.number == number:
                return table
        return None

    def get_all_tables(self) -> list:
        """מחזיר עותק של רשימת כל השולחנות"""
        return self._tables.copy()

    def get_free_tables(self) -> list:
        """מחזיר רשימת שולחנות פנויים"""
        free_list = []
        for table in self._tables:
            if not table.is_occupied:
                free_list.append(table)
        return free_list

    def get_occupied_tables(self) -> list:
        """מחזיר רשימת שולחנות תפוסים"""
        occupied_list = []
        for table in self._tables:
            if table.is_occupied:
                occupied_list.append(table)
        return occupied_list

    # --- Order Management ---

    def open_order(self, table_number: int) -> Order:
        """
        פתיחת הזמנה חדשה לשולחן.

        דרישות:
        - לבדוק שהשולחן קיים (אם לא, ValueError עם "Table X does not exist")
        - לבדוק שהשולחן פנוי (אם תפוס, ValueError עם "Table X is already occupied")
        - לסמן את השולחן כתפוס
        - ליצור Order חדש ולהוסיף לרשימת ההזמנות הפעילות

        Args:
            table_number: מספר השולחן

        Returns:
            ההזמנה החדשה

        Raises:
            ValueError: אם השולחן לא קיים או תפוס
        """
        table = self.get_table(table_number)
        if table is None:
            raise ValueError(f"Table {table_number} does not exist")

        if table.is_occupied:
            raise ValueError(f"Table {table_number} is already occupied")

        table.occupy()
        new_order = Order(table)
        self._active_orders.append(new_order)
        return new_order

    def get_active_orders(self) -> list:
        """מחזיר עותק של רשימת הזמנות פעילות"""
        return self._active_orders.copy()

    def get_order_by_table(self, table_number: int) -> Order:
        """
        מחזיר הזמנה פעילה לפי מספר שולחן.

        Returns:
            ההזמנה אם נמצאה, None אחרת
        """
        for order in self._active_orders:
            if order.table.number == table_number:
                return order
        return None

    def close_order(self, order: Order, tip_percent: float = None) -> float:
        """
        סגירת הזמנה וחישוב סכום לתשלום.

        דרישות:
        - לבדוק שההזמנה ברשימת ההזמנות הפעילות (אם לא, ValueError עם "Order not found in active orders")
        - לחשב את הסכום הסופי
        - לקרוא ל-close של ההזמנה
        - להעביר מרשימת הפעילות לסגורות
        - להוסיף את הסכום ל-_total_revenue

        Args:
            order: ההזמנה לסגירה
            tip_percent: אחוז טיפ (ברירת מחדל: None)

        Returns:
            הסכום הסופי לתשלום
        """
        if order not in self._active_orders:
            raise ValueError("Order not found in active orders")

        final_total = order.get_total(tip_percent)
        order.close()

        self._active_orders.remove(order)
        self._closed_orders.append(order)
        self._total_revenue += final_total

        return final_total

    # --- Statistics (Bonus) ---

    def get_total_revenue(self) -> float:
        """מחזיר סה"כ הככנסות"""
        return self._total_revenue

    def get_orders_count(self) -> int:
        """מחזיר כמות הזמנות שנסגרו"""
        return len(self._closed_orders)

    def get_average_order_value(self) -> float:
        """
        מחזיר ממוצע סכום הזמנה.

        Returns:
            ממוצע, או 0.0 אם אין הזמנות
        """
        if not self._closed_orders:
            return 0.0

        total_value = 0.0
        for order in self._closed_orders:
            total_value += order.get_subtotal()

        return total_value / len(self._closed_orders)

    def get_most_popular_item(self) -> tuple:
        """
        מחזיר את הפריט שהוזמן הכי הרבה.

        דרישות:
        - לעבור על כל ההזמנות הסגורות
        - לספור כמה פעמים כל פריט הוזמן
        - להחזיר את הפריט עם הספירה הגבוהה ביותר

        Returns:
            (item_name, count) או (None, 0) אם אין נתונים
        """
        if not self._closed_orders:
            return (None, 0)

        counts = {}
        for order in self._closed_orders:
            for item in order.items:
                name = item.menu_item.name
                counts[name] = counts.get(name, 0) + item.quantity

        if not counts:
            return (None, 0)

        most_popular = max(counts, key=counts.get)
        return (most_popular, counts[most_popular])

    def get_revenue_by_category(self) -> dict:
        """
        מחזיר הכנסות מחולקות לפי קטגוריה.

        Returns:
            מילון {category: amount}
        """
        revenue_map = {}
        for order in self._closed_orders:
            for item in order.items:
                category = item.menu_item.get_category()
                revenue_map[category] = revenue_map.get(category, 0.0) + item.subtotal
        return revenue_map

    # --- Magic Methods ---

    def __str__(self) -> str:
        """
        ייצוג מחרוזת.

        Returns:
            "Restaurant 'name' - X tables, Y menu items"
        """
        return f"Restaurant '{self._name}' - {len(self._tables)} tables, {len(self._menu)} menu items"
