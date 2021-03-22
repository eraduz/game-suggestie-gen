import sqlite3

conn = sqlite3.connect('games.db')

c = conn.cursor()

# c.execute("SELECT * FROM games")
# print(c.fetchall())

# Create games table
# c.execute("""
#     CREATE TABLE IF NOT EXISTS games (
# 	id integer PRIMARY KEY,
# 	naam text NOT NULL,
# 	jaartal text,
# 	genre text,
#     uitgever text,
#     rating int
#     );
# """)
# conn.commit()

# add records to db
# c.execute("INSERT INTO games VALUES (2, 'Apex Legends', '2019', 'Battle Royale', 'Respawn Entertainment', 10)")
# c.execute("INSERT INTO games VALUES (3, 'Call of Duty: Modern Warfare', '2019', 'FPS', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (4, 'Among us', '2020', 'Casual', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (5, 'FIFA 21', '2020', 'Sports', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (6, 'The Sims 4', '2020', 'Casual', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (7, 'Tom Clancy Rainbow Six Siege', '2020', 'FPS', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (8, 'Old School RuneScape', '2020', 'MMO', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (9, 'Marbles on Stream', '2020', 'Casual', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (10, 'Plasmophobia', '2020', 'Horror', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (11, 'Overwatch', '2020', 'FPS', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (12, 'Animal Crossing', '2020', 'Casual', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (13, 'Valheim', '2020', 'Survival', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (14, 'Roblox', '2020', 'Casual', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (15, 'World of Warcraft', '2020', 'MMORPG', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (16, 'Dead by Daylight', '2020', 'Horror', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (17, 'Call of Duty: Black Ops', '2020', 'FPS', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (18, 'Rust', '2020', 'Survival', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (19, 'Sea of Thieves', '2020', 'Adventure', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (20, 'Brawlhalla', '2020', 'Casual', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (21, 'DayZ', '2020', 'Survival', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (22, 'Mario Kart 8', '2020', 'Casual', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (23, 'Player Unknowns Battleground', '2020', 'Battle Royale', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (24, 'Age of Empires II', '2020', 'RTS', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (25, 'Genshin Impact', '2020', 'Adventure', 'Steam', 10)")
# c.execute("INSERT INTO games VALUES (26, 'RuneScape', '2020', 'MMO', 'Steam', 10)")

# print('Succesful added to db')
# conn.commit()

#Delete table
# c.execute("""DROP TABLE games""")



#View all tables
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(c.fetchall())

# conn.close()

