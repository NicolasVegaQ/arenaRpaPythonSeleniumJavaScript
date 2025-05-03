# 🤖 Arena RPA Python Selenium JavaScript

Este proyecto es un bot de automatización desarrollado con **Python + Selenium**, optimizado con **inyección de JavaScript**, que completa un reto de formulario web de manera ultrarrápida.

---

## 🚀 Descripción del proyecto

El objetivo es automatizar el llenado de un formulario web dentro del reto Arena RPA, con foco en:

- Alta velocidad de ejecución (resultado: hasta **150 ms** en envío)
- Precisión de llenado
- Reducción de latencia usando `execute_script` (JavaScript inyectado)

---

## 🧱 Estructura del proyecto
```bash
rpaAreaSelenium/
├── drivers/ # Configuración del navegador y WebDriver
│ └── driver_setup.py
├── pages/ # Lógica de la página web (PO: Page Object)
│ └── form_page.py
├── flows/ # Flujo de ejecución (cómo se usa el bot)
│ └── form_flow.py
├── utils/ # Funciones auxiliares (leer Excel, tiempos)
│ └── leer_excel.py
├── main.py # Script principal que ejecuta el reto
├── requirements.txt # Librerías necesarias
└── README.md # Este archivo
```
---

## ⚙️ Requerimientos

- Python 3.9 o superior
- Google Chrome
- Git (opcional, para clonar)

Instalar dependencias con:
```bash
pip install -r requirements.txt
```

## 📊 Tecnologías utilizadas
- Selenium para automatización web
- webdriver-manager para gestionar el ChromeDriver automáticamente
- pandas para lectura de datos desde archivos Excel
- Inyección de JavaScript para optimización del llenado de formularios
- Page Object Model (POM) para organizar el código

## 🧠 Estrategia de optimización
- Se evitó el uso de send_keys() y click() tradicionales.
- Se utilizaron funciones JavaScript inyectadas con execute_script para mayor velocidad.
- Se simularon eventos como input, change, y click para mantener la validación del formulario.
- Se minimizó el uso de esperas y se trabajó con respuestas DOM inmediatas.

## ✍️ Autor
- Nicolás Vega Q.
- Automatización RPA • Python • Selenium • JavaScript
- GitHub: @NicolasVegaQ