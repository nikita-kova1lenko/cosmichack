import folium
import os
from tkinter import *

x = "OpenStreetMap"

def vibrat1():
    global x
    x = "OpenStreetMap"
    window.destroy()
def vibrat2():
    global x
    x = "CartoDB dark_matter"
    window.destroy()
def vibrat3():
    global x
    x = "Stamen Toner"
    window.destroy()
def vibrat4():
    global x
    x = "Stamen Terrain"
    window.destroy()











window = Tk()
window.geometry("200x170")
labl = Label(window, text="В какой теме вы хотите просматривать карту?")
butt1 = Button(window,text="В стандартной", bg="cyan", command=vibrat1)
butt2 = Button(window,text="темная", bg="cyan", command=vibrat2)
butt3 = Button(window,text="монохром", bg="cyan", command=vibrat3)
butt4 = Button(window,text="Физическая", bg="cyan", command=vibrat4)
butt1.pack(padx=1,pady=1)
butt2.pack(padx=1,pady=2)
butt3.pack(padx=1,pady=3)
butt4.pack(padx=1,pady=4)





window.mainloop()


map = folium.Map(location=[64.02339283495208, 91.97043892854606], zoom_start = 3, tiles=x)

plesetsc = "<img src='1234.jpg' alt='Описание изображения' width=200><p><strong>Космодром Плесецк</strong><br>17 марта 1966 года произошел первый запуск, Произведено свыше 3000 полетов<br>Работает и сегодня<br>62.92785, 40.5748416</p>"
baikonur = "<img src='baikonur.jpg' alt='Описание изображения' width=200><p><strong> Космодром Байконур</strong><br>15 мая 1957 года — запуск первой ракеты Р-7 с космодрома<br> работает по сей день, почти 5000 запусков<br>45.6276817, 63.3035766</p>"
vostochniy = "<img src='vostochiy.jpg' alt='Описание изображения' width=200><p><strong>Космодром Восточный</strong><br>в данное время работает <br>было произведено 10 запусков, 51.850073751,128.35530296</p>"
kapustin = "<img src='kapustin.jpeg' alt='описание изображения' width=200><p><strong>Полигон Капустин Яр</strong><br>18 октября 1947 года-первый старт, произведено 19 стартов, работает по сей день, 48.5760320, 45.760823</p>"
yasniy = "<img src='yasniy.jpeg' alt='описание изображения' width=200><p><strong>Пусковая база Ясный</strong><br>12 июля 2006-первый запуск,было произведено 10 запусков<br>на данный момент работает<br>51.094365, 59.842400</p>"




folium.Marker(location=[62.92785553227608, 40.57484161888088], popup =plesetsc, icon=folium.Icon(color = 'gray')).add_to(map)
folium.Marker(location=[51.850073751155534, 128.35530296707194], popup =vostochniy, icon=folium.Icon(color = 'gray')).add_to(map)
folium.Marker(location=[45.62768179473454, 63.30357664082761], popup =baikonur, icon=folium.Icon(color = 'gray')).add_to(map)
folium.Marker(location=[51.09436503089844, 59.842400822099265], popup =yasniy, icon=folium.Icon(color = 'gray')).add_to(map)
folium.Marker(location=[48.576032025424425, 45.76082302161889], popup =kapustin, icon=folium.Icon(color = 'gray')).add_to(map)
map.save("Карты Космодромов России.html")
os.startfile("Карты Космодромов России.html")