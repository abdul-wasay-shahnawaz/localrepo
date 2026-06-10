Perfect 👍 You’ve uploaded the full assignment for **“Class and Objects (Encapsulation and Inheritance)”**.
Let’s create **simple beginner-friendly Python solutions** for all the tasks mentioned.

---

## 🧩 Part 1: Encapsulation Practice Tasks

### **Task 1: Bank Account**

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # Private
        self.__balance = balance  # Private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance


# Test the class
account1 = BankAccount("123")
account1.deposit(500)
account1.withdraw(200)
print("Balance:", account1.get_balance())
```

---

### **Task 2: Student Marks Validation**

```python
class Student:
    def __init__(self, name, roll_no, marks=0):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks


# Test the class
s1 = Student("Ali", 101)
s1.set_marks(85)
print(s1.get_name(), s1.get_roll_no(), s1.get_marks())
```

---

### **Task 3: Password Manager**

```python
class PasswordManager:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def __check_username(self, name):
        return self.username == name

    def __check_password(self, input_pass):
        return self.__password == input_pass

    def set_password(self, old, new):
        if self.__check_password(old):
            self.__password = new
            print("Password updated successfully!")
        else:
            print("Incorrect old password.")


# Test the class
pm = PasswordManager("user1", "1234")
pm.set_password("1234", "abcd")
```

---

### **Task 4: Employee Salary Protection**

```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive.")

    def show_details(self):
        print(f"Name: {self.__name}, Salary: {self.__salary}")


# Test the class
emp = Employee("Sara", 50000)
emp.show_details()
```

---

### **Task 5: Shopping Cart**

```python
class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        if item not in self.__items:
            self.__items.append(item)
        else:
            print("Item already in cart!")

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print("Item not found!")

    def view_cart(self):
        return self.__items


# Test the class
cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
print(cart.view_cart())
```

---

## 🧬 Part 2: Inheritance Practice Tasks

### **Task 1: Single Level – Animal**

```python
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark!")


# Test
dog = Dog()
dog.make_sound()
```

---

### **Task 2: Single Level – Vehicle**

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Seats: {self.seats}")


# Test
car = Car("Toyota", "Corolla", 5)
car.display()
```

---

### **Task 3: Multi-Level – Family Tree**

```python
class GrandParent:
    def family_name(self):
        print("We are the Johnson family.")

class Parent(GrandParent):
    def occupation(self):
        print("Parent is a teacher.")

class Child(Parent):
    def hobby(self):
        print("Child loves painting.")


# Test
c = Child()
c.family_name()
c.occupation()
c.hobby()
```

---

### **Task 4: Multiple Inheritance – Skills**

```python
class Father:
    def skills(self):
        return "Scientist"

class Mother:
    def skills(self):
        return "Freelancer"

class Child(Father, Mother):
    def skills(self):
        return f"{Father.skills(self)} and {Mother.skills(self)}"


# Test
ch = Child()
print(ch.skills())
```

---

Would you like me to combine all of these into a **single `.py` file** so you can download and run it directly?
