import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from speedtest import Speedtest

class SpeedtestPoller():
    # Firebase database reference
    DATABASE_REF = '/logs'

    # Speedtest servers ID's for testing against (http://www.speedtest.net/speedtest-servers.php)
    SPEEDTEST_SERVERS = [3396]

    def __init__(self):
        try:
            certificate_path = os.environ['FIREBASE_CERTIFICATE']
        except:
            raise SystemExit('Environment variable $FIREBASE_CERTIFICATE does not exist')

        if not os.path.exists(certificate_path):
            raise SystemExit('Certificate file does not exist on %s' % certificate_path)

        print('Initialize Firebase app...')

        certificate = credentials.Certificate(certificate_path)
        firebase_admin.initialize_app(certificate)
        self.db = db.reference(self.DATABASE_REF)
        self.speedtest = Speedtest()

    def __getTestResults(self):
        print('Get speedtest results...')

        self.speedtest.get_servers(self.SPEEDTEST_SERVERS)
        self.speedtest.get_best_server()
        self.speedtest.download()
        self.speedtest.upload(pre_allocate=False)

        return {
            'date': self.speedtest.results.timestamp,
            'download': self.speedtest.results.download,
            'upload': self.speedtest.results.upload,
            'ping': self.speedtest.results.ping,
        }

    def __saveTestResults(self, testResults):
        print('Save speedtest results...')

        self.db.push(testResults)

    def runTest(self):
        print('Run test...')

        testResults = self.__getTestResults()
        self.__saveTestResults(testResults)

if __name__ == '__main__':
    poller = SpeedtestPoller()
    poller.runTest()
