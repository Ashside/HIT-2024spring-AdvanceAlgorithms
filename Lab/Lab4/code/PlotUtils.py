import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


weight_times = np.array([0.0009992122650146484,3.0797290802001953,0.023352622985839844,9.468703031539917])
RS_times = np.array([0.04264402389526367,0.3873867988586426,1.839130163192749,3.4945101737976074,19.147817373275757])
EW_times = np.array([0.03461575508117676,0.33904409408569336,1.801034688949585,3.4524266719818115,18.225322484970093])
EO_times = np.array([0.035219430923461914,0.369171142578125,1.7322697639465332,3.506014585494995,18.153198719024658])
OE_times = np.array([0.03456544876098633,0.35442209243774414,1.8143458366394043,3.5645976066589355,18.734230756759644])
X = np.array([1,10,50,100,500])

plt.plot(X, RS_times, label='RS Time', marker='o')
plt.plot(X, EW_times, label='EW Time', marker='o')
plt.plot(X, EO_times, label='EO Time', marker='o')
plt.plot(X, OE_times, label='OE Time', marker='o')
plt.xlabel('Sample Num')
plt.ylabel('Time')
plt.title('Time vs Sample Num')

plt.legend()

plt.show()
plt.plot(["RS","EW","EO","OE"], weight_times, label='Weight Time', marker='o')
plt.xlabel('Sample Num')
plt.ylabel('Time')
plt.title('Time vs Method')
plt.legend()
plt.show()
