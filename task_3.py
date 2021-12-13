import sqlite3
import sys


class Database:
    def __init__(self, path: str = None, db_name: str = None):
        """
        To connect to the database, it is enough to specify the file name, but only if the database file is located
        in the same directory as the executable file of this script, otherwise you should specify the path
        to the database file and its name.
        In the path to the database file, you can immediately add its name,
        in this case, you do not need to specify the name of the database file separately.
        """

        if path and db_name:
            self.connection = sqlite3.connect(path + db_name)
        elif path or db_name:
            self.connection = sqlite3.connect(path or db_name)
        else:
            raise Exception('The path and name of the database file is missing.')

        self.cursor = self.connection.cursor()

    def list_of_clients_with_purchases(self):
        """Returns a list of customers with the total amount of their purchases"""

        self.cursor.execute(
            """
            select Clients.user_name, sum(Products.price) from Orders
            join Clients on Orders.id_users = Clients.id_users
            join Products on Orders.id_product = Products.id_product
            group by Clients.user_name
            order by Clients.id_users
            """
        )
        return self.cursor.fetchall()

    def list_of_clients_who_bought_product(self, product_number: int):
        """Returns a list of customers who have purchased the product specified in the argument product_number."""

        self.cursor.execute(
            f"""
            select Clients.user_name from Orders
            join Clients on Orders.id_users = Clients.id_users
            where Orders.id_product = {product_number}
            """
        )
        return self.cursor.fetchall()

    def list_of_products_with_orders(self):
        """Returns a list of products with the number of their orders"""

        self.cursor.execute(
            """
            select Products.product_name, count(Orders.id_product) from Orders
            join Products on Orders.id_product = Products.id_product
            group by Products.product_name
            """
        )
        return self.cursor.fetchall()


def output(output_list: list):
    for element in output_list:
        if len(element) > 1:
            output_string = ''
            for sub_element in element:
                output_string += str(sub_element) + ' : '
            print(output_string[:len(output_string)-3])
        else:
            print(*element)
    print('\n')


def terminal_handler(args: list, db: Database):
    for argument in args:
        if 'loc-with-purchases' in argument:
            output(db.list_of_clients_with_purchases())
        if 'lop-with-orders' in argument:
            output(db.list_of_products_with_orders())
        if 'loc-who-bought-product' in argument:
            output(db.list_of_clients_who_bought_product(argument[23:]))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        db = Database(input('Enter path to database file: '))
        terminal_handler(
            [args for args in input('Enter which methods you want to use: ').split(',')],
            db
        )
        input()
    else:
        db = Database(sys.argv[1][5:])

        if sys.argv[2:]:
            terminal_handler(sys.argv[2:], db)
        else:
            terminal_handler(
                [args for args in input('Enter which methods you want to use: ').split(',')],
                db
            )
        input()
