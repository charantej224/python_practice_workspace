class MyClass(object):
    def install(self):
        print("printing function by name")

    def call_method(self):
        method_name = 'install'
        try:
            method = getattr(self, method_name)
        except AttributeError:
            raise NotImplementedError(
                "Class `{}` does not implement `{}`".format(my_cls.__class__.__name__, method_name))
        method()


my_cls = MyClass()
my_cls.call_method()
