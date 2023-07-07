class DBRouter:
    mongo_db = "mongo"
    default_db = "default"

    def db_for_read(self, model, **hints):
        model_name = model._meta.model_name
        # print("read out",model,model_name)
    
        if model_name.startswith("mongo_"):
            # print("read",model,model_name)
            return self.mongo_db
        else:
            return None

    def db_for_write(self, model, **hints):
        model_name = model._meta.model_name
        # print("write",model,model_name)
        if model_name.startswith("mongo_"):
            return self.mongo_db
        else:
            return None
        
  

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print("model_name",model_name)
        if model_name and model_name.startswith("mongo"):  
                print("migrate",model_name,db)
                return db==self.mongo_db
        else:
            print("else migrate",model_name,db)
            return db==self.default_db 