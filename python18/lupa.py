import lupa
from lupa import LuaRuntime

import logging
logging.basicConfig(format="%(process)d %(thread)d %(message)s", level=logging.INFO)

lua = LuaRuntime()
print(lua.eval('1+3'))

def pyfunc(n):
    import socket
    logging.info('hello')
    return socket.gethostname()

luafunc = lua.eval('''
function(f,n)
    return f(n)
end''')
logging.info('main')
print(luafunc(pyfunc, 1))

add = lua.eval('''
function (x,y)
    return x+y
end
''')
print(add(4,5))




