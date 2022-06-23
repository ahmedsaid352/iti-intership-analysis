import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# D:\Data\dataAnalysis\iti\Accepted List Zagazig University.xlsx
df = pd.read_excel("all.xlsx")

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
        print("please Enter integer number 1:8\n")
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
    sns.boxplot(x='complete score',y='Specialization',data=df)
    plt.show()
    choose()
#   filtering dataframe final score > 89 ==> (grade A)

def grade_A():

    print(df[df['complete score']>84.99])
    choose()

#   filtering dataframe names contains data entered

def search():
    studname = input("\n\nEnter student name then press enter \n\n").strip().lower()
    print(df[df['name'].str.contains(studname)])
    choose()    

#   say good bye and exit program

def exit():
    print("good-bye")
    quit()

#   calling choose function 

choose()