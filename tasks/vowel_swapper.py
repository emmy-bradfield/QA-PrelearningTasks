def vowel_swapper(string):
    # ==============
    # Your code here
    string.replace('a', '4')
    string.replace('e', '3')
    string.replace('i', '!')
    string.replace('o', 'ooo')
    string.replace('O', '000')
    string.replace('u', '|_|')
    # ==============

print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console
