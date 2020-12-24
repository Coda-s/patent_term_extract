# patent_term_extract

某摸鱼症晚期患者的毕业设计

正在缓慢更新中......

### 文件说明
#### data
源数据, 分为 train,dev,test, 格式比较清奇.

仅考虑原子术语, 不考虑嵌套术语的情况

#### processed_data
处理后的数据，分为 train,dev,test. 将术语标注为BIO格式


#### data_processing.py
主要用于处理源数据, 将源数据变为可用于模型的数据, 保存在processed_data中

添加了一个check函数, 用于测试正则转换是否正确

build_vocab函数, 用于根据训练集数据建立词表

