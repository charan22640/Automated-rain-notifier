
## 🌧️ Automated Rain Notifier  

### 📌 Project Overview  
**Automated Rain Notifier** is a Python-based service that fetches weather data from OpenWeather API and sends SMS alerts via Twilio when rain is expected. This helps users stay prepared for rainy conditions in their location.  

---

### 🚀 Features  
✅ Fetches real-time weather data using the OpenWeather API  
✅ Identifies upcoming rain conditions  
✅ Sends SMS alerts via Twilio to notify users  
✅ Uses environment variables to keep credentials secure  

---

### 🛠️ Installation & Setup  

#### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/your-username/automated-rain-notifier.git
cd automated-rain-notifier
```

#### 2️⃣ Create a Virtual Environment (Optional but Recommended)  
```sh
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

#### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

#### 4️⃣ Set Up Environment Variables  
Create a `.env` file in the project root and add the following:  

```
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TO_PHONE=your_target_phone_number
FROM_PHONE=your_twilio_phone_number
WEATHER_API_KEY=your_openweather_api_key
MY_LAT=your_latitude
MY_LONG=your_longitude
```

#### 5️⃣ Run the Script  
```sh
python app.py
```

---

### 🖥️ How It Works  
1. The script fetches weather forecasts for the provided latitude and longitude.  
2. It checks if rain is expected in the upcoming hours.  
3. If rain is detected, an SMS alert is sent using Twilio.  

---

### 📝 Requirements  
- Python 3.x  
- Twilio API account  
- OpenWeather API key  
- `requests`, `twilio`, and `python-dotenv` packages  

To install all dependencies, run:  
```sh
pip install requests twilio python-dotenv
```

---

### 🔒 Security Best Practices  
- **DO NOT** expose your `.env` file in public repositories.  
- Add `.env` to your `.gitignore`:  
  ```
  .env
  ```
- Use **Twilio trial accounts** with verified numbers for testing.  

---

### 📌 Author  
👤 **Sai Charan**  
🔗 [GitHub](https://github.com/charan22640)  

---

