# csv-to-json
## This library converts .csv to .json  
Example:  
.csv file format (Input) 
```
key,en,id,ms,zh
search,Search,Cari,Cari,搜索
settings,Settings,Pengaturan,Tetapan,设置
```

.json file format (Output)
```
{"translations": [{"key": "search", "value": "Search"}, {"key": "settings", "value": "Settings"}]}
```

4 json files will be created due to 4 different keys, the output is inside `./output` directory

## Commands to run:  
`python3 csv_to_json.py ./example.csv`
