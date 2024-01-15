print(60 * '-')
while True:


    var0 = str(input('Nome completo : ').strip())
    kaz = 0
    def func():
        print('minusculo: ' + var0.lower())
        print('maiusculo: ' + var0.upper())
        print('total de letra: {}'  .format(var0.strip().__len__() - var0.count(' ')))
        splitter = var0.split()    
    
        kaz = int(len(splitter) - 1)
        print('seu primeiro nome é : {} e tem {} letras' .format(splitter[0].capitalize(), splitter[0].__len__()))

        print('seu sobrenome é : {} e tem {} letras' .format(splitter[kaz].capitalize() , splitter[kaz].__len__()) )
        print(100 * '-')

    func()

