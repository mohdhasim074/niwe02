class EnglishRouter:
    def db_for_read(self, model, **hints):
        """Direct read operations for English models to 'default'."""
        if model._meta.app_label == 'english_app':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """Direct write operations for English models to 'default'."""
        if model._meta.app_label == 'english_app':
            return 'default'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure English models are only created in the 'default' database."""
        if app_label == 'english_app':
            return db == 'default'
        return None


class HindiRouter:
    def db_for_read(self, model, **hints):
        """Direct read operations for Hindi models to 'hindi'."""
        if model._meta.app_label == 'hindi_app':
            return 'hindi'
        return None

    def db_for_write(self, model, **hints):
        """Direct write operations for Hindi models to 'hindi'."""
        if model._meta.app_label == 'hindi_app':
            return 'hindi'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure Hindi models are only created in the 'hindi' database."""
        if app_label == 'hindi_app':
            return db == 'hindi'
        return None
