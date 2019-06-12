import time

from testmake_mode2 import OvcAutoMake

if __name__ == '__main__':
    preloaddata = {
        "lastlong": "15s",
        "picnum": "5p",
        "makedata": {
            "entrance": 2,
            "industry": 2403,#通用是1，服装是2403
            "duration": 15,
            "proportion": "9:16",
            "lens_type":1,
            "transition_type":1,
            "material": "[{\"id\":25896901,\"text\":[\"测试片头！\",\"测试片头！\"],\"custom_type\":1,\"duration\":3},"
                        "{\"id\":25897301,\"text\":[\"今日真系好热\",\"牛欢喜系乜？\"],\"custom_type\":2,\"duration\":3},"
                        "{\"id\":25895301,\"text\":[\"竖版素材图片\",\"竖版素材图片\"],\"custom_type\":2,\"duration\":3},"
                        "{\"id\":25895001,\"text\":[\"横版素材图片\",\"立即抢购\",\"限时包邮\"],\"custom_type\":2,\"duration\":3},"
                        "{\"id\":25898001,\"text\":[\"没错我就是那条狗\",\"测试视频片尾\"],\"custom_type\":3,\"duration\":3}]"
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