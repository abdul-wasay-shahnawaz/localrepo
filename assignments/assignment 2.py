 #05: Class and Objects (Encapsulation and Inheritance)

## 🔹 Task 1: Bank Account (Encapsulation)



Heres the **beginner-friendly code with comments**:

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew: {amount}")

    def get_balance(self):
        return self.__balance


# Create 3 objects and test methods
acc1 = BankAccount("123456")
acc2 = BankAccount("987654", 1000)
acc3 = BankAccount("111222", 500)

acc1.deposit(200)
acc1.withdraw(50)
print("Balance acc1:", acc1.get_balance())

acc2.withdraw(2000)  # Should show "insufficient"
print("Balance acc2:", acc2.get_balance())

acc3.deposit(300)
acc3.withdraw(100)
print("Balance acc3:", acc3.get_balance())
```

---

## 🔹 Task 2: Student Marks Validation

We'll validate that **marks are between 0 and 100**, and we'll use **getter and setter** methods for encapsulation.

```python
class Student:
    def __init__(self, name, roll_no, marks=0):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = 0
        self.set_marks(marks)  # Use setter to initialize

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks. Must be between 0 and 100.")

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks


# Create 3 objects and test methods
s1 = Student("Ali", 101, 85)
s2 = Student("Sara", 102)
s3 = Student("John", 103, 110)  # Invalid marks

s2.set_marks(70)

print(f"{s1.get_name()} ({s1.get_roll_no()}) - Marks: {s1.get_marks()}")
print(f"{s2.get_name()} ({s2.get_roll_no()}) - Marks: {s2.get_marks()}")
print(f"{s3.get_name()} ({s3.get_roll_no()}) - Marks: {s3.get_marks()}")
```

---

## ✅ What’s next?

Would you like to move on to **Task 3: Password Manager**, or review inheritance examples (like single-level, multi-level, or multiple inheritance)?

Let me know your next step.


## 🔷 Task 3: Password Manager

```python
class PasswordManager:
    def __init__(self, username, password):
        self.username = username          # Public attribute
        self.__password = password        # Private attribute

    def set_password(self, old, new):
        if self.__check_password(old):
            self.__password = new
            print("Password updated.")
        else:
            print("Old password is incorrect.")

    def __check_username(self, name):     # Private method
        return self.username == name

    def __check_password(self, input):    # Private method
        return self.__password == input


# Create 3 objects and test
user1 = PasswordManager("admin", "1234")
user2 = PasswordManager("user", "pass")
user3 = PasswordManager("test", "abc")

user1.set_password("wrong", "new123")  # Incorrect old password
user1.set_password("1234", "new123")   # Correct old password
```

---

## 🔷 Task 4: Employee Salary Protection

```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = 0
        self.set_salary(salary)  # Use setter

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive.")

    def show_details(self):
        print(f"Name: {self.__name}, Salary: {self.__salary}")


# Create and test 3 objects
emp1 = Employee("Ali", 50000)
emp2 = Employee("Sara", -1000)   # Should show error
emp3 = Employee("John", 75000)

emp1.show_details()
emp2.set_salary(45000)           # Update valid salary
emp2.show_details()
```

---

## 🔷 Task 5: Shopping Cart

```python
class ShoppingCart:
    def __init__(self):
        self.__items = []  # Private list

    def add_item(self, item):
        if item not in self.__items:
            self.__items.append(item)
            print(f"Added: {item}")
        else:
            print("Item already in cart.")

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            print(f"Removed: {item}")
        else:
            print("Item not found.")

    def view_cart(self):
        return self.__items


# Create and test 3 objects
cart1 = ShoppingCart()
cart2 = ShoppingCart()
cart3 = ShoppingCart()

cart1.add_item("Apples")
cart1.add_item("Bananas")
cart1.add_item("Apples")  # Should not add again
print("Cart 1:", cart1.view_cart())

cart2.add_item("Milk")
cart2.remove_item("Milk")
print("Cart 2:", cart2.view_cart())
```

---

# ✅ Part 2: Inheritance Practice

---

## 🔷 Task 1: Single Level – Animal

```python
class Animal:
    def make_sound(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def make_sound(self):  # Method overriding
        print("Bark!")


# Test objects
a1 = Animal()
d1 = Dog()

a1.make_sound()  # Output: generic sound
d1.make_sound()  # Output: Bark!
```

---

## 🔷 Task 2: Single Level – Vehicle

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)  # Call parent constructor
        self.seats = seats


# Create 3 objects
car1 = Car("Toyota", "Corolla", 5)
car2 = Car("Honda", "Civic", 4)
car3 = Car("Tesla", "Model 3", 5)

print(f"{car1.brand} {car1.model} - Seats: {car1.seats}")
print(f"{car2.brand} {car2.model} - Seats: {car2.seats}")
print(f"{car3.brand} {car3.model} - Seats: {car3.seats}")
```

---

 **Done!**
Youve now completed all the **Encapsulation** and **Single-Level Inheritance** tasks.

Would you like to:

* Continue with **multi-level** or **multiple inheritance** tasks?
* Export all this code into a `.py` file or `.docx` report?
* Practice writing your own classes based on this?

Let me know how youd like to proceed.


## 🔷 Task 3: Multi-Level Inheritance – **Family Tree**

Well go:
`GrandParent  Parent  Child`
Each class adds one method.

```python
# Base class
class GrandParent:
    def family_name(self):
        print("Family Name: Khan")

# Parent inherits GrandParent
class Parent(GrandParent):
    def occupation(self):
        print("Occupation: Engineer")

# Child inherits Parent (multi-level)
class Child(Parent):
    def hobby(self):
        print("Hobby: Painting")


# Create Child object and call all methods
child = Child()
child.family_name()
child.occupation()
child.hobby()
```

---

## 🔷 Task 4: Multiple Inheritance – **Skills**

Well combine methods from two parent classes using multiple inheritance:

```python
# Parent 1
class Father:
    def skills(self):
        return "Scientist"

# Parent 2
class Mother:
    def skills(self):
        return "Freelancer"

# Child inherits both
class Child(Father, Mother):
    def skills(self):
        # Call skills from both parents
        return Father.skills(self) + " and " + Mother.skills(self)


# Test the Child class
child = Child()
print("Combined Skills:", child.skills())
```

---

 **Thats all!**
Youve now finished all:

*  Encapsulation tasks
*  Inheritance tasks (Single-Level, Multi-Level, Multiple)

---

### Would you like me to:

* Bundle all this into a `.py` or `.docx` file?
* Help you add input/output for user interaction?
* Quiz you on what youve learned?

Let me know how youd like to wrap up!
