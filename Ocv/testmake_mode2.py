import json
import time

import datetime
import requests
import hashlib

#     "Accept":"application/json, text/plain, */*",
#     "Accept-Encoding":"gzip, deflate",
#     "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
#     "Cache-Control":"no-cache",
#     "Connection":"keep-alive",
#     "Content-Length":"51",
#     "SIGNATURE":"12fffdd6812a8747dd575eb053604fc2",
#     "Cookie":"PHPSESSID=dad889fa153b5b690260bf75ba81107d; sid=ddb0d4578e61cdb7ce3bf90057caf649",
#     "LANGUAGE":"cn",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"})



# # 获取进度
# print('\n获取进度')
# progressdata = {"req_no":req_no,
#                 "batch_no":batch_no}
#
# print(progressdata)
# print(s.headers)
# signature = __generatesignature(params=progressdata, authorization=authorization)
# print(signature)
# s.headers.update({"AUTHORIZATION":authorization,"SIGNATURE":signature})
# print(s.headers)
# progressequest = s.post(progressurl, data=progressdata)
# progressdict = json.loads(progressequest.text)
# print(progressdict["data"]["end"], progressdict["data"]["list"])
# for i in range(300):
#     time.sleep(2)
#     progressequest = s.post(progressurl, data=progressdata)
#     progressdict = json.loads(progressequest.text)
#     if progressdict["data"]["list"] != []:
#         print(progressdict["data"]["list"][0]["progress"])
#     else:
#         print(progressdict)
#     if progressdict["data"]["end"] == 1:
#         creative_id = progressdict["data"]["list"][0]["creative_id"]
#         break
#
#
# print('\n保存')
# savedata = {"creative_id":creative_id, "name":"test0314"}
# signature = __generatesignature(params=savedata, authorization=authorization)
# s.headers.update({"AUTHORIZATION":authorization,"SIGNATURE":signature})
# saverequest = s.post(saveurl, data = savedata)
# saverequest = json.loads(saverequest.text)
# print(saverequest)



