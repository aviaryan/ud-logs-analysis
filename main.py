import psycopg2

ques_1 = 'What are the most popular three articles of all time?'
query_1 = """
select title, t.views from articles inner join
(select path, count(*) as views from log where path like '/article%'
group by path order by views desc limit 3)
as t on concat('/article/', slug) = t.path order by t.views desc;
"""

ques_2 = 'Who are the most popular article authors of all time?'
query_2 = """
select authors.name, count(*) as views from articles inner
join authors on articles.author = authors.id inner join log
on concat('/article/', articles.slug) = log.path where
log.status like '%200%' group by authors.name order by views desc
"""


class Problem:
    def __init__(self):
        try:
            self.db = psycopg2.connect('dbname=news')
            self.cursor = self.db.cursor()
        except Exception as e:
            print e

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def solve(self, ques, query):
        query = query.replace('\n', ' ')
        result = self.execute_query(query)
        print ques
        for i in range(len(result)):
            print '\t', i + 1, '.', result[i][0], '--', result[i][1]
        # blank line
        print ''

    def exit(self):
        self.db.close()


if __name__ == '__main__':
    problem = Problem()
    problem.solve(ques_1, query_1)
    problem.solve(ques_2, query_2)
    problem.exit()
