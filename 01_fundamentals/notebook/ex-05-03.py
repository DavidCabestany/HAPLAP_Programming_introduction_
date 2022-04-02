def londons_weather(temp :int, iPath :str, oPath:str):
    import pandas as pd
    
    iFile = pd.read_csv(iPath, sep = '\t')
     
    temp_av= 0
    t_entry = 0
    s_rain = 0
    wind_av = 0
    
    for index, value in iFile.iterrows():
        if value['Temperature'] >= temp:
            temp_av += value['Temperature']
            t_entry +=1
            s_rain += value['Precipitation']
            wind_av += value['Wind-speed']
    
    temp_av = temp_av/t_entry
    wind_av = wind_av/t_entry
    outFile = open(oPath, 'w')
    
    txt1 = "Total entries: {}\nAverage temperature: {}\nTotal precipitation: {}\nAverage wind-speed: {}".format(t_entry,
                                                                                                               format(temp_av, '.2f'), 
                                                                                                               format(s_rain, '.2f'), 
                                                                                                               format(wind_av, '.2f'))
    
    oFile = iFile[['Year','Month', 'Day', 'Temperature', 'Precipitation', 'Wind-speed']]
    df_tail = iFile[['Temperature', 'Precipitation', 'Wind-speed']]
    
    df_head = oFile.assign(Date = oFile.Year.astype(str) + '-' + oFile.Month.astype(str) + '- ' + oFile.Day.astype(str))
    output = pd.concat([df_head, df_tail], ignore_index=True, sort=False)
    output = output[['Date', 'Temperature', 'Precipitation', 'Wind-speed']]
    
    output.to_csv(oPath, sep='\t', index=False)
    
    return txt1.strip()
    