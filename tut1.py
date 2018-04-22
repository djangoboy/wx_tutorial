# nominimizebox.py

import wx
app=wx.App()
w=wx.Frame(None,style=wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX)
w.Show(True)

app.MainLoop()
