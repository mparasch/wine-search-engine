# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:19:56 2020

@author: Matt
"""

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import time

import tkinter as tk

def complete_msg():
    msg = tk.Tk()
    msg.geometry("200x100")
    msg.resizable(0, 0)
    tk.Label(msg, text = 'The report is completed!').place(msg, rely = 0.5, relx = 0.5)
    msg.mainloop()
    
def create_data(rating_, price_):
    data = []
    
    for n in range(1,12):
        URL = 'https://www.wine.com/list/wine/7155/' + str(n) + '?pricemax=' + price_ + '&ratingmin=' + rating_
        
        sauce = urllib.request.urlopen(URL)
        
        soup = BeautifulSoup(sauce, 'lxml')
        
        items = soup.find_all('li', {'class', 'prodItem'})
        
        for i in items:
            name = i.find('span', {'class', 'prodItemInfo_name'})['title']
            wine_type = i.find('span', {'class', 'prodItemInfo_varietal'}).text
            origin = i.find('span', {'class', 'prodItemInfo_originText'}).text
            rating = i.find('span', {'class', 'averageRating_average'}).text
            reviews = i.find('span', {'class', 'averageRating_number'}).text
            sale_price = i.find('span', {'class', 'productPrice_price-regWhole'}).text
            savings = i.find('span', {'class', 'productPrice_savings-amount'}).text
            savings_percent = i.find('span', {'class', 'productPrice_savings-percentage'}).text
            
            ind_lst = [name, wine_type, origin, rating, reviews, sale_price, savings, savings_percent]
            data.append(ind_lst)
    
    df = pd.DataFrame(data, columns = ['Name', 'Wine_type', 'Origin', 'Rating', 'Reviews', 'Sale_Price', 'Savings_Amount', 'Savings_Percentage'])
    
    tm = time.localtime()
    tm_year = tm[0]
    tm_month = tm[2]
    tm_day = tm[3]
    
    title = 'Wine_Rating-' + rating_ + '_Price-' + price_ + '_' + str(tm_year) + str(tm_month) + str(tm_day)
    
    df.to_csv(title + '.csv', encoding="utf-8-sig")
    
    complete_msg()

root = tk.Tk()
root.geometry("400x200")
root.resizable(0,0)

back = tk.PhotoImage(file = 'wine_graphic.png')
tk.Label(root, image = back).place(x = 0, y = 0, relwidth = 1, relheight = 1)

label1 = tk.Label(root, text = 'Select Minimum Rating (0-100) : ')
label1.place(relx = 0.1, rely = 0.1, height = 30)

rating_tk = tk.StringVar(root)
rating_tk.set('90')

min_rating_tk = tk.OptionMenu(root, rating_tk, *list(range(0,105,5)))
min_rating_tk.place(relx = 0.6, rely = 0.1)

label2 = tk.Label(root, text = 'Select Maximum Price (10-100) : ')
label2.place(relx = 0.1, rely = 0.3, height = 30)

price_tk = tk.StringVar(root)
price_tk.set('30')

max_price_tk = tk.OptionMenu(root, price_tk, *list(range(10,105)))
max_price_tk.place(relx = 0.6, rely = 0.3)

get_data = tk.Button(root, text = 'Create Wine List', command = lambda: create_data(rating_tk.get(), price_tk.get()))
get_data.place(anchor = 'center', relx = 0.5, rely = 0.6, height = 40)

root.mainloop()
