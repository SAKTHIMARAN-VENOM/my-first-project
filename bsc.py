'''Takes a city name from the user.

Calls a public API to get the weather (e.g. OpenWeatherMap).

Calls another API to get currency exchange rate (e.g. USD to INR).

Prints a neat summary in the terminal.

Optionally saves the data into a local file (CSV/JSON) for history.'''
import requests
import time
import csv
from termcolor import colored
import pandas  as pd
import os
def show_weather(city):
    url=f"http://api.weatherapi.com/v1/current.json?key=562c0a0ab53d43f38e010645252509&q={city}&aqi=yes"
    details= requests.get(url)
    if details.status_code==200:
        print("retriving the data....")
        time.sleep(5)
        details2= details.json()
        current= details2.get('current',{})
        condition=current.get('condition',{})
        a=condition.get('text')
        print(f"IN {city} TODAY TEMPRATURE: {current.get('temp_c')}°C")
        print(colored(f"IN {city} TODAY WEATHER: {condition.get('text')} ","green"))
        return a
def show_CER(country):
    url="http://api.exchangerate.host/live?access_key=fcfe3654959aa8585169d70e5779cd17"
    url2="https://v6.exchangerate-api.com/v6/e4f65190f22cfb2902bf89e6/codes"
    details=requests.get(url2).json()
    for i in details.get('supported_codes'):
        if i[1]==country:
            var1="USD"+i[0]
    details=requests.get(url)
    details2=details.json()
    usdtoind=details2.get('quotes')
    rate=usdtoind.get(var1)
    print(f"THE USD TO INR EXCHANGE IS: {usdtoind.get(var1)}")
    return rate
def show_summary(city,country):
    print("********************************")
    a=show_weather(city)
    b=show_CER(country)
    save_data(country,b,a,city)
    print("**********************************")
def save_data(country,rate,cityweather,city):
    with open('your_file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['COUNTRY NAME', 'rate', 'CITY','CITY WEATHER'])
        writer.writerow([country, f"{rate:.2f}",city,cityweather])
        print("DATA HAS BEEN SUCESSFULLY STORED")
def main():
    city=input("enter the city to check the weather: ")
    country=input("Enter the country name to convert form USD: ")
    show_summary(city,country)
    df=pd.read_csv('your_file.csv')
    print(df.head())
    os.startfile(filepath="C:/Python/your_file.csv")

if __name__=="__main__":
    main()
 