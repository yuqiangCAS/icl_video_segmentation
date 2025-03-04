from PyQt4 import phonon
from PyQt4 import QtCore, QtGui
from Gui import Ui_MainWindow
from VideoWrapper import *
from Client import *
import FaceClustering
from SegmentRegister import *
from VideoInfo import *
import cv2
import random
import time
from multiprocessing import Process, Queue
from Segmenter import *
import csv
import os.path
import ast

class DesktopClient(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.segments = SegmentRegister([])
        self.basicInfo = None
        self.faceIndexing = []

        QtCore.QObject.connect(self.ui.segmentButton, QtCore.SIGNAL("clicked()"), self.segment)
        QtCore.QObject.connect(self.ui.browseButton, QtCore.SIGNAL("clicked()"), self.browse)
        QtCore.QObject.connect(self.ui.loadButton, QtCore.SIGNAL("clicked()"), self.loadCSV)
        QtCore.QObject.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"), self.save)
        QtCore.QObject.connect(self.ui.playButton, QtCore.SIGNAL("clicked()"), self.play)
        QtCore.QObject.connect(self.ui.pauseButton, QtCore.SIGNAL("clicked()"), self.ui.videoPlayer.pause)
        QtCore.QObject.connect(self.ui.nextButton, QtCore.SIGNAL("clicked()"), self.next)
        QtCore.QObject.connect(self.ui.previousButton, QtCore.SIGNAL("clicked()"), self.previous)
        QtCore.QObject.connect(self.ui.filePath, QtCore.SIGNAL("returnPressed()"), self.preload)
        QtCore.QObject.connect(self.ui.lastFrameButton, QtCore.SIGNAL("clicked()"), self.setLastFrame)
        QtCore.QObject.connect(self.ui.newButton, QtCore.SIGNAL("clicked()"), self.reset)
        QtCore.QObject.connect(self.ui.playNextButton, QtCore.SIGNAL("clicked()"), self.playNext)
        QtCore.QObject.connect(self.ui.advancedButton, QtCore.SIGNAL("clicked()"), self.toggleAdvanced)
        self.ui.segmentList.doubleClicked.connect(self.selectSegment)
        self.ui.faceList.doubleClicked.connect(self.selectSegmentFromFace)
        self.ui.faceList.setIconSize(QtCore.QSize(100,100))

        self.advanced = False
        self.reset()

    def toggleAdvanced(self, advancedSetting = None):
        if advancedSetting is None:
            self.advanced = not self.advanced
        else:
            self.advanced = advancedSetting

        if self.advanced:
            self.ui.advancedSettings.show()
            self.ui.advancedButton.setText("Hide advanced settings")
            self.ui.segmentLength.show()
            self.ui.segmentLengthLabel.show()
        else:
            self.ui.advancedSettings.hide()
            self.ui.advancedButton.setText("Show advanced settings")
            self.ui.segmentLength.hide()
            self.ui.segmentLengthLabel.hide()

    def selectSegmentFromFace(self):
        index = self.ui.faceList.selectedIndexes()[0]

        if index.parent().row() == -1:
            return

        _, start, _, end = index.data().toString().split(" ")
        start = int(start)
        end   = int(end)

        index = self.segments.getIndexFromStartEnd(start, end)
        self.segments.select(index);
        self.selectListEntry()
        self.selectSegment()

    def genIndexing(self, segments, clusters):
        self.faceIndexing = []

        for i, cluster in enumerate(clusters):
            image = cv2.resize(cluster[0][1], (100, 100))
            name = "Face {0}".format(i + 1)
            file = "{0}/face-{1}.jpg".format(directory, random.random())
            cv2.imwrite(file, image)

            segmentSet = set()
            for frame, _ in cluster:
                for _, start, end in segments:
                    if frame >= start and frame < end:
                        segmentSet.add((start, end))

            segmentList = sorted(list(segmentSet))
            self.faceIndexing.append((name, file, segmentList))

    def fillFaces(self):
        model = QtGui.QStandardItemModel()
        for name, file, segmentList in self.faceIndexing:
            item = QtGui.QStandardItem(QtGui.QIcon(file), name)
            item.setEditable(True)

            for start, end in segmentList:
                item2 = QtGui.QStandardItem("Segment %d - %d" % (start, end))
                item2.setEditable(False)
                item.appendRow(item2)

            model.appendRow(item)

        self.ui.faceList.setModel(model)

    def setLastFrame(self):
        """ Set the end frame to be the last frame of the video. """
        self.ui.endFrame.setText(str(self.basicInfo.numberOfFrames()))

    def browse(self):
        """ Opens a system "browse" dialog box and preloads the video file. """
        file = str(QtGui.QFileDialog.getOpenFileName(self, "Open Video"))

        if file != "":
            self.ui.filePath.setText(file)

            self.preload()

    def save(self):
        file = str(QtGui.QFileDialog.getSaveFileName(self, "Save Project File"))

        try:
            os.mkdir(file)
            self.segments.save(file)
            self.saveClusters(file)
        except IOError:
            self.errorBox("Charlie")
        except OSError:
            self.errorBox("Charlie")

    def saveClusters(self, file):
        with open(os.path.join(file, "indexing.csv"), 'wb') as raw:
            f = csv.writer(raw)
            for name, filename, segments in self.faceIndexing:
                f.writerow([name, os.path.split(filename)[1], segments])
                shutil.copy(filename, file)

    def loadCSV(self):
        # TODO : restrict to CSV files
        file = str(QtGui.QFileDialog.getOpenFileName(self, "Open Segments File", "", "Segments file (*.csv)"))
        if file == "": return

        segmentNames = []
        self.faceIndexing = []
        try:
            with open(file, 'rb') as raw:
                f = csv.reader(raw)
                for [s, e, name] in f:
                    segmentNames.append((os.path.join(os.path.dirname(file), name), int(s), int(e)))
            indexFile = os.path.join(os.path.dirname(file), "indexing.csv")
            if os.path.exists(indexFile):
                with open(indexFile, 'rb') as raw:
                    f = csv.reader(raw)
                    for arr in f:
                        name     = arr[0]
                        filename = os.path.join(os.path.dirname(file), arr[1])
                        vals     = ast.literal_eval(arr[2])
                        self.faceIndexing.append((name, filename, vals))
        except IOError:
            self.errorBox("Roxana")
            return
        except ValueError:
            self.errorBox("Agnieszka")
            return

        self.fillFaces()
        self.fillList(segmentNames)

        #load segments into the GUI, ignoring start and end frames
        self.segments = SegmentRegister(segmentNames)
        #self.ui.videoBackground.hide()
        self.setControls(True)
        self.updatePreviousNextButton()
        self.load(self.segments.current()) 
        self.showVideoScreen()
        self.selectListEntry()


    def switchView(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        #self.resize(self.ui.verticalLayout.sizeHint())
    
    def selectSegment(self):
        index = self.ui.segmentList.selectedIndexes()[0].row()

        self.segments.select(index)
        self.updatePreviousNextButton()
        self.load(self.segments.current())

    def errorBox(self, name):
        """ Customized error box. """
        birthday, error = "007", "Wrong video file: please load Skyfall trailer."
        if name == "Jasper":
            birthday, error = "1311", "Please enter a valid path."
        elif name == "Ben":
            birthday, error = "2211", "Start and end frames out of bounds."
        elif name == "Roxana":
            birthday, error = "2405b", "I/O Error, could not load save file."
        elif name == "Agnieszka":
            birthday, error = "2405a", "Not a valid save file."
        elif name == "Charlie":
            birthday, error = "2709", "I/O Error, could not save file."

        QtGui.QMessageBox.critical(self, "Error " + birthday, error)

    def preload(self):
        """
        Creates a VideoInfo object to fill in basic info about video file.
        Does not cause any segmenting or bounds checking to occur.
        """
        try:
            self.basicInfo = VideoInfo(str(self.ui.filePath.text()))
        except:
            self.errorBox("Jasper")
            return

        self.ui.startFrame.setText("0")
        self.ui.endFrame.setText("")
        self.ui.videoTitleLabel.setText("Title: " + self.basicInfo.prettyTitle())
        self.ui.videoLengthLabel.setText("Video length: " + self.basicInfo.prettyLength())
        self.ui.segmentButton.setEnabled(True)
        self.ui.lastFrameButton.setEnabled(True)

    def load(self, segment):
        """ 
        Loads but does not play a video file.
        Makes sure the first frame is shown by calling "pause()".
        """
        media = phonon.Phonon.MediaSource(segment)
        self.ui.videoPlayer.load(media)
        self.ui.videoPlayer.pause()

    def next(self):
        """ Grabs next segment, loads it, and updates GUI accordingly. """
        self.load(self.segments.next())
        self.updatePreviousNextButton()
        self.selectListEntry()

    def previous(self):
        """ Grabs previous segment, loads it, and updates GUI accordingly. """
        self.load(self.segments.previous())
        self.updatePreviousNextButton()
        self.selectListEntry()

    def play(self):
        """ Plays the current segment. """
        self.load(self.segments.current())
        self.ui.videoPlayer.play()

    def playNext(self):
        """ Plays the next segment. """
        self.next()
        self.play()

    def selectListEntry(self):
        """ Select an entry from the list to synchronise player/face indexing. """
        index = self.ui.segmentList.model().index(self.segments.currIndex(), 0, QtCore.QModelIndex())
        self.ui.segmentList.selectionModel().select(index, self.ui.segmentList.selectionModel().ClearAndSelect)

    def updatePreviousNextButton(self):
        """
        Enable or disable the "previous" and "next" buttons depending on the 
        index of the current segment.
        """
        self.ui.previousButton.setDisabled(self.segments.first())
        self.ui.nextButton.setDisabled(self.segments.last())
        self.ui.playNextButton.setDisabled(self.segments.last())

    def setControls(self, enabled):
        """ Global GUI button toggle. """
        self.ui.pauseButton.setEnabled(enabled)
        self.ui.playButton.setEnabled(enabled)
        self.ui.nextButton.setEnabled(enabled)
        self.ui.previousButton.setEnabled(enabled)
        self.ui.lastFrameButton.setEnabled(enabled)
        self.ui.playNextButton.setEnabled(enabled)

    def getSplitType(self):
        """ Radio button options to SplitType map. """
        if self.ui.blackFramesOption.isChecked():
            return SplitType.ON_BLACK_FRAMES
        if self.ui.everyXSecondsOption.isChecked():
            return SplitType.EVERY_X_SECONDS
        if self.ui.onFaceClustersOption.isChecked():
            return SplitType.ON_FACE_CLUSTERS

        return None

    def getClusterType(self):
        """ Radio button options for cluster types. """
        if self.ui.clusterStandard.isChecked():
            return FaceClustering.standardCluster
        if self.ui.clusterKMeans.isChecked():
            return FaceClustering.kMeansCluster
        if self.ui.clusterMeanShift.isChecked():
            return FaceClustering.meanShiftCluster

        return None

    def getComparisonMethod(self):
        """ Radio button options for comparison methods. """
        if self.ui.comparisonCombo.currentIndex() == 0:
            return FaceClustering.HistogramComparator
        if self.ui.comparisonCombo.currentIndex() == 1:
            return FaceClustering.PCAComparator

        return None

    def reset(self):
        """ Reset the controls to their defaults. """
        self.setControls(False)
        self.ui.videoTitleLabel.setText("Title:")
        self.ui.videoLengthLabel.setText("Video length:")
        self.ui.filePath.setText("")
        self.ui.segmentButton.setEnabled(False)
        self.ui.lastFrameButton.setEnabled(False)
        self.ui.highlightFacesOption.setCheckState(False)
        self.ui.onFaceClustersOption.click()
        self.ui.startFrame.setText("0")
        self.ui.endFrame.setText("")
        self.ui.segProgress.setProperty("value", 0)
        self.ui.barState.setText("")

        self.toggleAdvanced(False)

        model = QtGui.QStandardItemModel()
        self.ui.faceList.setModel(model)

        self.showOptionsScreen()

    def setProgress(self, x):
        """ Set the progress bar when running. """
        self.ui.segProgress.setProperty("value", x),
        QtGui.QApplication.processEvents()

    def setState(self, x):
        """ Set the state text when running. """
        self.ui.barState.setText(x)
        QtGui.QApplication.processEvents()

    def segment(self):
        """
        Calls the Client class to perform segmenting. Handles bound checking
        errors. Fills in segment register and updates GUI (button activation).
        """
        self.setControls(False)
        self.currSegment = 0

        #Get all the correct options and create a client
        cap = None
        try:
            start            = int(self.ui.startFrame.text())
            end              = int(self.ui.endFrame.text())
            splitType        = self.getSplitType()
            clusterType      = self.getClusterType()
            comparisonMethod = self.getComparisonMethod()

            options = {}
            if splitType == SplitType.EVERY_X_SECONDS:
                options["xSeconds"] = int(self.ui.xSecs.value())

            options["clusterThreshold"] = float(self.ui.clusterThreshold.value())
            options["k"]                = int(self.ui.kValue.value())
            options["cutoff"]           = float(self.ui.shiftCutoff.value())
            options["maxIterations"]    = int(self.ui.maxIters.value())
            options["segmentLength"]    = int(self.ui.segmentLength.value())
            options["audio"]            = str(self.ui.filePath.text())
            options["clusterAlgorithm"] = clusterType

            if clusterType == FaceClustering.standardCluster:
                options["comparator"]   = comparisonMethod
            else:
                options["comparator"]   = FaceClustering.PCAComparator

            cap = Client(str(self.ui.filePath.text()), splitType,
                         lambda x: self.setProgress(x),
                         lambda x: self.setState(x),
                         start, end)
        except IOError:
            return self.errorBox("Jasper")
        except (ValueError, BoundsError):
            return self.errorBox("Ben")

        # create Segmenter object to segment the video
        self.seg = Segmenter()

        # call Client.run, which in turn calls Segmenter.run to perform the segmentation
        segmentNames = cap.run(self.seg, self.ui.highlightFacesOption.isChecked(), "MP42", "mkv", True, options)

        if "clusters" in options:
            self.genIndexing(segmentNames, options["clusters"])
        else:
            self.genIndexing(segmentNames, [])

        self.fillFaces()
        self.fillList(segmentNames)

        #load segments into the GUI, ignoring start and end frames
        self.segments = SegmentRegister(segmentNames)
        #self.ui.videoBackground.hide()
        self.setControls(True)
        self.updatePreviousNextButton()
        self.load(self.segments.current()) 
        self.showVideoScreen()
        self.selectListEntry()

    def fillList(self, segments):
        """ Fill the frames list with the correct segments. """
        model = QtGui.QStandardItemModel()

        for i, (_, start, end) in enumerate(segments):
            item = QtGui.QStandardItem('{0} - frames {1} to {2}'.format(i+1, start, end))
            item.setEditable(False)
            model.appendRow(item)

        self.ui.segmentList.setModel(model)

    def showVideoScreen(self):
        """ Switch to the video screen. """
        self.ui.stackedWidget.setCurrentIndex(1)
        self.resize(1200, 500)

    def showOptionsScreen(self):
        """ Switch to the options screen. """
        self.ui.stackedWidget.setCurrentIndex(0)
        self.resize(581, 440)

