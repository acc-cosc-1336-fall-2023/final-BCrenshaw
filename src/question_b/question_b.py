class Stock:

    __stock_file = 'stock_file.dat'
    __stock_dictionary = {}
    with open(__stock_file, "r") as file:
            lines = file.readlines()
            stock_dictionary = {}
            for line in lines:
                symbol, company_name = line.strip().split(',')
                stock_dictionary[company_name] = symbol
    __stock_dictionary = stock_dictionary
    file.close()

    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__stock_dictionary[self.__company_name]

    def get_company_name(self):
        for i in self.__stock_dictionary:
             if self.__symbol == self.__stock_dictionary[i]:
                return i
    
    def list_stock_dictionary_contents(self):
        for i in self.__stock_dictionary:
            print('\t\t' + self.__stock_dictionary[i] + ':\t' + i)
        print('')

    

