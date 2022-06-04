def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))
    
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
