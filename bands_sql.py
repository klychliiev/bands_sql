from multiprocessing import connection
import sqlite3

conn = sqlite3.connect("music_band.db")

c = conn.cursor()

c.execute(""" CREATE TABLE bands(
    band_id integer NOT NULL,
    name text NOT NULL,
    num_members integer NOT NULL,
    last_album text NOT NULL,
    residence text NOT NULL
)
""")

c.execute("INSERT INTO bands VALUES (1,'Pusca',3,'Ephemere','Lviv')")
c.execute("INSERT INTO bands VALUES (2, 'White Ward',5,'False Light','Odesa')")
c.execute("INSERT INTO bands VALUES (3, 'Drudkh',4,'A few lines in Archaic Ukrainian', 'Kharkiv')")
c.execute("INSERT INTO bands VALUES (4, 'КАТ',3,'Поклик','Kharkiv')")
c.execute("INSERT INTO bands VALUES (5, 'Mauser',3,'Self-Titled','Lviv')")

c.execute("SELECT * from bands WHERE num_members=3 ")

print(c.fetchall())

c.execute("UPDATE bands SET num_members=4 WHERE name='Mauser'")

c.execute("SELECT * from bands WHERE num_members=3 ")

c.execute("SELECT * FROM bands")

print(c.fetchall())

c.execute("INSERT INTO bands VALUES (6, 'DakhaBrakha',4,'Alambari','Kyiv')")
c.execute("INSERT INTO bands VALUES (7, 'Nokturnal Mortum',5,'До лунарної поезії','Kharkiv')")
c.execute("INSERT INTO bands VALUES (8, 'Lucifugum',2,'Infernalistica','Zhytomyr')")

c.execute("SELECT * FROM bands")

print(c.fetchall())

conn.commit()

conn.close()