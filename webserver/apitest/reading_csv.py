import csv

csvFileDir = "theater_info.txt"
csvFile = open(csvFileDir, 'r', encoding='UTF-8')
try:
    spamreader = csv.reader(csvFile)
    for row in spamreader:
        print("theatherName:{}, theaterCode:{}, regionCode:{}, brand:{}, latitude:{}, longitude:{}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        #print(', '.join(row))
finally:
    csvFile.close()