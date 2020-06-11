
# .. ................................................................................... .. #
# .. Proyecto: UrbanLab - Plataforma de ayuda para micro y pequeñas empresas             .. #
# .. Archivo: datos.py - procesos de obtencion y almacenamiento de datos                 .. #
# .. Desarrolla: ITERA LABS, SAPI de CV                                                  .. #
# .. Licencia: Todos los derechos reservados                                             .. #
# .. Repositorio: https://github.com/IFFranciscoME/Urban_Lab.git                         .. #
# .. ................................................................................... .. #


# Importing and initializing main Python libraries
import pandas as pd
import numpy as np
import entradas as ent


# -- ------------------------------------------------------------------------------------ -- #
# -- Function: Read data file and storing it in to a DataFrame
# -- ------------------------------------------------------------------------------------ -- #
def read_file(file_path, sheet):
    """
    Parameters
    ---------
    :param:
        file: str : nombre de archivo leer
		sheet: str : nombre de la pestana
    Returns
    ---------
    :return:
        df_data: DataFrame : Datos del archivo

    Debuggin
    ---------
        file_path = 'Base_de_datos.xlsx'
		sheet = 'IIEG_E_1'

    """
    # Leer archivo xls
    df_data = pd.read_excel('archivos/' + file_path, sheet_name=sheet)
    return df_data

df_data = read_file(ent.path, ent.sheet)


# -- ------------------------------------------------------------------------------------ -- #
# -- Function: Cleaning Database that is in a DataFrame
# -- ------------------------------------------------------------------------------------ -- #
def clear_data(df_data):
    """
    Parameters
    ---------
    :param:
        df_data: DataFrame : datos en DF

    Returns
    ---------
    :return:
        df: DataFrame : Datos del archivo

    Debuggin
    ---------
        df_data = read_file(ent.path, ent.sheet)

    """
    df = df_data.copy()
    df.replace([998, 999, 'No contesto', 'No sé'], np.nan, inplace=True)

    return df

df = clear_data(df_data)