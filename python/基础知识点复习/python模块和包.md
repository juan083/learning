python模块和包
====

### 导入模块

#### 3种写法
```
import mymodule as my
import sys, mymodule as my

from mymodule import module_value, printvalue
from mymodule import (module_value, printvalue)

from module import *
```

#### 查找模块的3个步骤：
1. 在当前目录中查找mymodule.py
2. 若找不到，则继续从环境变量PYTHONPATH中查找
3. 若没有PYTHONPATH变量，就到安装目录查找

包是一组模块的集合，而模块是一个python文件，所以包就是放着若干python文件、__init__.py

__init__.py可以是空文件

其里面的__all__属性，是包的一个重要属性，一般用来存放模块名

from mypackage import * , 实际就是，按照__all__给出的模块名进行导入，可以看做是包的索引。

一般都建议在__init__.py里明确的设置__all__列表
