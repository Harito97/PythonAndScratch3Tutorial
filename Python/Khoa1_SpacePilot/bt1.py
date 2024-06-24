'''
Bai tap: 
1. Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
How I wonder what you are! 
Up above the world so high,   		
Like a diamond in the sky. 
Twinkle, twinkle, little star, 
How I wonder what you are
'''

def format_string(string:str):
    result = ''
    for character in string:
        if character.isupper() and character != 'I':
            result = result + '\n' + character
        else:
            result += character
    return result

if __name__ == "__main__":
    input_string = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
    result_format = format_string(input_string)
    print(result_format)