def main():

    #     [python ,ppa, lsp, angular]
    #     [0  ,  1 ,    2 ,     3   ]
    fees= [12500,15000,21000,15500]
    print(fees)

    print("please enter batch name:")
    batch=input()
    
    print("thaku for selecting batch:",batch)

    if batch == "ppa":
        print("fees are:",fees[1])
    elif batch =="lsp":
        print("fees are:",fees[2])
    elif batch =="python":
        print("fees are:",fees[0])
    elif batch =="angular":
        print("fees are:",fees[3])
    else:
        print("ther is no such batch like this")
    
if __name__ == "__main__":
    main()