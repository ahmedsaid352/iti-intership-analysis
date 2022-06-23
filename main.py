import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("dataframe.xlsx")

print("\t \t Wellcome \n\n")
print("\tMenu of options\n")
print("1.Show Data \n")
print("2.Column statistics \n")
print("3.Show students of grade A \n")
print("4.Search By name \n")
print("5.show box plot \n")
print("6.Exit \n")

# handling options 

def choose():

    ch = int(input("Enter option number then press enter\n"))
    if(ch==1):
        show_data()
    elif(ch==2):
        stats()
    elif(ch==3):
        grade_A()
    elif(ch==4):
        search()
    elif(ch==5):
        box()
        choose()
    elif(ch==6):
        exit()
    else:
        print("please Enter integer number 1:6\n")
        choose()

#   showing data function

def show_data():
    print(df)
    print("\n\n")
    choose()



def stats():
    print(df.describe())
    choose()


def box():
    print("box plot relations options\n\n")
    print("1.relation between track & score \n\n")
    print("2.relation between Specialization & score\n\n")
    print("3.relation between Faculty & score\n\n")
    print("4.back to main menu of options\n\n")
    choice = int(input("Enter option number then press enter\n\n"))
    if(choice==1):
        xvar = 'complete score'
        yvar = 'track'
    elif(choice==2):
        xvar = 'complete score'
        yvar = 'Specialization'
    elif(choice==3):
        xvar = 'complete score'
        yvar = 'Faculty'
    elif(choice==4):
        choose()
    else:
        print("please Enter integer number 1:4\n")
        box()
    sns.boxplot(x=xvar,y=yvar,data=df)
    plt.show()
    choose()
#   filtering dataframe final score > 89 ==> (grade A)

def grade_A():

    print(df[df['complete score']>84.99])
    choose()

#   filtering dataframe names contains data entered

def search():
    studname = input("\n\nEnter student name then press enter \n\n").strip().lower()
    print(df[df['Name'].str.contains(studname)])
    choose()    

#   say good bye and exit program

def exit():
    print("good-bye")
    quit()

#   calling choose function 

choose()