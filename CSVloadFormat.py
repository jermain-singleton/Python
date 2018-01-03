from urllib import request
#what we want to download
goog_url = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1510069610&period2=1512661610&interval=1d&events=history&crumb=mw8tkvU7rLo.csv"
#my function
def download_stock_data(csv_url):
    #connect
    response = request.urlopen(csv_url)
    csv = response.read()
    #save it as a string
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    #make a file on local PC
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    #write to the file
    for line in lines:
        fx.write(line + "\n")
        #close file
    fx.close()

download_stock_data(goog_url)
