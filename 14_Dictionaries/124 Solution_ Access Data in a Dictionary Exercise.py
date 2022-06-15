artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist["first"] + " " + artist["last"]
print(full_name)

full_name2 = f"{artist['first']} {artist['last']}"  # ne ide dupli i single cak i ako je single unutar kljuca!!
print(full_name2)
