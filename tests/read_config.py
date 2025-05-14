from configparser import ConfigParser

def get_config(category,key):
    config=ConfigParser()
    config.read("C:\\Users\\Lenovo\\Desktop\\Python-Test1\\tests\\config.ini")    
    return config.get(category,key)


