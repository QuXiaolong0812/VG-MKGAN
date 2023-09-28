import requests
from bs4 import BeautifulSoup


def search_baidu_baike(keyword):
    base_url = "https://baike.baidu.com"
    search_url = f"{base_url}/item/{keyword}"

    # 发送HTTP请求并获取页面内容
    response = requests.get(search_url)

    # 检查HTTP响应状态
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # 查找包含简介的标签，通常是<div class="lemma-summary">
        summary_tag = soup.find("div", class_="lemma-summary")

        if summary_tag:
            summary = summary_tag.get_text()
            return summary.strip()
        else:
            return "未找到相关简介"
    else:
        return "请求失败"


if __name__ == "__main__":
    keyword = "人参"
    result = search_baidu_baike(keyword)
    print(f"{keyword}的简介：\n{result}")
