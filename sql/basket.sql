DROP TABLE IF EXISTS Basket;
CREATE TABLE IF NOT EXISTS Basket (
    user_id NUMBER NOT NULL,
    catchable_id NUMBER NOT NULL,
    amount NUMBER NOT NULL);