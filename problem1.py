def check_anagram (a:str,b:str):
    if len(a)==len(b):
        for i in (set(a.lower())):
            if a.count(i)!=b.count(i):
                return False
        else:
                return True
               
    else:
        return False
    
print(check_anagram( a=input("So`z kiriting: "), b=input("So`z kiriting: ")))