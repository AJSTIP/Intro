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
    in_file = open('enc_passage.txt', 'r')  # Open the file in read mode
    result = convert(in_file)  # Pass the file object to the convert function
    print(result)  # Print the decoded text
    in_file.close()  # Close the file after reading

def convert(file):
    text = file.read()
    dec_text = ''
    
    # Iterate through each character in the text
    for ch in text:
        if ch.isspace():
            dec_text = dec_text + ch  # Preserve spaces
        elif ch in CODE:
            dec_text = dec_text + CODE[ch]  # Decode using the CODE dictionary
        else:
            dec_text = dec_text + ch  # Preserve characters not in CODE
    return dec_text

if __name__ == '__main__':
    main()