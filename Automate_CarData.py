from tkinter import *
from tkinter import ttk
import datetime
import pyttsx3
from PIL import ImageTk, Image
import pandas as pd

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

currentDataAndTime = datetime.datetime.now()
dateAndTime = currentDataAndTime.strftime("%Y.%m.%d--%H.%M.%S")

cardataset = pd.read_csv('CarsData.csv')

def completedataset():
    speak("Show complete dataset of car details")
    print("Complete Dataset of car data\n\n")
    print(cardataset)
    filename = "all_data_of_cars"+str(dateAndTime)+".csv"
    cardataset.to_csv(filename)

def shapeofdata():
    speak("tell shape of complete dataset of car details")
    print("shape Dataset of car data\n\n")
    shapedata = cardataset.shape
    print(shapedata)
    file = open('shapedetailsdata.txt','a')
    file.write(dateAndTime)
    file.write('\nshape of data: '+str(shapedata))
    file.write('\n\n')
    file.close()

def completerecord(n):
    speak("Feature complete by mean in car dataset and feature is "+n)
    print("Feature complete by mean in car dataset and feature is "+n+"\n\n")
    compfeature = cardataset[n].fillna(cardataset[n].mean(), inplace=True)
    print(compfeature)
    filename = "complete_feature_"+n+"_"+str(dateAndTime)+".csv"
    compfeature.to_csv(filename)

def nullvalues():
    speak("Check Null Values in complete dataset of car details")
    print("null values Dataset of car data\n\n")
    nulldata = cardataset.isnull().sum()
    print(nulldata)
    file = open('nullvaluesdata.txt','a')
    file.write(dateAndTime)
    file.write('\n null values of data: '+str(nulldata))
    file.write('\n\n')
    file.close()

def getheads(n):
    speak("Print first "+str(n)+" records from complete dataset of car details")
    print("Dataset of car data according to head\n\n")
    dataheads = cardataset.head(int(n))
    print(dataheads)
    filename = "data_of_cars_heads"+str(dateAndTime)+".csv"
    dataheads.to_csv(filename)

def gettails(n):
    speak("Print last "+str(n)+" records from complete dataset of car details")
    print("Dataset of car data according to tails\n\n")
    datatails = cardataset.tail(int(n))
    print(datatails)
    filename = "data_of_cars_tails"+str(dateAndTime)+".csv"
    datatails.to_csv(filename)

def getmpgcity(n):
    speak("Increase M P G City by "+str(n)+" numbers from complete dataset of car details")
    print("Increase M P G City by "+str(n)+" numbers from complete dataset of car details\n\n")
    cardataset['MPG_City'] = cardataset['MPG_City'].apply(lambda x:x+int(n))
    print(cardataset)
    filename = "dataset_increased_mpgcity"+str(dateAndTime)+".csv"
    cardataset.to_csv(filename)

def removedrecord(n):
    speak("New dataset of car details after removing records which have wieght more than "+str(n))
    print("New dataset of car details after removing records which have wieght more than "+n+"\n\n")
    newdata = cardataset[~(cardataset['Weight']>int(n))]
    print(newdata)
    filename = "newdataset"+str(dateAndTime)+".csv"
    newdata.to_csv(filename)

def countrecord(n):
    speak("Feature each count from car dataset according to feature "+n)
    print("Feature each count from car dataset according to feature "+n+"\n\n")
    countdata = cardataset[n].value_counts()
    print(countdata)
    file = open('feature count.txt','a')
    file.write(dateAndTime)
    file.write("\nFeature each count from car dataset according to feature "+n)
    file.write('\n null values of data: '+str(countdata))
    file.write('\n\n')
    file.close()

def Specificrecord(n):
    speak("Specific records for data set according to origin "+n)
    print("Specific records for data set according to origin "+n+"\n\n")
    specificdata = cardataset[cardataset['Origin'].isin([n])]
    print(specificdata)
    filename = "specificdata_byorigin_"+n+"_"+str(dateAndTime)+".csv"
    specificdata.to_csv(filename)


