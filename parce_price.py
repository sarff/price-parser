from app.database import MySql
from app.parser import Parce

if __name__ == '__main__':
    newtable = Parce.returntable()
    MySql.update_price(newtable)