def permutation():
    count = 0
    words = str(input("enter the word \n"))
    print(len(words))
    b = [words[i] for i in range(0,len(words),1)]
    q = len(b)
    vowels = ['a','e','i','o','u']
    for i in range(len(b)):
        for j in range(len(vowels)):
            if (b[i] == vowels[j]):
                print("found")
                count = count+1
                print("total no of commom word ",count)
                sp  = q-count
                t_sp = sp+1
                sp_ct = t_sp - count
                print("total space",t_sp)
                    
            else:
                print("aborted...............")
            
    if t_sp ==0:
        return "no space"
    
    else:
        fact_sp = 1
        for k in range(1,t_sp + 1):
            if t_sp == 0:
                print("only one way")
            else:
                fact_sp = fact_sp*k
            print(fact_sp)
    
    
    
        fact_sp_ct = 1
    
        for l in range(1,sp_ct+1):
        
            sp_ct = t_sp - count
            if sp_ct<0:
                print("not enough space")
            elif sp_ct == 0:
                print("word cannot be form")
            else:
                fact_sp_ct = fact_sp_ct * l 
            print("sp - ct.........=",fact_sp_ct)
        
        
        rem_wd= len(words)- count
        fact_rem_wd = 1
        print(rem_wd)
        for m in range(1,rem_wd+1):
            fact_rem_wd = fact_rem_wd*m
        print("no... of remaining word fectorial is.....\n ",fact_rem_wd)
    
    
    tot_way= (fact_sp/fact_sp_ct)*fact_rem_wd
    return tot_way
    
    
                
    
    
    
        
                
