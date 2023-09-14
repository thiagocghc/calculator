from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (350,580)

class First(App):
    def build(self):
        container = BoxLayout(orientation='vertical')

        self.tela = Label(text='',font_size=50)

        header = BoxLayout(orientation='horizontal')
        self.bot1 = Button(text='1',font_size=50,on_press=lambda x:self.click('1'))
        self.bot2 = Button(text='2',font_size=50,on_press=lambda x:self.click('2'))
        self.bot3 = Button(text='3',font_size=50,on_press=lambda x:self.click('3'))
        self.bot4 = Button(text='+',font_size=50,on_press=lambda x:self.click('+'))
        self.bot17 = Button(text='<<',font_size=50,on_press=self.backspace)

        header.add_widget(self.bot1)
        header.add_widget(self.bot2)
        header.add_widget(self.bot3)
        header.add_widget(self.bot4)
        header.add_widget(self.bot17)

        main = BoxLayout(orientation='horizontal')
        self.bot5 = Button(text='4',font_size=50,on_press=lambda x:self.click('4'))
        self.bot6 = Button(text='5',font_size=50,on_press=lambda x:self.click('5'))
        self.bot7 = Button(text='6',font_size=50,on_press=lambda x:self.click('6'))
        self.bot8 = Button(text='-',font_size=50)
        self.bot18 = Button(text='Z',font_size=50)

        main.add_widget(self.bot5)
        main.add_widget(self.bot6)
        main.add_widget(self.bot7)
        main.add_widget(self.bot8)
        main.add_widget(self.bot18)
        

        footer = BoxLayout(orientation='horizontal')
        self.bot9 = Button(text='7',font_size=50,on_press=lambda x:self.click('7'))
        self.bot10 = Button(text='8',font_size=50,on_press=lambda x:self.click('8'))
        self.bot11 = Button(text='9',font_size=50,on_press=lambda x:self.click('9'))
        self.bot12 = Button(text='*',font_size=50,on_press=lambda x:self.click('*'))
        self.bot19 = Button(text='R',font_size=50,on_press=self.raiz)

        footer.add_widget(self.bot9)
        footer.add_widget(self.bot10)
        footer.add_widget(self.bot11)
        footer.add_widget(self.bot12)
        footer.add_widget(self.bot19)

        bottom = BoxLayout(orientation='horizontal')
        self.bot13 = Button(text='C',font_size=50,on_press=self.reset)
        self.bot14 = Button(text='0',font_size=50,on_press=lambda x:self.click('0'))
        self.bot15 = Button(text='.',font_size=50)
        self.bot16 = Button(text='/',font_size=50)
        self.bot20 = Button(text='=',font_size=50,on_press=self.calcula)

        bottom.add_widget(self.bot13)
        bottom.add_widget(self.bot14)
        bottom.add_widget(self.bot15)
        bottom.add_widget(self.bot16)
        bottom.add_widget(self.bot20)


        container.add_widget(self.tela)
        container.add_widget(header)
        container.add_widget(main)
        container.add_widget(footer)
        container.add_widget(bottom)

        return container
    
    def calcula(self,text):
        if "+" in self.tela.text:
            a = self.tela.text.split("+")
            self.tela.text = str(int(a[0])+int(a[1]))

        if "*" in self.tela.text:
            a = self.tela.text.split("*")
            self.tela.text = str(int(a[0])*int(a[1]))

    def click(self,text):
        self.tela.text +=  text

    def raiz(self,text):
        res = float(self.tela.text)**0.5
        self.tela.text = str(res)

    def reset(self,text):
        self.tela.text =  ""

    def backspace(self,text):
        self.tela.text = self.tela.text[:-1]
    

if __name__ == '__main__':
    First().run()