class OvcAutoMake:
    def __init__(self, preloaddata):

        self.lastlong = preloaddata["lastlong"]
        self.picnum = preloaddata["picnum"]
        self.logindata = preloaddata["logindata"]
        self.makedata = preloaddata["makedata"]
        #print(type(self.makedata))

        self.headers = {
            "Referer": "http://ocv.kuaizi.co/user/",
            "LANGUAGE": "cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"}

        self.authorization = "5b42d304caff2"
        self.signature = ''
        self.loginurl = 'http://ocv.kuaizi.co/user/apply/login'
        self.tokenurl = 'http://ocv.kuaizi.co/user/account/token'
        self.makeurl = 'http://ocv.kuaizi.co/user/video/make'
        self.progressurl = 'http://ocv.kuaizi.co/user/video/progress'
        self.lensurl = 'http://ocv.kuaizi.co/user/video/lens'
        self.saveurl = 'http://ocv.kuaizi.co/user/video/save'
        self.changeurl = 'http://ocv.kuaizi.co/user/video/change'
        self.s = requests.Session()
        self.s.headers.update(self.headers)
        self.launchtime = time.strftime("%m%d%H%M", time.localtime(time.time()))
        self.filename = "log/m2-%s-%s-%s.txt" % (self.launchtime, self.lastlong, self.picnum)

    def __generatesignature(self, params={}, auth= True):
        if auth == False:
            authorization = "5b42d304caff2"
        else:
            authorization = self.authorization
        #print(authorization)
        paramstr = ""
        if params != {}:
            dict = sorted(params.items(), key=lambda d: d[0], reverse=False)
            for i in dict:
                # print(i[0], i[1])
                if i[1] != "":
                    paramstr = paramstr + str(i[1])
        keytomd5 = authorization + paramstr
        #print(keytomd5)
        s1 = hashlib.md5()
        s1.update(keytomd5.encode())
        self.signature = s1.hexdigest()
        #print(self.signature)
        #return signature
        self.s.headers.update({"AUTHORIZATION": self.authorization, "SIGNATURE": self.signature})

    def login(self):
        # 登录后台
        print('登录后台')
        self.__generatesignature(params=self.logindata, auth=False)
        #self.s.headers.update({"SIGNATURE": self.signature})
        makerequest = self.s.post(self.loginurl, data=self.logindata)
        #print(makerequest.status_code)
        #print(makerequest.text)
        makerequest = json.loads(makerequest.text)
        #print(makerequest)
        self.authorization = makerequest['data']['token']

    def refreshtoken(self):
        # 保持token
        print('刷新token')
        self.s.headers.update({"AUTHORIZATION": self.authorization})
        self.__generatesignature()
        #print(self.s.headers)
        makerequest = self.s.post(self.tokenurl)
        #print(makerequest.status_code)  # 获取加载code
        #print(makerequest.text)
        makerequest = json.loads(makerequest.text)
        self.authorization = makerequest['data']['token']
        self.__generatesignature()

    def make(self):
        # 发起制作
        print('发起制作')
        self.maketime = time.strftime("%m%d_%H%M", time.localtime(time.time()))
        #print(self.maketime)
        self.__generatesignature(params=self.makedata)
        #self.s.headers.update({"SIGNATURE": self.signature})
        self.starttime = datetime.datetime.now()
        #print(self.makedata)
        #print(str(self.makedata))
        makerequest = self.s.post(self.makeurl, data=self.makedata)
        #print(makerequest.status_code)  # 获取加载code
        #print(makerequest.text)
        self.req_no = json.loads(makerequest.text)["data"]["req_no"]
        self.batch_no = json.loads(makerequest.text)["data"]["batch_no"]
        #print(self.req_no)
        #print(self.batch_no)

    def progress(self):
        # 获取进度
        print('获取进度')
        self.progressdata = {"req_no": self.req_no,
                        "batch_no": self.batch_no}
        self.__generatesignature(params=self.progressdata)
        self.progresstime = ""
        for i in range(9999):
            progressequest = self.s.post(self.progressurl, data=self.progressdata)
            progressdict = json.loads(progressequest.text)
            if progressdict["data"]["list"] != []:
                if self.progresstime == "":
                    self.progresstime = datetime.datetime.now()
                print(str(progressdict["data"]["list"][0]["progress"]))
            else:

                print(".", end='')
                print('')
            if progressdict["data"]["end"] == 1:
                self.endtime = datetime.datetime.now()
                self.waitingtime = "%.2fs" % float((self.progresstime - self.starttime).total_seconds())
                self.usingtime = "%.2fs" % float((self.endtime - self.progresstime).total_seconds())
                self.totaltime = "%.2fs" % float((self.endtime - self.starttime).total_seconds())
                self.creative_id = progressdict["data"]["list"][0]["creative_id"]
                print("合成完成")
                break
            if progressdict["data"]["end"] >1:
                print("=======================================\n"
                      "==============有大于1的情况==============\n"
                      "=======================================")
            time.sleep(1)
        print("超时，退出轮询")

    def getlens(self):
        # 获取进度
        print('获取片段')
        self.getlensdata = {"creative_id": self.creative_id}
        self.__generatesignature(params=self.getlensdata)
        getlensrequest = self.s.get(self.lensurl, params=self.getlensdata)
        getlensdict = json.loads(getlensrequest.text)
        composite_id = []
        for i in getlensdict["data"]["list"]:
            composite_id.append(str(i["composite_id"]))
            #print(composite_id)
        self.composite_id = ",".join(composite_id)
        #print(self.composite_id)
        self.audio_id = getlensdict["data"]["audio_id"]
        #self.__generatesignature(params=self.changedata)
        #self.s.headers.update({"AUTHORIZATION": self.authorization, "SIGNATURE": self.signature})

    def save(self):
        print('保存')
        self.savename = "%s-%s-m2-%s-%s" %(self.totaltime, self.starttime.strftime("%H:%M:%S"), self.lastlong, self.picnum)
        print(self.savename)
        self.savedata = {"creative_id": self.creative_id, "name": self.savename}
        self.__generatesignature(params=self.savedata)
        self.s.headers.update({"AUTHORIZATION": self.authorization, "SIGNATURE": self.signature})
        saverequest = self.s.post(self.saveurl, data=self.savedata)
        saverequest = json.loads(saverequest.text)
        if saverequest["message"]=="success":
            print("保存成功")
            self.comment = "batch_no:%s\t%s\t%s\t%s\t%s\t%s\n" \
                           %(str(self.batch_no),self.creative_id,self.savename,self.waitingtime,self.usingtime,self.totaltime)
            self.writetxt(self.comment)
        else:
            print("没有保存成功："+ saverequest)

    def change(self):
        print('换一换')
        if self.batch_no == 1:
            print("换一换参数不正确")
        else:
            print("batch_no:"+str(self.batch_no))
            self.changedata = {"req_no": self.req_no,
                               "batch_no": self.batch_no,
                               "composite_id":self.composite_id,
                               "audio_id":""#self.audio_id
                               }
            self.__generatesignature(params=self.changedata)
            self.s.headers.update({"AUTHORIZATION": self.authorization, "SIGNATURE": self.signature})
            self.starttime = datetime.datetime.now()
            changerequest = self.s.post(self.changeurl, data=self.changedata)
            self.req_no = json.loads(changerequest.text)["data"]["req_no"]
            self.batch_no = json.loads(changerequest.text)["data"]["batch_no"]

    def writetxt(self, conment):
        print(self.filename)
        # txt打开文件
        txt = open(self.filename, 'a')
        # 输出文件名字
        #print("Here's your file %s:" % filename)
        # 调用read函数，输出读取到txt打开的内容
        # print txt.read()
        txt.write(conment)
        txt.close()

    def saveloop(self,looptimes=14):
        for i in range(looptimes):
            self.batch_no = int(self.batch_no) + 1
            self.refreshtoken()
            self.change()
            self.progress()
            self.getlens()
            self.save()

if __name__ == '__main__':
    # preloaddata = {
    #     "lastlong": "6s",
    #     "picnum": "2p",
    #     "makedata": {
    #         "industry": 2403,
    #         "duration": 6,
    #         "proportion": "9:16",
    #         "material": "[{\"id\":21962801,\"text\":[\"筷子测试1\",\"\"]},"
    #                     "{\"id\":21962701,\"text\":[\"筷子测试2\",\"筷子测试2\"]}]"
    #     },
    #     "logindata": {
    #         "email": "282850031@qq.com",
    #         "password": "123456"
    #     }
    # }
    # print(time.strftime('%H:%M:%S', time.localtime(time.time())))
    # run = OvcAutoMake(preloaddata)
    # run.login()
    # run.refreshtoken()
    # run.make()
    # run.progress()
    # run.save()
    #
    # # for i in range(29):
    # #     run.batch_no = int(run.batch_no) + 1
    # #     run.refreshtoken()
    # #     run.change()
    # #     run.progress()
    # #     run.save()
    # print(time.strftime('%H:%M:%S', time.localtime(time.time())))
    pass