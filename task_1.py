import xlsxwriter
import json
import os
import re


found_files = [file for file in os.listdir() if '.json' in file]
table_info = {}
search_patterns = ['\d+,\d\d', '[A-Z]{3}', '\d\d-\d+', '']

if found_files:
    with xlsxwriter.Workbook('result.xlsx') as workbook:
        list_number = 1

        for xl_list in found_files:
            with open(xl_list, 'rb') as file:
                data = json.load(file)

            header_format = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'valign': 'top'
            })

            worksheet = workbook.add_worksheet(f'List_{list_number}')
            worksheet.set_column(0, len(data['headers'])-1, 15)

            col = 0
            headers_row = []
            value_columns = []

            for index, header in enumerate(data['headers']):
                headers_row.append(header['properties']['QuickInfo'])
                value_columns = []

                for value in data['values']:
                    val = value['properties']['Text']

                    if index < 3 and re.search(search_patterns[index], val):
                        value_columns.append(val)
                    elif index == 3 and len(val) < 3:
                        value_columns.append(val)

                worksheet.write_column(1, col, value_columns)
                col += 1

            worksheet.write_row(0, 0, headers_row, header_format)
            list_number += 1
else:
    raise Exception('JSON files is not found.')
