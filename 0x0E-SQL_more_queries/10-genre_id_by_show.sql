-- tv shows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDED BY tv_show.title, tv_show_genres.genre_id;
