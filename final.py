# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        MainWindow.resize(921, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_data = QtWidgets.QPushButton(self.centralwidget)
        self.open_data.setMinimumSize(QtCore.QSize(75, 23))
        self.open_data.setObjectName("open_data")
        self.horizontalLayout.addWidget(self.open_data)
        self.in_sol_button_box = QtWidgets.QGroupBox(self.centralwidget)
        self.in_sol_button_box.setMinimumSize(QtCore.QSize(161, 121))
        self.in_sol_button_box.setMaximumSize(QtCore.QSize(161, 121))
        self.in_sol_button_box.setObjectName("in_sol_button_box")
        self.gridLayout = QtWidgets.QGridLayout(self.in_sol_button_box)
        self.gridLayout.setObjectName("gridLayout")
        self.button_export_as_in_sol = QtWidgets.QPushButton(self.in_sol_button_box)
        self.button_export_as_in_sol.setMinimumSize(QtCore.QSize(41, 31))
        self.button_export_as_in_sol.setMaximumSize(QtCore.QSize(41, 31))
        self.button_export_as_in_sol.setObjectName("button_export_as_in_sol")
        self.gridLayout.addWidget(self.button_export_as_in_sol, 0, 1, 1, 2)
        self.button_clear_in_sol = QtWidgets.QPushButton(self.in_sol_button_box)
        self.button_clear_in_sol.setMinimumSize(QtCore.QSize(41, 31))
        self.button_clear_in_sol.setMaximumSize(QtCore.QSize(41, 31))
        self.button_clear_in_sol.setObjectName("button_clear_in_sol")
        self.gridLayout.addWidget(self.button_clear_in_sol, 0, 3, 1, 1)
        self.button_undo_in_sol = QtWidgets.QPushButton(self.in_sol_button_box)
        self.button_undo_in_sol.setMinimumSize(QtCore.QSize(41, 31))
        self.button_undo_in_sol.setMaximumSize(QtCore.QSize(41, 31))
        self.button_undo_in_sol.setObjectName("button_undo_in_sol")
        self.gridLayout.addWidget(self.button_undo_in_sol, 2, 0, 1, 2)
        self.button_save_in_so = QtWidgets.QPushButton(self.in_sol_button_box)
        self.button_save_in_so.setMinimumSize(QtCore.QSize(41, 31))
        self.button_save_in_so.setMaximumSize(QtCore.QSize(41, 31))
        self.button_save_in_so.setObjectName("button_save_in_so")
        self.gridLayout.addWidget(self.button_save_in_so, 0, 0, 1, 1)
        self.button_redo_in_sol = QtWidgets.QPushButton(self.in_sol_button_box)
        self.button_redo_in_sol.setMinimumSize(QtCore.QSize(41, 31))
        self.button_redo_in_sol.setMaximumSize(QtCore.QSize(41, 31))
        self.button_redo_in_sol.setObjectName("button_redo_in_sol")
        self.gridLayout.addWidget(self.button_redo_in_sol, 2, 3, 1, 1)
        self.horizontalLayout.addWidget(self.in_sol_button_box)
        self.fin_sol_button_box = QtWidgets.QGroupBox(self.centralwidget)
        self.fin_sol_button_box.setMinimumSize(QtCore.QSize(161, 121))
        self.fin_sol_button_box.setMaximumSize(QtCore.QSize(161, 121))
        self.fin_sol_button_box.setObjectName("fin_sol_button_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.fin_sol_button_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_save_fin_sol = QtWidgets.QPushButton(self.fin_sol_button_box)
        self.button_save_fin_sol.setMinimumSize(QtCore.QSize(41, 31))
        self.button_save_fin_sol.setMaximumSize(QtCore.QSize(41, 31))
        self.button_save_fin_sol.setObjectName("button_save_fin_sol")
        self.gridLayout_2.addWidget(self.button_save_fin_sol, 0, 0, 1, 1)
        self.button_export_as_fin_sol = QtWidgets.QPushButton(self.fin_sol_button_box)
        self.button_export_as_fin_sol.setMinimumSize(QtCore.QSize(41, 31))
        self.button_export_as_fin_sol.setMaximumSize(QtCore.QSize(41, 31))
        self.button_export_as_fin_sol.setObjectName("button_export_as_fin_sol")
        self.gridLayout_2.addWidget(self.button_export_as_fin_sol, 0, 1, 1, 1)
        self.button_clear_fin_sol = QtWidgets.QPushButton(self.fin_sol_button_box)
        self.button_clear_fin_sol.setMinimumSize(QtCore.QSize(41, 31))
        self.button_clear_fin_sol.setMaximumSize(QtCore.QSize(41, 31))
        self.button_clear_fin_sol.setObjectName("button_clear_fin_sol")
        self.gridLayout_2.addWidget(self.button_clear_fin_sol, 0, 2, 1, 1)
        self.button_undo_fin_sol = QtWidgets.QPushButton(self.fin_sol_button_box)
        self.button_undo_fin_sol.setMinimumSize(QtCore.QSize(41, 31))
        self.button_undo_fin_sol.setMaximumSize(QtCore.QSize(41, 31))
        self.button_undo_fin_sol.setObjectName("button_undo_fin_sol")
        self.gridLayout_2.addWidget(self.button_undo_fin_sol, 1, 0, 1, 1)
        self.button_redo_fin_sol = QtWidgets.QPushButton(self.fin_sol_button_box)
        self.button_redo_fin_sol.setMinimumSize(QtCore.QSize(41, 31))
        self.button_redo_fin_sol.setMaximumSize(QtCore.QSize(41, 31))
        self.button_redo_fin_sol.setObjectName("button_redo_fin_sol")
        self.gridLayout_2.addWidget(self.button_redo_fin_sol, 1, 2, 1, 1)
        self.horizontalLayout.addWidget(self.fin_sol_button_box)
        self.clus_button_box = QtWidgets.QGroupBox(self.centralwidget)
        self.clus_button_box.setMinimumSize(QtCore.QSize(191, 121))
        self.clus_button_box.setMaximumSize(QtCore.QSize(191, 121))
        self.clus_button_box.setObjectName("clus_button_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.clus_button_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.button_k_means = QtWidgets.QPushButton(self.clus_button_box)
        self.button_k_means.setMinimumSize(QtCore.QSize(41, 31))
        self.button_k_means.setMaximumSize(QtCore.QSize(41, 31))
        self.button_k_means.setObjectName("button_k_means")
        self.gridLayout_3.addWidget(self.button_k_means, 0, 0, 1, 1)
        self.button_affinity = QtWidgets.QPushButton(self.clus_button_box)
        self.button_affinity.setMinimumSize(QtCore.QSize(41, 31))
        self.button_affinity.setMaximumSize(QtCore.QSize(41, 31))
        self.button_affinity.setObjectName("button_affinity")
        self.gridLayout_3.addWidget(self.button_affinity, 0, 1, 1, 1)
        self.button_mean = QtWidgets.QPushButton(self.clus_button_box)
        self.button_mean.setMinimumSize(QtCore.QSize(41, 31))
        self.button_mean.setMaximumSize(QtCore.QSize(41, 31))
        self.button_mean.setObjectName("button_mean")
        self.gridLayout_3.addWidget(self.button_mean, 0, 2, 1, 1)
        self.button_spectral = QtWidgets.QPushButton(self.clus_button_box)
        self.button_spectral.setMinimumSize(QtCore.QSize(41, 31))
        self.button_spectral.setMaximumSize(QtCore.QSize(41, 31))
        self.button_spectral.setObjectName("button_spectral")
        self.gridLayout_3.addWidget(self.button_spectral, 1, 0, 1, 1)
        self.button_hierarchy = QtWidgets.QPushButton(self.clus_button_box)
        self.button_hierarchy.setMinimumSize(QtCore.QSize(41, 31))
        self.button_hierarchy.setMaximumSize(QtCore.QSize(41, 31))
        self.button_hierarchy.setObjectName("button_hierarchy")
        self.gridLayout_3.addWidget(self.button_hierarchy, 1, 1, 1, 1)
        self.button_dbscan = QtWidgets.QPushButton(self.clus_button_box)
        self.button_dbscan.setMinimumSize(QtCore.QSize(41, 31))
        self.button_dbscan.setMaximumSize(QtCore.QSize(41, 31))
        self.button_dbscan.setObjectName("button_dbscan")
        self.gridLayout_3.addWidget(self.button_dbscan, 1, 2, 1, 1)
        self.horizontalLayout.addWidget(self.clus_button_box)
        self.heur_button_box = QtWidgets.QGroupBox(self.centralwidget)
        self.heur_button_box.setMinimumSize(QtCore.QSize(111, 121))
        self.heur_button_box.setMaximumSize(QtCore.QSize(111, 121))
        self.heur_button_box.setObjectName("heur_button_box")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.heur_button_box)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.button_hill = QtWidgets.QPushButton(self.heur_button_box)
        self.button_hill.setMinimumSize(QtCore.QSize(41, 31))
        self.button_hill.setMaximumSize(QtCore.QSize(41, 31))
        self.button_hill.setObjectName("button_hill")
        self.verticalLayout_8.addWidget(self.button_hill)
        self.button_simulated = QtWidgets.QPushButton(self.heur_button_box)
        self.button_simulated.setMinimumSize(QtCore.QSize(41, 31))
        self.button_simulated.setMaximumSize(QtCore.QSize(41, 31))
        self.button_simulated.setObjectName("button_simulated")
        self.verticalLayout_8.addWidget(self.button_simulated)
        self.horizontalLayout.addWidget(self.heur_button_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_sol_box = QtWidgets.QGroupBox(self.centralwidget)
        self.in_sol_box.setMinimumSize(QtCore.QSize(381, 221))
        self.in_sol_box.setMaximumSize(QtCore.QSize(381, 221))
        self.in_sol_box.setObjectName("in_sol_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.in_sol_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.in_sol_text = QtWidgets.QTextBrowser(self.in_sol_box)
        self.in_sol_text.setObjectName("in_sol_text")
        self.verticalLayout_3.addWidget(self.in_sol_text)
        self.horizontalLayout_2.addWidget(self.in_sol_box)
        self.fin_sol_box = QtWidgets.QGroupBox(self.centralwidget)
        self.fin_sol_box.setMinimumSize(QtCore.QSize(371, 221))
        self.fin_sol_box.setMaximumSize(QtCore.QSize(371, 221))
        self.fin_sol_box.setObjectName("fin_sol_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fin_sol_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fin_sol_label = QtWidgets.QLabel(self.fin_sol_box)
        self.fin_sol_label.setMinimumSize(QtCore.QSize(351, 191))
        self.fin_sol_label.setMaximumSize(QtCore.QSize(351, 191))
        self.fin_sol_label.setObjectName("fin_sol_label")
        self.verticalLayout_4.addWidget(self.fin_sol_label)
        self.horizontalLayout_2.addWidget(self.fin_sol_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.info_box = QtWidgets.QGroupBox(self.centralwidget)
        self.info_box.setMinimumSize(QtCore.QSize(756, 181))
        self.info_box.setMaximumSize(QtCore.QSize(756, 181))
        self.info_box.setObjectName("info_box")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.info_box)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.info_text = QtWidgets.QTextBrowser(self.info_box)
        self.info_text.setObjectName("info_text")
        self.verticalLayout_5.addWidget(self.info_text)
        self.verticalLayout_2.addWidget(self.info_box)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Man_sol_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Man_sol_box.setMinimumSize(QtCore.QSize(146, 152))
        self.Man_sol_box.setMaximumSize(QtCore.QSize(146, 152))
        self.Man_sol_box.setObjectName("Man_sol_box")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Man_sol_box)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.hubs_label = QtWidgets.QLabel(self.Man_sol_box)
        self.hubs_label.setObjectName("hubs_label")
        self.verticalLayout_6.addWidget(self.hubs_label)
        self.hubs_text = QtWidgets.QTextBrowser(self.Man_sol_box)
        self.hubs_text.setObjectName("hubs_text")
        self.verticalLayout_6.addWidget(self.hubs_text)
        self.nodes_label = QtWidgets.QLabel(self.Man_sol_box)
        self.nodes_label.setObjectName("nodes_label")
        self.verticalLayout_6.addWidget(self.nodes_label)
        self.nodes_text = QtWidgets.QTextBrowser(self.Man_sol_box)
        self.nodes_text.setObjectName("nodes_text")
        self.verticalLayout_6.addWidget(self.nodes_text)
        self.verticalLayout.addWidget(self.Man_sol_box)
        self.Res_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Res_box.setMinimumSize(QtCore.QSize(146, 368))
        self.Res_box.setMaximumSize(QtCore.QSize(146, 368))
        self.Res_box.setObjectName("Res_box")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Res_box)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.res_label = QtWidgets.QLabel(self.Res_box)
        self.res_label.setMinimumSize(QtCore.QSize(121, 341))
        self.res_label.setMaximumSize(QtCore.QSize(121, 341))
        self.res_label.setObjectName("res_label")
        self.verticalLayout_7.addWidget(self.res_label)
        self.verticalLayout.addWidget(self.Res_box)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_as = QtWidgets.QMenu(self.menuFile)
        self.menuExport_as.setObjectName("menuExport_as")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuClear = QtWidgets.QMenu(self.menuEdit)
        self.menuClear.setObjectName("menuClear")
        self.menuUndo = QtWidgets.QMenu(self.menuEdit)
        self.menuUndo.setObjectName("menuUndo")
        self.menuRedo = QtWidgets.QMenu(self.menuEdit)
        self.menuRedo.setObjectName("menuRedo")
        self.menuClustering = QtWidgets.QMenu(self.menubar)
        self.menuClustering.setObjectName("menuClustering")
        self.menuHeuristics = QtWidgets.QMenu(self.menubar)
        self.menuHeuristics.setObjectName("menuHeuristics")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       
       
        self.actionOpen_Data = QtWidgets.QAction(MainWindow)
        self.actionOpen_Data.setObjectName("actionOpen_Data")
       
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
       
        self.actionSave_Initial_Solution = QtWidgets.QAction(MainWindow)
        self.actionSave_Initial_Solution.setObjectName("actionSave_Initial_Solution")
        self.actionSave_Initial_Solution.setEnabled(False)

        self.actionSave_Final_Solution = QtWidgets.QAction(MainWindow)
        self.actionSave_Final_Solution.setObjectName("actionSave_Final_Solution")
        self.actionSave_Final_Solution.setEnabled(False)

        self.actionExport_as = QtWidgets.QAction(MainWindow)
        self.actionExport_as.setObjectName("actionExport_as")
        self.actionExport_as.setEnabled(False)

        self.actionExport_as_Initial_Solution = QtWidgets.QAction(MainWindow)
        self.actionExport_as_Initial_Solution.setObjectName("actionInitial_Solution")
        self.actionExport_as_Initial_Solution.setEnabled(False)

        self.actionExport_as_Final_Solution = QtWidgets.QAction(MainWindow)
        self.actionExport_as_Final_Solution.setObjectName("actionFinal_Solution")
        self.actionExport_as_Final_Solution.setEnabled(False)

        self.actionclear_Initial_Solution = QtWidgets.QAction(MainWindow)
        self.actionclear_Initial_Solution.setObjectName("actionclear_Initial_Solution")
        self.actionclear_Initial_Solution.setEnabled(False)

        self.actionclear_Final_Solution = QtWidgets.QAction(MainWindow)
        self.actionclear_Final_Solution.setObjectName("actionclear_Final_Solution")
        self.actionclear_Final_Solution.setEnabled(False)

        self.actionundo_Initial_Solution = QtWidgets.QAction(MainWindow)
        self.actionundo_Initial_Solution.setObjectName("actionundo_Initial_Solution")
        self.actionundo_Initial_Solution.setEnabled(False)

        self.actionundo_Final_Solution = QtWidgets.QAction(MainWindow)
        self.actionundo_Final_Solution.setObjectName("actionundo_Final_Solution")
        self.actionundo_Final_Solution.setEnabled(False)

        self.actionredo_Initial_Solution = QtWidgets.QAction(MainWindow)
        self.actionredo_Initial_Solution.setObjectName("actionredo_Initial_Solution")
        self.actionredo_Initial_Solution.setEnabled(False)

        self.actionredoFinal_Solution = QtWidgets.QAction(MainWindow)
        self.actionredoFinal_Solution.setObjectName("actionredoFinal_Solution")
        self.actionredoFinal_Solution.setEnabled(False)

        self.actionK_Means = QtWidgets.QAction(MainWindow)
        self.actionK_Means.setObjectName("actionK_Means")
        self.actionK_Means.setEnabled(False)

        self.actionAffinity_Propagation = QtWidgets.QAction(MainWindow)
        self.actionAffinity_Propagation.setObjectName("actionAffinity_Propagation")
        self.actionAffinity_Propagation.setEnabled(False)

        self.actionMean_shift = QtWidgets.QAction(MainWindow)
        self.actionMean_shift.setObjectName("actionMean_shift")
        self.actionMean_shift.setEnabled(False)

        self.actionSpectral_Clustering = QtWidgets.QAction(MainWindow)
        self.actionSpectral_Clustering.setObjectName("actionSpectral_Clustering")
        self.actionSpectral_Clustering.setEnabled(False)

        self.actionHierarchical_Clustering = QtWidgets.QAction(MainWindow)
        self.actionHierarchical_Clustering.setObjectName("actionHierarchical_Clustering")
        self.actionHierarchical_Clustering.setEnabled(False)

        self.actionDBSCAN = QtWidgets.QAction(MainWindow)
        self.actionDBSCAN.setObjectName("actionDBSCAN")
        self.actionDBSCAN.setEnabled(False)

        self.actionHill_Climbing = QtWidgets.QAction(MainWindow)
        self.actionHill_Climbing.setObjectName("actionHill_Climbing")
        self.actionHill_Climbing.setEnabled(False)

        self.actionSimulated_Anneling = QtWidgets.QAction(MainWindow)
        self.actionSimulated_Anneling.setObjectName("actionSimulated_Anneling")
        self.actionSimulated_Anneling.setEnabled(False)

        self.menuExport_as.addAction(self.actionExport_as_Initial_Solution)
        self.menuExport_as.addAction(self.actionExport_as_Final_Solution)
        self.menuFile.addAction(self.actionOpen_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Initial_Solution)
        self.menuFile.addAction(self.actionSave_Final_Solution)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExport_as.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuClear.addAction(self.actionclear_Initial_Solution)
        self.menuClear.addAction(self.actionclear_Final_Solution)
        self.menuUndo.addAction(self.actionundo_Initial_Solution)
        self.menuUndo.addAction(self.actionundo_Final_Solution)
        self.menuRedo.addAction(self.actionredo_Initial_Solution)
        self.menuRedo.addAction(self.actionredoFinal_Solution)
        self.menuEdit.addAction(self.menuClear.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuUndo.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuRedo.menuAction())
        self.menuClustering.addAction(self.actionK_Means)
        self.menuClustering.addAction(self.actionAffinity_Propagation)
        self.menuClustering.addAction(self.actionMean_shift)
        self.menuClustering.addAction(self.actionSpectral_Clustering)
        self.menuClustering.addAction(self.actionHierarchical_Clustering)
        self.menuClustering.addAction(self.actionDBSCAN)
        self.menuHeuristics.addAction(self.actionHill_Climbing)
        self.menuHeuristics.addAction(self.actionSimulated_Anneling)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuClustering.menuAction())
        self.menubar.addAction(self.menuHeuristics.menuAction())

        self.retranslateUi(MainWindow)

        #Actions
        #calls open data, enables cluster menu
        #self.actionOpen_Data.triggered.connect(self.open_data)
        self.actionOpen_Data.triggered.connect(self.enable_cluster)

        #enables save and export initial sol after a cluster item is clicked
        self.actionK_Means.triggered.connect(self.enable_init)
        self.actionAffinity_Propagation.triggered.connect(self.enable_init)
        self.actionMean_shift.triggered.connect(self.enable_init)
        self.actionSpectral_Clustering.triggered.connect(self.enable_init)
        self.actionHierarchical_Clustering.triggered.connect(self.enable_init)
        self.actionDBSCAN.triggered.connect(self.enable_init)

        #enables save and export final sol after a heuristics item is clicked
        self.actionHill_Climbing.triggered.connect(self.enable_final)
        self.actionSimulated_Anneling.triggered.connect(self.enable_final)

        #clear functions
        self.actionclear_Initial_Solution.triggered.connect(self.in_sol_text.close)
        self.actionclear_Initial_Solution.triggered.connect(self.fin_sol_label.close)
        self.actionclear_Final_Solution.triggered.connect(self.fin_sol_label.close)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_data.setText(_translate("MainWindow", "Open Data"))
        self.in_sol_button_box.setTitle(_translate("MainWindow", "Initial Solution"))
        self.button_export_as_in_sol.setText(_translate("MainWindow", "PushButton"))
        self.button_clear_in_sol.setText(_translate("MainWindow", "PushButton"))
        self.button_undo_in_sol.setText(_translate("MainWindow", "PushButton"))
        self.button_save_in_so.setText(_translate("MainWindow", "PushButton"))
        self.button_redo_in_sol.setText(_translate("MainWindow", "PushButton"))
        self.fin_sol_button_box.setTitle(_translate("MainWindow", "Final Solution"))
        self.button_save_fin_sol.setText(_translate("MainWindow", "PushButton"))
        self.button_export_as_fin_sol.setText(_translate("MainWindow", "PushButton"))
        self.button_clear_fin_sol.setText(_translate("MainWindow", "PushButton"))
        self.button_undo_fin_sol.setText(_translate("MainWindow", "PushButton"))
        self.button_redo_fin_sol.setText(_translate("MainWindow", "PushButton"))
        self.clus_button_box.setTitle(_translate("MainWindow", "Clustering"))
        self.button_k_means.setText(_translate("MainWindow", "PushButton"))
        self.button_affinity.setText(_translate("MainWindow", "PushButton"))
        self.button_mean.setText(_translate("MainWindow", "PushButton"))
        self.button_spectral.setText(_translate("MainWindow", "PushButton"))
        self.button_hierarchy.setText(_translate("MainWindow", "PushButton"))
        self.button_dbscan.setText(_translate("MainWindow", "PushButton"))
        self.heur_button_box.setTitle(_translate("MainWindow", "Heuristics"))
        self.button_hill.setText(_translate("MainWindow", "PushButton"))
        self.button_simulated.setText(_translate("MainWindow", "PushButton"))
        self.in_sol_box.setTitle(_translate("MainWindow", "Initial Solution"))
        self.fin_sol_box.setTitle(_translate("MainWindow", "Final Solution"))
        self.fin_sol_label.setText(_translate("MainWindow", "Final Solution"))
        self.info_box.setTitle(_translate("MainWindow", "Info Panel"))
        self.Man_sol_box.setTitle(_translate("MainWindow", "Manual Solution"))
        self.hubs_label.setText(_translate("MainWindow", "Hubs"))
        self.nodes_label.setText(_translate("MainWindow", "Nodes"))
        self.Res_box.setTitle(_translate("MainWindow", "Results"))
        self.res_label.setText(_translate("MainWindow", "Results"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_as.setTitle(_translate("MainWindow", "Export as.."))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuUndo.setTitle(_translate("MainWindow", "Undo"))
        self.menuRedo.setTitle(_translate("MainWindow", "Redo"))
        self.menuClustering.setTitle(_translate("MainWindow", "Clustering"))
        self.menuHeuristics.setTitle(_translate("MainWindow", "Heuristics"))
        self.actionOpen_Data.setText(_translate("MainWindow", "Open Data"))
        self.actionSave_Initial_Solution.setText(_translate("MainWindow", "Save Initial Solution"))
        self.actionSave_Final_Solution.setText(_translate("MainWindow", "Save Final Solution"))
        self.actionExport_as.setText(_translate("MainWindow", "Export as"))
        self.actionExport_as_Initial_Solution.setText(_translate("MainWindow", "Initial Solution"))
        self.actionExport_as_Final_Solution.setText(_translate("MainWindow", "Final Solution"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionclear_Initial_Solution.setText(_translate("MainWindow", "Initial Solution"))
        self.actionclear_Final_Solution.setText(_translate("MainWindow", "Final Solution"))
        self.actionundo_Initial_Solution.setText(_translate("MainWindow", "Initial Solution"))
        self.actionundo_Final_Solution.setText(_translate("MainWindow", "Final Solution"))
        self.actionredo_Initial_Solution.setText(_translate("MainWindow", "Initial Solution"))
        self.actionredoFinal_Solution.setText(_translate("MainWindow", "Final Solution"))
        self.actionK_Means.setText(_translate("MainWindow", "K-Means"))
        self.actionAffinity_Propagation.setText(_translate("MainWindow", "Affinity Propagation"))
        self.actionMean_shift.setText(_translate("MainWindow", "Mean-shift"))
        self.actionSpectral_Clustering.setText(_translate("MainWindow", "Spectral Clustering"))
        self.actionHierarchical_Clustering.setText(_translate("MainWindow", "Hierarchical Clustering"))
        self.actionDBSCAN.setText(_translate("MainWindow", "DBSCAN"))
        self.actionHill_Climbing.setText(_translate("MainWindow", "Hill Climbing"))
        self.actionSimulated_Anneling.setText(_translate("MainWindow", "Simulated Anneling"))

    def enable_cluster(self):
        
        self.actionK_Means.setEnabled(True)
        self.actionAffinity_Propagation.setEnabled(True)
        self.actionMean_shift.setEnabled(True)
        self.actionSpectral_Clustering.setEnabled(True)
        self.actionHierarchical_Clustering.setEnabled(True)
        self.actionDBSCAN.setEnabled(True)
        self.actionclear_Initial_Solution.setEnabled(True)

    def enable_heuritics(self):
        self.actionHill_Climbing.setEnabled(True)
        self.actionSimulated_Anneling.setEnabled(True)
        self.actionclear_Final_Solution.setEnabled(True)

    def enable_init(self):
        self.actionExport_as.setEnabled(True)
        self.actionSave_Initial_Solution.setEnabled(True)
        self.actionExport_as_Initial_Solution.setEnabled(True)
        self.actionredo_Initial_Solution.setEnabled(True)
        self.actionundo_Initial_Solution.setEnabled(True)

    def enable_final(self):
        self.actionSave_Final_Solution.setEnabled(True)
        self.actionExport_as_Final_Solution.setEnabled(True)
        self.actionredoFinal_Solution.setEnabled(True)
        self.actionundo_Final_Solution.setEnabled(True)  

    def open_data(self):
        self.fname, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Text", 'Desktop:\\',"Text Files (*.txt)")

    def save_initial(self):
        fname=QFileDialog.getSaveFileName(QFileDialog(),'Save As', 'c\\','Text files (*.txt)')
        with open(fname, 'w') as f:
            f.write()

    def save_final(self):
        fname=QFileDialog.getSaveFileName(QFileDialog(),'Save As', 'c\\','Text files (*.txt)')
        with open(fname, 'w') as f:
            f.write()    

    def export_initial(self):
        fname=QFileDialog.getSaveFileName(QFileDialog(),'Save As', 'c\\','Image files (*.jpg)')
        source_export_path = fname[0]
        io.imsave(source_export_path, self.Source_image)   

    def export_final(self):
        fname=QFileDialog.getSaveFileName(QFileDialog(),'Save As', 'c\\','Image files (*.jpg)')
        source_export_path = fname[0]
        io.imsave(source_export_path, self.Source_image)  

import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())