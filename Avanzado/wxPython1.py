#Primer Formulario con wxPython
#1. instalar la libreria pip install -U wxPython
import wx

app = wx.App()

#marco
frame = wx.Frame(None,-1,'Primer Formulario',style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

frame.Show()

app.MainLoop() #ciclo infinito para mantenerla viva
