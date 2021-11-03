import re

#4자리수 중 3자리만 안다고 가정. 3자리를 가지고 4자리수를 맞추는 정규식
#ca?e
#어떤 정규식을 컴파일 할지 정함
p = re.compile("ca.e") 

def print_match(m):
    # print(m.group())
    if m: 
        print("m.group(): "+m.group()) #일치하는 문자열 반환
        print("m.string(): "+m.string) #입력받은 문자열 반환
        print("m.start(): ",m.start()) #일치하는 문자열의 시작 index
        print("m.end(): ",m.end()) #일치하는 문자열의 끝 index
        print("m.span(): ",m.span()) #일치하는 문자열의 시작/끝 index
        
    else:
        print("Not match")

# m = p.match("case")
# print_match(m)
# '.':하나의 문자를 의미 -> care, cafe, case (o) | caffee (x)
# '^':문자열의 시작 -> ^de -> desk, destination (o) | fade(x)
# '$':문자열의 끝 -> se$ -> case, base (o) | face (x)

# m = p.search("careless") #주어진 문자열중에 일치하는게 있는지 찾음
# print_match(m)

# list = p.findall("good care cafe") # 일치하는 모든것을 리스트 형태로 반환
# print(list)
