-- 14. My genres
-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tvg.name
FROM tv_genres AS tvg
INNER JOIN tv_show_genres AS tvsg ON tvg.id = tvsg.genre_id
INNER JOIN tv_shows AS tv ON tv.id = tvsg.show_id
WHERE tv.title = 'Dexter'
ORDER BY tvg.name;
