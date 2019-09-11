# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# import sys
# 
# for path in sys.path:
#     print(path)
    
import lesson_005.room_1 as r1
import lesson_005.room_2 as r2


print('В комнате', r1.__name__[-6:], 'живут:', ', '.join(r1.folks))
print('В комнате', r2.__name__[-6:], 'живёт:', ', '.join(r2.folks))
# Такой способ получения имени зависит от его длины. Лучше сделать через split по символу точки
# и взятия последней части:
print(r1.__name__.split('.')[-1])

# зачет!
