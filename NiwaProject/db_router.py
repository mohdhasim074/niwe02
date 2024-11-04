class HindiRouter:
    """
    A router to control all database operations on models in
    the English and Hindi databases.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'hi':
            return 'hindi'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'hi':
            return 'hindi'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'hi' and obj2._meta.app_label == 'hi':
            return 'hindi'
        return 'default'
 
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'hi':
            return db == 'hindi'
        return db == 'default'
