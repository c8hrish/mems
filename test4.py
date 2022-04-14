import sys
if sys.version_info[0] >= 3:
    import tkinter as tk
else:
    import Tkinter as tk


class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.dict = {'Asia': ['Japan', 'China', 'Malaysia'],
                     'Europe': ['Germany', 'France', 'Switzerland']}

        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)

        self.variable_a.trace('w', self.update_options)

        self.optionmenu_a = tk.OptionMenu(self, self.variable_a, *self.dict.keys())
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, '')

        self.variable_a.set('Asia')

        self.optionmenu_a.pack()
        self.optionmenu_b.pack()
        self.pack()


    def update_options(self, *args):
        countries = self.dict[self.variable_a.get()]
        self.variable_b.set(countries[0])

        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')

        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: self.variable_b.set(nation))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.mainloop()

from tkinter import *
root = Tk()

def update_options_B(*args):
    countries = data[variable_a.get()]
    variable_b.set(countries[0])
    menu = optionmenu_b['menu']
    menu.delete(0, 'end')
    for country in countries:
        menu.add_command(label=country, command=lambda nation=country: variable_b.set(nation))

def update_options_C(*args):
    cities = data2[variable_b.get()]
    variable_c.set(cities[0])
    menu = optionmenu_c['menu']
    menu.delete(0, "end")
    for city in cities:
        menu.add_command(label=city, command=lambda nation=city: variable_c.set(nation))


data = {'Asia': ['Japan', 'China', 'Malasia'],'Europe': ['Germany', 'France', 'Switzerland'], 'Africa': ['Nigeria', 'Kenya', 'Ethiopia']}
data2 = {'Japan': ["jiustu", "kamikaz", "Tokyo"], 'China': ["Shaigon", "Hong Kong"], 'Malasia': ["tiramusto", "quala lopour"], 'Germany': ["Dusseldorf", "Berlin", "Hambourg"], 'France': ["Paris", "Lille"], 'Switzerland': ["Biern", "Bonn"], 'Nigeria': ['Nigeria1', 'Nigeria3'], 'Kenya': ["Keny West", "Notorious"], 'Ethiopia': ["Etanpi", "Neeandertaal"]}
variable_a = StringVar()
variable_b = StringVar()
variable_c = StringVar()

variable_a.trace('w', update_options_B)
variable_b.trace('w', update_options_C)
optionmenu_a = OptionMenu(root, variable_a, *data.keys())
optionmenu_b = OptionMenu(root, variable_b, '')
optionmenu_c = OptionMenu(root, variable_c, '')

variable_a.set('Asia')
optionmenu_a.pack()