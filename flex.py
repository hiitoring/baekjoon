from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# 첫 번째와 두 번째 커맨드 라인 인자를 읽습니다.
# username = sys.argv[1]
# password = sys.argv[2]

driver = webdriver.Chrome()
driver.get('https://flex.team/home')  # 웹페이지를 엽니다.

# 입력 필드가 로딩될 때까지 기다립니다.
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'radix-:r0:'))
)

# 입력 필드에 텍스트를 입력합니다.
email_field.send_keys('박지환 ㅄ ㅋㅋ' + Keys.RETURN)

# 비밀번호 입력 필드가 로딩될 때까지 기다립니다.
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'radix-:rf:'))
)

# 비밀번호 입력 필드에 텍스트를 입력합니다.
password_field.send_keys('플렉스비밀번호' + Keys.RETURN)

time.sleep(10)

# ?? 사이드바 펼치기
# c-bIRrzL c-bIRrzL-dcxSjI-size-default c-bIRrzL-lbEVww-variant-ghost c-bIRrzL-ibjCwas-css
# c-bIRrzL c-bIRrzL-dcxSjI-size-default c-bIRrzL-lbEVww-variant-ghost c-bIRrzL-ibjCwas-css
button0 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.c-bIRrzL.c-bIRrzL-dcxSjI-size-default.c-bIRrzL-lbEVww-variant-ghost.c-bIRrzL-ibjCwas-css'))
)
button0.click()

time.sleep(3)

# ?? 근무시작버튼 클릭
button1 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.c-bIRrzL.c-gNtnBi.c-bIRrzL-glaMVD-size-default.c-bIRrzL-duTMEK-variant-outline.c-bIRrzL-icJWhYr-css.c-toRGo'))
)
button1.click()

time.sleep(3)

# ?? 사무실근무 버튼 클릭
button2 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.c-eECIIA'))
)
button2.click()

time.sleep(3)

# ?? 근무 시작 클릭
button3 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.c-eTLAUT'))
)
button3.click()

time.sleep(3)

driver.quit()
