import rasterio
from rasterio.merge import merge
from rasterio.io import MemoryFile
import glob
import os
from collections import defaultdict

# 输入和输出路径
input_dir = r'Output1'
output_dir = r'Output'

# 获取所有tif文件路径
all_tifs = glob.glob(os.path.join(input_dir, '*.tif'))

# 按时间标签分组（MOD09Q1.A2008241）
grouped_files = defaultdict(list)
for tif in all_tifs:
    filename = os.path.basename(tif)
    key = '.'.join(filename.split('.')[:2])  # 提取 MOD09Q1.A2008241
    grouped_files[key].append(tif)

# 对每组进行合成
for key, files in grouped_files.items():
    # 按波段顺序排序（b01, b02, ...）
    files.sort()

    # 读取所有波段数据
    bands = []
    meta = None
    for f in files:
        with rasterio.open(f) as src:
            bands.append(src.read(1))
            if meta is None:
                meta = src.meta.copy()

    # 更新元数据为多波段
    meta.update(count=len(bands))

    # 输出文件路径
    output_path = os.path.join(output_dir, f"{key}.tif")

    # 写入合成的多波段tif
    with rasterio.open(output_path, 'w', **meta) as dst:
        for i, band in enumerate(bands, start=1):
            dst.write(band, i)

    print(f"合成完成：{output_path}")