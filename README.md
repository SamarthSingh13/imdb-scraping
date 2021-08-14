 # imdb-scraping
Endpoints:
 1) List all movies in the data
 2) Above endpoint should have the ability to sort on the following fields : title, year, rating
 3) Search by Name

Usage:
  
  a) go to myproject/
  
  b) run python3 manage.py runserver
  
  
Endpoints: 
 1) localhost:8000/scraper => displays list of all movies sorted in descending order of rating
 2) localhost:8000/scraper/display/<field> => displays list of all movies sorted in ascending order of field
 3) localhost:8000/scraper/search/<query> => dislpay movie with title = query
