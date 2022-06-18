def vowel_swapper(string):
    # ==============
    # Your code here
    new_string=string.replace('A', '1')
    string=new_string
    new_string=string.replace('E', '3')
    string=new_string
    new_string=string.replace('I', '!')
    string=new_string
    new_string=string.replace('O', '000')
    string=new_string
    new_string=string.replace('U','|_|')
    string=new_string
    return string
    # ==============

print(vowel_swapper("aAa eEe iIi oOo uUu")) # Should print "a/\a e3e i!i o000o u\/u" to the console
print(vowel_swapper("Hello World")) # Should print "Hello Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "Ev3rything's Av/\!lable" to the console
