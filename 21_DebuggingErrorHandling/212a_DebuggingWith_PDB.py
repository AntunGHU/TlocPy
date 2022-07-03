# 10'13''
# pdb unutar funkcija starta tek njenim izvršenjem!!

def add_numbers(a,b,c,d):
    import pdb; pdb.set_trace() # -> return a+b+c+d
                                # (Pdb) p a     # provjera kombinacije, jedan i vise razmak ali ni jedan ne radi i daje error
                                # 3
    print(a+b+c+d)                            
    return a+b+c+d
    
add_numbers(3,4,5,6)

# ako se varijable poklapaju imenomsa komandama pdb-ea do vrijednosti varijable mozemo doci koristenjem kombinacije p c (ili kako se vec poklapajuca varijabla zove)