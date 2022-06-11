def vise_slova_u_rjeci(rjec):
    return {slovo.lower():rjec.lower().count(slovo) for slovo in rjec}

print(vise_slova_u_rjeci("ekspanzija"))
print(vise_slova_u_rjeci("DERVENTA"))
print(vise_slova_u_rjeci("EutaAnazija"))

def vise_slova_u_rjeci(rjec):
    return [len(rjec), {slovo:rjec.count(slovo) for slovo in rjec}]

print(vise_slova_u_rjeci("ekspanzija"))
print(vise_slova_u_rjeci("DERVENTA"))
print(vise_slova_u_rjeci("EutaAnazija"))