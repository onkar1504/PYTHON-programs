def main():

    #     [python ,ppa, lsp, angular]
    #fees= [12500,15000,21000,15500]

    fees = {"python":12500,"ppa":15000,"lsp":21000,"angular":15500}

    print(fees)

    print("please enter batch name:")
    batch=input()
    
    print("thaku for selecting batch:",batch)

    print("fees are :",fees[batch])
    
if __name__ == "__main__":
    main()