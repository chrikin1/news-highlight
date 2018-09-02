import os

class Config:
	'''
	General configuration parent class
	'''
	NEWS-HIGHLIGHT-API URL ='https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
	NEWS_ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&language=en&apiKey={}'
	HEADLINES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=gb&category={}&apiKey={}'
	NEWS_API_KEY = os.environ.get('HIGHLIGHT API_KEY')
    
class ProdConfig(Config):
	'''
	Production configuration smsaller class
	
	Args:
		Config : The parent configuration class with General configuration settings
	'''
	pass


class DevConfig(Config):
	'''
	Development Configuration smaller class

	Args:
		Config:The parent configuration class with General configuration settings
	'''
	DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}	