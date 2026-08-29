# NEtflix-film-SCRAPER


A simple Python script that logs into Netflix, searches for a movie or series, and displays its title, release year, maturity rating, description, cast, and genres.

⚠️ Disclaimer: This tool is for educational purposes only. Scraping Netflix may violate their Terms of Service. Use it responsibly and only on your own account.
<hr>
🚀 Features
Automatically logs into your Netflix account.

Searches for any title by name.

Extracts:

Title

Year & maturity rating (e.g., 2021 | 16+)

Synopsis / description

Main cast members

Genres / categories

Interactive command-line interface – keep searching until you type quit.
<hr>
🛠️ How It Works
Selenium with ChromeDriver opens a browser.

It navigates to Netflix’s login page, enters your credentials, and submits.

It then constructs a search URL and clicks the first result.

On the title’s detail page, it scrapes the required fields using XPath selectors.

The information is printed to the console.
<hr>
📦 Requirements
Python 3.6+

Google Chrome browser installed.

A Netflix account (active subscription).
<hr>
🔧 Installation & Usage
Clone the repository


bash
git clone https://github.com/yourusername/netflix-scraper.git
cd netflix-scraper
Install dependencies


bash
pip install -r requirements.txt
Run the script


bash
python netflix_scraper.py
Enter your Netflix email and password when prompted (they are not stored anywhere).

Type a title (e.g., Stranger Things) and press Enter.

View the results, then search again or type quit to exit.
<hr>
📂 Project Structure
text
.
├── netflix_scraper.py   # Main script
└── requirements.txt     # Python dependencies
❗ Important Notes
The script uses XPath selectors that depend on Netflix’s current HTML structure. If Netflix updates their site, the script may break.

If your account has two‑factor authentication (2FA), this script will not work.

The script is intentionally kept simple for beginners – no error handling for many edge cases.
<hr>
🔮 Possible Improvements (for you to try)
---

Add support for 2FA.

Save results to a file (CSV/JSON).

Use environment variables for credentials.

Implement a GUI or a web interface.

Handle pagination or multiple search results.
<hr>
📄 License
no license... just use it

Happy coding! 🎬
