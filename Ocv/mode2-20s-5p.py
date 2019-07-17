import time

from testmake_mode2 import OvcAutoMake

if __name__ == '__main__':
    preloaddata = {
        "lastlong": "20s",
        "picnum": "5p",
        "makedata": {
            "entrance": 2,
            "industry": 1,#通用是1，服装是2403
            "duration": 20,
            "proportion": "9:16",
            "lens_type":1,
            "transition_type":1,
            "material": "[{\"id\":25397501,\"text\":[\"测试片头！\",\"每日美女图片！\"],\"custom_type\":1,\"duration\":3},"
                        "{\"id\":26408601,\"text\":[\"吹下吹~\",\"让这风吹？？\"],\"custom_type\":2,\"duration\":3},"
                        "{\"id\":26408701,\"text\":[\"小猪佩奇的嘴\",\"骗人的嘴\"],\"custom_type\":2,\"duration\":3},"
                        "{\"id\":26408501,\"text\":[\"短小精悍\",\"突突突突突\",\"限时包邮\"],\"custom_type\":2,\"duration\":3},"
                        "{\"id\":25397201,\"text\":[\"感谢观看今天的\",\"《每日推荐》\"],\"custom_type\":3,\"duration\":3}]"
        },
        "logindata": {
            "email": "lizhuozhao@kuaizi.co",
            "password": "KUAIZI123@KZ"
        }
    }
    print(time.strftime('%H:%M:%S', time.localtime(time.time())))
    run = OvcAutoMake(preloaddata)
    run.login()
    run.refreshtoken()
    run.make()
    run.progress()
    run.getlens()
    run.save()
    run.saveloop()

    print(time.strftime('%H:%M:%S', time.localtime(time.time())))