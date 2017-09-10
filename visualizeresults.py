import os
import sys
import VisualUI 
from PyQt5 import Qt,QtCore,QtGui
from PIL import Image
import pandas as pd
import pyqtgraph as pg
import numpy as np


class visresults(QtGui.QMainWindow, VisualUI.Ui_MainWindow):
	
	def __init__(self):
		self.names = {}
		self.names[0] = 'Melanoma'
		self.names[1] = 'Nevus'
		self.names[2] = 'Keratosis'

		super(visresults,self).__init__()
		self.setupUi(self)

		self.rootdir = os.path.join(os.path.dirname(sys.executable), 'data')

  		self.pushButton_3.clicked.connect(lambda:self.loadcsv())
  		self.pushButton.clicked.connect(lambda:self.showmap())
		self.pushButton_2.clicked.connect(lambda:self.showmask())
		self.pushButton_4.clicked.connect(lambda:self.addvalue(self.pushButton_4))
		
		self.pushButton_5.clicked.connect(lambda:self.addvalue(self.pushButton_5))

  		self.horizontalSlider.setMinimum(0)
  		self.horizontalSlider.valueChanged.connect(lambda:self.showimages())
  		
  		self.show()


	def loadcsv(self):
		try:
			sourcecsv = QtGui.QFileDialog.getOpenFileName(directory=os.path.dirname(sys.executable))
			self.name = str(sourcecsv[0])
			self.csvfile = pd.read_csv(self.name)

			if 'vis_correct' not in list(self.csvfile.columns.values):
				self.csvfile['vis_correct'] = ''
			else:
				self.csvfile.fillna(value='',inplace=True)
			self.horizontalSlider.setMaximum(len(self.csvfile)-1)
			self.showimages()
		except:
			pass

	def showmap(self):
		try:
			idx = self.horizontalSlider.value()
			popup = pg.image(np.asarray(Image.open(os.path.join(self.rootdir,self.csvfile.iloc[idx,0] + 'maps.png'))).transpose(1,0), autoRange=False)
		except:
			pass

	def showmask(self):
		try:
			idx = self.horizontalSlider.value()
			popup = pg.image(np.asarray(Image.open(os.path.join(self.rootdir,self.csvfile.iloc[idx,0] + 'mask.png'))).transpose(1,0), autoRange=False)
		except:
			pass

	
	def showimages(self):
		idx = self.horizontalSlider.value()
		img = pg.ImageItem(np.asarray(Image.open(os.path.join(self.rootdir,self.csvfile.iloc[idx,0] + 'overlayedmap.png'))).transpose(1,0,2))
		img.setRect(self.graphicsView.viewRect())
		self.graphicsView.addItem(img)

		img = pg.ImageItem(np.asarray(Image.open(os.path.join(self.rootdir,self.csvfile.iloc[idx,0] + '.png'))).transpose(1,0,2))
		img.setRect(self.graphicsView_2.viewRect())
		self.graphicsView_2.addItem(img)

		if self.csvfile.ix[idx,3] == '':
			status = 'unmarked'
		else:
			status = 'marked'

		self.textBrowser_2.setText('Label: ' + self.names[self.csvfile.iloc[idx,1]] +'\nPrediction: ' + self.names[self.csvfile.iloc[idx,2]] + '\nStatus: ' + status)
		marked = sum(self.csvfile['vis_correct'] != '')

		total_corrects = sum(self.csvfile['vis_correct'] == 1) 

		self.textBrowser_1.setText('Images Marked: %d/%d \nTotal Corrects: %d' % (marked,len(self.csvfile), total_corrects))


	def addvalue(self,b):
		if b.text() == 'Correct':
			self.csvfile.loc[self.horizontalSlider.value(),'vis_correct'] = 1
		if b.text() == 'Incorrect':
			self.csvfile.loc[self.horizontalSlider.value(),'vis_correct'] = 0
		self.showimages()

	def closeEvent(self,evnt):
		self.csvfile.to_csv(self.name,index=False)
		super(visresults, self).closeEvent(evnt)

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = visresults()
	sys.exit(app.exec_())

run()




