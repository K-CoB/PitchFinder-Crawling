CREATE TABLE music (
    id INT AUTO_INCREMENT PRIMARY KEY,
    singer VARCHAR(255),
    song VARCHAR(255),
    highest_pitch VARCHAR(20),
    lowest_pitch VARCHAR(20),
    gender INT,
    genre VARCHAR(50),
    key_of_song INT
);
