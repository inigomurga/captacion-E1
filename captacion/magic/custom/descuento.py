if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
from sqlalchemy import create_engine

@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    user = 'usuario'
    password = 'contrasena'
    host = 'postgres-magic'
    port = '5432'
    database = 'dbproyecto'

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    connection = engine.connect()

    df = pd.read_sql("SELECT * FROM productos", con=connection)
    
    df['precio_descuento'] = df['precio'] * 0.8

    df.to_sql('productos_descuento', con=connection, if_exists='replace', index=False)

    connection.close()
    
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
