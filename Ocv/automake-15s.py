import time

from testmake import OvcAutoMake

if __name__ == '__main__':
    preloaddata = {
        "lastlong": "15s",
        "picnum": "5p",
        "makedata": {
            "entrance": 1,
            "industry": 1,#通用是1，服装是2403
            "duration": 15,
            "proportion": "9:16",
            "material": "[{\"id\":21924801,\"text\":[\"筷子测试11\",\"筷子测试11\"]},"
                        "{\"id\":21923301,\"text\":[\"测试测试22\",\"\"]},"
                        "{\"id\":21923901,\"text\":[\"测试测试33\",\"测试测试33\"]},"
                        "{\"id\":21923701,\"text\":[\"测试测试44\",\"\"]},"
                        "{\"id\":21923001,\"text\":[\"测试测试55\",\"测试测试55\"]}]"

        },
        "logindata": {
            "email": "oujin@kuaizi.co",
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