CREATE or REPLACE FUNCTION age_actor(fn varchar(50), lan varchar(100)) 
RETURNS date AS $birthdate$
BEGIN
   RETURN(SELECT age FROM actors WHERE actors.first_name = fn AND actors.last_name=lan);
END;
$birthdate$ LANGUAGE plpgsql;

SELECT *FROM actors

SELECT * FROM age_actor('Tom', 'Hanks');

CREATE or REPLACE FUNCTION fullname_actor(fn varchar(50), lan varchar(100)) RETURNS VARCHAR(100) AS $fullname$
BEGIN
   RETURN(SELECT CONCAT(first_name, ' ', last_name) FROM actors WHERE actors.first_name = fn AND actors.last_name=lan);
END;
$fullname$ LANGUAGE plpgsql;

SELECT * FROM fullname_actor('Tom', 'Hanks');

CREATE or REPLACE FUNCTION current_age_actor(fn varchar(50), lan varchar(100)) RETURNS int AS $current_age$
declare
    current_age integer;
    birthdate date;
    now_date date := CURRENT_DATE;
BEGIN
   birthdate := (SELECT age FROM actors WHERE actors.first_name = fn AND actors.last_name=lan);
   current_age := DATE_PART('year', now_date) - DATE_PART('year', birthdate);
   RETURN current_age;
END;
$current_age$ LANGUAGE plpgsql;

SELECT * FROM current_age_actor('Tom', 'Hanks');


