#!usr/bin/env python
# Import PostGreSQL library psycopg2
import psycopg2

DBNAME = "newsname"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()


# Method is used to fetch the date on which
# more than 1 % of requests lead to errors requests
def get_articles():
    """The query is used to fetch the top three articles in the database"""
    c.execute("select count(*) as count,articles.title from log join articles"
              "on log.path='/article/'||articles.slug where"
              "path LIKE '/article%' group"
              "by articles.title order by count desc limit 3;")  # noqa
    rows = c.fetchall()
    print("1. The top most popular three articles are\n")
    for row in rows:
        print("\u2022", row[1], " - ", row[0], " views\n")
# Method is used to print the most popular top three authors


def get_authors():
    """query to fetch top three articles of all time"""
    c.execute("select authorName.count,name from authors join(select"
              "SUM(count) as count,author from articles join (select count(*)"
              "as count,path from log where path LIKE '/article%'"
              "group by path) countPath on countPath.path='/article/"
              "'||articles.slug group by author) authorName on"
              "authorName.author=authors.id order by authorName.count"
              "desc;")  # noqa
    rows = c.fetchall()
    print("2. The top most popular article authors are\n")
    for row in rows:
        print("\u2022", row[1], " - ", row[0], " views\n")


# Method is used to fetch the date on which
# more than 1 % of requests lead to errors requests
def getErrors():
    """query to fetch date on which more than 1 % of requests lead to errors"""
    c.execute("select errorReq.count, allReq.countt, errorReq.e from"
              "(select count(*) as count,time::date as e from log"
              "where status!='200 OK' group by e) errorReq join"
              "(select count(*) as countt,time::date as f from"
              "log group by f) allReq on errorReq.e=allReq.f"
              "where errorReq.count>(allReq.countt/100)"
              "order by errorReq.e;")  # noqa
    rows = c.fetchall()
    print("3. The day that had more than 1%"
          "of requests that lead to errors was on\n")
    for row in rows:
        errorCount = row[0]*100
        errorCount = errorCount/row[1]
        errorCount = round(errorCount, 2)
        print("\u2022", row[2], " \u2014 ", errorCount, "% errors\n")


# Printing and returning the results from the newsname database
get_articles()
get_authors()
getErrors()
db.close()
