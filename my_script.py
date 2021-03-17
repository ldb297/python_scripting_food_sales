# Read only

def read_only():
    #a method that only reads the file
    try: #try and except for error handling
        file1 = open('data.txt', 'r') #passing second parameter 'r' allows read only
        text = file1.read()
        print(text)
        file1.close() #in python, file will remain open in memory until it is closed
    except FileNotFoundError:
        text = None
        print(text)

def write_only():
    #a method that only writes to a file
        #if(file): will be overwritten
        #if(!file): will be created
        file2 = open('more_data.txt', 'w')
        file2.write('tomatoes')
        file2.close()

# #python will automagically close this file, even with errors
# with open('data.txt') as f:
#     txt = f.read()
#     print(txt)

def read_food_sales():
    all_dates = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        
        for food_sale in data:
            split_food_sale = food_sale.split(',')
            order_date = split_food_sale[0]
            all_dates.append(order_date)
    print(all_dates)

    with open('dates.txt', 'w') as f:
        for date in all_dates:
            f.write(date)
            f.write('\n')

def append_text():
    #append data to an existing file
    with open('dates.txt', 'a') as f:
        f.write('3/17/2021')
        print('done')

def read_region():
    all_regions = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()

        for food_sale in data:
            split_food_sale = food_sale.split(',')
            order_region = split_food_sale[1]
            all_regions.append(order_region)
    print(all_regions)

    with open('regions.txt', 'a') as f:
        for region in all_regions:
            f.write(region)
            f.write('\n')

def read_city():
    all_cities = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()

        for food_sale in data:
            split_food_sale = food_sale.split(',')
            order_city = split_food_sale[2]
            all_cities.append(order_city)
    print(all_cities)

    with open('cities.txt', 'a') as f:
        for city in all_cities:
            f.write(city)
            f.write('\n')
            

if __name__ == '__main__':
    #read_only()
    #write_only()
    #read_food_sales()
    append_text()