import instaloader

instadata=instaloader.Instaloader()

User=""
Password=""
instadata.login(User,Password)
profile= instaloader.Profile.from_username(instadata.context, User)
x=int

"Esse calculo pega o numero de curtidas do User por foto Y é o numero de curtidas e N é o numero de post"
def CalLikepPost():
    y = 0
    n = 0

    for post in profile.get_posts():

        for c in set(post.get_likes()):
            y = y + 1

        n = n + 1

"Def para listar todos os seguidores da conta;"
lista=[]
listadeSeguidor=[]

def FollList():
    for x in profile.get_followers():
        lista.append(x)
    for y in lista:
        o=str(y)
        g=o.split()
        listadeSeguidor.append(g[1])


"saber o numero de seguidores do User"
def Follmines():
    b = 0
    for c in profile.get_followers():
        b=b+1
    print(f"esse é o numero de seguidores {b}")



