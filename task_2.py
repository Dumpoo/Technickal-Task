import requests
import sys


def _get_payee_details(ifns: str, oktmmf: str) -> list:
    payload = {
        'c': 'next',
        'step': '1',
        'npKind': 'fl',
        'objectAddr': '',
        'objectAddr_zip': '',
        'objectAddr_ifns': '',
        'objectAddr_okatom': '',
        'ifns': ifns,
        'oktmmf': oktmmf,
        'PreventChromeAutocomplete': ''
    }

    response = requests.post('https://service.nalog.ru/addrno-proc.json', data=payload)
    response_data = response.json()

    return [
        response_data['payeeDetails']['payeeName'],
        response_data['payeeDetails']['payeeInn'],
        response_data['payeeDetails']['payeeKpp'],
        response_data['payeeDetails']['bankName'],
        response_data['payeeDetails']['bankBic'],
        response_data['payeeDetails']['payeeAcc']
    ]


def input_handler(ifns: str = None, oktmmf: str = None) -> list:
    if ifns and oktmmf:
        return _get_payee_details(ifns, oktmmf)
    elif ifns or oktmmf:
        raise Exception('The function got 2 arguments, but given 1')
    else:
        return _get_payee_details(input('Enter Federal Tax Service Inspection code: '), input('Enter Municipality code: '))


if __name__ == '__main__':
    try:
        print(input_handler(sys.argv[1], sys.argv[2]))
    except IndexError:
        print(input_handler())
