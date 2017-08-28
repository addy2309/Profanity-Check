from urllib import request, parse

def read_file():
    fhand = open(r"C:\Users\Aditya\Documents\Codes\2\cursewords.txt")
    file_content = fhand.read()
    #print (file_content)
    fhand.close()
    profanity_check(file_content)

def profanity_check(input_to_check):
    url = "http://www.wdylike.appspot.com/?q="
    url = url + parse.quote(input_to_check)
    req = request.urlopen(url)
    answer = req.read()
    #print(answer)
    req.close()

    if b"true" in answer:
        print ("Profanity Alret!!!")
    else:
        print ("Nothing to worry")


read_file()
