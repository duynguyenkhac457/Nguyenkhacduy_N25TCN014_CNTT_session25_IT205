class NetflixAccount:
    """
    NetflixAccount represents a user account in the Netflix system.
    Demonstrates Encapsulation, Static Method, Class Method, and Instance Method.
    """

    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email: str):
        self.email = email
        self.__password = None      # private attribute (name mangling)
        self.__plan = "Basic"       # private attribute (name mangling)
        self.profiles = []

    @property
    def password(self):
        """
        Property for password (read access).
        Always returns masked value for security.
        """
        return "********"

    @password.setter
    def password(self, new_password: str):
        """
        Setter for password.
        Enforces minimum length security rule.
        """
        if len(new_password) < 6:
            raise ValueError("Password is too short")
        self.__password = new_password

    @property
    def plan(self):
        """
        Read-only property for subscription plan.
        Prevents external modification.
        """
        return self.__plan

    @staticmethod
    def validate_email(email: str):
        """
        Static method to validate email format.
        Does not depend on class or instance state.
        """
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit: int):
        """
        Class method to update global Netflix profile policy.
        Affects all existing and future accounts.
        """
        if new_limit <= 0:
            print("Giới hạn profile không hợp lệ")
            return
        cls.max_profiles = new_limit

    def add_profile(self, profile_name: str):
        """
        Instance method to add a viewer profile.
        Respects global max_profiles policy.
        """
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
            return
        self.profiles.append(profile_name)
        print(f"Đã thêm profile: {profile_name}")

    def upgrade_plan(self, new_plan: str):
        """
        The only valid way to change subscription plan.
        """
        allowed_plans = ["Basic", "Standard", "Premium"]
        if new_plan not in allowed_plans:
            print("Gói cước không hợp lệ")
            return
        self.__plan = new_plan
        print(f"Nâng cấp gói cước thành công: {new_plan}")

    def display_info(self):
        """
        Display account information with masked password.
        """
        print("Email:", self.email)
        print("Password:", self.password)
        print("Plan:", self.plan)
        print("Profiles:", self.profiles)


def main():
    current_account = None

    while True:
        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Đăng ký tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Thêm người xem")
        print("4. Nâng cấp gói cước")
        print("5. Cập nhật chính sách Netflix")
        print("6. Thoát chương trình")
        choice = input("Chọn chức năng (1-6): ")

        match choice:
            case "1":
                email = input("Nhập email: ")
                if not NetflixAccount.validate_email(email):
                    print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")
                    continue

                account = NetflixAccount(email)

                while True:
                    try:
                        pwd = input("Nhập mật khẩu: ")
                        account.password = pwd
                        break
                    except ValueError as e:
                        print(e)

                current_account = account
                print("Đăng ký tài khoản thành công!")

            case "2":
                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                    continue
                current_account.display_info()

            case "3":
                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                    continue
                name = input("Nhập tên profile: ")
                current_account.add_profile(name)

            case "4":
                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                    continue
                print("Các gói: Basic, Standard, Premium")
                plan = input("Nhập gói muốn nâng cấp: ")
                current_account.upgrade_plan(plan)

            case "5":
                try:
                    new_limit = int(input("Nhập giới hạn profile mới: "))
                    NetflixAccount.update_max_profiles(new_limit)
                    print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành {NetflixAccount.max_profiles}")
                except ValueError:
                    print("Giá trị không hợp lệ")

            case "6":
                print("Cảm ơn bạn đã sử dụng Netflix Account Manager!")
                break

            case _:
                print("Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()