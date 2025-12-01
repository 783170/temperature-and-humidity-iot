import smtplib

def sendEmail (tempC):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("raspberry64bit@gmail.com","nuzhwsvclktmbfeb")
    message = """It's too warn, temp reading at %s degrees Celsius""" % (tempC)
    s.sendmail("raspberry64bit@gmail.com","raspberry64bit@gmail.com",message)
    s.quit
