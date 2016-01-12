#!/usr/bin/python
# -*- coding: latin-1 -*-
import sqlite3
query_file_01 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_01.txt', 'r').read()
query_file_02 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_02.txt', 'r').read()
query_file_03 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_03.txt', 'r').read()
query_file_04 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_04.txt', 'r').read()
query_file_05 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_05.txt', 'r').read()
query_file_06 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_06.txt', 'r').read()
query_file_07 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_07.txt', 'r').read()
query_file_08 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_08.txt', 'r').read()
query_file_09 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_09.txt', 'r').read()
query_file_10 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_10.txt', 'r').read()
query_file_11 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_11.txt', 'r').read()
query_file_12 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_12.txt', 'r').read()
query_file_13 = open('d:\PrivateGIT\Word_frequency_in_a_book\sqls\part_13.txt', 'r').read()


conn = sqlite3.connect('AnkiCards19.db')
conn.execute(query_file_01)
conn.execute(query_file_02)
conn.execute(query_file_03)
conn.execute(query_file_04)
conn.execute(query_file_05)
conn.execute("INSERT INTO notes VALUES(1398130088495,'Ot0!xywPWG',1342697561419,1398130110,-1,'French','Bonjour�Hello','Bonjour',4077833205,0,'data');")
conn.execute("INSERT INTO notes VALUES(1398130111274,'OQxYbRc]Dm',1342697561419,1398130117,-1,'French','Merci�Thank you','Merci',1273459409,0,'data');")



conn.execute(query_file_08)
conn.execute(query_file_09)
conn.execute(query_file_10)
conn.execute(query_file_11)
conn.execute(query_file_12)
conn.execute('ANALYZE sqlite_master;')
conn.execute("INSERT INTO \"sqlite_stat1\" VALUES('col',NULL,'1');")
conn.execute('CREATE INDEX ix_notes_usn on notes (usn);')
conn.execute('CREATE INDEX ix_cards_usn on cards (usn);')
conn.execute('CREATE INDEX ix_revlog_usn on revlog (usn);')
conn.execute('CREATE INDEX ix_cards_nid on cards (nid);')
conn.execute('CREATE INDEX ix_cards_sched on cards (did, queue, due);')
conn.execute('CREATE INDEX ix_revlog_cid on revlog (cid);')
conn.execute('CREATE INDEX ix_notes_csum on notes (csum);')
#conn.execute('COMMIT;')


#conn.executescript(query_file)