class guianalysis:
    def __init__(self, root):  # main gui of project through constructor
        self.root = root
        root.geometry("500x300")
        root.title('Analyization of Car Data')
        root.iconbitmap(r'logo.ico')
        root.configure(bg='gray92')

        # top root for headings
        top_root = Frame(root, bg="gray92", height=200, width=500)
        labeltoplvl = Label(top_root, text="CODER TECH Solution", font=('arial', 16, 'bold'), width=20,
                            height=2, bg="DodgerBlue3", )
        label2toplvl = Label(top_root, text="Automate Car Data Store", font=('arial', 12, 'bold'), width=24,
                             height=2, bg="DodgerBlue3", )
        top_root.pack(side=TOP, fill=BOTH)
        labeltoplvl.pack(side=TOP, pady=10)
        label2toplvl.pack(side=TOP, pady=5)

        # Center root for buttons
        middle_frame = Frame(root, bg="mint cream", height=240, width=400)
        middle_frame.pack(side=TOP, fill=BOTH, pady=5, padx=50)
        # button1 for menu in center frame
        menubutton = Button(middle_frame, text="Menu", bg="DodgerBlue3", font=('Garuda', 12, 'bold'),
                            width=15, height=3, fg="gray92", activebackground="gray92",
                            activeforeground="DodgerBlue3", command=lambda: self.menugui(root))
        menubutton.pack(side=LEFT, pady=25, padx=20)

        # button2 for about  in center frame
        aboutbutton = Button(middle_frame, text="About", bg="DodgerBlue3", font=('Garuda', 12, 'bold'),
                             width=15, height=3, fg="gray92", activebackground="gray92",
                             activeforeground="DodgerBlue3", command=lambda: self.aboutgui(root))
        aboutbutton.pack(side=LEFT, pady=25, padx=20)

        # bottom root for copy right
        bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
        copytight_label = Label(bottom_frame, text="© CODER TECH Solution 2021, All Rights Reserved", bg="DodgerBlue3",
                                font=('Garuda', 12, 'bold'))
        bottom_frame.pack(side=BOTTOM, fill=BOTH)
        copytight_label.pack(pady=5)
        self.wishme()

    @staticmethod
    def wishme():  # function for welcome speaking by project
        hour = int(datetime.datetime.now().hour)
        if hour >= 5 and hour < 10:
            speak('Good Morning!')
        elif hour >= 10 and hour < 16:
            speak('Good Afternoon!')
        elif hour >= 16 and hour < 18:
            speak('Good Evening!')
        else:
            speak('Good Night!')
        speak('Welcome to Automate Car Data Store by Coder TECH Solution')

    @staticmethod
    def aboutgui(root):  # function for about gui
        root.destroy()

        class aboutgui:
            def __init__(self, root):
                self.root = root
                root.geometry("400x540")
                root.maxsize(400, 540)
                root.minsize(400, 540)
                root.iconbitmap('logo.ico')
                root.title("Coder TECH Solution - About Us")

                # top root for headings
                top_root = Frame(root, bg="gray92", height=200, width=500)
                labeltoplvl = Label(top_root, text="CODER TECH Solution", font=('arial', 16, 'bold'), width=20,
                                    height=2, bg="DodgerBlue3", )
                label2toplvl = Label(top_root, text="Automate Car Data Store", font=('arial', 12, 'bold'), width=24,
                                     height=2, bg="DodgerBlue3", )
                top_root.pack(side=TOP, fill=BOTH)
                labeltoplvl.pack(side=TOP, pady=10)
                label2toplvl.pack(side=TOP, pady=5)

                # middle root
                middle2_frame = Frame(root, bg="mint cream", height=320)
                haeding_frame = Frame(middle2_frame, bg="mint cream", height=40)
                subheading_label = Label(haeding_frame, text="CODER TECH Solution CEO", font=('Garuda', 10, 'bold'),
                                         bg="DodgerBlue3",
                                         width=25, height=1)
                team_detial_frame = Frame(middle2_frame, bg="mint cream", height=303)
                team1_frame = Frame(team_detial_frame, bg="medium aquamarine", height=283, width=300)
                self.team1_pic = Image.open("CEO.png")
                self.resizedt1 = self.team1_pic.resize((250, 250), Image.ANTIALIAS)
                self.t1pic = ImageTk.PhotoImage(self.resizedt1)
                pic1_label = Label(team1_frame, bg="black", width=250.87, height=250, image=self.t1pic)
                t1_button = Button(team1_frame, text="Abdullah Maroof", bg="black", font=('Garuda', 12, 'bold'),
                                   width=15,
                                   height=1, fg="mint cream", activebackground="mint cream", activeforeground="black",
                                   command=lambda: self.CEOabout())

                middle2_frame.pack(side=TOP, fill=BOTH)
                haeding_frame.pack(side=TOP, fill=BOTH, expand=1)
                team_detial_frame.pack(side=TOP, fill=BOTH, expand=1)
                subheading_label.pack(pady=10)
                team1_frame.pack(side=TOP, padx=15, pady=10)
                pic1_label.pack(side=TOP, fill=BOTH, padx=25, pady=5)
                t1_button.pack(pady=5)

                # bottom root for copy right
                bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
                copytight_label = Label(bottom_frame, text="© CODER TECH Solution 2021, All Rights Reserved",
                                        bg="DodgerBlue3",
                                        font=('Garuda', 12, 'bold'))
                bottom_frame.pack(side=BOTTOM, fill=BOTH)
                copytight_label.pack(pady=5)
                self.aboutme()

            @staticmethod
            def aboutme():  # function for speaking about gui page
                speak("you can see About of CODER TECH Solution!!!")

            @staticmethod
            def CEOabout():  # function for speaking details of me
                speak("He is a CEO of coder tech Solution!!!")
                speak("Name: Abdullah Maroof")
                speak("Rollnumber: B A I M - F 19 - 0 0 7")
                speak("section: 4 A")
                speak("Program: B S Artificial Intelligence")
                speak("Department: Software Engineering")
                speak("Student of Superior University, gold campus")

        root = Tk()
        obj = aboutgui(root)
        mainloop()

    @staticmethod
    def menugui(root):  # function for menu gui of project
        root.destroy()

        class menupage:
            def __init__(self, root):
                self.root = root
                root.geometry("600x660")
                root.maxsize(600, 660)
                root.minsize(600, 660)
                root.iconbitmap('logo.ico')
                root.title("Automate Car Data Store - Menu")

                # top root for headings
                top_root = Frame(root, bg="gray92", height=200, width=600)
                labeltoplvl = Label(top_root, text="CODER TECH Solution", font=('arial', 16, 'bold'), width=20,
                                    height=2, bg="DodgerBlue3", )
                label2toplvl = Label(top_root, text="Automate Car Data Store", font=('arial', 12, 'bold'), width=24,
                                     height=2, bg="DodgerBlue3", )
                top_root.pack(side=TOP, fill=BOTH)
                labeltoplvl.pack(side=TOP, pady=10)
                label2toplvl.pack(side=TOP, pady=5)

                # middle root
                middle_root = Frame(root, bg="mint cream", height=400, width=600)
                haeding_frame = Frame(middle_root, bg="mint cream", height=40)
                # heading in middle root
                subheading_label = Label(haeding_frame, text="MENU", font=('Garuda', 10, 'bold'), bg="DodgerBlue3",
                                         width=15, height=1)

                # frame for showing full dataset, shape, nullvalue
                frame1 = Frame(middle_root, bg="gray92", height=40)
                buttonfulldata = Button(frame1, text="Complete Dataset", bg="DodgerBlue3", font=('Garuda', 12, 'bold'),
                                        width=15, height=1, fg="mint cream", activebackground="gray92",
                                        activeforeground="black",
                                        command=lambda: completedataset())
                buttonshapedata = Button(frame1, text="Car Dataset Shape", bg="DodgerBlue3",
                                         font=('Garuda', 12, 'bold'),
                                         width=15, height=1, fg="mint cream", activebackground="gray92",
                                         activeforeground="black", command=lambda: shapeofdata())
                buttonnull = Button(frame1, text="Dataset Null Values", bg="DodgerBlue3", font=('Garuda', 12, 'bold'),
                                    width=17, height=1, fg="mint cream", activebackground="gray92",
                                    activeforeground="black",
                                    command=lambda: nullvalues())

                # frame for showing heads dataset
                frame2 = Frame(middle_root, bg="gray92", height=40)
                labelheads = Label(frame2, text="Total Heads:  ", font=('Garuda', 10, 'bold'), bg="Gray92",
                                   width=10, height=1)
                self.entryheads = Entry(frame2, width=25)
                buttonhead = Button(frame2, text="Show Heads", bg="DodgerBlue3", font=('Garuda', 12, 'bold'), width=15,
                                    height=1, fg="mint cream", activebackground="gray92", activeforeground="black",
                                    command=lambda: getheads(int(self.entryheads.get())))

                # frame for showing tails dataset
                frame3 = Frame(middle_root, bg="gray92", height=40)
                labeltails = Label(frame3, text="Total Tails:  ", font=('Garuda', 10, 'bold'), bg="Gray92",
                                   width=10, height=1)
                self.entrytails = Entry(frame3, width=25)
                buttontail = Button(frame3, text="Show Tails", bg="DodgerBlue3", font=('Garuda', 12, 'bold'), width=15,
                                    height=1, fg="mint cream", activebackground="gray92", activeforeground="black",
                                    command=lambda: gettails(int(self.entrytails.get())))

                # frame for completing null values dataset
                frame4 = Frame(middle_root, bg="PeachPuff2", height=40)
                labelcomp = Label(frame4, text="complete feature by mean:", font=('Garuda', 8, 'bold'), bg="PeachPuff2",
                                  width=23, height=1)
                self.comp_box = ttk.Combobox(frame4, width=17, state="readonly", justify=CENTER, font=('Garuda', 9))
                self.comp_box['values'] = ('EngineSize', 'Cylinders', 'Horsepower', 'MPG_City', 'MPG_Highway', 'Weight'
                                           , 'Wheelbase', 'Length')
                buttoncomp = Button(frame4, text="Completefeature", bg="DodgerBlue3", font=('Garuda', 10, 'bold'),
                                    width=15,
                                    height=1, fg="mint cream", activebackground="gray92", activeforeground="black",
                                    command=lambda: completerecord(self.comp_box.get()))

                # frame for count of features in dataset
                frame5 = Frame(middle_root, bg="PeachPuff2", height=40)
                labelcount = Label(frame5, text="Total  each count in Feature:", font=('Garuda', 8, 'bold'),
                                   bg="PeachPuff2",
                                   width=23, height=1)
                self.count_box = ttk.Combobox(frame5, width=17, state="readonly", justify=CENTER, font=('Garuda', 9))
                self.count_box['values'] = (
                'Make', 'Model', 'Type', 'Origin', 'DriveTrain', 'MSRP', 'Invoice', 'EngineSize'
                , 'Cylinders')
                buttoncount = Button(frame5, text="Show each count", bg="DodgerBlue3", font=('Garuda', 10, 'bold'),
                                     width=15,
                                     height=1, fg="mint cream", activebackground="gray92", activeforeground="black",
                                     command=lambda: countrecord(self.count_box.get()))

                # frame for show all records for origin by USA, Asia & Europe
                frame6 = Frame(middle_root, bg="PeachPuff2", height=40)
                labelspecificrecord = Label(frame6, text="records by Origin:", font=('Garuda', 8, 'bold'),
                                            bg="PeachPuff2",
                                            width=23, height=1)
                self.specificrecord_box = ttk.Combobox(frame6, width=17, state="readonly", justify=CENTER,
                                                       font=('Garuda', 9))
                self.specificrecord_box['values'] = ('Asia', 'Europe', 'USA')
                buttonspecificrecord = Button(frame6, text="Show Records", bg="DodgerBlue3",
                                              font=('Garuda', 10, 'bold'), width=15,
                                              height=1, fg="mint cream", activebackground="gray92",
                                              activeforeground="black",
                                              command=lambda: Specificrecord(self.specificrecord_box.get()))

                # frame for wieght to remove records above 2500,3000,3500,4000
                frame7 = Frame(middle_root, bg="PeachPuff2", height=40)
                labelrecordsremove = Label(frame7, text="Remove Records by Wieght:  ", font=('Garuda', 8, 'bold'),
                                           bg="PeachPuff2",
                                           width=23, height=1)
                self.removerecord_box = ttk.Combobox(frame7, width=17, state="readonly", justify=CENTER,
                                                     font=('Garuda', 9))
                self.removerecord_box['values'] = (2500, 3000, 3500, 4000)
                buttonremoverecord = Button(frame7, text="Show New Dataset", bg="DodgerBlue3",
                                            font=('Garuda', 10, 'bold'),
                                            width=15, height=1, fg="mint cream", activebackground="gray92",
                                            activeforeground="black",
                                            command=lambda: removedrecord(self.removerecord_box.get()))

                # frame for increasing values of MPG_City by user choice
                frame8 = Frame(middle_root, bg="PeachPuff2", height=40)
                labelmpgcity = Label(frame8, text="Increase MPG City:  ", font=('Garuda', 10, 'bold'), bg="PeachPuff2",
                                     width=19, height=1)
                self.entrympgcity = Entry(frame8, width=25)
                buttonmpgcity = Button(frame8, text="Show Result", bg="DodgerBlue3", font=('Garuda', 10, 'bold'),
                                       width=15,
                                       height=1, fg="mint cream", activebackground="gray92", activeforeground="black",
                                       command=lambda: getmpgcity(int(self.entrympgcity.get())))

                middle_root.pack(side=TOP, fill=BOTH)
                haeding_frame.pack(side=TOP, fill=BOTH)
                subheading_label.pack(pady=10)
                frame1.pack(side=TOP, fill=BOTH, padx=20, pady=5)
                buttonfulldata.pack(side=LEFT, padx=13, pady=5)
                buttonshapedata.pack(side=LEFT, padx=13, pady=5)
                buttonnull.pack(side=LEFT, padx=13, pady=5)
                frame2.pack(side=TOP, fill=BOTH, padx=20, pady=5)
                labelheads.pack(side=LEFT, padx=50, pady=5)
                self.entryheads.pack(side=LEFT, padx=20, pady=5)
                buttonhead.pack(side=LEFT, padx=15, pady=5)
                frame3.pack(side=TOP, fill=BOTH, padx=20, pady=5)
                labeltails.pack(side=LEFT, padx=50, pady=5)
                self.entrytails.pack(side=LEFT, padx=20, pady=5)
                buttontail.pack(side=LEFT, padx=15, pady=5)
                frame4.pack(side=TOP, fill=BOTH, padx=20, pady=5)
                labelcomp.pack(side=LEFT, padx=15, pady=5)
                self.comp_box.pack(side=LEFT, pady=15, padx=20)
                self.comp_box.current(0)
                buttoncomp.pack(side=LEFT, padx=15, pady=5)
                frame5.pack(side=TOP, fill=BOTH, padx=20, pady=5)
                labelcount.pack(side=LEFT, padx=15, pady=5)
                self.count_box.pack(side=LEFT, pady=15, padx=20)
                self.count_box.current(0)
                buttoncount.pack(side=LEFT, padx=15, pady=5)
                frame6.pack(side=TOP, fill=BOTH, padx=20, pady=5)
                labelspecificrecord.pack(side=LEFT, padx=15, pady=5)
                self.specificrecord_box.pack(side=LEFT, pady=15, padx=20)
                self.specificrecord_box.current(0)
                buttonspecificrecord.pack(side=LEFT, padx=15, pady=5)
                frame7.pack(side=TOP, fill=BOTH, padx=20, pady=5)
                labelrecordsremove.pack(side=LEFT, padx=15, pady=5)
                self.removerecord_box.pack(side=LEFT, pady=15, padx=20)
                self.removerecord_box.current(0)
                buttonremoverecord.pack(side=LEFT, padx=15, pady=5)
                frame8.pack(side=TOP, fill=BOTH, padx=20, pady=5)
                labelmpgcity.pack(side=LEFT, padx=15, pady=5)
                self.entrympgcity.pack(side=LEFT, padx=18, pady=5)
                buttonmpgcity.pack(side=LEFT, padx=15, pady=5)

                # bottom root for copy right
                bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
                copytight_label = Label(bottom_frame, text="© CODER TECH Solution 2021, All Rights Reserved",
                                        bg="DodgerBlue3",
                                        font=('Garuda', 12, 'bold'))
                bottom_frame.pack(side=BOTTOM, fill=BOTH)
                copytight_label.pack(pady=5)
                self.menuvoice()

            @staticmethod
            def menuvoice():  # function for speaking menu page
                speak("Menu of Automate Car Data Store!!!")

        root = Tk()
        obj = menupage(root)
        mainloop()