from pyAudioAnalysis import audioSegmentation as aS
# [flagsInd, classesAll, acc, CM] = aS.mtFileClassification("data/scottish.wav", "data/svmSM", "svm", True, 'data/scottish.segments')
[flagsInd, classesAll, acc, CM] = aS.mtFileClassification("data/20170621_16sec.wav", "data/svmSM", "svm", True, 'data/scottish.segments')
