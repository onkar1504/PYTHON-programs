import threading,_thread
amount = 0

def Counter(fun,lock):
    fun(lock)

def Creadit(lock):
    Value = int(input("enter amount to be creadit:"))
    lock.acquire()
    global amount
    amount += Value
    print("balance is",amount)
    lock.relese()

def Debit(lock):
    Value = int(input("enter amount to be withdraw:"))
    lock.acquire()
    global amount
    if amount < Value:
        print("unable to withdraw")
    else:
        amount += Value
        print("amount to witharw",Value)
        print("balance is",Value)

    lock.release()

def main():
    lock =threading.Lock()

    t1=threading.Thread(target=Counter,args=(Creadit,lock,))
    t2=threading.Thread(target=Counter,args=(Debit,lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()