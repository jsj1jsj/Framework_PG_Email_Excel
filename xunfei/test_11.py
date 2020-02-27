# from common import globalB
from selenium import webdriver
import unittest
# from HTMLTestRunner import HTMLTestRunner
import time
from common import globalB
from common import ReadAndWriteFiles
from common import test_case_time_manager as TIME_MANAGER


class IndexSet():
    aIndex = 0

    @staticmethod
    def add():
        IndexSet.aIndex = IndexSet.aIndex + 1


class Request1( unittest.TestCase ):
    # '''三方支付-协议支付请求'''
    @classmethod
    def setUpClass(self):
        # 点击登录
        time.sleep(0.01)

    def isElementExist(self, element):
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_css_selector( element )
            return flag

        except:
            flag = False
            return flag

    def test_001(self):
        '''发送报文'''
        assert ('期望结果1'in "123")  # //


    def test_002(self):  # 查询结果
        assert ('1'in "123")

    def test_003(self):
        assert ('1'in "123")

    def test_004(self):
        assert ('期望结果1'in "123")

    def test_005(self):
        assert ('期望结果1'in "123")
        IndexSet.add()

    @classmethod
    def tearDownClass(self) -> None:
        time.sleep(0.001)


# if __name__ == "__main__":
#     unittest.main()
if __name__ == "__main__":
    globalB.testunit.addTest( Request1( "test_case1" ) )
    # globalB.testunit.addTest(Request1("test_case5"))
    # now=time.strftime("%Y-%m-%d %H_%M_%S")
    # filename='./'+now+'result.html'
    # fp=open(filename,'wb')
    # runner = HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况：')
    # runner.run(testunit)
    # fp.close()