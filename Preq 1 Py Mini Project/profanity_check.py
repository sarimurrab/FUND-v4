import urllib.request


def read_file():
    header = open(r'C:\Users\SARIM\Desktop\FUND CODE\read_quotes.txt')
    content = header.read()

    list_temp = content.split()
    set_var = False
    for i in list_temp:
        response = urllib.request.urlopen(
            'http://www.wdylike.appspot.com/?q='+i)
        if(response.read() == b'true'):
            set_var = True
            break
    if(set_var == True):
        print("Profanity Detected")
    else:
        print("Not Detected")

        header.close()


read_file()
