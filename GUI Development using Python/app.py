from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API


class NLPApp:

    def __init__(self):

        self.dbo = Database()
        self.apio = API()

        # login ka GUI load krna hai
        self.root = Tk()
        self.root.title('NLP App')
        self.root.iconbitmap('resources/nlp.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50)
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Login', width=30, height=2, command=self.perform_login)
        login_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now', command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        # clear the existing gui
        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration Successful. You can login now')
        else:
            messagebox.showerror('Error', 'Email already exists')

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.home__gui()
        else:
            messagebox.showerror('Error', 'Incorrect email/password')

    def home__gui(self):

        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment', width=30, height=4, command=self.sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4, command=self.ner_analysis)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4, command=self.emotion_analysis)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_analysis(self):

        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Sentiment Analysis", bg='#34495E', fg='white')
        heading2.pack(pady=(30, 30))
        heading2.configure(font=('verdana', 24))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.result = Label(self.root, text='', bg='#34495E', fg='white')
        self.result.pack(pady=(10, 10))
        self.result.configure(font=('verdana', 16, 'bold'))

        goback_btn = Button(self.root, text='Go Back', command=self.home__gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        messagebox.showinfo(result)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + '->' + str(result['sentiment'][i]) + '\n'

        print(txt)
        self.result['text'] = txt

    def ner_analysis(self):

        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Named Entity Recognition Analysis", bg='#34495E', fg='white')
        heading2.pack(pady=(30, 30))
        heading2.configure(font=('verdana', 24))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text='Do Analysis', command=self.do_ner_analysis)
        ner_btn.pack(pady=(10, 10))

        self.result = Label(self.root, text='', bg='#34495E', fg='white')
        self.result.pack(pady=(10, 10))
        self.result.configure(font=('verdana', 16, 'bold'))

        goback_btn = Button(self.root, text='Go Back', command=self.home__gui)
        goback_btn.pack(pady=(10, 10))

    def do_ner_analysis(self):

        text = self.ner_input.get()
        result = self.apio.ner_analysis(text)
        messagebox.showinfo(result)

        txt = ''
        for i in result['entities']:
            txt = txt + 'Name-> ' + i['name'] + ', ' + 'Category->' + str(i['category']) + '\n'

        print(txt)
        self.result['text'] = txt

    def emotion_analysis(self):

        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Emotion Analysis", bg='#34495E', fg='white')
        heading2.pack(pady=(30, 30))
        heading2.configure(font=('verdana', 24))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.emo_input = Entry(self.root, width=50)
        self.emo_input.pack(pady=(5, 10), ipady=4)

        emo_btn = Button(self.root, text='Do Analysis', command=self.do_emo_analysis)
        emo_btn.pack(pady=(10, 10))

        self.result = Label(self.root, text='', bg='#34495E', fg='white')
        self.result.pack(pady=(10, 10))
        self.result.configure(font=('verdana', 16, 'bold'))

        goback_btn = Button(self.root, text='Go Back', command=self.home__gui)
        goback_btn.pack(pady=(10, 10))

    def do_emo_analysis(self):

        text = self.emo_input.get()
        result = self.apio.emotion_analysis(text)
        messagebox.showinfo(result)

        l = []
        for i in result['emotion']:
            l.append((i, result['emotion'][i]))
        txt = sorted(l, key=lambda x: x[1], reverse=True)[0][0]

        print(txt)
        self.result['text'] = txt


nlp = NLPApp()
