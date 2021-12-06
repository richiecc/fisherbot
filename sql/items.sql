DROP TABLE IF EXISTS Items;
CREATE TABLE IF NOT EXISTS Items (
    item_id NUMBER PRIMARY_KEY UNIQUE,
    item_name TEXT NOT NULL,
    rarity TEXT NOT NULL,
    value NUMBER DEFAULT NULL,
    type TEXT NOT NULL,
    attribute TEXT DEFAULT NULL);
INSERT INTO Items
VALUES
    (4, "Omni Rod", "Unique", 99999999, "rod", "None"),
    (3, "Heavy Rod", "Legendary", 1000000, "rod", "None"),
    (2, "Lava Rod", "Rare", 10000, "rod", "None"),
    (1, "Glow Rod", "Uncommon", 500, "rod", "None"),
    (0, "Basic Rod", "Common", 0, "rod", "None");