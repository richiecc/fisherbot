DROP TABLE IF EXISTS Areas;
CREATE TABLE IF NOT EXISTS Areas (
    area_id NUMBER PRIMARY_KEY UNIQUE,
    area_name TEXT NOT NULL);
INSERT INTO Areas
VALUES
    (4, "Dimensional Rift"),
    (3, "Outer Space"),
    (2, "Lava Pool"),
    (1, "Deep Cave"),
    (0, "The Ocean");