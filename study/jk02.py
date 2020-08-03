import requests,unittest
class getall_list(unittest.TestCase):
    def __init__(self,url,params,headers):
        self.url = url
        self.params = params
        self.headers = headers
    def setUp(self):
        self.url = 'https://beta.fengjr.com/fengInfo/api/v2/common/getListAll'
        self.headers = {
            'Authorization': "Bearer Rxp1GxIn2VC27ylFIdy3Sh4WNMVSslm38AjNHB7vPhj0oLnRMiiirC73wbXG7o9x",
        }
        self.params = {
            "category_type": "16",
            "page_size": "10",
            "user_id": "22B52EA7-5D85-44BF-8E89-96D3F43E2597",
            "version": "2.0"}
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()