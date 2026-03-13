# 🔎 Scholar Search CLI (Python)

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)


A lightweight **Python CLI tool** that searches research-related pages from **Google Scholar** using the Exa API.

Users can enter any query (for example: *quantum computing*, *machine learning*, etc.), and the script returns relevant scholar pages with their titles and URLs.

---

## 🎬 Demo Images 

<img width="981" height="614" alt="image" src="https://github.com/user-attachments/assets/ed8e1fdd-92cd-48ac-a52b-a6dc4d545cd9" />
<img width="996" height="390" alt="image" src="https://github.com/user-attachments/assets/73d4eac9-146b-4e7a-a7e4-bccfd8721fc4" />


Example CLI usage:

```
Search here: machine learning

Title: Geoffrey Hinton - Google Scholar
URL: https://scholar.google.com/...

Title: Tom Mitchell - Google Scholar
URL: https://scholar.google.com/...
```

---

## 🚀 Features

* 🔎 Search academic content from Google Scholar
* 💻 Simple command-line interface
* ⚡ Powered by the Exa Search API
* 🪶 Lightweight Python script
* 🧩 Easy to extend for research tools

---

## 🛠 Tech Stack

* Python 3
* Exa API
* Command Line Interface (CLI)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/MadhuTiwari-345/Scholor-Search-CLI.git
cd Scholor-Search-CLI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install exa-py
```

---

## 🔑 Setup API Key

Get your API key from the Exa dashboard.

Set it as an environment variable instead of hardcoding it.

Example (PowerShell):

```bash
$env:EXA_API_KEY="your_api_key_here"
```

---

## ▶️ Run the Program

```bash
python main.py
```

Example:

```
Search here: quantum computing
```

Example Output:

```
Title: Quantum Mechanics - Classic papers - Google Scholar
URL: https://scholar.google.com/...

Title: Seth Lloyd - Google Scholar
URL: https://scholar.google.com/...
```

---

## 📂 Project Structure

```
Scholar-Search-CLI
│
├── main.py
├── README.md
├── LICENSE
```

---

## ⚠️ Security Note

Never commit API keys to GitHub.

Use environment variables or a `.env` file instead.

Example inside Python:

```python
import os
from exa_py import Exa

exa = Exa(os.getenv("EXA_API_KEY"))
```

---

## 📈 Possible Improvements

* Add pagination for more results
* Export results to CSV
* Add filters (year, author, topic)
* Build a web interface
* Package as a pip installable CLI tool

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License.

---
