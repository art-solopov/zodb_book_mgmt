import persistent

models_registry = []

class _DbMetaclass(type):
    def __init__(cls, name, bases, namespace, **kwargs):
        namespace['model_name'] = name
        super().__init__(name, bases, namespace, **kwargs)
        if name != 'Base':
            models_registry.append(cls)

class Base(persistent.Persistent, metaclass=_DbMetaclass):
    pass
