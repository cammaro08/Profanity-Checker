import urllib

def read_text():
    doc = open("D:\Full_stack_files\Python\check_doc.txt")
    contents_doc = doc.read()
    #print(contents_doc)
    profanity_check(contents_doc)
    doc.close()

def profanity_check(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    if "true" in output:
        print("you swear alot huh...")
    elif "false" in output:
        print("You are such a sweetheart")
    else:
        print("couldnt check :o")
    

read_text()



