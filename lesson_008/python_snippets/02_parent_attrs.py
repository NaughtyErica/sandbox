# -*- coding: utf-8 -*-

# Ко всем ли атрибутам родительского класса можно обратиться?


class Parent:
    class_var_1 = 'поле класса'
    _class_var_2 = '_поле класса'
    __class_var_3 = '__поле класса'

    def __init__(self):
        self.var_1 = 'поле объекта'
        self._var_2 = '_поле объекта'
        self.__var_3 = '__поле объекта'

    @classmethod
    def parent_method_class_field(cls):
        print(cls.class_var_1)
        print(cls._class_var_2)
        print(cls.__class_var_3)

    def paren_method_obj_field(self):
        Parent.parent_method_class_field()
        print(self.var_1)
        print(self._var_2)
        print(self.__var_3)


class Child(Parent):

    def method(self):
        self.paren_method_obj_field()


# obj_parent = Parent()
# obj_parent.paren_method_obj_field()
# obj_parent.parent_method_class_field()
# print("=============================")
obj_child = Child()
# obj_child.parent_method_class_field()
# obj_child.paren_method_obj_field()
obj_child.method()
