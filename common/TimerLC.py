import threading
from bin import generatecase
from common.ReadAndWriteFiles import ReadAndWriteFiles
from common import EmailSend
from common.PgSql import deleteOperate
from common.report_screenshot import reportscreenshot
from common import EmailSend
from common import globalB
import datetime
class TimerLM(object):
    @staticmethod
    def func():
        print("haha")
        # 如果需要循环调用，就要添加以下方法
        delePG = deleteOperate()
        a = generatecase.Run()
        b = ReadAndWriteFiles()
        test_report = b.path_testreport()
        report = generatecase.new_report(test_report)
        c=reportscreenshot()
        EmailSend.sendmail(globalB.Gpng)


if __name__ == "__main__":
    b = TimerLM.func()


