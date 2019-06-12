import time

from testmake import OvcAutoMake

if __name__ == '__main__':
    preloaddata = {
        "lastlong": "10s",
        "picnum": "3p",
        "makedata": {
            "entrance": 1,
            "industry": 1,#通用是1，服装是2403
            "duration": 10,
            "proportion": "9:16",
            "material": "[{\"id\":21904644,\"text\":[\"筷子测试11\",\"筷子测试11\"]},"
                        "{\"id\":21904647,\"text\":[\"测试测试22\",\"\"]},"
                        "{\"id\":22397101,\"text\":[\"测试测试33\",\"测试测试33\"]}]"

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