in_tag = False # 특수문자 문자열 구분 boolean
og = list(input()) 
imsi = []
for i in og:
  imsi.append(i) 
  if i == "<": # 문자열이라면 reverse 출력
    in_tag = True # < 부터 특수문자 처리
    imsi.pop()
    print("".join(imsi[::-1]), end= "")
    imsi = []
    imsi.append(i)
  elif i == ">":  # 특수문자라면 그대로 출력
    in_tag = False # > 이후로 문자열 처리
    print("".join(imsi), end= "")
    imsi = []
  if in_tag == False: # 문자열이라면
    if i == " ": # 공백 전 문자열 reverse 출력
      imsi.pop()
      print("".join(imsi[::-1]), end= " ")
      imsi = []
print("".join(imsi[::-1])) # 문자열로 끝나는 경우 reverse 출력
