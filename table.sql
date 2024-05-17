CREATE TABLE music (
    id INT AUTO_INCREMENT PRIMARY KEY,
    singer VARCHAR(255),
    title VARCHAR(255),
    highest_pitch INT,
    lowest_pitch INT,
    gender INT,
    genre VARCHAR(50),
    youtube_listen_url VARCHAR(255),
    youtube_image VARCHAR(255),
    youtube_sing_url VARCHAR(255)
);
