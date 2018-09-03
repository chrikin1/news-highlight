from flask import render_template,url_for,request,redirect
from . import main
from ..request import get_news,get_articles,get_headlines

#Views
@main.route('/')
def index():
	'''
	View root page function that returns the index page and its data
	'''
	# The trending News 
	general_news = get_headlines('general')
	title = 'Home Page - GET ONLY THE BEST FROM US'
	return render_template('index.html',title = title,general=general_news)

@main.route('/general')
def general():
	general_news = get_news('general')
	title = 'Home Page - Get The latest From Across The World'
	return render_template('general.html',general=general_news)

@main.route('/business')
def business():

	business_news = get_news('business')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('business.html',business=business_news)

@main.route('/sports')
def sports():

	sports_news = get_news('Todays sports')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('sports.html',sports=sports_news)

