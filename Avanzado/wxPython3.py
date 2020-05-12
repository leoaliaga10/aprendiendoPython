#CON CONSTRUCTOR
import wx

class Ventana_Ejemplo(wx.Frame):
	def __init__(self,parent,title):
		super(Ventana_Ejemplo,self).__init__(parent,title='Tercera Ventana',size=(800,400))
		#self.Centre()
		self.SetPosition((10,10))
		self.Show(True)


if __name__ == '__main__':
	app = wx.App()
	ventana = Ventana_Ejemplo(None, title = 'Nueva Ventana')
	app.MainLoop()
