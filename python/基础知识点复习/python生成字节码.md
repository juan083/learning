python生成字节码
====

```
python -m py_compile file.py #把单个.py文件编译为字节码文件
python -m py_compile /path/to/src/ #批量生成字节码文件，/path/to/src/是包含.py文件名的路径
python -m compileall file.py #把单个.py文件编译为字节码文件
python -m compileall /path/to/src/ #批量生成字节码文件，/path/to/src/是包含.py文件名的路径
或者：
python -O -m py_compile file.py
python -O -m py_compile /path/to/src/
python -O -m compileall file.py
python -O -m compileall /path/to/src/

或者
python -OO -m py_compile file.py
python -OO -m py_compile /path/to/src/
python -OO -m compileall file.py
python -OO -m compileall /path/to/src/
```

注解：
-m参数相当于脚本中的import，这里的`-m py_compile` 相当于上面的 `import py_compile`，
也即把后边跟随的库模块当做脚本运行。这样生成的字节码文件后缀名为.pyc

-O参数表明要生成更加紧凑的优化后的字节码,-OO会进一步移除-O选项生成的优化后的字节码文件中的文档字符串。
这样生成的字节码文件后缀名为.pyo，
对于.pyo文件可以通过 python命令加-O参数执行导入了该模块的python程序来调用。

需注意的是，不同版本编译后的pyc文件是不同的，比如2.5编译的pyc文件2.4版本的python是无法执行的。
