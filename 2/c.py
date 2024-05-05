import json

def data_convert(data):

  datalist = []
  for annotation in data["annotations"]:
    for result in annotation["result"]:
      if result["from_name"] == "transcription":
        text = result["value"]["text"][0]
        points = result["value"]["points"]
        dict = {
            "transcription": text,
            "points": points
        }
        datalist.append(dict)
  return datalist

fr = open("need_to_process.json","r")
fw = open("target.txt",'w')
fw.write(str(data_convert(json.load(fr))))
