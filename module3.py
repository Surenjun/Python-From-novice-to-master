def foo():
    pass

def bar():
    #1、空语句，什么也不做  2、在特别的时候用来保证格式或是语义的完整性
    pass

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()