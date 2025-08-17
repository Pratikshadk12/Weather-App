# 🌤️ Weather App (Python)

A simple **Tkinter-based GUI Weather Application** built in Python. It fetches real-time weather data from the **OpenWeatherMap API** and displays temperature, humidity, weather description, and wind speed for any city.

Perfect for beginners to learn **Python GUI (Tkinter)**, **APIs (requests)**, and **JSON parsing**.

---

## 🚀 Features

* 🏙️ Enter a city and get real-time weather
* 🌡️ Displays temperature, feels-like, and humidity
* 🌬️ Shows wind speed
* 🖼️ Weather icons support (optional images)
* ❌ Error handling for invalid cities

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** (GUI)
* **Requests** (API calls)
* **Pillow (PIL)** for weather icons
* **Git & GitHub** for version control

---

## 📁 Folder Structure

```
weather-app/
│
├── icons/                  # Weather icons (optional)
│   ├── clear.png
│   ├── clouds.png
│   ├── rain.png
│   └── ...
│
├── weather_app.py          # Main Python program
│
├── README.md
└── .gitignore
```

---

## 🧩 Setup Instructions (VS Code)

### 1️⃣ Install Required Tools

* [Python](https://www.python.org/downloads/)
* [VS Code](https://code.visualstudio.com/)
* **Python Extension Pack** in VS Code
* [Git](https://git-scm.com/)

---

### 2️⃣ Install Dependencies

Open terminal in your project folder and run:

```bash
pip install requests pillow
```

---

### 3️⃣ Get API Key

* Sign up at [OpenWeatherMap](https://openweathermap.org/api)
* Generate a free **API key**
* Replace inside `weather_app.py`:

```python
api_key = "YOUR_API_KEY"
```

---

## 🖥️ How to Run the Project

From project root, run:

```bash
python weather_app.py
```

Enter any **city name** in the input box and press **Get Weather** 🌎.

---

## ⬆️ How to Push Code to GitHub

### 1️⃣ Create a New Repository on GitHub

* Go to **GitHub → New Repository** → Name: `weather-app`

### 2️⃣ Initialize Git and Push

```bash
git init
git add .
git commit -m "Initial commit - Weather App"
git branch -M main
git remote add origin https://github.com/your-username/weather-app.git
git push -u origin main
```

---

## 📌 Future Enhancements

* 📍 Add location-based weather (auto-detect city)
* 📊 Show 5-day forecast
* 🎨 Improved UI with custom themes
* 🔔 Add weather alerts

---

## 🙌 Author

Created by **Pratiksha** – 2nd Year AIML Student, Reva University
GitHub: [pratikshadk12](https://github.com/pratikshadk12)

---

## ⚠️ .gitignore Recommendation

Add a `.gitignore` file to exclude cache files:

```
__pycache__/
*.pyc
*.pyo
```

---

☁️ Happy Coding with Weather Data! 🌈

---
