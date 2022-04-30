/*
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/


DROP TABLE IF EXISTS Shop;
DROP TABLE IF EXISTS Basket;
DROP TABLE IF EXISTS Catchable;
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Areas;

-- CREATE AREAS
CREATE TABLE IF NOT EXISTS Areas (
    area_id INT PRIMARY KEY UNIQUE,
    area_name TEXT NOT NULL);
    
-- CREATE ITEMS
CREATE TABLE IF NOT EXISTS Items (
    item_id INT PRIMARY KEY UNIQUE,
    item_name TEXT NOT NULL,
    rarity TEXT NOT NULL,
    value INT DEFAULT NULL,
    type TEXT NOT NULL,
    attribute TEXT DEFAULT NULL);
    
-- CREATE USERS
CREATE TABLE IF NOT EXISTS Users (
    user_id INT PRIMARY KEY NOT NULL,
    xp INT NOT NULL,
    gold INT NOT NULL,
    area_id INT NOT NULL,
    fish_caught INT NOT NULL,
    CONSTRAINT FK_Users_Area FOREIGN KEY (area_id)
    REFERENCES Areas(area_id));

-- CREATE INVENTORY
CREATE TABLE IF NOT EXISTS Inventory (
    user_id INT NOT NULL,
    item_id INT NOT NULL,
    amount INT NOT NULL,
    CONSTRAINT FK_Inventory_Users FOREIGN KEY (user_id)
    REFERENCES Users (user_id));

-- CREATE CATCHABLE
CREATE TABLE IF NOT EXISTS Catchable (
    catchable_id INT PRIMARY KEY,
    catchable_name TEXT NOT NULL,
    area_id INT NOT NULL,
    xp_on_catch INT NOT NULL,
    rarity TEXT NOT NULL,
    attribute TEXT NOT NULL);

-- CREATE BASKET
CREATE TABLE IF NOT EXISTS Basket (
    user_id INT NOT NULL,
    catchable_id INT NOT NULL,
    amount INT NOT NULL,
    CONSTRAINT FK_Basket_Users FOREIGN KEY (user_id)
    REFERENCES Users(user_id),
    CONSTRAINT FK_Basket_Catchable FOREIGN KEY (catchable_id) 
    REFERENCES Catchable(catchable_id));

-- CREATE SHOP
CREATE TABLE IF NOT EXISTS Shop (
    catchable_id INT NOT NULL,
    buy_price INT NOT NULL,
    CONSTRAINT FK_Shop_Catchable FOREIGN KEY (catchable_id)
    REFERENCES Catchable(catchable_id));

-- STATIC DATA
INSERT INTO Catchable
VALUES
    (0, "Cod", 0, 5, "Common", "fish"),
    (1, "Salmon", 0, 7, "Common", "fish"),
    (2, "Pufferfish", 0, 10, "Common", "fish"),
    (3, "Boots", -1, 1, "Junk", "junk"),
    (4, "Broken Glass", -1, 1, "Junk", "junk"),
    (5, "Carrot", -1, 1, "Junk", "junk"),
    (6, "Seaweed", -1, 1, "Junk", "junk"),
    (7, "Stick", -1, 1, "Junk", "junk"),
    (8, "Cichlid", 1, 20, "Common", "fish"),
    (9, "Blue Dory", 1, 20, "Common", "fish"),
    (10, "Butterflyfish", 1, 20, "Common", "fish"),
    (11, "Triggerfish", 1, 20, "Common", "fish"),
    (12, "Blue Tang", 1, 80, "Uncommon", "fish"),
    (13, "Black Tang", 1, 80, "Uncommon", "fish"),
    (14, "Red-Lipped Blenny", 1, 90, "Uncommon", "fish"),
    (15, "Red Cichlid", 2, 50, "Common", "fish"),
    (16, "Red Snapper", 2, 50, "Common", "fish"),
    (17, "Emperor Red Snapper", 2, 75, "Common", "fish"),
    (18, "Tomato Clown", 2, 50, "Common", "fish"),
    (19, "Tomato Clownfish", 2, 95, "Uncommon", "fish"),
    (20, "Ornate Butterfly", 2, 95, "Uncommon", "fish"),
    (21, "Anemone", 2, 165, "Rare", "fish"),
    (22, "White-Silver SunStreak", 3, 100, "Common", "fish"),
    (23, "White-Gray Dasher", 3, 100, "Common", "fish"),
    (24, "Moorish Idol", 3, 100, "Common", "fish"),
    (25, "Threadfin", 3, 110, "Common", "fish"),
    (26, "Yellow Tang", 3, 250, "Uncommon", "fish"),
    (27, "Goatfish", 3, 250, "Uncommon", "fish"),
    (28, "Yellowtail Parrot", 3, 250, "Uncommon", "fish"),
    (29, "Clownfish", 3, 300, "Rare", "fish"),
    (30, "Tropical Fish Preview (gr)", 3, 2000, "Legendary", "fish"),
    (31, "Tropical Fish Preview (w)", 3, 2000, "Legendary", "fish"),
    (32, "Cotton Candy Betta", 4, 150, "Common", "fish"),
    (33, "Parrotfish", 4, 275, "Uncommon", "fish"),
    (34, "Queen Angelfish", 4, 350, "Rare", "fish"),
    (35, "Dottyback", 4, 2500, "Legendary", "fish"),
    (36, "Pogfish", 4, 12500, "Unique", "fish");
INSERT INTO Areas
VALUES
    (0, "The Ocean"),
    (1, "Deep Cave"),
    (2, "Lava Pool"),
    (3, "Outer Space"),
    (4, "Dimensional Rift");
INSERT INTO Items
VALUES
    (0, "Basic Rod", "Common", 0, "rod", "None"),
    (1, "Glow Rod", "Uncommon", 500, "rod", "None"),
    (2, "Lava Rod", "Rare", 10000, "rod", "None"),
    (3, "Heavy Rod", "Legendary", 1000000, "rod", "None"),
    (4, "Omni Rod", "Unique", 99999999, "rod", "None");
INSERT INTO Shop
VALUES
    (0, 10),
    (1, 10),
    (2, 10),
    (8, 20),
    (9, 20),
    (10, 20),
    (11, 20),
    (12, 40),
    (13, 40),
    (14, 40),
    (15, 30),
    (16, 30),
    (17, 30),
    (18, 30),
    (19, 60),
    (20, 60),
    (21, 135),
    (22, 40),
    (23, 40),
    (24, 40),
    (25, 40),
    (26, 80),
    (27, 80),
    (28, 80),
    (29, 180),
    (30, 460),
    (31, 460),
    (32, 50),
    (33, 100),
    (34, 225),
    (35, 575),
    (36, 1500);