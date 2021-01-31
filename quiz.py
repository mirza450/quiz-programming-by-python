q1= """1.What is one of the big differences between traditional media and social media?

    a. participatory production
    b. social media reaches only a few people at a time
    c. the management structure of the companies
    d. traditional media offers no way for audiences to communicate with media producers\n """
q2="""2.A website that lets anyone add, edit, or delete pages of content is called a

    a. wiki
    b. online forum
    c. usenet
    d. lurker site
    e. social network
   \n """
q3=""" 3.Today the most popular social networking site is

    a. MySpace
    b. Twitter
    c. Weibo
    d. Facebook\n
    """
q4=""" 4.The Central Rice Research Station is situated in?
 a. Chennai
 b. Cuttack
 c. Bangalore
 d. Quilon\n"""
q5="""5. The hottest planet in the solar system?
 a. Mercury
 b. Venus
 c. Mars
 d. Jupiter\n
"""
questions={q1:"d",q2:"a",q3:"d",q4:"b",q5:"b"}
print("********************************** Welcome To the Future Quiz programme***********************************************************\n")
user=input("Enter your name:\n")
print("Hello",user,"get ready for the quiz.")
score=0
for i in questions:
    print(i)
    flag1=input("do you want to Skip this question (yes/no)")
    if flag1=="yes" :
            continue
    ans=input("enter the correct answer (a/b/c/d).")
    if ans==questions[i]:
        print("you have won 1 point.")
        score=score+1
    else:
        print("you have lost 1 point.")
        score=score-1
    flag2=input("do you want to Exit. (yes/no)")
    if flag2=="yes":
        break
print("your total score is",score)
print("***********************************Have A Good Day**********************************************************************************************")
