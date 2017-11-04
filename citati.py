from BeautifulSoup import BeautifulSoup
import urllib
import random
import Tkinter

def quotes():
    marriageUrl = 'http://quotes.yourdictionary.com/theme/marriage/'
    marriageHtml = urllib.urlopen(marriageUrl).read()
    soupHelp = BeautifulSoup(marriageHtml)

    quotes = soupHelp.findAll('p', attrs={'class': 'quoteContent'})
    quote_list = []
    for quote in quotes:
        quote_list.append(quote.text)
    generator = random.sample(quote_list, 5)
    every_quote_in_new_line = ""
    for quote in generator:
        every_quote_in_new_line += quote + "\n\n"
    generated_quotes.config(text=every_quote_in_new_line)

frame = Tkinter.Tk()
frame.geometry("1500x300")
frame.title("Dayly dose of quotes")
greeting = Tkinter.Label(frame, text="Generate yourself your dayly dose of quotes...\n\n")
greeting.pack()

get_quotes_button = Tkinter.Button(frame, text="Get quotes", command = quotes)
get_quotes_button.pack()
place_holder = Tkinter.Label(frame, text="")
place_holder.pack()

generated_quotes = Tkinter.Label(frame, text="")
generated_quotes.pack()

frame.mainloop()