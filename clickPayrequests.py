def getPayNowData():
    dataUrl = '''https://www.clickpay.com/MobileService/Service.asmx/get_data_allow_impersonation_json'''

    payload1 = "{\"RequestType\":\"get_user_paynow_desktop\",\"FilterByGroupLabel\":\"1\",\"GroupLabel\":\"\"}"
    headers1 = {
        'authority': 'www.clickpay.com',
        'accept': '*/*',
        'accept-language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
        'antiforgerytoken': 'd771037d03144a3ea620635833835151',
        'content-type': 'text/plain; charset=UTF-8',
        'cookie': 'BIGipServerCLICKPAY-PROD-WEB-8080=514466058.36895.0000; __Secure-SessionId=fteldmdqfdhm23vo0iwa245n; _ga=GA1.2.323754191.1656009314; _gid=GA1.2.2076971893.1656009314; __zlcmid=1Acl1UpVBt7beGr; _vwo_uuid_v2=DF1CFAEA57DB44F1BCB3227393F5E1823|50128d73ddf5c5d2718fced6e403dd8a; _gcl_au=1.1.1093695245.1656009468; _fbp=fb.1.1656009468247.1430151185; ADRUM=s=1656064625201&r=https%3A%2F%2Fwww.clickpay.com%2FLoginPage.aspx%3F-1482280748; LP_LoginPath=~/Custom/clickpay/login.html; TS017e471b=01c7a403d7e52b3127d041f91ddb46f257f021e6daaa7096129fd0072dc2b74cd76c1ecf22833fce65c4aee9ea6e554a807cde8b73b3c5b37931790a68e921df9ab8ba3c501a5a027a18ed96975f528b173b582299d85bbea5dae2b35f0447dbed5eb09236140ca59229d84e6c040389752dadc5f3; _gat=1',
        'origin': 'https://www.clickpay.com',
        'referer': 'https://www.clickpay.com/app',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    return [dataUrl, payload1, headers1]


###########################################################################
def getUserProfileData():
    UserProfileurl = "https://www.clickpay.com/MobileService/Service.asmx/getUserContextJSON"

    payload2 = "NovelPayApp"
    headers2 = {
        'authority': 'www.clickpay.com',
        'accept': '*/*',
        'accept-language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
        'adrum': 'isAjax:true',
        'antiforgerytoken': '06e76418d7ef4d4da8aa34b28bbf6813',
        'content-type': 'text/plain;charset=UTF-8',
        'cookie': '_ga=GA1.2.1341743850.1655913846; _gid=GA1.2.2097986931.1655913846; _gcl_au=1.1.179288023.1655913846; _vwo_uuid_v2=D956FB0137631CEEF0408F88AD5DD3CC2|02193675d5025ce7f7c1a1116464c0e0; __zlcmid=1Abl1KPaqweezpB; BIGipServerCLICKPAY-PROD-WEB-8080=514466058.36895.0000; __Secure-SessionId=ozqqz3rli2cjhgnh02v2hlum; fpestid=2mem5BK4KQye3BcEBl8jmpVnhKhZ6YylJ5rcAvXsiBonefHKN4QZu6AuYf2tNZrXh0TIOQ; LP_LoginPath=~/Custom/moinianocean/login.html; TS017e471b=01c7a403d7cfdb941f0ccc813c04eb2b39276af73f79174796e9ffb8ae6f267f5650c34b439ae5035a044439990094f755e0e682aeb057d70958781d3a53688cf5e259834704e5c941cd213fccb5ba699c2d8dd688bbb22073fa6d396e81680e2329332b9d2ecbc4c2845248db6a1b3b67893d189c; _gat=1; ADRUM=s=1656065489811&r=https%3A%2F%2Fwww.clickpay.com%2Fapp%3F-913512687; TS017e471b=01c7a403d72ab9855b3d2cc4bdecdb5c5b1acf764d1703ca8e32bdaa23af5a0ee36130bb2c12fcf94fd7a58aafea19a106804942911953582e56ec979d916df594e72215f19ebbd6bd11f8b010f06fdcbbcb0d889008748221fdbd0650cb6a4557ba429f5860eeec91be2bc4d03d6450c6aaa84914',
        'origin': 'https://www.clickpay.com',
        'referer': 'https://www.clickpay.com/app',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    return [UserProfileurl, payload2, headers2]

    ###########################################################################


def login(username, password):
    usernameFix = username.replace("@", "%")
    loginUrl = "https://www.clickpay.com/LoginPage.aspx?LandingPageRefID=eda20c00-b404-4565-b12a-1d40a760f189"

    payload3 = 'PPID=c10bfc12-5d4c-4474-ac7e-0f37fd3dc9aa&__EVENTTARGET=LOGIN&__EVENTARGUMENT=undefined&__VIEWSTATE=&__EVENTVALIDATION=grCPzEz%2Bkd6roT1Upb%2Fd1GGxLp7%2FnH5vkBGR8WNfAX8xBPC%2FSW%2FelybPH5YMNauLhUjVnXhLb%2F82yBwXQKA%2BwJahtUVPnmt6QmWNsdS0azJBUIQvCefoRybwhoua2hizW2wcQZXZyPR02oS16IWgOgQDdSkPcyuSEvHcwsim3ekWxnVBVXM4Q%2B3yAx11bQQXxEPAKg%3D%3D&h_uc_UCLoginForm%24h_P_HomePage_Login%24h_txt_master_url=~%2FCustom%2Fmoinianocean%2Flogin.html&h_uc_UCLoginForm%24h_P_HomePage_Login%24h_TB_UserName%24State=%7B%26quot%3BrawValue%26quot%3B%3A%26quot%3{usernameFix}%26quot%3B%7D&h_uc_UCLoginForm%24h_P_HomePage_Login%24h_TB_UserName=+{usernameFix}+&h_uc_UCLoginForm%24h_P_HomePage_Login%24h_TB_Password%24State=%7B%26quot%3BrawValue%26quot%3B%3A%26quot%3B{password}%26quot%3B%7D&h_uc_UCLoginForm%24h_P_HomePage_Login%24h_TB_Password={password}&h_uc_UCLoginForm%24h_P_HomePage_Login%24h_CB_RemMyLogin=I&h_uc_UCLoginForm%24h_P_HomePage_Login%24h_inp_StartPage=&h_uc_UCLoginForm%24h_P_HomePage_Activate%24h_txt_TenantAccountIdentifier%24State=%7B%26quot%3BrawValue%26quot%3B%3A%26quot%3B%26quot%3B%7D&h_uc_UCLoginForm%24h_P_HomePage_Activate%24h_txt_TenantAccountIdentifier=&h_uc_UCLoginForm%24h_P_HomePage_Activate%24h_txt_BankAccountNumber%24State=%7B%26quot%3BrawValue%26quot%3B%3A%26quot%3B%26quot%3B%7D&h_uc_UCLoginForm%24h_P_HomePage_Activate%24h_txt_BankAccountNumber=&h_uc_UCLoginForm%24h_P_HomePage_Activate%24h_txt_BankRoutingNumber%24State=%7B%26quot%3BrawValue%26quot%3B%3A%26quot%3B%26quot%3B%7D&h_uc_UCLoginForm%24h_P_HomePage_Activate%24h_txt_BankRoutingNumber=&h_uc_UCLoginForm%24h_P_HomePage_Activate%24h_cap_UserActivation%24TB%24State=%7B%26quot%3BvalidationState%26quot%3B%3A%26quot%3B%26quot%3B%7D&h_uc_UCLoginForm%24h_P_HomePage_Activate%24h_cap_UserActivation%24TB=&h_inp_CheckActivation_URI=%2Fnpapi%2FwsClickPay.asmx%2Fcheck_activation&DXScript=1_11%2C1_252%2C1_64%2C1_12%2C1_13%2C1_14%2C1_15%2C1_23%2C1_183%2C1_184%2C1_188%2C1_182%2C1_8%2C1_203%2C1_189%2C1_49&DXCss=1_74%2C1_68%2C1_73%2C1_210%2C1_207%2C1_209%2C1_206' \
        .format(usernameFix=usernameFix, password=password)
    headers3 = {
        'authority': 'www.clickpay.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '_ga=GA1.2.1341743850.1655913846; _gid=GA1.2.2097986931.1655913846; _gcl_au=1.1.179288023.1655913846; _vwo_uuid_v2=D956FB0137631CEEF0408F88AD5DD3CC2|02193675d5025ce7f7c1a1116464c0e0; __zlcmid=1Abl1KPaqweezpB; fpestid=2mem5BK4KQye3BcEBl8jmpVnhKhZ6YylJ5rcAvXsiBonefHKN4QZu6AuYf2tNZrXh0TIOQ; BIGipServerCLICKPAY-PROD-WEB-8080=531243274.36895.0000; __Secure-SessionId=5c3oii2rzs0fxerwwl2wfnhk; _gat=1; _gat_UA-34121618-2=1; _gat_UA-34121618-1=1; TS017e471b=01c7a403d7f2bd4835aaba78f64bcbc42e41b310fdc94350ec7831d4f02acc9a8f09dca8f7a6781074767c0fcb69c17bf842b20c4f68d36cfb1c963c6c4f544f0d99d344aafdd327fc5e3075a0c737898d095954e8b1c6549bc6da8844c57e44c1916a6faa; ADRUM=s=1656067334643&r=https%3A%2F%2Fwww.clickpay.com%2FLoginPage.aspx%3F62662192',
        'origin': 'https://www.clickpay.com',
        'referer': 'https://www.clickpay.com/LoginPage.aspx?LandingPageRefID=eda20c00-b404-4565-b12a-1d40a760f189',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    return [loginUrl, payload3, headers3]
