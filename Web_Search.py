import webbrowser as wb
import string
#from Virtual_Assistant import 

class Websearch():
    
    def open_chrome():
        wb.open_new("https://www.google.com/")

    def SearchChrome(s):
        newS = s.replace(' ', '+')
        q = "https://www.google.com/search?q=" + newS + '&'
        wb.open_new(q)

    def OpenMail():
        wb.open_new("https://mail.google.com/mail/u/1/#inbox")
   


