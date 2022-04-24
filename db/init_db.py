import os
import psycopg2

def getConnection():
    conn = psycopg2.connect(host='ec2-3-230-122-20.compute-1.amazonaws.com',
                            database='d16l4f8fojv0d3',
                            user='dgsitkfgyzkuev',
                            password='5bab5efdefe1923873c82735d8dcc559c38c4fde5d6b4d6666cc0b920754079b')
    return conn

