import tkinter
import pyshorteners


window = tkinter.Tk()

window.title('URl Shortener')

window.geometry('400x250')

window.config(bg = '#8EE4AF')

def shortenURL():
    #create instance of shortner class
    shortener = pyshorteners.Shortener()
    #shorten text as short_url
    short_url = shortener.tinyurl.short(longurl_entry.get())
    
    shorturl_entry.insert(0, short_url)


#Labels initialized
longurl_label = tkinter.Label(window, text = 'Enter Long URL', bg='#8EE4AF')
longurl_entry = tkinter.Entry(window)

shorturl_label = tkinter.Label(window, text = 'Shortened URL', bg='#8EE4AF')
shorturl_entry = tkinter.Entry(window)

shortenurl_button = tkinter.Button(window, text='Shorten URl',bg='#8EE4AF', command = shortenURL)

#Labels placed on window(options = grid, place, pack)
longurl_label.pack()
longurl_entry.pack()

shorturl_label.pack()
shorturl_entry.pack()

shortenurl_button.pack()


window.mainloop()