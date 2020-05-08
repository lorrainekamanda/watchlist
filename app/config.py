class Config:
    '''
    General configuration parent class
    '''
    
  
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://grace:leils@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'   


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True