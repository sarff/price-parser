from app.database import MySql
from app.parser import Parce
import toml

if __name__ == '__main__':
    newtable = Parce.returntable()
    MySql.update_price(newtable)
    newtable2 = Parce.returntable_upd()
    MySql.update_upd(newtable2)