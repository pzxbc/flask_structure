## A Flask Project Basic Structure


## 运行

```
export FLASK_APP=run.py
flask run -h 0.0.0.0 -p 8080
```

本地测试配置文件运行
```
export FLASK_APP=run_local.py
flask run -h 0.0.0.0 -p 8080
```

## 开发

使用`Blueprint`方法模块化开发，参考`HelloWorld`模块
