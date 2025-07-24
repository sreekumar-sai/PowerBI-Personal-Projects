from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

# --- User Input ---
fp1_url = input("Paste the FP1 URL: ").strip()
track_name = input("Enter the track name (e.g., Australia): ").strip()

# --- Session URLs ---
base_prefix = fp1_url.rsplit('/', 1)[0]  # removes '/1'
session_urls = {
    "FP1": fp1_url,
    "FP2": f"{base_prefix}/2",
    "FP3": f"{base_prefix}/3"
}

# --- Setup Selenium ---
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(), options=chrome_options)

# --- Function to extract table and save CSV ---
def extract_table_to_csv(session_name, session_url):
    print(f"\n🌐 Scraping {session_name} from: {session_url}")
    try:
        driver.get(session_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table.f1-table"))
        )
        time.sleep(2)  # allow JS to fully render

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.select_one("table.f1-table")

        if not table:
            print(f"❌ Table not found for {session_name}")
            return

        headers = [th.get_text(strip=True) for th in table.select("thead th")]
        rows = []
        for tr in table.select("tbody tr"):
            cells = [td.get_text(strip=True) for td in tr.select("td")]
            if cells:
                rows.append(cells)

        df = pd.DataFrame(rows, columns=headers)
        filename = f"{track_name}_{session_name}.csv"
        df.to_csv(filename, index=False)
        print(f"✅ Saved: {filename}")

    except Exception as e:
        print(f"⚠️ Error with {session_name}: {e}")

# --- Loop through FP1, FP2, FP3 ---
for name, url in session_urls.items():
    extract_table_to_csv(name, url)

driver.quit()
