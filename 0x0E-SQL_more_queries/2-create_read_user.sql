-- Create datebase and user
CREATE DATEBASE IF NOT EXISTS 'hbtn_0d_2';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
