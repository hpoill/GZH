from flask import Flask

# 安装依赖
# pip3 install -U flask

app = Flask(__name__)


@app.route('/')
def index():
    return "测试容器部署!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

# 浏览器访问测试
# http://127.0.0.1:8888/