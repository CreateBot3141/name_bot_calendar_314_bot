
def get_menu  (user_id,namebot):
        import iz_telegram
        from telebot import types          
        message_out,menu = iz_telegram.get_message (user_id,'Начальное сообщение',namebot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu11 = 'Январь'
        menu12 = 'Февраль'
        menu13 = 'Март'
        menu21 = 'Апрель'
        menu22 = 'Май'
        menu23 = 'Июнь'
        menu31 = 'Июль'
        menu32 = 'Август'
        menu33 = 'Сентябрь'
        menu41 = 'Октябрь'
        menu42 = 'Ноябрь'
        menu43 = 'Декабрь'
        menu51 = "Настройки"
        year   = iz_telegram.load_variable (user_id,namebot,"Year")

        if year == '':
            year = '2021'

        if year == '2021':
            menu52 = iz_telegram.get_namekey (user_id,namebot,'V 2021')

        if year == '2022':
            menu52 = iz_telegram.get_namekey (user_id,namebot,'V 2022')

        if year == '2023':
            menu52 = iz_telegram.get_namekey (user_id,namebot,'V 2023')

        if year == '2024':
            menu52 = iz_telegram.get_namekey (user_id,namebot,'V 2024')

        markup.row(menu11,menu12,menu13)
        markup.row(menu21,menu22,menu23)
        markup.row(menu31,menu32,menu33)
        markup.row(menu41,menu42,menu43)
        markup.row(menu51,menu52)
        return markup

def get_years (year,user_id,namebot):
        import iz_telegram
        from telebot import types          
        message_out,menu = iz_telegram.get_message (user_id,'Начальное сообщение',namebot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        year   = iz_telegram.load_variable (user_id,namebot,"Year")

        if year == '2021':
            menu11 = iz_telegram.get_namekey (user_id,namebot,'V 2021')
        else:    
            menu11 = iz_telegram.get_namekey (user_id,namebot,'2021')


        if year == '2022':
            menu12 = iz_telegram.get_namekey (user_id,namebot,'V 2022')
        else:    
            menu12 = iz_telegram.get_namekey (user_id,namebot,'2022')


        if year == '2023':
            menu13 = iz_telegram.get_namekey (user_id,namebot,'V 2023')
        else:    
            menu13 = iz_telegram.get_namekey (user_id,namebot,'2023')
        menu14 = iz_telegram.get_namekey (user_id,namebot,'Назад')
        markup.row(menu11)
        markup.row(menu12)
        markup.row(menu13)
        markup.row(menu14)
        return markup 

def category_menu (user_id,namebot):
    import iz_telegram
    from telebot import types          
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Category01 = iz_telegram.load_variable (user_id,namebot,"Category01")
    Category02 = iz_telegram.load_variable (user_id,namebot,"Category02")
    Category03 = iz_telegram.load_variable (user_id,namebot,"Category03")
    Category04 = iz_telegram.load_variable (user_id,namebot,"Category04")
    Category05 = iz_telegram.load_variable (user_id,namebot,"Category05")
    if Category01 == '':
        menu11 = iz_telegram.get_namekey (user_id,namebot,'Все категории')
    else:    
        menu11 = iz_telegram.get_namekey (user_id,namebot,'V Все категории')
    if Category02 == '':    
        menu21 = iz_telegram.get_namekey (user_id,namebot,'Крипто')
    else:
        menu21 = iz_telegram.get_namekey (user_id,namebot,'V Крипто')
    if Category03 == '':    
        menu22 = iz_telegram.get_namekey (user_id,namebot,'Недвижимость')
    else:
        menu22 = iz_telegram.get_namekey (user_id,namebot,'V Недвижимость')
    if Category04 == '':    
        menu31 = iz_telegram.get_namekey (user_id,namebot,'Финтех')
    else:
        menu31 = iz_telegram.get_namekey (user_id,namebot,'V Финтех')
    if Category05 == '':    
        menu32 = iz_telegram.get_namekey (user_id,namebot,'Бизнес')
    else:
        menu32 = iz_telegram.get_namekey (user_id,namebot,'V Бизнес')
    menu41 = iz_telegram.get_namekey (user_id,namebot,'Назад')
    menu42 = iz_telegram.get_namekey (user_id,namebot,'В главное меню')
    markup.row(menu11)
    markup.row(menu21,menu22)
    markup.row(menu31)
    markup.row(menu32)
    markup.row(menu41,menu42)
    return markup    

def location_menu (user_id,namebot):
    import iz_telegram
    from telebot import types          
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Location = iz_telegram.load_variable (user_id,namebot,"Location")

    if Location == 'Весь мир':
        menu11 = iz_telegram.get_namekey (user_id,namebot,'V Весь мир')
    else:    
        menu11 = iz_telegram.get_namekey (user_id,namebot,'Весь мир')

    if Location == 'Все онлайн':
        menu21 = iz_telegram.get_namekey (user_id,namebot,'V Все онлайн')
    else:
        menu21 = iz_telegram.get_namekey (user_id,namebot,'Все онлайн')

    if Location == 'Все оффлайн':
        menu22 = iz_telegram.get_namekey (user_id,namebot,'V Все оффлайн')
    else:
        menu22 = iz_telegram.get_namekey (user_id,namebot,'Все оффлайн')

    if Location == 'Россия':
        menu31 = iz_telegram.get_namekey (user_id,namebot,'V Россия')
    else:    
        menu31 = iz_telegram.get_namekey (user_id,namebot,'Россия')

    if Location == 'ОАЭ':
        menu32 = iz_telegram.get_namekey (user_id,namebot,'V ОАЭ')
    else:    
        menu32 = iz_telegram.get_namekey (user_id,namebot,'ОАЭ')

    menu41 = iz_telegram.get_namekey (user_id,namebot,'Назад')
    menu42 = iz_telegram.get_namekey (user_id,namebot,'В главное меню')

    markup.row(menu11)
    markup.row(menu21,menu22)
    markup.row(menu31,menu32)
    markup.row(menu41,menu42)

    return markup 

def change (user_id,namebot,message_in):  
    import iz_telegram
    Language = iz_telegram.load_variable (user_id,namebot,"Language")
    Year     = iz_telegram.load_variable (user_id,namebot,"Year")
    Location = iz_telegram.load_variable (user_id,namebot,"Location")
    #Category = iz_telegram.load_variable (user_id,namebot,"Category")

    Category01 = iz_telegram.load_variable (user_id,namebot,"Category01")
    Category02 = iz_telegram.load_variable (user_id,namebot,"Category02")
    Category03 = iz_telegram.load_variable (user_id,namebot,"Category03")
    Category04 = iz_telegram.load_variable (user_id,namebot,"Category04")
    Category05 = iz_telegram.load_variable (user_id,namebot,"Category05")

    Category = ''
    if Category01 == 'V':
        Category = Category + "Все категории" + ','
    if Category02 == 'V':
        Category = Category + "Крипто" + ','
    if Category03 == 'V':
        Category = Category + "Недвижимость" + ','
    if Category04 == 'V':
        Category = Category + "Финтех" + ','
    if Category05 == 'V':
        Category = Category + "Бизнес" + ''

    if Language == '':
        Language = 'ru'
    if Year == '':
        Year = '2021'
    if Location == '':
        Location = 'Весь мир'
    #Category = ''
    message_out = message_in
    message_out = message_out.replace('%%Language%%',Language)
    message_out = message_out.replace('%%Year%%',Year)
    message_out = message_out.replace('%%Location%%',Location)
    message_out = message_out.replace('%%Category%%',Category)
    return message_out

def get_setting (user_id,namebot,message_in):    
    import iz_telegram
    from telebot import types          
    message_out,menu = iz_telegram.get_message (user_id,'Начальное сообщение',namebot)

    message_out = change (user_id,namebot,message_out)
    Language = iz_telegram.load_variable (user_id,namebot,"Language")
    if Language == '':
        Language = 'ru'
    Location = iz_telegram.load_variable (user_id,namebot,"Location")
    if Location == '':
        Location = 'Весь мир'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu11 = iz_telegram.get_namekey (user_id,namebot,'Категории')
    menu12 = iz_telegram.get_namekey (user_id,namebot,'Локация')+' '+str(Location)
    menu21 = iz_telegram.get_namekey (user_id,namebot,'Формат сообщений')
    menu31 = iz_telegram.get_namekey (user_id,namebot,'Язык бота ')+str(Language)
    menu41 = iz_telegram.get_namekey (user_id,namebot,'Обратная связь')
    menu51 = iz_telegram.get_namekey (user_id,namebot,'В главное меню')
    markup.row(menu11,menu12)
    markup.row(menu21)
    markup.row(menu31)
    markup.row(menu41)
    markup.row(menu51)
    return message_out,markup

def format_message (user_id,namebot):
    import iz_telegram
    from telebot import types          
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    format_message = iz_telegram.load_variable (user_id,namebot,"Format message")
    if format_message == '':
        format_message = 'Стандартно'
    if format_message == 'Стандартно':
        menu11 = iz_telegram.get_namekey (user_id,namebot,'V Стандартно')
    else:    
        menu11 = iz_telegram.get_namekey (user_id,namebot,'Стандартно')
    if format_message == 'Компактно':
        menu21 = iz_telegram.get_namekey (user_id,namebot,'V Компактно')
    else:    
        menu21 = iz_telegram.get_namekey (user_id,namebot,'Компактно')
    menu31 = iz_telegram.get_namekey (user_id,namebot,'Назад')
    menu32 = iz_telegram.get_namekey (user_id,namebot,'В главное меню')
    markup.row(menu11)
    markup.row(menu21)
    markup.row(menu31,menu32)
    return markup

def language (user_id,namebot):
    import iz_telegram
    from telebot import types          
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    language = iz_telegram.load_variable (user_id,namebot,"Language")
    if language == '':
        language = 'ru'
    if language == 'ru':
        menu11 = 'V ru'
    else:    
        menu11 = 'ru'
    if language == 'en':
        menu21 = 'V en'
    else:    
        menu21 = 'en'
    menu31 = 'Назад'
    menu32 = 'В главное меню'
    markup.row(menu11)
    markup.row(menu21)
    markup.row(menu31,menu32)

    return markup

def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    namebot = "@Allconfsbot"
    import time
    import iz_func
    import iz_game
    import iz_telegram
    from telebot import types          
    db,cursor = iz_func.connect ()
    if message_in.find ('/start') != -1:        
        iz_telegram.save_variable (user_id,namebot,"Language",'ru')
        iz_telegram.save_variable (user_id,namebot,"Year",'2021')
        iz_telegram.save_variable (user_id,namebot,"Location",'Весь мир')
        iz_telegram.save_variable (user_id,namebot,"Category02","V")
        iz_telegram.save_variable (user_id,namebot,"Category04","V")
        iz_telegram.save_variable (user_id,namebot,"Category05","V")   
        iz_telegram.save_variable (user_id,namebot,"Format message",'Стандартно')
        message_out,menu = iz_telegram.get_message (user_id,'Начальное сообщение',namebot)
        message_out = change (user_id,namebot,message_out)
        markup = get_menu (user_id,namebot)
        #markup = ""
        #message_out = "TEST TEST"
        #print ('[+] user_id',user_id)
        #print ('[+] namebot',namebot)
        #print ('[+] message_out',message_out)
        #print ('[+] markup',markup)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)



    if message_in == '/add_news':
        label_send = True
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Ввод новый данных через Excel",'S',0)
        iz_telegram.save_variable (user_id,namebot,"status",'Ввод новый данных через Excel')
        status = ""

    if status == 'Ввод новый данных через Excel':
        label_send = True
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Информация принята",'S',0)
        iz_telegram.save_variable (user_id,namebot,"status",'')
        iz_telegram.save_Excel(message_in,"","","","","","","","","","")
        
        
    print ("[+]",message_in[0:9])
    if message_in[0:9] == "/add_news":
        label_send = True
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Информация принята",'S',0)
        iz_telegram.save_variable (user_id,namebot,"status",'')
        iz_telegram.save_Excel(message_in,"","","","","","","","","","")
        


    #if message_in == '/add':
    #    message_out,menu = iz_telegram.get_message (user_id,'Введите название',namebot)
    #    markup = ''
    #    iz_telegram.save_variable (user_id,namebot,"status",'Введите название')
    #    answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)        


    if status == 'Введите название':
        message_out,menu = iz_telegram.get_message (user_id,'Укажите ссылку',namebot)
        markup = ''
        iz_telegram.save_variable (user_id,namebot,"status",'Укажите ссылку')
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)            


    if status == 'Укажите ссылку':
        message_out,menu = iz_telegram.get_message (user_id,'Введите ссылку мероприяте',namebot)
        markup = ''
        iz_telegram.save_variable (user_id,namebot,"status",'Спасибо за данные')
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)            


    if status == 'Спасибо за данные':
        message_out,menu = iz_telegram.get_message (user_id,'Спасибо за данные',namebot)
        markup = ''
        iz_telegram.save_variable (user_id,namebot,"status",'')
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)            



    if message_in == 'Отправить':
        message_out,menu = iz_telegram.get_message (user_id,'Сообщение передано администратору',namebot)
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in.find ('Язык бота') != -1:
        message_out,menu = iz_telegram.get_message (user_id,'Язык сообщений',namebot)
        markup = language (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'ru':
        message_out,menu = iz_telegram.get_message (user_id,'Язык сообщений',namebot)
        iz_telegram.save_variable (user_id,namebot,"Language",'ru')
        markup = language (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V ru':
        message_out,menu = iz_telegram.get_message (user_id,'Язык сообщений',namebot)
        iz_telegram.save_variable (user_id,namebot,"Language",'')
        markup = language (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'en':
        message_out,menu = iz_telegram.get_message (user_id,'Язык сообщений',namebot)
        iz_telegram.save_variable (user_id,namebot,"Language",'en')
        markup = language (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V en':
        message_out,menu = iz_telegram.get_message (user_id,'Язык сообщений',namebot)
        iz_telegram.save_variable (user_id,namebot,"Language",'')
        markup = language (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Формат сообщений':
        message_out,menu = iz_telegram.get_message (user_id,'Формат сообщений системы',namebot)
        markup = format_message (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Стандартно':
        message_out,menu = iz_telegram.get_message (user_id,'Формат сообщений системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Format message",'Стандартно')
        markup = format_message (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Компактно':
        message_out,menu = iz_telegram.get_message (user_id,'Формат сообщений системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Format message",'Компактно')
        markup = format_message (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Назад':
        message_out,markup = get_setting (user_id,namebot,'Настройки') 
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Настройки':
        message_out,markup = get_setting (user_id,namebot,'Настройки') 
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'В главное меню':
        message_out,menu = iz_telegram.get_message (user_id,'Начальное сообщение',namebot)
        message_out = change (user_id,namebot,message_out)
        markup = get_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)

    if message_in =='Январь' or message_in =='Февраль' or message_in =='Март' or message_in =='Апрель' or message_in =='Май' or message_in =='Июнь'  or message_in =='Июль' or message_in =='Август' or message_in =='Сентябрь' or message_in =='Октябрь' or message_in =='Ноябрь' or message_in =='Декабрь':
        Year     = iz_telegram.load_variable (user_id,namebot,"Year")
        Month    = message_in
        sql = "select id,name,link,participation,date,task,category,location,format_date from bot_calendar where year = '"+str(Year)+"' and month = '"+str(Month)+"' and namebot = '"+str(namebot)+"';"
        cursor.execute(sql)
        data = cursor.fetchall()
        message_compact = '<b>Список мероприятий\n\n</b>'
        for rec in data: 
            id,name,link,participation,date,task,category,location,format_date  = rec.values()
            category_send  = "No"       
            category01 = iz_telegram.load_variable (user_id,namebot,"Category01")
            category02 = iz_telegram.load_variable (user_id,namebot,"Category02")
            category03 = iz_telegram.load_variable (user_id,namebot,"Category03")
            category04 = iz_telegram.load_variable (user_id,namebot,"Category04")
            category05 = iz_telegram.load_variable (user_id,namebot,"Category05")
            if category01 == 'V':
                category_send  = "Yes"
            if category02 == 'V' and category.find ('Крипто') != -1:
                category_send  = "Yes"
            if category03 == 'V' and category.find ('Недвижимость') != -1:
                category_send  = "Yes"
            if category04 == 'V' and category.find ('Финтех') != -1:
                category_send  = "Yes"
            if category05 == 'V' and category.find ('Бизнес') != -1:
                category_send  = "Yes"

            location_send  = "No" 
            location_save = iz_telegram.load_variable (user_id,namebot,"Location")
            if location_save == 'Весь мир':
                location_send  = "Yes"
            if location_save == 'Россия' and location == 'Россия':
                location_send  = "Yes"
            if category_send == "Yes" and location_send  == "Yes":
                message_out,menu = iz_telegram.get_message (user_id,'События месяца',namebot)
                message_out = message_out.replace('%%name%%',str(name))
                message_out = message_out.replace('%%link%%',str(link))
                message_out = message_out.replace('%%participation%%',str(participation))
                message_out = message_out.replace('%%location%%',str(location))            
                message_out = message_out.replace('%%date%%',str(date))
                message_out = message_out.replace('%%task%%',str(task))
                message_out = message_out.replace('%%category%%',str(category))

                name_ics = 'my'
                date_begin = str(format_date) 
                name_file  = '/var/www/html/download/'+name_ics+'.ics' 
                #iz_func.crete_calendar (str(name),date_begin,name_file)
                message_out = message_out.replace('%%namefile%%',str(name_ics+'.ics'))

                markup = get_menu (user_id,namebot)
                format_mess = iz_telegram.load_variable (user_id,namebot,"Format message") 
                if format_mess == 'Стандартно' or format_mess == '':
                    answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)
                else:  
                    message_compact = message_compact +"▪️ <b>" + str(date) +"</b>    "+ str(name) +'   <a href="'+str(link)+'">детали</a>'+ "\n\n" 





        format_mess = iz_telegram.load_variable (user_id,namebot,"Format message") 
        if format_mess == 'Компактно':
            markup = ''
            answer = iz_telegram.bot_send (user_id,namebot,message_compact,markup,message_id)

    if message_in == 'V 2021' or message_in == 'V 2022' or message_in == 'V 2023' or message_in == 'V 2024':
        message_out,menu = iz_telegram.get_message (user_id,'Начальное сообщение',namebot)
        Language = iz_telegram.load_variable (user_id,namebot,"Language")
        Year     = iz_telegram.load_variable (user_id,namebot,"Year")
        Location = iz_telegram.load_variable (user_id,namebot,"Location")
        Category = iz_telegram.load_variable (user_id,namebot,"Category")
        message_out = message_out.replace('%%Language%%',Language)
        message_out = message_out.replace('%%Year%%',Year)
        message_out = message_out.replace('%%Location%%',Location)
        message_out = message_out.replace('%%Category%%',Category)
        markup = get_years ('2021',user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)

    if message_in == '2021':
        iz_telegram.save_variable (user_id,namebot,"Year",'2021')
        message_out,menu = iz_telegram.get_message (user_id,'Начальное сообщение',namebot)
        Language = iz_telegram.load_variable (user_id,namebot,"Language")
        Year     = iz_telegram.load_variable (user_id,namebot,"Year")
        Location = iz_telegram.load_variable (user_id,namebot,"Location")
        Category = iz_telegram.load_variable (user_id,namebot,"Category")
        message_out = message_out.replace('%%Language%%',Language)
        message_out = message_out.replace('%%Year%%',Year)
        message_out = message_out.replace('%%Location%%',Location)
        message_out = message_out.replace('%%Category%%',Category)
        #markup = get_years ('2021',user_id,namebot)
        markup = get_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)

    if message_in == '2022':
        iz_telegram.save_variable (user_id,namebot,"Year",'2022')
        message_out,menu = iz_telegram.get_message (user_id,'Начальное сообщение',namebot)
        Language = iz_telegram.load_variable (user_id,namebot,"Language")
        Year     = iz_telegram.load_variable (user_id,namebot,"Year")
        Location = iz_telegram.load_variable (user_id,namebot,"Location")
        Category = iz_telegram.load_variable (user_id,namebot,"Category")
        message_out = message_out.replace('%%Language%%',Language)
        message_out = message_out.replace('%%Year%%',Year)
        message_out = message_out.replace('%%Location%%',Location)
        message_out = message_out.replace('%%Category%%',Category)        
        markup = get_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)

    if message_in == '2023':
        iz_telegram.save_variable (user_id,namebot,"Year",'2023')
        message_out,menu = iz_telegram.get_message (user_id,'Начальное сообщение',namebot)
        Language = iz_telegram.load_variable (user_id,namebot,"Language")
        Year     = iz_telegram.load_variable (user_id,namebot,"Year")
        Location = iz_telegram.load_variable (user_id,namebot,"Location")
        Category = iz_telegram.load_variable (user_id,namebot,"Category")
        message_out = message_out.replace('%%Language%%',Language)
        message_out = message_out.replace('%%Year%%',Year)
        message_out = message_out.replace('%%Location%%',Location)
        message_out = message_out.replace('%%Category%%',Category)        
        markup = get_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)

    if message_in == '2024':
        iz_telegram.save_variable (user_id,namebot,"Year",'2024')
        message_out,menu = iz_telegram.get_message (user_id,'Начальное сообщение',namebot)
        Language = iz_telegram.load_variable (user_id,namebot,"Language")
        Year     = iz_telegram.load_variable (user_id,namebot,"Year")
        Location = iz_telegram.load_variable (user_id,namebot,"Location")
        Category = iz_telegram.load_variable (user_id,namebot,"Category")
        message_out = message_out.replace('%%Language%%',Language)
        message_out = message_out.replace('%%Year%%',Year)
        message_out = message_out.replace('%%Location%%',Location)
        message_out = message_out.replace('%%Category%%',Category)        
        markup = get_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)

    if message_in.find ('Локация') != -1:
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Весь мир':
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        iz_telegram.save_variable (user_id,namebot,"Location",'Весь мир')
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Все онлайн':
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        iz_telegram.save_variable (user_id,namebot,"Location",'Все онлайн')
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Все оффлайн':
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        iz_telegram.save_variable (user_id,namebot,"Location",'Все оффлайн')
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Россия':
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        iz_telegram.save_variable (user_id,namebot,"Location",'Россия')
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'ОАЭ':
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        iz_telegram.save_variable (user_id,namebot,"Location",'ОАЭ')
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V Весь мир':
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        iz_telegram.save_variable (user_id,namebot,"Location",'')
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V Все онлайн':
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        iz_telegram.save_variable (user_id,namebot,"Location",'')
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V Все оффлайн':
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        iz_telegram.save_variable (user_id,namebot,"Location",'')
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V Россия':
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        iz_telegram.save_variable (user_id,namebot,"Location",'')
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V ОАЭ':
        message_out,menu = iz_telegram.get_message (user_id,'Локация',namebot)
        iz_telegram.save_variable (user_id,namebot,"Location",'')
        markup = location_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Категории':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)
        iz_telegram.save_variable (user_id,namebot,"Меню назад",'Категории')

    if message_in == 'Все категории':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Category01","V")
        iz_telegram.save_variable (user_id,namebot,"Category02","V")
        iz_telegram.save_variable (user_id,namebot,"Category03","V")
        iz_telegram.save_variable (user_id,namebot,"Category04","V")
        iz_telegram.save_variable (user_id,namebot,"Category05","V")
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V Все категории':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Category01","")
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Крипто':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Category02","V")
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V Крипто':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Category02","")
        iz_telegram.save_variable (user_id,namebot,"Category01","")
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Недвижимость':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Category03","V")
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V Недвижимость':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Category03","")
        iz_telegram.save_variable (user_id,namebot,"Category01","")
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Финтех':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Category04","V")
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V Финтех':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Category04","")
        iz_telegram.save_variable (user_id,namebot,"Category01","")
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'Бизнес':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Category05","V")
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

    if message_in == 'V Бизнес':
        message_out,menu = iz_telegram.get_message (user_id,'Категории системы',namebot)
        iz_telegram.save_variable (user_id,namebot,"Category05","")
        iz_telegram.save_variable (user_id,namebot,"Category01","")
        markup = category_menu (user_id,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)


