
class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number

#practice
class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, first_name, last_name, passport_number):
        customer = Customer(first_name, last_name, passport_number)
        self.customers[customer.passport_number] = customer

    def add_account(self, account, customer):
        self.accounts[customer] = account

    def deposit(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.deposit(amount)

    def withdraw(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.withdraw(amount)

    def get_customer(self, passport_number):
        if passport_number not in self.customers:
            raise KeyError("Customer not found")
        return self.customers[passport_number]

    def get_customer_account(self, passport_number):
        customer = self.get_customer(passport_number)
        if customer not in self.accounts:
            raise KeyError("Account not found")
        return self.accounts[customer]


class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.amount = 0
        self.currency = currency

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if amount > self.amount:
            raise ValueError("Недостаточно денег на счету")
        self.amount -= amount


bank=Bank()
# Добавление клиентов
bank.add_customer("Иван", "Иванов", "1234567890")
bank.add_customer("Петр", "Петров", "0987654321")

# Создание счетов
account1 = BankAccount("111111", "USD")
account2 = BankAccount("222222", "EUR")

# Привязка счетов к клиентам
bank.add_account(account1, bank.get_customer("1234567890"))
bank.add_account(account2, bank.get_customer("0987654321"))

# Внесение депозитов
bank.deposit("1234567890", 100)
bank.deposit("0987654321", 100)

# Вывод информации о счетах
print(bank.get_customer_account("1234567890").amount)  # Выведет 100
print(bank.get_customer_account("0987654321").amount)  # Выведет 100
