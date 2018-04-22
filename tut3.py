#move.py
import wx
class Exampla(wx.Frame):

    def __init__(self,parent,title):
        super(Exampla,self).__init__(parent,title=title,
                                     size=(300,200))

        self.Move((800,200))
        self.Show()


if __name__=='__main__':
    app=wx.App()
    Exampla(None,title='Move')
    app.MainLoop()