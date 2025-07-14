import psycopg
from config import load_config

def connect(config):
    psycopg.connect("dbname=postgres  user=postgres password=password host=localhost port=5433") as conn:
            


if __name__ == '__main__':

