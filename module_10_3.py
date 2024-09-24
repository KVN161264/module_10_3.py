import threading
import random
import time
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        for i in range(100):
            summ = random.randint(50, 500)
            self.balance += summ
            print(f"Пополнение: {summ}. Баланс: {self.balance}")
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print("Замок разблокирован")

    def take(self):
        for i in range(100):
            summ = random.randint(50, 500)
            print(f"Запрос на {summ}")
            if summ <= self.balance:
                self.balance -= summ
                print(f"Снятие: {summ}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)

if __name__ == "__main__":
    bk = Bank()

t1 = threading.Thread(target=bk.deposit)
t2 = threading.Thread(target=bk.take)

t1.start()
t2.start()
t1.join()
t2.join()

print(f'Итоговый баланс: {bk.balance}')
