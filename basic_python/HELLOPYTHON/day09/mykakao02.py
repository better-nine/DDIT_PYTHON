import json
#ctrl + shift + F : 제이슨 자동정렬


with open('mykakao.json','rt',encoding='UTF8') as json_file:
    json_data = json.load(json_file)
    
#   json_data["documents"][0].values()
#   for j in json_data["documents"][0].values():
#       print(j)
    
    for i in range(len(json_data["documents"])):
        collection = json_data["documents"][i]["collection"]
        datetime = json_data["documents"][i]["datetime"]
        sitename = json_data["documents"][i]["display_sitename"]
        doc_url = json_data["documents"][i]["doc_url"]
        thumbnail = json_data["documents"][i]["thumbnail_url"]
        image = json_data["documents"][i]["image_url"]
        width = json_data["documents"][i]["width"]
        height = json_data["documents"][i]["height"]
        
        print("collection:", collection)
        print("datetime:", datetime)
        print("sitename:", sitename)
        print("doc_url:", doc_url)
        print("thumbnail:", thumbnail)
        print("image:", image)
        print("width:", width)
        print("height:", height)
        print()
        