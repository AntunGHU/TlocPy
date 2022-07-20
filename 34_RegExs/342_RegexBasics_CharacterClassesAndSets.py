# 4'22

# * Klases and Sets
# [aeiou]   Ako stavim "aeiou" trazi samo "aeiou" kombinaciju ali ako stavim [aeiou] sve kombinacije "a", "ai", "aou" itd su ok a ako [aeiou]{2} svaka kombinacija moze 2x.
# [a-z] bilo koje slovo malo od a do z; [a-f] bilo koje od a do f
# [A-Z] bilo koje veliko slovo kao i [A-F]
# [A-Z]{2,} bilo koje veliko slovo 2 put i vise npr. ="PURPLE" ali ne i "A"
# [0-9]{2,} bilo koje 2 znamenke i vise = 4154129876 = 75 ali ne i 3
# [0-9a-z] kombinacija gornjih
# [^k] sva slova osim k ili svega sto ga sljedi npr[^kaeio] sva osim kaeio
