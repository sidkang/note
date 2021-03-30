import wbdata
import datetime as dt

indicatorSelection = {"DT.DOD.DLXF.CD": "ExternalDebtStock"}

# NY.GDP.DEFL.KD.ZG

locationSelection = ["US", "SSA", "SAS", "LAC", "MNA", "EAP"]

timeSelection = (dt.datetime(2009, 1, 1), dt.datetime(2018, 12, 31))

IDS = wbdata.get_source(source_id=6)

print(IDS)
