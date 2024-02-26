# ----- 코드 정의 ------
class Member:
    # TODO : 코드 구현이 필요합니다.
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
    

    def display(self):
        # TODO : 코드 구현이 필요합니다.
        print("*회원정보*")
        temp = "이름:"+ self.name + " 아이디:"+ self.username
        print(temp)


class Post:
    # TODO : 코드 구현이 필요합니다.
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    



# ----- 코드 실행 ------
members = []
posts = []


# TODO : 임의 객체 3개 생성
members.append(Member("abc","홍길동","1234"))
members.append(Member("xyz","가나다","9876"))
members.append(Member("ijk","이순신","1357"))

#회원정보 출력
members[0].display()
members[1].display()
members[2].display()

#게시글 생성 코드
posts.append(Post("제목123","내용123",members[0].username))
posts.append(Post("제목456","내용456",members[0].username))
posts.append(Post("제목789","내용789",members[0].username))
posts.append(Post("제목abc","내용abc",members[1].username))
posts.append(Post("제목abc","내용abc",members[1].username))
posts.append(Post("제목abc","내용abc",members[1].username))
posts.append(Post("제목123","내용123",members[2].username))
posts.append(Post("제목456","내용456",members[2].username))
posts.append(Post("제목789","내용789",members[2].username))

#제목 출력
for x in posts:
    print(x.title)

print(" ")

#특정단어("123") 있는 제목 출력
for x in posts:
    if x.content.find("123") != -1:
      print(x.title)