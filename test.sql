select path, count(*) as views from log where path like '/article%' group by path order by views desc limit 3;

select title, t.views from articles inner join (select path, count(*) as views from log where path like '/article%' group by path order by views desc limit 3) as t on concat('/article/', slug) = t.path order by t.views desc;

inner join (select title, slug from articles) as t on concat('/article/', t.slug) = path

select authors.name, t.views from articles inner join (select path, count(*) as views from log where path like '/article%' group by path order by views desc limit 3) as t on concat('/article/', slug) = t.path order by t.views desc;
