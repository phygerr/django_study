# django_study
django study,contains jQuery,H5,bootstrap etc.

### django Apache部署静态文件的路径注意点

静态文件放在对应的 app 下的 static 文件夹中 或者 STATICFILES_DIRS 中的文件夹中。

当 DEBUG = True 时，Django 就能自动找到放在里面的静态文件。（Django 通过 STATICFILES_FINDERS 中的“查找器”，找到符合的就停下来，寻找的过程 类似于 Python 中使用 import xxx 时，找 xxx 这个包的过程）。

示例项目 dj18static, 应用 app 下面有一个 static 里面有一个 zqxt.png 图片：

```
dj18static
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── static # 应用 blog 下的 static, 默认会找这个文件夹
│   │   └── 【zqxt.png】
│   ├── tests.py
│   │
│   └── views.py
├── common_static # 已经添加到了 STATICFILES_DIRS 的文件夹
│   └── js
│       └── 【jquery.js】
│
├── dj18static
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

当 settings.py 中的 DEBUG = True 时，打开开发服务器 python manage.py runserver 直接访问 /static/zqxt.png 就可以找到这个静态文件。

也可以在 settings.py 中指定所有 app 共用的静态文件，比如 jquery.js 等

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "common_static"),
)
把 jquery.js 放在 common_static/js/ 下，这样就可以 在 /static/js/jquery.js 中访问到它！