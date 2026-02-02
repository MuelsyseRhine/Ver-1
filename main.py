import numpy as np
import matplotlib.pyplot as plt

# 随机生成一个 100x100 的数据矩阵
data = np.random.rand(100, 100)

# 创建热力图
plt.figure(figsize=(8, 6))
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()  # 添加颜色条
plt.title('Random Heatmap 100x100')

# 保存图像
plt.savefig('heatmap_100x100.png', dpi=300, bbox_inches='tight')

# 显示图像（可选）
plt.show()