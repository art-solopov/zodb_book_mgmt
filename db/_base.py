import persistent

models_registry = []

class _DbMetaclass(type):
    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)
        if name != 'Base':
            models_registry.append(cls)
        cls.model_name = name

class Base(persistent.Persistent, metaclass=_DbMetaclass):
    pass
