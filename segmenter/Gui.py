# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segmenter/gui.ui'
#
# Created: Tue Jan  8 21:13:22 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1030, 714)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 1px solid gray; \n"
"     border-radius: 5px; \n"
" } \n"
"\n"
"QGroupBox::title { \n"
"     background-color: transparent;\n"
"     subcontrol-position: top left; /* position at the top left*/ \n"
"     padding:3 8px;\n"
" } "))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.optionsPage = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionsPage.sizePolicy().hasHeightForWidth())
        self.optionsPage.setSizePolicy(sizePolicy)
        self.optionsPage.setObjectName(_fromUtf8("optionsPage"))
        self.gridLayout = QtGui.QGridLayout(self.optionsPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.optionsLayout = QtGui.QVBoxLayout()
        self.optionsLayout.setObjectName(_fromUtf8("optionsLayout"))
        self.filePathLayout = QtGui.QHBoxLayout()
        self.filePathLayout.setObjectName(_fromUtf8("filePathLayout"))
        self.filePath = QtGui.QLineEdit(self.optionsPage)
        self.filePath.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.filePath.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.filePath.setToolTip(_fromUtf8(""))
        self.filePath.setStatusTip(_fromUtf8(""))
        self.filePath.setWhatsThis(_fromUtf8(""))
        self.filePath.setText(_fromUtf8(""))
        self.filePath.setReadOnly(False)
        self.filePath.setObjectName(_fromUtf8("filePath"))
        self.filePathLayout.addWidget(self.filePath)
        self.browseButton = QtGui.QPushButton(self.optionsPage)
        self.browseButton.setDefault(False)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.filePathLayout.addWidget(self.browseButton)
        self.loadButton = QtGui.QPushButton(self.optionsPage)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.filePathLayout.addWidget(self.loadButton)
        self.optionsLayout.addLayout(self.filePathLayout)
        self.parametersLayout = QtGui.QHBoxLayout()
        self.parametersLayout.setObjectName(_fromUtf8("parametersLayout"))
        spacerItem = QtGui.QSpacerItem(0, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.parametersLayout.addItem(spacerItem)
        self.groupBox = QtGui.QGroupBox(self.optionsPage)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.startFrame = QtGui.QLineEdit(self.groupBox)
        self.startFrame.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.startFrame.setObjectName(_fromUtf8("startFrame"))
        self.gridLayout_5.addWidget(self.startFrame, 12, 0, 1, 1)
        self.segProgress = QtGui.QProgressBar(self.groupBox)
        self.segProgress.setMaximum(100)
        self.segProgress.setProperty("value", 0)
        self.segProgress.setObjectName(_fromUtf8("segProgress"))
        self.gridLayout_5.addWidget(self.segProgress, 17, 0, 1, 2)
        self.segmentButton = QtGui.QPushButton(self.groupBox)
        self.segmentButton.setEnabled(False)
        self.segmentButton.setObjectName(_fromUtf8("segmentButton"))
        self.gridLayout_5.addWidget(self.segmentButton, 16, 0, 1, 1)
        self.barState = QtGui.QLabel(self.groupBox)
        self.barState.setText(_fromUtf8(""))
        self.barState.setObjectName(_fromUtf8("barState"))
        self.gridLayout_5.addWidget(self.barState, 18, 0, 1, 2)
        self.highlightFacesOption = QtGui.QCheckBox(self.groupBox)
        self.highlightFacesOption.setObjectName(_fromUtf8("highlightFacesOption"))
        self.gridLayout_5.addWidget(self.highlightFacesOption, 15, 0, 1, 2)
        self.lastFrameButton = QtGui.QPushButton(self.groupBox)
        self.lastFrameButton.setEnabled(False)
        self.lastFrameButton.setCheckable(False)
        self.lastFrameButton.setObjectName(_fromUtf8("lastFrameButton"))
        self.gridLayout_5.addWidget(self.lastFrameButton, 14, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 11, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 13, 0, 1, 1)
        self.endFrame = QtGui.QLineEdit(self.groupBox)
        self.endFrame.setText(_fromUtf8(""))
        self.endFrame.setObjectName(_fromUtf8("endFrame"))
        self.gridLayout_5.addWidget(self.endFrame, 14, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 19, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(340, 300))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 331, 291))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_6.addWidget(self.label)
        self.onFaceClustersOption = QtGui.QRadioButton(self.verticalLayoutWidget_4)
        self.onFaceClustersOption.setChecked(True)
        self.onFaceClustersOption.setObjectName(_fromUtf8("onFaceClustersOption"))
        self.verticalLayout_6.addWidget(self.onFaceClustersOption)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.segmentLengthLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.segmentLengthLabel.setIndent(20)
        self.segmentLengthLabel.setObjectName(_fromUtf8("segmentLengthLabel"))
        self.horizontalLayout_8.addWidget(self.segmentLengthLabel)
        self.segmentLength = QtGui.QSpinBox(self.verticalLayoutWidget_4)
        self.segmentLength.setMinimum(1)
        self.segmentLength.setMaximum(1000000)
        self.segmentLength.setProperty("value", 20)
        self.segmentLength.setObjectName(_fromUtf8("segmentLength"))
        self.horizontalLayout_8.addWidget(self.segmentLength)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.everyXSecondsOption = QtGui.QRadioButton(self.verticalLayoutWidget_4)
        self.everyXSecondsOption.setObjectName(_fromUtf8("everyXSecondsOption"))
        self.verticalLayout_6.addWidget(self.everyXSecondsOption)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_10.setIndent(20)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_7.addWidget(self.label_10)
        self.xSecs = QtGui.QSpinBox(self.verticalLayoutWidget_4)
        self.xSecs.setMinimum(1)
        self.xSecs.setMaximum(999999999)
        self.xSecs.setProperty("value", 1)
        self.xSecs.setObjectName(_fromUtf8("xSecs"))
        self.horizontalLayout_7.addWidget(self.xSecs)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.blackFramesOption = QtGui.QRadioButton(self.verticalLayoutWidget_4)
        self.blackFramesOption.setObjectName(_fromUtf8("blackFramesOption"))
        self.verticalLayout_6.addWidget(self.blackFramesOption)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.advancedButton = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.advancedButton.setObjectName(_fromUtf8("advancedButton"))
        self.horizontalLayout_9.addWidget(self.advancedButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.advancedSettings = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advancedSettings.sizePolicy().hasHeightForWidth())
        self.advancedSettings.setSizePolicy(sizePolicy)
        self.advancedSettings.setMinimumSize(QtCore.QSize(360, 300))
        self.advancedSettings.setObjectName(_fromUtf8("advancedSettings"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.advancedSettings)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 351, 301))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.clusterStandard = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.clusterStandard.setChecked(True)
        self.clusterStandard.setObjectName(_fromUtf8("clusterStandard"))
        self.verticalLayout_5.addWidget(self.clusterStandard)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setIndent(20)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.clusterThreshold = QtGui.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.clusterThreshold.setDecimals(4)
        self.clusterThreshold.setMaximum(1.0)
        self.clusterThreshold.setSingleStep(0.01)
        self.clusterThreshold.setProperty("value", 0.63)
        self.clusterThreshold.setObjectName(_fromUtf8("clusterThreshold"))
        self.horizontalLayout_2.addWidget(self.clusterThreshold)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setIndent(20)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        self.comparisonCombo = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.comparisonCombo.setObjectName(_fromUtf8("comparisonCombo"))
        self.comparisonCombo.addItem(_fromUtf8(""))
        self.comparisonCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.comparisonCombo)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.clusterKMeans = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.clusterKMeans.setObjectName(_fromUtf8("clusterKMeans"))
        self.verticalLayout_5.addWidget(self.clusterKMeans)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setIndent(20)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.kValue = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.kValue.setMinimum(1)
        self.kValue.setMaximum(99999999)
        self.kValue.setSingleStep(1)
        self.kValue.setProperty("value", 2)
        self.kValue.setObjectName(_fromUtf8("kValue"))
        self.horizontalLayout_3.addWidget(self.kValue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setIndent(20)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.shiftCutoff = QtGui.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.shiftCutoff.setDecimals(4)
        self.shiftCutoff.setMaximum(100000.0)
        self.shiftCutoff.setSingleStep(0.5)
        self.shiftCutoff.setProperty("value", 1.0)
        self.shiftCutoff.setObjectName(_fromUtf8("shiftCutoff"))
        self.horizontalLayout_4.addWidget(self.shiftCutoff)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setIndent(20)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.maxIters = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.maxIters.setMinimum(-1)
        self.maxIters.setMaximum(999999999)
        self.maxIters.setProperty("value", -1)
        self.maxIters.setObjectName(_fromUtf8("maxIters"))
        self.horizontalLayout_5.addWidget(self.maxIters)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.clusterMeanShift = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.clusterMeanShift.setObjectName(_fromUtf8("clusterMeanShift"))
        self.verticalLayout_5.addWidget(self.clusterMeanShift)
        self.horizontalLayout.addWidget(self.advancedSettings)
        self.gridLayout_5.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.parametersLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.optionsPage)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.videoTitleLabel = QtGui.QLabel(self.groupBox_2)
        self.videoTitleLabel.setEnabled(True)
        self.videoTitleLabel.setObjectName(_fromUtf8("videoTitleLabel"))
        self.verticalLayout_2.addWidget(self.videoTitleLabel)
        self.videoLengthLabel = QtGui.QLabel(self.groupBox_2)
        self.videoLengthLabel.setObjectName(_fromUtf8("videoLengthLabel"))
        self.verticalLayout_2.addWidget(self.videoLengthLabel)
        spacerItem4 = QtGui.QSpacerItem(180, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.parametersLayout.addWidget(self.groupBox_2)
        self.optionsLayout.addLayout(self.parametersLayout)
        self.gridLayout.addLayout(self.optionsLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.optionsPage)
        self.videoPage = QtGui.QWidget()
        self.videoPage.setObjectName(_fromUtf8("videoPage"))
        self.gridLayout_3 = QtGui.QGridLayout(self.videoPage)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.videoLayout = QtGui.QVBoxLayout()
        self.videoLayout.setObjectName(_fromUtf8("videoLayout"))
        self.menuLayout = QtGui.QHBoxLayout()
        self.menuLayout.setObjectName(_fromUtf8("menuLayout"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.menuLayout.addItem(spacerItem5)
        self.newButton = QtGui.QPushButton(self.videoPage)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.menuLayout.addWidget(self.newButton)
        self.saveButton = QtGui.QPushButton(self.videoPage)
        self.saveButton.setEnabled(True)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.menuLayout.addWidget(self.saveButton)
        self.videoLayout.addLayout(self.menuLayout)
        self.previewLayout = QtGui.QHBoxLayout()
        self.previewLayout.setObjectName(_fromUtf8("previewLayout"))
        self.tabWidget = QtGui.QTabWidget(self.videoPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(256, 0))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.segmentTab = QtGui.QWidget()
        self.segmentTab.setObjectName(_fromUtf8("segmentTab"))
        self.gridLayout_9 = QtGui.QGridLayout(self.segmentTab)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.segmentList = QtGui.QListView(self.segmentTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.segmentList.sizePolicy().hasHeightForWidth())
        self.segmentList.setSizePolicy(sizePolicy)
        self.segmentList.setObjectName(_fromUtf8("segmentList"))
        self.gridLayout_8.addWidget(self.segmentList, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.segmentTab, _fromUtf8(""))
        self.facesTab = QtGui.QWidget()
        self.facesTab.setObjectName(_fromUtf8("facesTab"))
        self.gridLayout_7 = QtGui.QGridLayout(self.facesTab)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.faceList = QtGui.QTreeView(self.facesTab)
        self.faceList.setHeaderHidden(True)
        self.faceList.setObjectName(_fromUtf8("faceList"))
        self.gridLayout_6.addWidget(self.faceList, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.facesTab, _fromUtf8(""))
        self.previewLayout.addWidget(self.tabWidget)
        self.videoBackground = QtGui.QGroupBox(self.videoPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoBackground.sizePolicy().hasHeightForWidth())
        self.videoBackground.setSizePolicy(sizePolicy)
        self.videoBackground.setMinimumSize(QtCore.QSize(0, 0))
        self.videoBackground.setAutoFillBackground(False)
        self.videoBackground.setStyleSheet(_fromUtf8("QGroupBox#videoBackground { \n"
"     background: black;\n"
" } "))
        self.videoBackground.setTitle(_fromUtf8(""))
        self.videoBackground.setObjectName(_fromUtf8("videoBackground"))
        self.gridLayout_4 = QtGui.QGridLayout(self.videoBackground)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.videoBackground)
        self.videoPlayer.setMinimumSize(QtCore.QSize(0, 0))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.gridLayout_4.addWidget(self.videoPlayer, 0, 0, 1, 1)
        self.previewLayout.addWidget(self.videoBackground)
        self.videoLayout.addLayout(self.previewLayout)
        self.controlsLayout = QtGui.QHBoxLayout()
        self.controlsLayout.setObjectName(_fromUtf8("controlsLayout"))
        self.previousButton = QtGui.QPushButton(self.videoPage)
        self.previousButton.setEnabled(False)
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.controlsLayout.addWidget(self.previousButton)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.controlsLayout.addItem(spacerItem6)
        self.playButton = QtGui.QPushButton(self.videoPage)
        self.playButton.setEnabled(False)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.controlsLayout.addWidget(self.playButton)
        self.playNextButton = QtGui.QPushButton(self.videoPage)
        self.playNextButton.setEnabled(False)
        self.playNextButton.setObjectName(_fromUtf8("playNextButton"))
        self.controlsLayout.addWidget(self.playNextButton)
        self.pauseButton = QtGui.QPushButton(self.videoPage)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.controlsLayout.addWidget(self.pauseButton)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.controlsLayout.addItem(spacerItem7)
        self.nextButton = QtGui.QPushButton(self.videoPage)
        self.nextButton.setEnabled(False)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.controlsLayout.addWidget(self.nextButton)
        self.videoLayout.addLayout(self.controlsLayout)
        self.gridLayout_3.addLayout(self.videoLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.videoPage)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.startFrame, self.endFrame)
        MainWindow.setTabOrder(self.endFrame, self.lastFrameButton)
        MainWindow.setTabOrder(self.lastFrameButton, self.highlightFacesOption)
        MainWindow.setTabOrder(self.highlightFacesOption, self.segmentButton)
        MainWindow.setTabOrder(self.segmentButton, self.previousButton)
        MainWindow.setTabOrder(self.previousButton, self.playButton)
        MainWindow.setTabOrder(self.playButton, self.playNextButton)
        MainWindow.setTabOrder(self.playNextButton, self.pauseButton)
        MainWindow.setTabOrder(self.pauseButton, self.nextButton)
        MainWindow.setTabOrder(self.nextButton, self.newButton)
        MainWindow.setTabOrder(self.newButton, self.saveButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Segmentation", None))
        self.filePath.setPlaceholderText(_translate("MainWindow", "Please load a video file.", None))
        self.browseButton.setText(_translate("MainWindow", "Browse", None))
        self.loadButton.setText(_translate("MainWindow", "Load", None))
        self.groupBox.setTitle(_translate("MainWindow", "Options", None))
        self.startFrame.setText(_translate("MainWindow", "0", None))
        self.segmentButton.setText(_translate("MainWindow", "Segment", None))
        self.highlightFacesOption.setText(_translate("MainWindow", "Highlight faces", None))
        self.lastFrameButton.setText(_translate("MainWindow", "Last frame", None))
        self.label_2.setText(_translate("MainWindow", "Start frame : ", None))
        self.label_3.setText(_translate("MainWindow", "End frame : ", None))
        self.label.setText(_translate("MainWindow", "Split type", None))
        self.onFaceClustersOption.setText(_translate("MainWindow", "On face clusters", None))
        self.segmentLengthLabel.setText(_translate("MainWindow", "Max segment length:", None))
        self.everyXSecondsOption.setText(_translate("MainWindow", "Every X seconds", None))
        self.label_10.setText(_translate("MainWindow", "X:", None))
        self.blackFramesOption.setText(_translate("MainWindow", "On black frames", None))
        self.advancedButton.setText(_translate("MainWindow", "Show advanced settings", None))
        self.label_4.setText(_translate("MainWindow", "Clustering algorithm", None))
        self.clusterStandard.setText(_translate("MainWindow", "Standard", None))
        self.label_5.setText(_translate("MainWindow", "Clustering threshold:", None))
        self.label_9.setText(_translate("MainWindow", "Comparison method:", None))
        self.comparisonCombo.setItemText(0, _translate("MainWindow", "Histograms", None))
        self.comparisonCombo.setItemText(1, _translate("MainWindow", "PCA", None))
        self.clusterKMeans.setText(_translate("MainWindow", "K-means", None))
        self.label_6.setText(_translate("MainWindow", "K value:", None))
        self.label_7.setText(_translate("MainWindow", "Shift cutoff:", None))
        self.label_8.setText(_translate("MainWindow", "Maximum iterations:", None))
        self.clusterMeanShift.setText(_translate("MainWindow", "Mean-shift", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Info", None))
        self.videoTitleLabel.setText(_translate("MainWindow", "Title:", None))
        self.videoLengthLabel.setText(_translate("MainWindow", "Video length: ", None))
        self.newButton.setText(_translate("MainWindow", "New segmentation", None))
        self.saveButton.setText(_translate("MainWindow", "Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.segmentTab), _translate("MainWindow", "Segments", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.facesTab), _translate("MainWindow", "Faces", None))
        self.previousButton.setText(_translate("MainWindow", "Previous", None))
        self.playButton.setText(_translate("MainWindow", "Play", None))
        self.playNextButton.setText(_translate("MainWindow", "Play next", None))
        self.pauseButton.setText(_translate("MainWindow", "Pause", None))
        self.nextButton.setText(_translate("MainWindow", "Next", None))

from PyQt4 import phonon
