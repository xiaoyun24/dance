import numpy as np
import csv

# Set the means and standard deviations for the lists
jbg_means = [1.5,1.7,1.8,1.5,1.8,1.6,1.7,1.4,1.3,1.7,1.2,1.7,1.5,1.7,1.9,1.1,1.7,1.7,1.3,1.7,2.7,2.3,2 ]
jbg_std_devs = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5 ]
jbg_ranges = [(0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2),  (0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2),  (0, 2), (0, 2), (0, 2), (0, 2), (0, 3), (0, 3), (0, 3)]


ztq_means = [6,4,2,2,3,1]
ztq_std_devs = [1,1,1,0.5,0.5,0.2]
ztq_ranges = [(0,8), (0,4), (0, 2), (0, 2), (0, 3), (0, 1)]

gj_means = [4,4,3,2,3,2]
gj_std_devs = [1,1,1,1,1,0.5]
gj_ranges = [(0,6), (0,6), (0, 5), (0, 5), (0, 5), (0, 3)]

tj_means = [3.5, 3.7, 3.7, 6.2, 4.2]
tj_std_devs = [0.8, 0.8, 0.8, 1, 0.5]
tj_ranges = [(0, 5), (0, 5), (0, 5), (0, 9), (0, 6)]

sz_means = [6,4 , 3.2]
sz_std_devs = [0.8, 0.8, 0.8]
sz_ranges = [(0, 8), (0, 6), (0, 6)]

prev_means = [70]*15
prev_std_devs = [13 ]*15
prev_ranges = [(0,100)]*15


means = jbg_means + ztq_means + gj_means + tj_means + sz_means + prev_means
std_devs = jbg_std_devs + ztq_std_devs + gj_std_devs + tj_std_devs + sz_std_devs + prev_std_devs
ranges = jbg_ranges + ztq_ranges + gj_ranges + tj_ranges + sz_ranges + prev_ranges

length = len(means)




# Define the correlation coefficient
correlation = 0.5

# Create the covariance matrix for 5 lists
cov_matrix = np.full((length, length), correlation * std_devs[0] * std_devs[1])
for i in range(length):
    for j in range(length):
        cov_matrix[i, j] = correlation * std_devs[i] * std_devs[j] if i != j else std_devs[i]**2

# Generate 100 samples from a multivariate normal distribution
samples = np.random.multivariate_normal(means, cov_matrix, 100)

# Split the samples into five lists and clip them to the specified ranges
lists = [np.clip(np.round(samples[:, i]), ranges[i][0], ranges[i][1]) for i in range(length)]




jbg_score = np.zeros((1,100))
ztq_score = np.zeros((1,100))
gj_score = np.zeros((1,100))
tj_score = np.zeros((1,100))
sz_score = np.zeros((1,100))
total_score = np.zeros((1,100))


for l in lists[0:23]:
  jbg_score += l
for l in lists[23:29]:
  ztq_score += l
for l in lists[29:35]:
  gj_score += l
for l in lists[35:40]:
  tj_score+= l
for l in lists[40:43]:
  sz_score += l
for l in lists[0:43]:
  total_score += l






history_list = lists[43:58]

history_total_matrix = np.zeros_like(history_list)
history_total_matrix[0] = history_list[0]
for i in range(1, np.shape(history_list)[0]):
    history_total_matrix[i] = np.sum(history_list[:i+1], axis=0)


history_rank_matrix = np.zeros_like(history_list)
for i in range(0, np.shape(history_list)[0]):
    history_rank_matrix[i] = history_total_matrix[i].argsort()[::-1].argsort() + 1


semester_score = history_total_matrix[-1] + total_score*5
semester_rank = 100 - semester_score.argsort()[::-1].argsort() 




