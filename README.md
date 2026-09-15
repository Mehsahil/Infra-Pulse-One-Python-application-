# InfraPulse.

A lightweight, monolithic infrastructure health-monitoring dashboard built with Python.

InfraPulse monitors the health and system information of the machine running the application and presents it through a minimal, illustrative web dashboard.

# Features.

- CPU utilization monitoring
- Memory utilization monitoring
- Disk utilization monitoring
- Hostname information
- Operating system information
- Python version information
- Lightweight server-rendered architecture
- No separate frontend application
- No database required
- Simple `python app.py` startup
- Minimalistic and colorful dashboard UI

# Architecture.

InfraPulse follows a simple monolithic architecture:
                ┌─────────────────────┐
                │      Browser        │
                │                     │
                │  InfraPulse UI      │
                └──────────┬──────────┘
                           │
                           │ HTTP
                           ▼
                ┌─────────────────────┐
                │      app.py         │
                │                     │
                │  Python Web Server  │
                │  System Monitoring │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     Host Machine    │
                │                     │
                │ CPU / RAM / Disk    │
                │ OS / Hostname       │
                └─────────────────────┘

# Project Struc:
InfraPulse/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── app.js

# Tech stack.
Python
Flask
HTML5
CSS3
JavaScript
psutil