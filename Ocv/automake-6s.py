import time

from testmake import OvcAutoMake

if __name__ == '__main__':
    preloaddata = {
        "lastlong": "6s",
        "picnum": "2p",
        "makedata": {
            "entrance": 1,
            "industry": 1,#通用是1，服装是2403
            "duration": 6,
            "proportion": "9:16",
            "material": "[{\"id\":21962801,\"text\":[\"筷子测试1\",\"\"]},"
                        "{\"id\":21962701,\"text\":[\"筷子测试2\",\"筷子测试2\"]}]"
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