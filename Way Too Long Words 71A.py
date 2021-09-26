for _ in range(int(input())):
    string = input()
    print(string[0]+str(len(string)-2)+string[-1]) if len(string)> 10 else print(string) 
