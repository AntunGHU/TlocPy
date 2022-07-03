# 6'44''
# try and except javljaju gresku ali cod ide dalje!!

from gc import collect


try:
    foobar
except NameError as err:
    print(err)          # name 'foobar' is not defined
print("after the try")  # after the try

# pokusavati hvatati svaku gresku se ne preporuca nego specificirati

try:
    colt
# except:         # prihvaca svaku vrstu err-a
except NameError:    # prihvaca samo name-vrstu err-a i samo tada ide print
    print("you tried variable that wasn't declared")
    

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
d={"name":"Ricky"}
print(get(d,"name"))        # Ricky
print(get(d,"city"))        # None

    
