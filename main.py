import atm

def main():
    tmp = []
    storage = {}
    loop = True
    print("Welcome to Ab ATM")
    while loop:
        print("Apa yang ingin anda lakukan:")
        print("1. Buka rekening")
        print("2. Masuk ke rekening yang sudah ada")
        print("3. Quit")
        decision = int(input(">> "))
        if decision == 1:
            tmpAkun = atm.atm()
            print(f"Akun berhasil dibuat, Id pelanggan anda adalah {tmpAkun.getId()}")
            tmpPin = input("Masukan Pin untuk akun anda: ")
            tmpAkun.setPin(tmpPin)
            tmp.append(tmpAkun)
            storage[tmpAkun.getId()] = tmpAkun
        elif decision == 2:
            atmId = int(input("Masukan Id pelanggan anda: "))
            if (atmId in storage.keys()):
                pin = input("Masukan Pin anda: ")
                tmpAkun = storage[atmId]
                while tmpAkun.verifyPin(pin):
                    print("Apa yang ingin anda lakukan:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Change Pin")
                    print("4. Check Balance")
                    print("5. Quit")
                    dec = int(input(">> "))
                    if dec == 1:
                        saldo = int(input("Saldo: "))
                        tmpAkun.deposit(pin, saldo)
                    elif dec == 2:
                        saldo = int(input("Saldo: "))
                        tmpAkun.withdraw(pin, saldo)
                    elif dec == 3:
                        newPin = int(input("new pin: "))
                        tmpAkun.changePin(pin, newPin)
                    elif dec == 4:
                        print(tmpAkun.checkBal(pin))
                    elif dec == 5:
                        break
                else:
                    print("Wrong pin")
            else:
                print("Account not found")
        elif decision == 3:
            loop = False



if __name__ == "__main__":
    main()