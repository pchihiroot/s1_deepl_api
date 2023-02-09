from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from flask import Flask, request

app = Flask(__name__)

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome("./chromedriver", chrome_options=options)


@app.post("/trans")
def trans():
    data = request.get_json()
    jpn_prompt = data["prompt"]    
    
    driver.get(f"https://www.deepl.com/translator#ja/en/{jpn_prompt}")

    time.sleep(5)

    a = driver.execute_script('return document.getElementById("target-dummydiv").innerHTML;')
    
    return {"result": a}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5493)