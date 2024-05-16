CREATE TABLE music (
    id INT AUTO_INCREMENT PRIMARY KEY,
    singer VARCHAR(255),
    song VARCHAR(255),
    highest_pitch INT,
    lowest_pitch INT,
    gender INT,
    genre VARCHAR(50),
    youtube_url VARCHAR(255)
);
