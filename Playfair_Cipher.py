import string

letters = string.ascii_letters[0:26]

def encrypt(key):
    
    dup_letters = list(letters)

    for char in key:
        dup_letters.remove(char)
    
    dup_letters.remove("j")
    key_length = len(key)
    letters_length = len(dup_letters)
    key_index = 0
    letter_index = 0
    matrix = []
    
    for i in range(5):
        l = []
        for j in range(5):
            if(key_index < key_length):
                l.append(key[key_index])
                key_index += 1
            elif(letter_index < letters_length):
                l.append(dup_letters[letter_index])
                letter_index += 1
        matrix.append(l)    
    
    cipher_text = ""
    
    plain_text = input("\nEnter the plain text : ")
    modified_plain_text = "".join(plain_text.split(" "))
    
    plain_matrix = []
    
    plain_index = 0
    
    while(plain_index != len(modified_plain_text)):
        
        l = []
        l.append(modified_plain_text[plain_index])
        plain_index += 1
        
        if(plain_index < len(modified_plain_text)):
            if(modified_plain_text[plain_index] == l[0]):
                l.append('x')
            else:
                l.append(modified_plain_text[plain_index])
                plain_index += 1
        
        plain_matrix.append(l)
        
    if(len(plain_matrix[len(plain_matrix) - 1]) == 1):
        plain_matrix[len(plain_matrix) - 1].append('x')
    
    cipher_index = 0
    
    while(cipher_index != len(plain_matrix)):
        
        one = plain_matrix[cipher_index][0]
        two = plain_matrix[cipher_index][1]
        
        row1 = 0
        col1 = 0
        
        row2 = 0
        col2 = 0
        
        for i in range(5):
            for j in range(5):
                if(matrix[i][j] == one):
                    row1 = i
                    col1 = j
                elif(matrix[i][j] == two):
                    row2 = i
                    col2 = j
        
        if(row1 == row2):
           cipher_text += matrix[row1][(col1 + 1)%5] 
           cipher_text += matrix[row2][(col2 + 1)%5]
           
        elif(col1 == col2):
            cipher_text += matrix[(row1 + 1)%5][col1] 
            cipher_text += matrix[(row2 + 1)%5][col2]
            
        else:
            cipher_text += matrix[row1][col2] 
            cipher_text += matrix[row2][col1]
            
        cipher_index += 1
        
    print("The Cipher Text is : " + cipher_text)
    
def decrypt(key):
    
    dup_letters = list(letters)
    
    for char in key:
        dup_letters.remove(char)
    
    dup_letters.remove("j")
    key_length = len(key)
    letters_length = len(dup_letters)
    key_index = 0
    letter_index = 0
    matrix = []
    
    for i in range(5):
        l = []
        for j in range(5):
            if(key_index < key_length):
                l.append(key[key_index])
                key_index += 1
            elif(letter_index < letters_length):
                l.append(dup_letters[letter_index])
                letter_index += 1
        matrix.append(l)  
    
    cipher_text = input("\nEnter the cipher text : ")
    modified_cipher_text = "".join(cipher_text.split(" "))
    
    plain_text = ""
    
    cipher_matrix = []
    
    cipher_index = 0
    
    while(cipher_index != len(modified_cipher_text)):
        
        l = []
        l.append(modified_cipher_text[cipher_index])
        cipher_index += 1
        
        if(cipher_index < len(modified_cipher_text)):
            if(modified_cipher_text[cipher_index] == l[0]):
                l.append('x')
            else:
                l.append(modified_cipher_text[cipher_index])
                cipher_index += 1
        
        cipher_matrix.append(l)
        
    if(len(cipher_matrix[len(cipher_matrix) - 1]) == 1):
        cipher_matrix[len(cipher_matrix) - 1].append('x')
    
    plain_index = 0
    
    while(plain_index != len(cipher_matrix)):
        
        one = cipher_matrix[plain_index][0]
        two = cipher_matrix[plain_index][1]
        
        row1 = 0
        col1 = 0
        
        row2 = 0
        col2 = 0
        
        for i in range(5):
            for j in range(5):
                if(matrix[i][j] == one):
                    row1 = i
                    col1 = j
                elif(matrix[i][j] == two):
                    row2 = i
                    col2 = j
        
        if(row1 == row2):
           plain_text += matrix[row1][col1 - 1] 
           plain_text += matrix[row2][col2 - 1]
           
        elif(col1 == col2):
            plain_text += matrix[row1 - 1][col1] 
            plain_text += matrix[row2 - 1][col2]
            
        else:
            plain_text += matrix[row1][col2] 
            plain_text += matrix[row2][col1]
            
        plain_index += 1
    
    print("The Plain Text is : " + plain_text)
        
choice = 0
key = 0

while(True):
    
    choice = int(input("\n\n********MENU********\n\n1.Encrypt\n2.Decrypt\n3.Exit\n\nEnter your choice : "))
    
    if(choice == 1):
        
        key = input("\nEnter the key : ")
        encrypt(key)
        
    elif(choice == 2):
        
        key = input("\nEnter the key : ")
        decrypt(key)
        
    elif(choice == 3):
        break