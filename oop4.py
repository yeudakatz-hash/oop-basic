class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance or amount < 0:
            print("שגיאה")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(101, "Yossi", 1000)

print(acc.account_number)  # ידפיס: 101

print(acc._account_holder) # ידפיס: Yossi (אבל אסור לעשות את זה בקוד אמיתי!)



class Vehicle:
    def __init__(self, model, color):
        self.model = model
        self._color = color
        self.__speed = 0


    def accelerate(self, spead_increase):
        self.__speed += spead_increase

    def brake(self, speed_decrease):
        if speed_decrease > self.__speed:
            self.__speed = 0
        else:
            self.__speed -= speed_decrease

    def get_speed(self):
        return self.__speed

    def get_color(self):
        return self._color

class Car(Vehicle):

    def __init__(self, model, color, max_speed):
        super().__init__(model, color)
        self.__max_speed = max_speed

    def accelerate(self, spead_increase):
        if self.get_speed() + spead_increase > self.__max_speed:
            allowed_increase = self.__max_speed - self.get_speed()
            super().accelerate(allowed_increase)
        else:
            super().accelerate(spead_increase)

    def get_max_speed(self):
        return self.__max_speed


class DigitalSafe:
    def __init__(self, safe_id, code):
        self._safe_id = safe_id
        self.__code = code
        self.__is_locked = True
        self.__attempt_count = 0
    def try_unlock(self, code):
        if self.__attempt_count == 3:
            print("3 נסיונות כושלים")
            return
        self.__attempt_count +=1
        if code == self.__code:
            self.__is_locked = False
            self.__attempt_count == 0
            print("הכספת נפתחה")
        else:
            print(f"נשארו לך עוד{self.get_attempts_left()}נסיונות")

    def lock(self):
        self.__is_locked = True

    def is_locked(self):
        return self.__is_locked

    def get_attempts_left(self):
        return 3 - self.__attempt_count

    def reset_attempts(self):
        if self.__is_locked == False:
            self.__attempt_count = 0
            print("המונה אופס")
        else:
            print("אי אפשר לאפס כרגע")
