# Understanding the Database
## TODO: FINISH THIS

## Catchable
| Catchable      |                           |
| -------------- | ------------------------- |
| catchable_id   | NUMBER PRIMARY_KEY UNIQUE |
| catchable_name | TEXT NOT NULL             |
| area_id        | NUMBER NOT NULL           |
| xp_on_catch    | NUMBER NOT NULL           |
| rarity         | TEXT NOT NUL              |
| attribute      | TEXT NOT NULL             |

## Areas
| Areas     |                           |
| --------- | ------------------------- |
| area_id   | NUMBER PRIMARY_KEY UNIQUE |
| area_name | TEXT NOT NULL             |

## Items
| Items     |                           |
| --------- | ------------------------- |
| item_id   | NUMBER PRIMARY_KEY UNIQUE |
| item_name | TEXT NOT NULL             |
| rarity    | TEXT NOT NULL             |
| value     | NUMBER DEFAULT NULL       |
| type      | TEXT NOT NULL             |
| attribute | TEXT DEFAULT NULL         |

## Inventory
| Inventory |                 |
| --------- | --------------- |
| user_id   | NUMBER NOT NULL |
| item_id   | NUMBER NOT NULL |
| amount    | NUMBER NOT NULL |

# Basket
| Basket       |                 |
| ------------ | --------------- |
| user_id      | NUMBER NOT NULL |
| catchable_id | NUMBER NOT NULL |
| amount       | NUMBER NOT NULL |

# Users
| Users        |                             |
| ------------ | --------------------------- |
| user_id      | NUMBER PRIMARY_KEY NOT NULL |
| xp           | NUMBER NOT NULL             |
| gold         | NUMBER NOT NULL             |
| current_area | NUMBER NOT NULL             |
| fish_caught  | NUMBER NOT NULL             |

# Shop
| Shop         |                 |
| ------------ | --------------- |
| catchable_id | NUMBER NOT NULL |
| buy_price    | NUMBER NOT NULL |

