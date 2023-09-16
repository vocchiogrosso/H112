import msoffcrypto
import io
import pandas as pd
import json
import copy

tripTypeDict = ["Outbound", "Inbound"]
countryDict = ["ARG", "MEX"]

def extract_df():
    temp = io.BytesIO()

    rawFile = "./_raw/HZ_2023_ #01 Holcim MAQER Ventures_Logistics data MEX _ ARG YTD 2023.xlsx"
    password = "HMV*#01SL2023*"

    with open(rawFile, 'rb') as f:
        excel = msoffcrypto.OfficeFile(f)
        excel.load_key(password)
        excel.decrypt(temp)

    sheet_names = []
    for country in countryDict:
        for tripType in tripTypeDict:
            sheet_names.append(tripType + " " + country)

    dfs = {}
    for sheet_name in sheet_names:
        dfs.update({sheet_name: pd.read_excel(temp, sheet_name)})
        # import ipdb; ipdb.set_trace()
    del temp

    return dfs

def getcolumns(DFs, columns, new_keys, InOut):
    dicts = {}
    for country in countryDict:
        # import ipdb; ipdb.set_trace()
        sheet_name = InOut + country
        df = DFs[sheet_name]
        slices = df[columns]
        location = slices[columns[0]].tolist()
        data = slices[columns[1:]].values.tolist()

        # data_dicted = dict(zip(columns[1:], data))
        cur_dict = dict(zip(location, data))
        for k, v in cur_dict.items():
            cur_dict[k] = dict(zip(new_keys[1:], v))

        # import ipdb; ipdb.set_trace()
        dicts.update({sheet_name: cur_dict})
    return dicts
    

def getPlantsInfo(DFs, columns = ['Plant', 'Plant Name', 
                                 'Plant Latitude', 'Plant Longitude']):
    # import ipdb; ipdb.set_trace()
    new_keys = copy.deepcopy(columns)
    new_keys[2] = "Latitude"
    new_keys[3] = "Longitude"
    return getcolumns(DFs, columns, new_keys, "Outbound ")

def getClientInfo(DFs, columns = ['Client Code', 
                                  'Client Latitude', 'Client Longitude',
                                  'City']):
    new_keys = copy.deepcopy(columns)
    new_keys[1] = "Latitude"
    new_keys[2] = "Longitude"
    return getcolumns(DFs, columns, new_keys, "Outbound ")

def getProviderInfo(DFs, columns = ['Origin Code', 'Origin', 
                                    'Origin Latitude', 'Origin Longitude',
                                    'INCOTERMS',
                                    'Material Code', "Material"
                                    ]):
    new_keys = copy.deepcopy(columns)
    new_keys[2] = "Latitude"
    new_keys[3] = "Longitude"
    return getcolumns(DFs, columns, new_keys, "Inbound ")
            
#Done: get info about vehicles
# [Type], Capacity
def getVehicleInfo(DFs, columns = ['Vehicle Number', 'Type of Vehicle', 'Vehicle Capacity [tons]']):
    return getcolumns(DFs, columns, columns, "Outbound ")

#TODO: get info for route (seperate in and out)
# [RouteID], StartPoint, EndPoint, Distance, (AVG speet50), Freight Cost Per Ton(AVG), 
# Freight Cost Per Ton [$/ton]

# columns = ['Route ID', 'Route', 'Plant', 'Client Code', 
#                                     'Distance [km]'], val = ['Freight Cost Per Ton [$/ton]']):
def getAvgColums(DFs, columns, InOut, toAvg):
    dicts = {}
    for country in countryDict:
        # import ipdb; ipdb.set_trace()
        sheet_name = InOut + country
        df = DFs[sheet_name]
        df = df.drop(df[df[toAvg[0]] == '-'].index)
        slices = df[columns + toAvg]

        # import ipdb; ipdb.set_trace()
        grouped = slices[[columns[0], toAvg[0]]].groupby(columns[0])
        data_avg = grouped.mean()#.reset_index()

        data_all = slices[columns].groupby(columns[0]).first()#.reset_index()
        cur_df = pd.concat([data_all, data_avg], axis=1)

        # import ipdb; ipdb.set_trace()
        dicts.update({sheet_name: cur_df.to_dict('index')})
    return dicts
    
def getOutRouteInfo(DFs, columns = ['Route ID', 'Route', 'Plant', 'Client Code', 
                                    'Distance [km]'], val = ['Freight Cost Per Ton [$/ton]']):
    return getAvgColums(DFs, columns, "Outbound ", val)

def getInRouteInfo(DFs, columns = ['Route ID', 'Route', 'Origin Code', 'Destination Code',
                                   'Distance [km]'], val = ['Freight Cost Per Ton [$/ton]']):
    return getAvgColums(DFs, columns, "Inbound ", val)

if __name__ == "__main__":
    DFs = extract_df()
    DATAPATH = "./data/"
    infoPlants = getPlantsInfo(DFs) #, columns = ['Plant', 'Plant Name'])
    json.dump(infoPlants, open(DATAPATH + "infoPlants.json", "w"), indent=4)
    json.dump(getClientInfo(DFs), open(DATAPATH + "infoClients.json", "w"), indent=4)
    json.dump(getProviderInfo(DFs), open(DATAPATH + "infoProviders.json", "w"), indent=4)
    json.dump(getVehicleInfo(DFs), open(DATAPATH + "infoVehicles.json", "w"), indent=4)
    
    json.dump(getOutRouteInfo(DFs), open(DATAPATH + "infoOutRoutes.json", "w"), indent=4)
    json.dump(getInRouteInfo(DFs), open(DATAPATH + "infoInRoutes.json", "w"), indent=4)
    
    # print(DFs)