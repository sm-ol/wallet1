from wallet import Wallet, ExchangeAccount, WalletError

def main():
    user_name_input = input("Добро пожаловать! Введите ваше имя для создания аккаунта: ").strip()
    if not user_name_input:
        user_name_input = "DefaultUser"
        
    account = ExchangeAccount(username=user_name_input)
    print(f"Создан аккаунт для пользователя: {account.username}")
    
    while True:
        operation = input("Введите операцию (СОЗДАТЬ, ПОПОЛНИТЬ, СПИСАТЬ, БАЛАНС, ВЫХОД): ").strip().upper()
        
        try:
            if operation == "ВЫХОД":
                break
                
            elif operation == "СОЗДАТЬ":
                name = input("Введите имя нового кошелька: ").strip()
                balance = float(input("Введите стартовый баланс (по умолчанию 0): ") or 0)
                account.create_rub_wallet(name, balance)
                
            elif operation == "ПОПОЛНИТЬ":
                name = input("Введите имя кошелька: ").strip()
                wallet = account.get_wallet(name)
                amount = float(input("Введите сумму пополнения: "))
                wallet.top_up(amount)
                print(f"Баланс кошелька '{name}': {wallet.balance} {wallet.currency}")
                
            elif operation == "СПИСАТЬ":
                name = input("Введите имя кошелька: ").strip()
                wallet = account.get_wallet(name)
                amount = float(input("Введите сумму списания: "))
                wallet.spend(amount)
                print(f"Баланс кошелька '{name}': {wallet.balance} {wallet.currency}")
                
            elif operation == "БАЛАНС":
                name = input("Введите имя кошелька: ").strip()
                wallet = account.get_wallet(name)
                print(f"Баланс кошелька '{name}': {wallet.balance} {wallet.currency}")
                
            else:
                print("Неизвестная команда. Попробуйте еще раз.")
                
        except WalletError as e:
            print(f"Ошибка: {e}")
        except ValueError:
            print("Ошибка: Введено неверное числовое значение")

if __name__=="__main__":
    main()


