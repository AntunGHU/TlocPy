# 8'07

# Quantifers
+	    One or more
{3}	    Exactly x times.  {3} - 3 times
{3, 5}	Three to five times
{4, }	Four or more times
*	    Zero or more times
?	    Once or none(optional)

# k     svi k
# k\w   like kittens kitty (ke ki ki)
# k\w+  like kittens kitty (ke kittens kitty)
# \sk\w+    _kittens _kitty
# \w\w\w\w\w = \w{5} hello world aaabbbccc (aaabb)
# \w{9} aaabbbccc
# \d{3} \d{3}-\d{4} = 415 412-9876
# ab*c = aaabbbccc (abbbc) = aaabccc (abc) = aaaccc (ac)
# ab*c*d = aaabbbcccdd (abbbcccd)
# kitens = kitens; kitens? = kiten = kitens
# \d{3} \d{3}-?\d{4} = 415 412-9876 = 415 4129876
