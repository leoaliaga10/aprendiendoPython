#EJEMPLO MENU
import wx

class EjemploMenu(wx.Frame):
	def __init__(self,parent,title):
		super(EjemploMenu,self).__init__(parent,title=title)
		self.InitUI()

	def InitUI(self):
		menubar = wx.MenuBar() 	#declaramos menu
		fileMenu = wx.Menu() 	#creamos menu

		fileItem = fileMenu.Append(wx.ID_EXIT,'Salir','Salir de la app')
		menubar.Append(fileMenu,'&Archivo')
		self.SetMenuBar(menubar)

		self.Bind(wx.EVT_MENU,self.OnQuit,fileItem)	#Invocamos es decir enlazamos
		self.Show(True)

	def OnQuit(self,e):
		self.Close()

frame = wx.App()
EjemploMenu(None,'Excel')
frame.MainLoop()
