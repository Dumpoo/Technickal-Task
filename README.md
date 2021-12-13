# Technical-Task

В данном репозитории присутствует 3 python файла (task_1.py, task_2.py, task_3.py), каждый из которых соответствует одному из 3-х заданий.</br>
Список зависимостей находится в файле freeze.txt

1. task_1.py - это парсер данных из JSON файлов в Ecxel таблицы. Для корректной работы парсера достаточно убедиться, что .json файлы находятся с ним в одной директории.
</br>После чего выполните команду: <code><b>python task_1.py</b></code> для запуска скрипта. В тойже директории появится файл <code><b>result.xlsx</b></code>
2. task_2.py - это скрипт, который выполняет REST запрос на сайт: <a>https://service.nalog.ru/addrno.do</a> и выгружает оттуда актуальные платежные реквизиты в виде массива данных.</br>
Использовать скрипт можно 3-мя способами:</br>
   * Запустить скритп через терминал <code><b>python task_2.py</b></code> или IDLE, после чего он последовательно попросит ввести пользователя код ИФНС и ОКТМО.
   * Запустить скрипт через терминал с передачей аргументов: <code><b>python task_2.py ифнс октмо</b></code>. </br>Пример: <code><b>python task_2.py 7840 40913000</b></code>
   * Импортировать скрипт, как модуль в своем проекте. </br>Пример:</br>
      ```
      from task_2 import input_handler
      
      info = input_handler(7840, 40913000)
      print(info)
      ```
3. task_3.py - это скрипт, выполняющий <b>SELECT</b> запросы в базу данных SQLite3.</br>
  Использовать скрипт можно 3-мя способами:</br>
   * Запустить скритп через терминал <code><b>python task_3.py</b></code> или IDLE, после чего он попросит указать путь к файлу, после чего нужно будет ввести спсиок методов через запятую.</br> 
     Пример: <code><b>Enter which methods you want to use: loc-with-purchases, lop-with-orders, loc-who-bought-product:2</b></code></br>
   * Запустить скрипт через терминал с передачей аргументов.</br>
     Пример: <code><b>python task_3.py path:task.db loc-with-purchases lop-with-orders</b></code></br>
     
     Список методов:</br>
      <code><b>loc-with-purchases</b></code> - Возвращает список клиентов с общей суммой их покупок.</br>
      <code><b>lop-with-orders</b></code> - Возвращает список товаров с указанием количества их заказов.</br>
      <code><b>loc-who-bought-product</b></code> - Возвращает список клиентов, которые приобрели продукт. Для работы нужно указать id продукта через двоеточие.
      
   * Импортировать скрипт, как модуль в своем проекте. </br>Пример:</br>
      ```
      from task_3 import Database
      
      db = Database('task.db')
      
      print(db.list_of_clients_with_purchases())
      print(db.list_of_products_with_orders())
      print(db.list_of_clients_who_bought_product(5))
      ```