csv_intro = ["姓名","学号","班号","排名","总分","基本功","主题曲","个人剧目","团队剧目","素质测评","舞步圆场","四拍舞步","地面练习提、沉、转腰","含、展、横移","踢、撩腿","大环动","压、扳腿","大踢腿（一）","扶把练习","蹲","小踢、弹腿","端、掖腿蹲","吸伸腿","大踢腿（二）","中间练习盘手","弯腰","平转","小跳（一）","小跳（二）","速度反应","蒙古族舞","唯吾尔族舞","傣族舞","技术动作","情感传达","肢体能量","乐感节奏","创新动作","舞台表现","舞蹈技巧","艺术表现","编排创意","舞台表现","音乐理解","服装","技术动作1","技术动作2","技术动作3","团队协作","情感传达","姿态体态","表现力","即兴编舞"]
csv_total = [0,0, 0,0, 150,50,20,30,30,20, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,8,4,2,2,3,1,6,6,5,5,5,4,5,5,5,9,6,8,6,6]
csv_average = [0,0,0,0 ] + [sum(jbg_means) + sum(ztq_means) + sum(gj_means) + sum(tj_means) + sum(sz_means)] +  [sum(jbg_means)] + [sum(ztq_means)]  + [sum(gj_means)] + [sum(tj_means)] + [sum(sz_means)] +  jbg_means + ztq_means + gj_means + tj_means + sz_means
csv_average = np.array(csv_average, dtype  = np.float64)


ranking = 100 - total_score.argsort()[::-1].argsort() 
person_num = np.linspace(353, 452, 100, dtype=int)
class_num = np.repeat(np.arange(1, 11), 10)
np.random.shuffle(class_num)
score = np.vstack(( person_num, class_num, ranking, total_score, jbg_score, ztq_score, gj_score ,tj_score, sz_score, lists))
score = score.T
score = score.astype(int)
name_list = ['白宇轩', '卞博文', '曹天宇', '常俊杰', '程昊天', '程子涵', '陈思羽', '陈思源', '陈子涵', '崔宇轩', '戴宇翔', '戴宇轩', '邓思羽', '邓子轩', '丁浩天', '翟子涵', '董子睿', '冯子睿', '付子豪', '高俊凯', '高思羽', '郭浩宇', '郭子豪', '韩思源', '何昊然', '贺俊杰', '何天宇', '贺宇翔', '华俊凯', '黄子涵', '胡俊凯', '胡天睿', '蒋睿博', '江宇轩', '蒋子睿', '蒋子轩', '柯昊然', '柯杰尹', '孔维熙', '黎博文', '李浩然', '李俊杰', '李俊熙', '林子轩', '李瑞泽', '刘瑞杰', '刘宇轩', '龙俊杰', '罗宇航', '马子睿', '潘子涵', '彭子航', '钱子豪', '史俊豪', '宋文杰', '孙思远', '孙子涵', '谭博文', '唐子豪', '唐子轩', '王俊豪', '王宇轩', '王子睿', '韦俊豪', '文子睿', '吴昊天', '吴子睿', '萧俊豪', '夏扬', '谢俊杰', '谢子涵', '熊昊天', '许晨曦', '许晨曦', '薛宇航', '徐浩轩', '许睿杰', '徐思远', '许子睿', '杨博文', '杨晨轩', '杨宇轩', '袁俊杰', '袁宇翔', '张俊豪', '张文博', '张宇航', '赵嘉文', '赵云飞', '赵子涵', '赵子睿', '郑浩天', '郑子睿', '周俊豪', '周宇浩', '周宇翔', '周子轩', '朱博文', '朱浩宇', '朱俊熙']


with open('score.csv', 'a', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(csv_intro)
   writer.writerow(csv_total)
   writer.writerow(csv_average)
   for i in range(len(score)):
     writer.writerow([name_list[i]] + list(score[i]))




rank = np.vstack(( person_num,  history_list, history_total_matrix, total_score, semester_score, history_rank_matrix , ranking, semester_rank))
rank = rank.T
rank = rank.astype(int)


csv_ranking_intro = ["姓名", "学号"] + ["第"+str(i + 1)+"周得分" for i in range(15)]  + ["第"+str(i + 1)+"总得分" for i in range(15)] + ["期末考试成绩", "学期成绩"]+ ["第"+str(i + 1)+"周排名" for i in range(15)] + ["期末考试排名", "学期排名"]

with open('ranking.csv', 'a', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(csv_ranking_intro)
   for i in range(len(rank)):
      
      writer.writerow([name_list[i]] + list(rank[i]))






