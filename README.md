# 🔎 Scholar Search CLI (Python)

A simple Python CLI tool that searches research-related pages on Google Scholar using the Exa API.

Users can enter any query (for example: *quantum computing*, *machine learning*, etc.), and the script returns relevant scholar pages with their titles and URLs.



![GitHub repo size](https://img.shields.io/github/repo-size/MadhuTiwari-345/scholar-search-cli)
![GitHub stars](https://img.shields.io/github/stars/MadhuTiwari-345/scholar-search-cli)


---

## 🚀 Features

* Search academic content from Google Scholar
* Simple command-line interface
* Uses the Exa search API
* Lightweight Python script
* Easy to modify for research tools

---

## 🛠 Tech Stack

* Python 3
* Exa API
* Command Line Interface (CLI)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/MadhuTiwari-345/scholar-search-cli.git
cd scholar-search-cli
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install exa-py
```

---

## 🔑 Setup API Key

Get an API key from the Exa dashboard.

Set it as an environment variable instead of hardcoding it in the code.

Example:

Windows PowerShell:

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

Example output:

```
Title: Quantum Mechanics - Classic papers - Google Scholar
URL: https://scholar.google.com/...

Title: Seth Lloyd - Google Scholar
URL: https://scholar.google.com/...
```

---

## 📂 Project Structure

```
scholar-search-cli
│
├── main.py
├── README.md

```

---

## ⚠️ Security Note

Never commit API keys to GitHub.

Always store them in environment variables or a `.env` file.

---

## 📈 Possible Improvements

* Add pagination for more results
* Export results to CSV
* Add filters (year, author, topic)
* Build a simple web interface

---

## 📜 License

MIT License
