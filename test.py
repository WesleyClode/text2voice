from selenium import webdriver

# 使用绝对路径启动chromedriver
chromedriver_path = "/usr/local/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver_path)

# 打开网页
driver.get("https://www.baidu.com")

# 在这里添加你的操作，例如查找元素、输入文本、点击按钮等

# 最后关闭浏览器
driver.quit()
