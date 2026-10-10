# Streamlit_robotic-demand-dashboard
Robotics is moving out of factories and into warehouses, hospitals, farms and classrooms. Students and career-switchers often ask: "Which industries are hiring? Which skills should I learn first?"
# 🤖 Robotics Demand Dashboard

> An interactive Streamlit dashboard that shows **why robotics skills are in demand today**: market growth, industry adoption, and the skills employers ask for most.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Charts-3F4F75?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

🔗 **Live demo:** [your-app-name.streamlit.app](https://robo.py)  <!-- replace after deploying -->

![Dashboard preview](screenshots/dashboard.png)  <!-- add a screenshot or GIF -->

---

## 📌 Why this project?

Robotics is moving out of factories and into warehouses, hospitals, farms and classrooms. Students and career-switchers often ask: *"Which industries are hiring? Which skills should I learn first?"*

This dashboard answers those questions visually, so anyone can explore the trends in seconds.

## ✨ Features

| Feature | What it does |
|---|---|
| 📈 **Market growth** | Area chart of the robotics market over time |
| 🏭 **Industry demand** | Compares demand across automotive, logistics, healthcare, agriculture and more |
| 🛠️ **In-demand skills** | Shows which skills (Python, ROS, Arduino, Computer Vision, AI/ML...) appear most in job postings |
| 🎯 **Roadmap builder** | Pick Beginner / Intermediate / Advanced and get a learning path |
| 📂 **Upload your own CSV** | Chart your own job-demand data instantly |

## 🧰 Tech Stack

- **Python**: core logic
- **Streamlit**: web app framework
- **Pandas**: data handling
- **Plotly**: interactive charts

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/robotics-demand-dashboard.git
cd robotics-demand-dashboard

# 2. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run robotics_demand_app.py
```

`requirements.txt`
```
streamlit
pandas
plotly
```

## 📁 Project Structure

```
robotics-demand-dashboard/
├── robotics_demand_app.py   # Main Streamlit app
├── requirements.txt         # Dependencies
├── screenshots/             # Images used in this README
└── README.md
```

## 📊 Data & Sources

The data tables sit at the top of `robotics_demand_app.py` and are easy to edit.

> ⚠️ **Note:** Replace the sample values with figures from your own sources and list them here, for example:
> - IFR *World Robotics* report
> - Statista market data
> - Job-portal counts (LinkedIn, Indeed, Naukri), with the date collected

## 🗺️ Roadmap

- [ ] Pull live job counts from a public jobs data source
- [ ] Add a region filter (India / Global)
- [ ] Add a salary-trend chart
- [ ] Add a "Student projects" gallery (Arduino Uno builds)
- [ ] Dark mode theme

## 🤝 Contributing

Suggestions and pull requests are welcome. Open an issue to discuss what you'd like to change.

## 👩‍💻 About the Author

**Fathima TH Zuhra C**: Data Science & Robotics Trainer, Calicut, Kerala
I teach Python, data analysis (Excel, Power BI) and hands-on robotics with Arduino to school and college students, and I'm now exploring AI automation.

🔗 [LinkedIn](https://www.linkedin.com/in/zuhrazahan) · 📧 your-email@example.com  <!-- update links -->

---

⭐ If you found this useful, please star the repo!
