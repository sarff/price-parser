from app.database import MySql
from app.parser import Parce
import toml

if __name__ == '__main__':
    config = toml.load("conf/config.toml")
    # config = toml.load("/root/priceupdate/price-parser/conf/config.toml")
    updwhere = config.get('dbtable').get('updwhere')
    updwhere2 = config.get('dbtable').get('updwhere2')

    newtable = Parce.returntable()
    MySql.update_price(newtable, updwhere)
    newtable2 = Parce.returntable_upd()
    MySql.update_price(newtable2, updwhere2)