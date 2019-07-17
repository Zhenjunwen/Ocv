import time

from testmake_mode2 import OvcAutoMake

if __name__ == '__main__':
    preloaddata = {
        "lastlong": "12s",
        "picnum": "4p",
        "makedata": {
            "entrance": 2,
            "industry": 1,#通用是1，服装是2403
            "duration": 12,
            "proportion": "9:16",
            "lens_type":1,
            "transition_type":1,
            "material": "[{\"id\":21963001,\"text\":[\"筷子测试11\",\"筷子测试11\"],\"custom_type\":1,\"duration\":3},"
                        "{\"id\":21963101,\"text\":[\"测试测试22\",\"\"],\"custom_type\":2,\"duration\":3},"
                        "{\"id\":21962801,\"text\":[\"测试测试33\",\"测试测试33\"],\"custom_type\":3,\"duration\":3},"
                        "{\"id\":21963301,\"text\":[\"测试测试44\",\"测试测试44\"],\"custom_type\":2,\"duration\":3}]"
        },
        "logindata": {
            "email": "282850031@qq.com",
            "password": "123456"
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