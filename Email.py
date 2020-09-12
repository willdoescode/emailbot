import smtplib
import urllib.request
import random


class Email:
    def __init__(self, cmail, password):
        self.cmail = cmail
        self.password = password
        self.smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        self.smtpObj.starttls()
        self.smtpObj.login(f'{cmail}', f'{self.password}')

    def send_mail(self, rec, subject, message):
        self.smtpObj.sendmail(f'{self.cmail}', f'{rec}', f'Subject: {subject}\n\n{message}')

    def spam(self, word_amount: int, spam_amount: int, rec: str):
        word_list = urllib.request.urlopen('http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain')
        words = word_list.read().decode().split('\n')
        for i in range(spam_amount):
            word = ' '.join(random.choices(population=words, k=word_amount))
            self.send_mail(rec=rec, subject=f'{" ".join(random.choices(population=words, k=3))}', message=word)

    def __str__(self):
        return self.cmail, self.password
