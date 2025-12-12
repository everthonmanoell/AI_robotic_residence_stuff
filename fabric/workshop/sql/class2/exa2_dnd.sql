DROP SCHEMA IF EXISTS dnd_game;
CREATE DATABASE dnd_game;
USE dnd_game;

CREATE TABLE Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    join_date DATE NOT NULL
);

CREATE TABLE Characters (
    character_id INT AUTO_INCREMENT PRIMARY KEY,
    character_name VARCHAR(100) NOT NULL,
    class VARCHAR(50) NOT NULL,
    race VARCHAR(50) NOT NULL,
    level INT NOT NULL DEFAULT 1,
    player_id INT,
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE SET NULL
);

CREATE TABLE Campaigns (
    campaign_id INT AUTO_INCREMENT PRIMARY KEY,
    campaign_name VARCHAR(100) NOT NULL,
    dungeon_master INT,
    start_date DATE NOT NULL,
    FOREIGN KEY (dungeon_master) REFERENCES Players(player_id) ON DELETE SET NULL
);

CREATE TABLE Campaign_Characters (
    campaign_id INT,
    character_id INT,
    PRIMARY KEY (campaign_id, character_id),
    FOREIGN KEY (campaign_id) REFERENCES Campaigns(campaign_id) ON DELETE CASCADE,
    FOREIGN KEY (character_id) REFERENCES Characters(character_id) ON DELETE CASCADE
);

CREATE TABLE Items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_type VARCHAR(50) NOT NULL,
    rarity VARCHAR(50),
    description TEXT
);

CREATE TABLE Character_Items (
    character_id INT,
    item_id INT,
    quantity INT NOT NULL DEFAULT 1,
    PRIMARY KEY (character_id, item_id),
    FOREIGN KEY (character_id) REFERENCES Characters(character_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES Items(item_id) ON DELETE CASCADE
);

CREATE TABLE Monsters (
    monster_id INT AUTO_INCREMENT PRIMARY KEY,
    monster_name VARCHAR(100) NOT NULL,
    monster_type VARCHAR(50) NOT NULL,
    hit_points INT NOT NULL,
    challenge_rating DECIMAL(3, 1) NOT NULL,
    description TEXT
);

INSERT INTO Players (player_name, email, join_date)
VALUES 
('Alice', 'alice@example.com', '2025-01-15'),
('Bob', 'bob@example.com', '2025-02-10'),
('Charlie', 'charlie@example.com', '2025-03-05');

INSERT INTO Characters (character_name, class, race, level, player_id)
VALUES 
('Tharion', 'Wizard', 'Elf', 5, 1),
('Gorak', 'Barbarian', 'Half-Orc', 3, 2),
('Luna', 'Cleric', 'Human', 4, 1),
('Drex', 'Rogue', 'Halfling', 2, 3);

INSERT INTO Campaigns (campaign_name, dungeon_master, start_date)
VALUES 
('The Lost Mines', 1, '2025-01-20'),
('Curse of Strahd', 2, '2025-02-15');

INSERT INTO Campaign_Characters (campaign_id, character_id)
VALUES 
(1, 1), (1, 2), (2, 3), (2, 4);

INSERT INTO Items (item_name, item_type, rarity, description)
VALUES 
('Sword of Truth', 'Weapon', 'Rare', 'A magical sword that glows in the dark.'),
('Healing Potion', 'Consumable', 'Common', 'Restores 10 HP.'),
('Ring of Invisibility', 'Accessory', 'Legendary', 'Grants temporary invisibility.'),
('Shield of Valor', 'Armor', 'Uncommon', 'A sturdy shield that provides extra protection.'),
('Amulet of Wisdom', 'Accessory', 'Rare', 'Increases intelligence by 2.'),
('Boots of Speed', 'Accessory', 'Uncommon', 'Increases movement speed by 10 feet.'),
('Staff of Fire', 'Weapon', 'Rare', 'A staff that can cast fire spells.'),
('Cloak of Protection', 'Armor', 'Rare', 'Grants a +1 bonus to AC and saving throws.'),
('Belt of Giant Strength', 'Accessory', 'Very Rare', 'Increases strength to 25.'),
('Potion of Giant Strength', 'Consumable', 'Rare', 'Increases strength to 25 for 1 hour.'),
('Wand of Magic Missiles', 'Weapon', 'Uncommon', 'A wand that casts magic missiles.'),
('Gauntlets of Ogre Power', 'Accessory', 'Rare', 'Increases strength to 19.'),
('Bracers of Defense', 'Armor', 'Uncommon', 'Grants a +2 bonus to AC when not wearing armor.'),
('Ring of Protection', 'Accessory', 'Rare', 'Grants a +1 bonus to AC and saving throws.'),
('Potion of Healing', 'Consumable', 'Common', 'Restores 2d4 + 2 HP.');

INSERT INTO Character_Items (character_id, item_id, quantity)
VALUES 
(1, 1, 1), (1, 2, 3), (2, 2, 2), (3, 3, 1);
