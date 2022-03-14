#Python 3.5.2
import urllib.request
import imgkit

url1 = "https://trust.yandex.ru/receipts/124-9bba9b3f6beb3b7cb701b8c1023a90e6/"

def k_url_pars(url):
    f = urllib.request.urlopen(url)
    page = f.read().decode("utf-8")
    f.close
    return(page)

def k_search_info_N(page_material):
    index_start = page_material.find('class="info-table')
    index_start = index_start + 59
    index_stop = page_material.find('</td', index_start)
    return(page_material[index_start:index_stop])

def k_search_info_Date(page_material):
    index_start_temp = page_material.find('class="info-table')
    index_start_temp = page_material.find('Смена', index_start_temp)
    index_start = page_material.find('</td>', index_start_temp)
    index_start = index_start + 9
    index_stop = index_start + 8
    return(page_material[index_start:index_stop])

def k_search_info_Total(page_material):
    index_start_temp = page_material.find('Итого')
    index_start = page_material.find('<td>', index_start_temp + 5)
    index_start = index_start + 4
    index_stop = page_material.find('</'    , index_start)
    index_stop = index_stop - 4
    return(page_material[index_start:index_stop])

def k_write_2file(name,data1,data2,data3):
    f = open(name, "a")
    f.write(data1 + "\t" + data2 + "\t" + data3 + "\t")
    f.write("\n")
    f.close()

strFile = open("urllist.txt" , "r")
for nextUrl in strFile:
    #nextUrl = strFile.readline()
    if nextUrl:
        material = k_url_pars(nextUrl)
        resultN = k_search_info_N(material)
        resultDate = k_search_info_Date(material)
        resultTotal = k_search_info_Total(material)
        print(nextUrl)
        picName = str(resultDate + " " + resultN + ".jpg")
        imgkit.from_url(nextUrl,picName)
        Xfile = "test.txt"
        k_write_2file(Xfile,resultDate,resultN,resultTotal)

#print(resultN)
#print(resultDate)
#print(resultTotal)
