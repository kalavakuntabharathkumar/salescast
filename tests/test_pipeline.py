import pandas as pd
from src.pipeline import prepare

def test_prepare_removes_missing_rows():
    df = pd.DataFrame({
        "Store":[1,2], "Dept":[1,1], "IsHoliday":[False,False],
        "Size":[100,100], "Temperature":[70,71], "Fuel_Price":[3.0,3.1],
        "CPI":[200,201], "Unemployment":[7,7], "Weekly_Sales":[1000,1100]
    })
    X, y = prepare(df)
    assert len(X) == 2
    assert len(y) == 2
