class DevelopmentConfig(): 
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER= ''
    MYSQL_PASSWORD='root'
    MYSQL_DB='api_utl'

config = {
    'development': DevelopmentConfig
    
}