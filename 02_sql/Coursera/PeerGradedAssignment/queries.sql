# 1 - Total Number of records for each table
# Do it for every table:

SELECT COUNT(count)
FROM checkin

# 2

#3
SELECT COUNT(*) - COUNT(id) as id, 	COUNT(*) - COUNT(name) as name, 	COUNT(*) - COUNT(review_count) as review_count, 	COUNT(*) - COUNT(yelping_since) as yelping_since, 	COUNT(*) - COUNT(useful) as useful, 	COUNT(*) - COUNT(funny) as funny, 	COUNT(*) - COUNT(cool) as cool, 	COUNT(*) - COUNT(fans) as fans, 	COUNT(*) - COUNT( average_stars) as  average_stars, 	COUNT(*) - COUNT(compliment_hot) as compliment_hot, 	COUNT(*) - COUNT(compliment_more) as compliment_more, 	COUNT(*) - COUNT(compliment_profile) as compliment_profile, 	COUNT(*) - COUNT(compliment_cute) as compliment_cute, 	COUNT(*) - COUNT(compliment_list) as compliment_list, 	COUNT(*) - COUNT(compliment_note) as compliment_note, 	COUNT(*) - COUNT(compliment_plain) as compliment_plain, 	COUNT(*) - COUNT(compliment_cool) as compliment_cool, 	COUNT(*) - COUNT(compliment_funny) as compliment_funny, 	COUNT(*) - COUNT(compliment_writer) as compliment_writer, 	COUNT(*) - COUNT(compliment_photos) as compliment_photos
FROM user

#9 
select avg( (review_count - avg_x) * (fans - avg_y) )*avg( (review_count - avg_x) * (fans - avg_y) )/(var_x*var_y) as R2 
from user, (select 
      avg_x,
      avg_y,
      avg((review_count - avg_x)*(review_count - avg_x)) as var_x, 
      avg((fans - avg_y)*(fans - avg_y)) as var_y 
      from user, (select 
          avg(review_count) as avg_x, 
          avg(fans) as avg_y 
          from user)
  );

# Part 2
#1)
# Which categories we have the most in Toronto? 
SELECT c.category, COUNT(c.category) as count_category, b.*
FROM business as b
INNER JOIN category as c ON b.id = c.business_id
WHERE b.city = 'Toronto'
GROUP BY c.category
ORDER BY count_category desc

#SELECT 
SELECT b.stars, c.category, b.*
FROM business as b
INNER JOIN category as c ON b.id = c.business_id
WHERE b.city = 'Toronto' and c.category = 'Bars'
ORDER BY stars desc

#Restaurants are too much, I will choose Bars

# Check hours
  SELECT h.hours, b.stars, c.category, b.*
  FROM business as b
  INNER JOIN category as c ON b.id = c.business_id
  INNER JOIN hours as h ON b.id = h.business_id
  WHERE b.city = 'Toronto' and c.category = 'Bars'
  ORDER BY b.stars desc

2) ii)
SELECT AVG(stars) as stars , AVG(review_count) as review_count, is_open
FROM business
GROUP BY is_open 
ORDER BY stars desc, review_count desc

3)
# Found no correlation:
SELECT AVG(b.stars) as avg_stars, AVG(b.review_count) as avg_review_count, p.label
FROM business as b
INNER JOIN photo as p ON b.id = p.business_id
GROUP BY p.label
ORDER BY avg_stars desc, avg_review_count desc


#Second attempt
# Analysis to check if there is a correlation among stars and photos taken inside or outside

SELECT label, COUNT(*) as count_label
FROM photo 
GROUP BY label
ORDER BY count_label desc

