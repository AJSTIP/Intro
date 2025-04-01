CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v', 
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s', 
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p', 
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m', 
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j', 
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g', 
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d', 
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a', 
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<', 
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'='}

def main():
    # Open the file in read mode
    in_file = open('passage.txt', 'r')
    result = convert(in_file)  # Pass the file object to the convert function
    in_file.close()  # Close the file after reading
    print(result)  # Print the encoded text

    out_file = open('enc_passage.txt', 'w')  # Open the file in write mode
    out_file.write(result)  # Write the encoded text to the file
    out_file.close()  # Close the output file

def convert(file):
    # Read the content of the file
    text = file.read()
    enc_text = ''
    
    # Iterate through each character in the text
    for ch in text:
        if ch.isspace():
            enc_text = enc_text + ch  # Preserve spaces
        elif ch in CODE:
            enc_text = enc_text + CODE[ch]  # Encode using the CODE dictionary
        else:
            enc_text = enc_text + ch  # Preserve characters not in CODE
    return enc_text

if __name__ == '__main__':
    main()