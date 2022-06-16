#
# Created by: tarik
#


from fnmatch import translate
from operator import truediv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from skimage import data , io , filters , color , segmentation , img_as_float, color
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        #BUTTONS AND LAYOUTS

        #Creating the source button box
        self.Source_button_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Source_button_box.setObjectName("Source_button_box")
        #Creating and aligning the vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Source_button_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setAlignment(Qt.AlignHCenter)

        #Creating the open source button
        self.Button_open_source = QtWidgets.QPushButton(self.Source_button_box)
        self.Button_open_source.setObjectName("Button_open_source")
        self.Button_open_source.setStatusTip("Open source")
        #Adding icon to open source button via pixmap
        pixmap = QPixmap("./open_source.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_open_source.setIcon(button_icon)
        self.Button_open_source.setIconSize(smaller_pixmap.rect().size())
        self.Button_open_source.setFixedSize(40,40)
        #Adding the button to the layout
        self.verticalLayout.addWidget(self.Button_open_source)
        #Calls the getfile func. when clicked
        self.Button_open_source.clicked.connect(self.getfile)
        
        #Creating the export as source button
        self.Button_exportas_source = QtWidgets.QPushButton(self.Source_button_box)
        self.Button_exportas_source.setObjectName("Button_exportas_source")
        self.Button_exportas_source.setStatusTip("Export as source")
        #Adding icon to export as source button via pixmap
        pixmap = QPixmap("./export_as_source.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_exportas_source.setIcon(button_icon)
        self.Button_exportas_source.setIconSize(smaller_pixmap.rect().size())
        self.Button_exportas_source.setFixedSize(40,40)
        #Adding the button to the layout
        self.verticalLayout.addWidget(self.Button_exportas_source)
        #Calls the export as source func. when clicked
        self.Button_exportas_source.clicked.connect(self.export_as_source)
        
        #Creating the clear source button
        self.Button_clear_source = QtWidgets.QPushButton(self.Source_button_box)
        self.Button_clear_source.setObjectName("Button_clear_source")
        self.Button_clear_source.setStatusTip("Clear source")
        #Adding icon to clear source button via pixmap
        pixmap = QPixmap("./clear_source.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_clear_source.setIcon(button_icon)
        self.Button_clear_source.setIconSize(smaller_pixmap.rect().size())
        self.Button_clear_source.setFixedSize(40,40)
        #Adding the button to the layout
        self.verticalLayout.addWidget(self.Button_clear_source)
        self.gridLayout.addWidget(self.Source_button_box, 0, 0, 1, 1)
    
        #Creating the image box and the layout
        self.Source_img_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Source_img_box.setObjectName("Source_img_box")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Source_img_box)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setAlignment(Qt.AlignHCenter)

        #Creating the label that will be used for holding the source image 
        self.source_img_label = QtWidgets.QLabel(self.Source_img_box)
        self.source_img_label.setObjectName("source_img_label")
        self.verticalLayout_6.addWidget(self.source_img_label)
        self.gridLayout.addWidget(self.Source_img_box, 1, 0, 1, 2)
        self.Button_clear_source.clicked.connect(self.source_img_label.close)

        self.Edge_button_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Edge_button_box.setObjectName("Edge_button_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Edge_button_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setAlignment(Qt.AlignHCenter)

        self.Button_roberts = QtWidgets.QPushButton(self.Edge_button_box)
        self.Button_roberts.setObjectName("Button_roberts")
        self.Button_roberts.setStatusTip("Roberts")
        #Adding icon to roberts button via pixmap
        pixmap = QPixmap("./one.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_roberts.setIcon(button_icon)
        self.Button_roberts.setIconSize(smaller_pixmap.rect().size())
        self.Button_roberts.setFixedSize(40,40)
        self.Button_roberts.clicked.connect(self.roberts)
        self.verticalLayout_3.addWidget(self.Button_roberts)

        self.Button_sobel = QtWidgets.QPushButton(self.Edge_button_box)
        self.Button_sobel.setObjectName("Button_sobel")
        self.Button_sobel.setStatusTip("Sobel")
        #Adding icon to sobel button via pixmap
        pixmap = QPixmap("./two.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_sobel.setIcon(button_icon)
        self.Button_sobel.setIconSize(smaller_pixmap.rect().size())
        self.Button_sobel.setFixedSize(40,40)
        self.Button_sobel.clicked.connect(self.sobel)
        self.verticalLayout_3.addWidget(self.Button_sobel)

        self.Button_scharr = QtWidgets.QPushButton(self.Edge_button_box)
        self.Button_scharr.setObjectName("Button_scharr")
        self.Button_scharr.setStatusTip("Scharr")
        #Adding icon to scharr button via pixmap
        pixmap = QPixmap("./three.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_scharr.setIcon(button_icon)
        self.Button_scharr.setIconSize(smaller_pixmap.rect().size())
        self.Button_scharr.setFixedSize(40,40)
        self.Button_scharr.clicked.connect(self.scharr)
        self.verticalLayout_3.addWidget(self.Button_scharr)

        self.Button_prewitt = QtWidgets.QPushButton(self.Edge_button_box)
        self.Button_prewitt.setObjectName("Button_prewitt")
        self.Button_prewitt.setStatusTip("Prewitt")
        #Adding icon to prewitt button via pixmap
        pixmap = QPixmap("./four.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_prewitt.setIcon(button_icon)
        self.Button_prewitt.setIconSize(smaller_pixmap.rect().size())
        self.Button_prewitt.setFixedSize(40,40)
        self.Button_prewitt.clicked.connect(self.prewitt)
        self.verticalLayout_3.addWidget(self.Button_prewitt)

        self.gridLayout.addWidget(self.Edge_button_box, 0, 4, 1, 1)

        self.Output_button_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Output_button_box.setObjectName("Output_button_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Output_button_box)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setAlignment(Qt.AlignHCenter)

        self.Button_save_output = QtWidgets.QPushButton(self.Output_button_box)
        self.Button_save_output.setObjectName("Button_save_output")
        self.Button_save_output.setStatusTip("Save output")
        #Adding icon to save output button via pixmap
        pixmap = QPixmap("./save_output.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_save_output.setIcon(button_icon)
        self.Button_save_output.setIconSize(smaller_pixmap.rect().size())
        self.Button_save_output.setFixedSize(40,40)
        self.verticalLayout_2.addWidget(self.Button_save_output)

        self.Button_saveas_output = QtWidgets.QPushButton(self.Output_button_box)
        self.Button_saveas_output.setObjectName("Button_saveas_output")
        self.Button_saveas_output.setStatusTip("Save as output")
        #Adding icon to save as output button via pixmap
        pixmap = QPixmap("./saveas_output.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_saveas_output.setIcon(button_icon)
        self.Button_saveas_output.setIconSize(smaller_pixmap.rect().size())
        self.Button_saveas_output.setFixedSize(40,40)
        self.verticalLayout_2.addWidget(self.Button_saveas_output)

        self.Button_exportas_output = QtWidgets.QPushButton(self.Output_button_box)
        self.Button_exportas_output.setObjectName("Button_exportas_output")
        self.Button_exportas_output.setStatusTip("Export as output")
        #Adding icon to export as output button via pixmap
        pixmap = QPixmap("./export_as_output.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_exportas_output.setIcon(button_icon)
        self.Button_exportas_output.setIconSize(smaller_pixmap.rect().size())
        self.Button_exportas_output.setFixedSize(40,40)
        self.verticalLayout_2.addWidget(self.Button_exportas_output)

        self.Button_clear_output = QtWidgets.QPushButton(self.Output_button_box)
        self.Button_clear_output.setObjectName("Button_clear_output")
        self.Button_clear_output.setStatusTip("Clear output")
        #Adding icon to clear output button via pixmap
        pixmap = QPixmap("./clear_output.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_clear_output.setIcon(button_icon)
        self.Button_clear_output.setIconSize(smaller_pixmap.rect().size())
        self.Button_clear_output.setFixedSize(40,40)
        
        self.verticalLayout_2.addWidget(self.Button_clear_output)

        self.Button_undo_output = QtWidgets.QPushButton(self.Output_button_box)
        self.Button_undo_output.setObjectName("Button_undo_output")
        self.Button_undo_output.setStatusTip("Undo output")
        #Adding icon to undo output button via pixmap
        pixmap = QPixmap("./undo_output.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_undo_output.setIcon(button_icon)
        self.Button_undo_output.setIconSize(smaller_pixmap.rect().size())
        self.Button_undo_output.setFixedSize(40,40)
        self.verticalLayout_2.addWidget(self.Button_undo_output)

        self.Button_redo_output = QtWidgets.QPushButton(self.Output_button_box)
        self.Button_redo_output.setObjectName("Button_redo_output")
        self.Button_redo_output.setStatusTip("Redo output")
        #Adding icon to redo output button via pixmap
        pixmap = QPixmap("./redo_output.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_redo_output.setIcon(button_icon)
        self.Button_redo_output.setIconSize(smaller_pixmap.rect().size())
        self.Button_redo_output.setFixedSize(40,40)
        self.verticalLayout_2.addWidget(self.Button_redo_output)

        self.gridLayout.addWidget(self.Output_button_box, 0, 1, 1, 1)

        self.Segment_button_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Segment_button_box.setObjectName("Segment_button_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Segment_button_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setAlignment(Qt.AlignHCenter)

        self.Button_multi_otsu = QtWidgets.QPushButton(self.Segment_button_box)
        self.Button_multi_otsu.setObjectName("Button_multi_otsu")
        self.Button_multi_otsu.setStatusTip("Multi - Otsu")
        #Adding icon to multi-otsu button via pixmap
        pixmap = QPixmap("./one_alt.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_multi_otsu.setIcon(button_icon)
        self.Button_multi_otsu.setIconSize(smaller_pixmap.rect().size())
        self.Button_multi_otsu.setFixedSize(40,40)
        self.Button_multi_otsu.clicked.connect(self.multi_otsu)
        self.verticalLayout_4.addWidget(self.Button_multi_otsu)

        self.Button_chan_vese = QtWidgets.QPushButton(self.Segment_button_box)
        self.Button_chan_vese.setObjectName("Button_chan_vese")
        self.Button_chan_vese.setStatusTip("Chan - Vese")
        #Adding icon to chan-vese button via pixmap
        pixmap = QPixmap("./two_alt.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_chan_vese.setIcon(button_icon)
        self.Button_chan_vese.setIconSize(smaller_pixmap.rect().size())
        self.Button_chan_vese.setFixedSize(40,40)
        self.Button_chan_vese.clicked.connect(self.chan_vese)
        self.verticalLayout_4.addWidget(self.Button_chan_vese)

        self.Button_morph = QtWidgets.QPushButton(self.Segment_button_box)
        self.Button_morph.setObjectName("Button_morph")
        self.Button_morph.setStatusTip("Morphological Snakes")
        #Adding icon to morph-snakes button via pixmap
        pixmap = QPixmap("./three_alt.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_morph.setIcon(button_icon)
        self.Button_morph.setIconSize(smaller_pixmap.rect().size())
        self.Button_morph.setFixedSize(40,40)
        self.Button_morph.clicked.connect(self.morph_snakes)
        self.verticalLayout_4.addWidget(self.Button_morph)
        

        self.gridLayout.addWidget(self.Segment_button_box, 0, 3, 1, 1)

        self.Output_img_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Output_img_box.setObjectName("Output_img_box")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Output_img_box)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setAlignment(Qt.AlignHCenter)

        self.output_img_label = QtWidgets.QLabel(self.Output_img_box)
        self.output_img_label.setObjectName("output_img_label")
        self.verticalLayout_7.addWidget(self.output_img_label)
        self.gridLayout.addWidget(self.Output_img_box, 1, 3, 1, 2)

        self.Button_clear_output.clicked.connect(self.output_img_label.close)

        self.Conv_button_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Conv_button_box.setObjectName("Conv_button_box")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Conv_button_box)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setAlignment(Qt.AlignHCenter)

        self.Button_rgb_to_gray = QtWidgets.QPushButton(self.Conv_button_box)
        self.Button_rgb_to_gray.setObjectName("Button_rgb_to_gray")
        self.Button_rgb_to_gray.setStatusTip("Rgb to grayscale")
        self.Button_rgb_to_gray.clicked.connect(self.rgbtogray)
        #Adding icon to rgb2gray button via pixmap
        pixmap = QPixmap("./rgb_to_gray.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_rgb_to_gray.setIcon(button_icon)
        self.Button_rgb_to_gray.setIconSize(smaller_pixmap.rect().size())
        self.Button_rgb_to_gray.setFixedSize(40,40)
        self.verticalLayout_5.addWidget(self.Button_rgb_to_gray)

        self.Button_rgb_to_hsv = QtWidgets.QPushButton(self.Conv_button_box)
        self.Button_rgb_to_hsv.setObjectName("Button_rgb_to_hsv")
        self.Button_rgb_to_hsv.setStatusTip("Rgb to Hsv")
        self.Button_rgb_to_hsv.clicked.connect(self.rgbtohsv)
        #Adding icon to rgb2hsv button via pixmap
        pixmap = QPixmap("./rgb_to_hsv.png")
        smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        button_icon = QIcon(smaller_pixmap)
        self.Button_rgb_to_hsv.setIcon(button_icon)
        self.Button_rgb_to_hsv.setIconSize(smaller_pixmap.rect().size())
        self.Button_rgb_to_hsv.setFixedSize(40,40)
        self.verticalLayout_5.addWidget(self.Button_rgb_to_hsv)

        self.gridLayout.addWidget(self.Conv_button_box, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_as = QtWidgets.QMenu(self.menuFile)
        self.menuExport_as.setObjectName("menuExport_as")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuClear = QtWidgets.QMenu(self.menuEdit)
        self.menuClear.setObjectName("menuClear")
        self.menuConversion = QtWidgets.QMenu(self.menubar)
        self.menuConversion.setObjectName("menuConversion")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen_Source = QtWidgets.QAction(MainWindow)
        self.actionOpen_Source.setObjectName("actionOpen_Source")

        self.actionSave_Output = QtWidgets.QAction(MainWindow)
        self.actionSave_Output.setObjectName("actionSave_Output")
        self.actionSave_Output.setEnabled(False)

        self.actionSave_as_Output = QtWidgets.QAction(MainWindow)
        self.actionSave_as_Output.setObjectName("actionSave_as_Output")
        self.actionSave_as_Output.setEnabled(False)

        self.actionExport_as_Source = QtWidgets.QAction(MainWindow)
        self.actionExport_as_Source.setObjectName("actionExport_as_Source")
        self.actionExport_as_Source.setEnabled(False)

        self.actionExport_as_Output = QtWidgets.QAction(MainWindow)
        self.actionExport_as_Output.setObjectName("actionExport_as_Output")
        self.actionExport_as_Output.setEnabled(False)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionClear_Source = QtWidgets.QAction(MainWindow)
        self.actionClear_Source.setObjectName("actionClear_Source")
        self.actionClear_Source.setEnabled(False)

        self.actionClear_Output = QtWidgets.QAction(MainWindow)
        self.actionClear_Output.setObjectName("actionClear_Output")
        self.actionClear_Output.setEnabled(False)

        self.actionUndo_Output = QtWidgets.QAction(MainWindow)
        self.actionUndo_Output.setObjectName("actionUndo_Output")
        self.actionUndo_Output.setEnabled(False)

        self.actionRedo_Output = QtWidgets.QAction(MainWindow)
        self.actionRedo_Output.setObjectName("actionRedo_Output")
        self.actionRedo_Output.setEnabled(False)

        self.actionRGB_to_Grayscale = QtWidgets.QAction(MainWindow)
        self.actionRGB_to_Grayscale.setObjectName("actionRGB_to_Grayscale")
        self.actionRGB_to_Grayscale.setEnabled(False)

        self.actionRGB_tp_HSV = QtWidgets.QAction(MainWindow)
        self.actionRGB_tp_HSV.setObjectName("actionRGB_tp_HSV")
        self.actionRGB_tp_HSV.setEnabled(False)

        self.actionMulti_Otsu_Thresholding = QtWidgets.QAction(MainWindow)
        self.actionMulti_Otsu_Thresholding.setObjectName("actionMulti_Otsu_Thresholding")
        self.actionMulti_Otsu_Thresholding.setEnabled(False)

        self.actionChans_Vese_Segmentation = QtWidgets.QAction(MainWindow)
        self.actionChans_Vese_Segmentation.setObjectName("actionChans_Vese_Segmentation")
        self.actionChans_Vese_Segmentation.setEnabled(False)

        self.actionMorphological_Snakes = QtWidgets.QAction(MainWindow)
        self.actionMorphological_Snakes.setObjectName("actionMorphological_Snakes")
        self.actionMorphological_Snakes.setEnabled(False)

        self.actionRoberts = QtWidgets.QAction(MainWindow)
        self.actionRoberts.setObjectName("actionRoberts")
        self.actionRoberts.setEnabled(False)

        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionSobel.setEnabled(False)

        self.actionScharr = QtWidgets.QAction(MainWindow)
        self.actionScharr.setObjectName("actionScharr")
        self.actionScharr.setEnabled(False)

        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.actionPrewitt.setEnabled(False)

        self.menuExport_as.addAction(self.actionExport_as_Source)
        self.menuExport_as.addAction(self.actionExport_as_Output)
        self.menuFile.addAction(self.actionOpen_Source)
        self.menuFile.addAction(self.actionSave_Output)
        self.menuFile.addAction(self.actionSave_as_Output)
        self.menuFile.addAction(self.menuExport_as.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuClear.addAction(self.actionClear_Source)
        self.menuClear.addAction(self.actionClear_Output)
        self.menuEdit.addAction(self.menuClear.menuAction())
        self.menuEdit.addAction(self.actionUndo_Output)
        self.menuEdit.addAction(self.actionRedo_Output)
        self.menuConversion.addAction(self.actionRGB_to_Grayscale)
        self.menuConversion.addAction(self.actionRGB_tp_HSV)
        self.menuSegmentation.addAction(self.actionMulti_Otsu_Thresholding)
        self.menuSegmentation.addAction(self.actionChans_Vese_Segmentation)
        self.menuSegmentation.addAction(self.actionMorphological_Snakes)
        self.menuEdge_Detection.addAction(self.actionRoberts)
        self.menuEdge_Detection.addAction(self.actionSobel)
        self.menuEdge_Detection.addAction(self.actionScharr)
        self.menuEdge_Detection.addAction(self.actionPrewitt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConversion.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())

        self.retranslateUi(MainWindow)

        #Actions
        self.actionExit.triggered.connect(MainWindow.close)

        self.actionClear_Source.triggered.connect(self.source_img_label.close)
        self.actionClear_Source.triggered.connect(self.output_img_label.close)
        self.actionClear_Output.triggered.connect(self.output_img_label.close)

        self.actionOpen_Source.triggered.connect(self.getfile)
        self.actionOpen_Source.triggered.connect(self.enableaction)

        self.actionSave_Output.triggered.connect(self.Save_Data)

        self.actionSave_as_Output.triggered.connect(self.Save_as_Output)

        self.actionExport_as_Source.triggered.connect(self.export_as_source)

        self.actionExport_as_Output.triggered.connect(self.export_as_output)

        self.actionRGB_to_Grayscale.triggered.connect(self.rgbtogray)
        self.actionRGB_to_Grayscale.triggered.connect(self.enableoutput)

        self.actionRGB_tp_HSV.triggered.connect(self.rgbtohsv)
        self.actionRGB_tp_HSV.triggered.connect(self.enableoutput)

        self.actionMulti_Otsu_Thresholding.triggered.connect(self.multi_otsu)
        self.actionMulti_Otsu_Thresholding.triggered.connect(self.enableoutput)

        self.actionChans_Vese_Segmentation.triggered.connect(self.chan_vese)
        self.actionChans_Vese_Segmentation.triggered.connect(self.enableoutput)

        self.actionMorphological_Snakes.triggered.connect(self.morph_snakes)
        self.actionMorphological_Snakes.triggered.connect(self.enableoutput)

        self.actionRoberts.triggered.connect(self.roberts)
        self.actionRoberts.triggered.connect(self.enableoutput)
        self.actionSobel.triggered.connect(self.sobel)
        self.actionSobel.triggered.connect(self.enableoutput)
        self.actionScharr.triggered.connect(self.scharr)
        self.actionScharr.triggered.connect(self.enableoutput)
        self.actionPrewitt.triggered.connect(self.prewitt)
        self.actionPrewitt.triggered.connect(self.enableoutput)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.Source_button_box.setTitle(_translate("MainWindow", "Source"))
        
        self.Source_img_box.setTitle(_translate("MainWindow", "Source"))
        
        self.Edge_button_box.setTitle(_translate("MainWindow", "Edge Detection"))
        
        self.Output_button_box.setTitle(_translate("MainWindow", "Output"))
        
        self.Segment_button_box.setTitle(_translate("MainWindow", "Segmentation"))
        
        self.Output_img_box.setTitle(_translate("MainWindow", "Output"))
        
        self.Conv_button_box.setTitle(_translate("MainWindow", "Conversion"))
        
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_as.setTitle(_translate("MainWindow", "Export as..."))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuConversion.setTitle(_translate("MainWindow", "Conversion"))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))

        self.actionOpen_Source.setText(_translate("MainWindow", "Open Source"))
        self.actionOpen_Source.setStatusTip(_translate("MainWindow", "Open Source"))
        self.actionOpen_Source.setShortcut(_translate("MainWindow", "CTRL+F"))

        self.actionSave_Output.setText(_translate("MainWindow", "Save Output"))
        self.actionSave_Output.setStatusTip(_translate("MainWindow", "Save Output"))
        self.actionSave_Output.setShortcut(_translate("MainWindow", "CTRL+S"))

        self.actionSave_as_Output.setText(_translate("MainWindow", "Save as Output"))
        self.actionSave_as_Output.setStatusTip(_translate("MainWindow", "Save as Output"))
        self.actionSave_as_Output.setShortcut(_translate("MainWindow", "CTRL+A"))


        self.actionExport_as_Source.setText(_translate("MainWindow", "Source"))
        self.actionExport_as_Source.setStatusTip(_translate("MainWindow", "Export as Source"))
        self.actionExport_as_Output.setText(_translate("MainWindow", "Output"))
        self.actionExport_as_Output.setStatusTip(_translate("MainWindow", "Export as Output"))


        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "CTRL+E"))

        self.actionClear_Source.setText(_translate("MainWindow", "Source"))
        self.actionClear_Source.setStatusTip(_translate("MainWindow", "Clear Source"))
        self.actionClear_Output.setText(_translate("MainWindow", "Output"))
        self.actionClear_Output.setStatusTip(_translate("MainWindow", "Clear Output"))


        self.actionUndo_Output.setText(_translate("MainWindow", "Undo Output"))
        self.actionUndo_Output.setStatusTip(_translate("MainWindow", "Undo Output"))
        self.actionUndo_Output.setShortcut(_translate("MainWindow", "CTRL+U"))

        self.actionRedo_Output.setText(_translate("MainWindow", "Redo Output"))
        self.actionRedo_Output.setStatusTip(_translate("MainWindow", "Redo Output"))
        self.actionRedo_Output.setShortcut(_translate("MainWindow", "CTRL+R"))

        self.actionRGB_to_Grayscale.setText(_translate("MainWindow", "RGB to Grayscale"))
        self.actionRGB_to_Grayscale.setStatusTip(_translate("MainWindow", "RGB to Grayscale"))

        self.actionRGB_tp_HSV.setText(_translate("MainWindow", "RGB tp HSV"))
        self.actionRGB_tp_HSV.setStatusTip(_translate("MainWindow", "RGB tp HSV"))

        self.actionMulti_Otsu_Thresholding.setText(_translate("MainWindow", "Multi-Otsu Thresholding"))
        self.actionMulti_Otsu_Thresholding.setStatusTip(_translate("MainWindow", "Multi-Otsu Thresholding"))

        self.actionChans_Vese_Segmentation.setText(_translate("MainWindow", "Chans-Vese Segmentation"))
        self.actionChans_Vese_Segmentation.setStatusTip(_translate("MainWindow", "Chans-Vese Segmentation"))

        self.actionMorphological_Snakes.setText(_translate("MainWindow", "Morphological Snakes"))
        self.actionMorphological_Snakes.setStatusTip(_translate("MainWindow", "Morphological Snakes"))

        self.actionRoberts.setText(_translate("MainWindow", "Roberts"))
        self.actionRoberts.setStatusTip(_translate("MainWindow", "Roberts"))

        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionSobel.setStatusTip(_translate("MainWindow", "Sobel"))

        self.actionScharr.setText(_translate("MainWindow", "Scharr"))
        self.actionScharr.setStatusTip(_translate("MainWindow", "Scharr"))
        
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionPrewitt.setStatusTip(_translate("MainWindow", "Prewitt"))

    def getfile(self):
        self.fname, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Images", 'Desktop:\\',"Image files (*.jpg *.png)")
        self.source_img_label.setPixmap(QtGui.QPixmap(self.fname))
        self.Source_image = io.imread(self.fname)[:,:,:3]
        
    def Save_Data(self):
        io.imsave(self.fname,self.Output_image)

    def Save_as_Output(self):
        fname=QFileDialog.getSaveFileName(QFileDialog(),'Save As', 'c\\','Image files (*.jpg *.png)')
        io.imsave(fname[0], self.Output_image)

    def export_as_source(self):

        if self.fname[-3:] == 'PNG':
            fname=QFileDialog.getSaveFileName(QFileDialog(),'Save As', 'c\\','Image files (*.jpg)')
        
        if self.fname[-3:] == 'JPG':
            fname=QFileDialog.getSaveFileName(QFileDialog(),'Save As', 'c\\','Image files (*.png)')
        
        source_export_path = fname[0]
        io.imsave(source_export_path, self.Source_image)

    def export_as_output(self):
        if self.fname[-3:] == 'PNG':
            fname=QFileDialog.getSaveFileName(QFileDialog(),'Save As', 'c\\','Image files (*.jpg)')
        
        if self.fname[-3:] == 'JPG':
            fname=QFileDialog.getSaveFileName(QFileDialog(),'Save As', 'c\\','Image files (*.png)')
        
        self.outputImagePath = fname[0]
        io.imsave(self.outputImagePath, self.Output_image)

    def enableaction(self):
        
        self.actionExport_as_Source.setEnabled(True)
        self.actionExport_as_Output.setEnabled(True)
        self.actionChans_Vese_Segmentation.setEnabled(True)
        self.actionClear_Output.setEnabled(True)
        self.actionClear_Source.setEnabled(True)
        self.actionMorphological_Snakes.setEnabled(True)
        self.actionMulti_Otsu_Thresholding.setEnabled(True)
        self.actionPrewitt.setEnabled(True)
        self.actionRedo_Output.setEnabled(True)
        self.actionRGB_to_Grayscale.setEnabled(True)
        self.actionRGB_tp_HSV.setEnabled(True)
        self.actionRoberts.setEnabled(True)
        self.actionScharr.setEnabled(True)
        self.actionSobel.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)

    def enableoutput(self):
        self.actionSave_Output.setEnabled(True)
        self.actionSave_as_Output.setEnabled(True)

    def rgbtogray(self):
        gray_im = color.rgb2gray(self.Source_image)
        self.Output_image = gray_im
        io.imsave('tempOutput.jpg',gray_im)
        pixmap = QtGui.QPixmap('tempOutput.jpg')
        self.output_img_label.setPixmap(pixmap)

    def rgbtohsv(self):
        hsv_im = color.rgb2hsv(self.Source_image)
        self.Output_image = hsv_im
        io.imsave('tempOutput.jpg',hsv_im)
        pixmap = QtGui.QPixmap('tempOutput.jpg')
        self.output_img_label.setPixmap(pixmap)
    
    def multi_otsu(self):
        mo_im = filters.threshold_multiotsu(self.Source_image)
        regions = np.digitize(self.Source_image, bins=mo_im)
        self.Output_image = regions
        io.imsave('tempOutput.jpg',regions)
        pixmap = QtGui.QPixmap('tempOutput.jpg')
        self.output_img_label.setPixmap(pixmap)
    
    def chan_vese(self):
        gray_im = color.rgb2gray(self.Source_image)
        cv_im = img_as_float(gray_im)
        image_chanVese = segmentation.chan_vese(cv_im,mu =0.25,lambda1=1,lambda2=1,tol=1e-3, 
                                                      max_iter=200,dt=0.5, init_level_set="checkerboard", extended_output=True)
        self.Output_image = image_chanVese[1]
        io.imsave('tempOutput.jpg',image_chanVese[1])
        pixmap = QtGui.QPixmap('tempOutput.jpg')
        self.output_img_label.setPixmap(pixmap)

    def morph_snakes(self):
        gray_im = color.rgb2gray(self.Source_image)
        input_img =img_as_float(gray_im)
        init_ls = segmentation.checkerboard_level_set(input_img.shape, 6)
        evolution = []
        callback = self.store_evolution_in(evolution)
        l_s = segmentation.morphological_chan_vese(input_img, 35, init_level_set=init_ls, smoothing=3,
                                                    iter_callback=callback)
        self.Output_image = l_s
        io.imsave('tempOutput.jpg',l_s)
        pixmap = QtGui.QPixmap('tempOutput.jpg')
        self.output_img_label.setPixmap(pixmap)

    def store_evolution_in(self,lst):
        def _store(x):
            lst.append(np.copy(x))

        return _store


    def roberts(self):
        gray_im = color.rgb2gray(self.Source_image)
        rob_im = filters.roberts(gray_im)
        self.Output_image = rob_im
        io.imsave('tempOutput.jpg',rob_im)
        pixmap = QtGui.QPixmap('tempOutput.jpg')
        self.output_img_label.setPixmap(pixmap)

    def sobel(self):
        gray_im = color.rgb2gray(self.Source_image)
        sob_im = filters.sobel(gray_im)
        self.Output_image = sob_im
        io.imsave('tempOutput.jpg',sob_im)
        pixmap = QtGui.QPixmap('tempOutput.jpg')
        self.output_img_label.setPixmap(pixmap)

    def scharr(self):
        gray_im = color.rgb2gray(self.Source_image)
        scharr_im = filters.scharr(gray_im)
        self.Output_image = scharr_im
        io.imsave('tempOutput.jpg',scharr_im)
        pixmap = QtGui.QPixmap('tempOutput.jpg')
        self.output_img_label.setPixmap(pixmap)

    def prewitt(self):
        gray_im = color.rgb2gray(self.Source_image)
        prew_im = filters.prewitt(gray_im)
        self.Output_image = prew_im
        io.imsave('tempOutput.jpg',prew_im)
        pixmap = QtGui.QPixmap('tempOutput.jpg')
        self.output_img_label.setPixmap(pixmap)

import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())