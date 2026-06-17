class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number: str, account_name: str):
        self.account_number = account_number
        self.__balance = 0
        self.account_name = account_name

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, new_name: str):
        cleaned_name = new_name.strip()
        if not cleaned_name:
            print("Tên tài khoản không được để trống")
            return
        self._account_name = cleaned_name.upper()

    @staticmethod
    def validate_account_number(account_number: str):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_transaction_fee(cls, new_fee: int):
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            return
        cls.transaction_fee = new_fee

    def deposit(self, amount: int):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return
        self.__balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VND")
        print(f"Số dư mới: {self.__balance:,} VND")

    def withdraw(self, amount: int):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return

        total = amount + BankAccount.transaction_fee
        if self.__balance < total:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            print(f"Số dư hiện tại: {self.__balance:,} VND")
            return

        self.__balance -= total
        print(f"Rút tiền thành công: -{amount:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
        print(f"Số dư mới: {self.__balance:,} VND")

    def display_info(self):
        print("Ngân hàng:", BankAccount.bank_name)
        print("Số tài khoản:", self.account_number)
        print("Tên chủ tài khoản:", self.account_name)
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")


def main():
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Giao dịch Nạp / Rút tiền")
        print("4. Cập nhật Tên chủ tài khoản")
        print("5. Đổi phí giao dịch hệ thống")
        print("6. Thoát chương trình")
        choice = input("Chọn chức năng (1-6): ")

        match choice:
            case "1":
                print("\n--- MỞ TÀI KHOẢN MỚI ---")
                while True:
                    acc_number = input("Nhập số tài khoản 10 chữ số: ")
                    if BankAccount.validate_account_number(acc_number):
                        break
                    print("Số tài khoản không hợp lệ!")
                    print("Số tài khoản phải gồm đúng 10 chữ số.")

                acc_name = input("Nhập tên chủ tài khoản: ")
                current_account = BankAccount(acc_number, acc_name)
                print("Mở tài khoản thành công!")
                print("Số tài khoản:", current_account.account_number)
                print("Tên chủ tài khoản:", current_account.account_name)

            case "2":
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản")
                    print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                else:
                    print("\n--- THÔNG TIN TÀI KHOẢN ---")
                    current_account.display_info()

            case "3":
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản")
                    continue

                print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
                print("1. Nạp tiền")
                print("2. Rút tiền")
                action = input("Chọn loại giao dịch (1-2): ")

                try:
                    amount = int(input("Nhập số tiền giao dịch: "))
                except ValueError:
                    print("Số tiền không hợp lệ")
                    continue

                if action == "1":
                    current_account.deposit(amount)
                elif action == "2":
                    current_account.withdraw(amount)

            case "4":
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản")
                    continue

                print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
                new_name = input("Nhập tên mới: ")
                old_name = current_account.account_name
                current_account.account_name = new_name
                if current_account.account_name != old_name:
                    print("Cập nhật thành công. Tên mới:", current_account.account_name)

            case "5":
                print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
                print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")
                try:
                    new_fee = int(input("Nhập phí giao dịch mới: "))
                except ValueError:
                    print("Phí giao dịch không hợp lệ")
                    continue

                BankAccount.update_transaction_fee(new_fee)
                print(f"Phí giao dịch hiện tại vẫn là {BankAccount.transaction_fee:,} VND")

            case "6":
                print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
                break

            case _:
                print("Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()