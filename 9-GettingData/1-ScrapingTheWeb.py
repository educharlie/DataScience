#Scraping to the web

from __future__ import division
from collections import Counter
import math, random, csv, json

from bs4 import BeautifulSoup
import requests

######
#
# BOOKS ABOUT DATA
#
######

def is_video(td):
    """it's a video if it has exactly one pricelabel, and if
    the stripped text inside that pricelabel starts with 'Video'"""
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and
            pricelabels[0].text.strip().startswith("Video"))

def book_info(td):
    """given a BeautifulSoup <td> Tag representing a book,
    extract the book's details and return a dict"""
    
    title = td.find("div", "thumbheader").a.text
    by_author = td.find('div', 'AuthorName').text
    authors = [x.strip() for x in re.sub("^By ", "", by_author).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0]
    date = td.find("span", "directorydate").text.strip()
    
    return {
        "title" : title,
        "authors" : authors,
        "isbn" : isbn,
        "date" : date
    }

from time import sleep

def scrape(num_pages=31):
    base_url = "http://shop.oreilly.com/category/browse-subjects/" + \
           "data.do?sortby=publicationDate&page="

    books = []

    for page_num in range(1, num_pages + 1):
        print "souping page", page_num
        url = base_url + str(page_num)
        soup = BeautifulSoup(requests.get(url).text, 'html5lib')
            
        for td in soup('td', 'thumbtext'):
            if not is_video(td):
                books.append(book_info(td))

        # now be a good citizen and respect the robots.txt!
        sleep(30)

    return books

def get_year(book):
    """book["date"] looks like 'November 2014' so we need to 
    split on the space and then take the second piece"""
    return int(book["date"].split()[1])

def plot_years(plt, books):
    # 2014 is the last complete year of data (when I ran this)
    year_counts = Counter(get_year(book) for book in books
                          if get_year(book) <= 2014)

    years = sorted(year_counts)
    book_counts = [year_counts[year] for year in x]
    plt.bar([x - 0.5 for x in years], book_counts)
    plt.xlabel("year")
    plt.ylabel("# of data books")
    plt.title("Data is Big!")
    plt.show()