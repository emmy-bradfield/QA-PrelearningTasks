def vowel_swapper(string):
    # ==============
    # Your code here
    new_string=string.replace('a', '1')
    string=new_string
    new_string=string.replace('e', '3')
    string=new_string
    new_string=string.replace('i', '!')
    string=new_string
    new_string=string.replace('o', 'ooo')
    string=new_string
    new_string=string.replace('O', '000')
    string=new_string
    new_string=string.replace('u','|_|')
    string=new_string
    return string
    # ==============

print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console
