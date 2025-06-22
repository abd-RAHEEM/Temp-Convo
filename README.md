# 🌡️ Temperature Converter CLI Tool

A simple Python command-line tool to convert temperatures between Celsius and Fahrenheit using the `argparse` module.

---

## 📌 Features

- Convert **Celsius to Fahrenheit** and **Fahrenheit to Celsius**
- Uses `argparse` for clean command-line interface
- Displays helpful messages and enforces valid input
- Output uses a friendly format like: `100.0°C is equal to 212.00°F`

---

## 🚀 Getting Started

###  Clone or Download

```bash
git clone https://github.com/abd-RAHEEM/Temp-Convo



### ⚙️ Usage
✅ Convert Celsius to Fahrenheit

python converter.py --c2f 100
Output:
100.0°C is equal to 212.00°F
✅ Convert Fahrenheit to Celsius
python converter.py --f2c 212
Output:
212.0°F is equal to 100.00°C
🧠 How It Works
--c2f: Convert Celsius to Fahrenheit (input a float or integer)

--f2c: Convert Fahrenheit to Celsius (input a float or integer)

Only one of the two options can be used at a time (mutually exclusive)

🧪 Example
python converter.py --c2f 37
37.0°C is equal to 98.60°F

📂 File Structure
temperature-converter-cli/
├── converter.py   # Main script
└── README.md           # This file
