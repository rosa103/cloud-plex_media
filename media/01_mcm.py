# -- coding: utf-8 --
from selenium import webdriver
import unittest #unittest 모듈을 가져온다
import time
class Welcome(unittest.TestCase): #TC를 작성하기위해 unittest를 상속한 Test Class를 작성
   def setUp(self): #테스트 전에 수행
       self.driver = webdriver.Chrome(
           executable_path="../venv/webdriver/chromedriver.exe")
       self.base_url = "http://mz-cm-console-dev.s3-website.ap-northeast-2.amazonaws.com/welcome"
   def test_TestWelcome(self): #test_라는 이름으로 시작하는 method는 모두 Test method가 됨
       driver = self.driver
       driver.get("http://mz-cm-console-dev.s3-website.ap-northeast-2.amazonaws.com/welcome")
       # 로고 출력 확인
       # [Welcome!] 텍스트 출력 확인
       #self.assertEqual("Welcome!", driver.find_element_by_xpath('(.//*[normalize-space(text()) and normalize-space(.)='You need to sign in a Megazone Accounts account to get started.'])[1]/preceding::h4[1]').text)
       self.assertEqual("Welcome!", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='You need to sign in a Megazone Accounts account to get started.'])[1]/preceding::h4[1]").text)
       # [Sign in with Megazone Accounts]버튼 출력 확인
       # :arrow_forward:find_element_by_link_text 하이퍼링크 텍스트로 찾기 (a href 인 애들)
       self.assertEqual("Sign in with Megazone Accounts", driver.find_element_by_link_text("Sign in with Megazone Accounts").text)
       # [Create account] 링크 출력 확인
       # :arrow_forward:find_element_by_link_text 하이퍼링크 텍스트로 찾기 (a href 인 애들)
       self.assertEqual("Create account", driver.find_element_by_link_text("Create account").text)

   def tearDown(self):  # 테스트 종료 후 파일 삭제
       # setUp과 tearDown은 특수한 메소드로, 각 테스트 시작 전과 후에 실행된다. 필자는 브라우저를 시작하고 닫을 때 사용하고 있다. try/except와 비슷한 구조로 테스트에 에러가 발생해도 tearDown이 실행된다. 이를 이용하면 크롬 창이 쓸데없이 떠다니는 것을 막을 수 있다. 단, setUp 내에 exception이 있는 경우는 tearDown이 실행되지 않는다.
       # [출처] 2. unittest 모듈을 이용한 기능테스트 확장|작성자 Jayguar
       self.driver.quit()
if __name__ == "__main__": # 현재 script 파일이 실행되는 상태를 파악하기 위해 사용된다, #__name__ : 모듈의 이름이 저장되는 변수
   unittest.main() #코드를 통해 테스트가 수행된다