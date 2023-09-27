import asyncio
from pyppeteer import launch
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

async def intercept_response(response):
    try:
        # 获取响应的URL
        url = response.url

        # 获取响应的内容
        response_content = await response.text()

        # 在这里可以添加你的处理逻辑，例如保存文件
        # 这里简单地打印响应的URL
        print(f"Received response for URL: {url}")

    except Exception as e:
        print(f"Error: {e}")

async def main():
    # 启动Chrome浏览器
    browser = await launch(headless=False)  # 打开可视化浏览器
    page = await browser.newPage()

    # 使用Selenium连接到已启动的Chrome浏览器
    chrome_options = ChromeOptions()
    chrome_options.debugger_address = "127.0.0.1:9222"  # 与已启动的Chrome浏览器连接
    chrome_service = ChromeService("/usr/local/chromedriver")  # 替换为你的chromedriver路径
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # 监听Network中的响应
    await page.goto("https://www.gstatic.com/cloud-site-ux/text_to_speech/text_to_speech.min.html")  # 访问需要监听的网站
    await page.waitForSelector("body")  # 等待页面加载完成
    await page.setRequestInterception(True)
    page.on('response', intercept_response)

    # 在这里你可以手动操作浏览器

    # 关闭浏览器
    await browser.close()
    driver.quit()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
