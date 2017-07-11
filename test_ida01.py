from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
[Fs, x] = audioBasicIO.readAudioFile("data/20170621_16sec.wav");
F = audioFeatureExtraction.stFeatureExtraction(x, float(Fs), float(0.1*Fs), float(0.1*Fs));
print(Fs)
print(x)
# plt.subplot(2,1,1); plt.plot(F[0,:]); plt.xlabel('Frame no'); plt.ylabel('ZCR'); 
plt.subplot(2,1,1); plt.plot(F[1,:]); plt.xlabel('Frame no'); plt.ylabel('Energy'); plt.show()

