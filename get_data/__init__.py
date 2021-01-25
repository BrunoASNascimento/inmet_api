from datetime import datetime, timedelta
import requests
import pandas as pd


def cleaner_data(data):
    columns = ['ESTACAO', 'LATITUDE', 'LONGITUDE', 'ALTITUDE', 'ANO', 'MES', 'DIA', 'HORA', 'TEMP', 'TMAX', 'TMIN', 'UR', 'URMAX', 'URMIN',
               'TD', 'TDMAX', 'TDMIN', 'PRESSAONNM', 'PRESSAONNM_MAX', 'PRESSAONNM_MIN', 'VELVENTO', 'DIR_VENTO', 'RAJADA', 'RADIACAO', 'PRECIPITACAO']
    df = pd.DataFrame(columns=columns)

    for i in range(1, len(data)):
        try:
            dado = [data[i].split(' ')]
            dado = pd.DataFrame(dado, columns=columns)
            # print(dado)
            df = df.append(dado)
        except:
            pass

    str_float = ['LATITUDE', 'LONGITUDE', 'ALTITUDE',
                 'TEMP', 'TMAX', 'TMIN', 'UR', 'URMAX', 'URMIN',
                 'TD', 'TDMAX', 'TDMIN',
                 'PRESSAONNM', 'PRESSAONNM_MAX',
                 'PRESSAONNM_MIN', 'VELVENTO', 'DIR_VENTO',
                 'RAJADA', 'RADIACAO', 'PRECIPITACAO']
    str_int = ['ANO', 'MES', 'DIA', 'HORA']

    df[str_float] = df[str_float].astype('float')
    df[str_int] = df[str_int].astype('int64')

    print(df.head)


def get_data():
    date_now = datetime.utcnow()
    date_delta = date_now - timedelta(days=1)
    date_str = date_delta.strftime("%Y%m%d")

    for hour in range(0, 24):
        print(hour)
        url = ("http://master.iag.usp.br/fig_dados/OBSERVACAO/INMET/UND_inmet_" +
               str(date_str)+str(hour).zfill(2)+"00.txt")
        # print(url)
        response = requests.request("GET", url)
        data = response.text.split('\n')
        print(len(data))
        cleaner_data(data)
    return data


cleaner_data(get_data())
