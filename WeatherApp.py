import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to get weather
def get_weather():
    city = city_entry.get()
    api_key = "03d56fc14e79e6461d85a83f43c5690b"   # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    if city.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]

        result = f"""
City: {city}
Temperature: {main['temp']}°C
Feels Like: {main['feels_like']}°C
Humidity: {main['humidity']}%
Weather: {weather['description'].title()}
Wind Speed: {wind['speed']} m/s
"""
        output_label.config(text=result, justify="left")

        # Update weather icon
        icon_name = weather["main"].lower()
        icon_path = f"icons/{icon_name}.png"

        try:
            img = Image.open(icon_path)
            img = img.resize((80, 80))
            weather_icon = ImageTk.PhotoImage(img)
            icon_label.config(image=weather_icon)
            icon_label.image = weather_icon
        except:
            icon_label.config(image="", text="(No Icon)")

    else:
        messagebox.showerror("Error", "City not found! Please try again.")

# Tkinter GUI setup
root = tk.Tk()
root.title("🌤️ Weather App")
root.geometry("420x500")
root.resizable(False, False)

# Heading
heading = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"))
heading.pack(pady=10)

# Input field
city_entry = tk.Entry(root, width=30, font=("Arial", 14))
city_entry.pack(pady=10)

# Button
search_btn = tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"), command=get_weather)
search_btn.pack(pady=10)

# Weather Icon
icon_label = tk.Label(root, text="", font=("Arial", 12))
icon_label.pack(pady=10)

# Output label
output_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
output_label.pack(pady=20)

# Run the app
root.mainloop()
