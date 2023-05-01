--1 Actors in Movie Anaconda Confessions.
SELECT actor.actor_name, film.title
FROM actor_has_film 
INNER JOIN actor ON actor_has_film.actor_id = actor.actor_id
INNER JOIN film ON actor_has_film.film_id = film.film_id
WHERE film.title = 'ANACONDA CONFESSIONS';
--2 Movies from Actress Penelope Guiness.
SELECT actor.actor_name, film.title
FROM actor_has_film 
INNER JOIN actor ON actor_has_film.actor_id = actor.actor_id
INNER JOIN film ON actor_has_film.film_id = film.film_id
WHERE actor.actor_name = 'PENELOPE GUINESS';
--3 Last long movies.
SELECT title, length
FROM film
WHERE length = (SELECT MAX(length) FROM film);
--4 Shortest movies.
SELECT title, length
FROM film
WHERE length = (SELECT MIN(length) FROM film);
--5 Movies in storage.
SELECT title
FROM film
WHERE film_id IN (
  SELECT film_id
  FROM inventory
);
--6 Missing movies from film list in storage.
SELECT title
FROM film
WHERE film_id NOT IN (
  SELECT film_id
  FROM inventory
);
--7 Movies in store suitable for all ages.
SELECT title, rating
FROM film
WHERE film_id IN (
  SELECT film_id
  FROM inventory
) AND rating = 'G';
--8 Number of titles per movie in storage.
SELECT film.title, SUM(inventory_count.count) AS total_count
FROM film
INNER JOIN (
  SELECT film_id, COUNT(*) AS count
  FROM inventory
  GROUP BY film_id
) AS inventory_count ON film.film_id = inventory_count.film_id
GROUP BY film.film_id;
--9 Average number of movies per title in storage.
SELECT AVG(inventory_count.count) AS avg_count
FROM (
  SELECT film_id, COUNT(*) AS count
  FROM inventory
  GROUP BY film_id
) AS inventory_count;
--10 Adult movies on list.
SELECT title
FROM film
WHERE rating = 'NC-17';