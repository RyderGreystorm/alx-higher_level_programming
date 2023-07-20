-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
