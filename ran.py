import numpy as np
import csv
import random

# Set the means and standard deviations for the lists
dan_jbg_means = [1.5,1.7,1.8,1.5,1.8,1.6,1.7,1.4,1.3,1.7,1.2,1.7,1.5,1.7,1.9,1.1,1.7,1.7,1.3,1.7,2.7,2.3,2 ]
dan_jbg_std_devs = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5 ]
dan_jbg_ranges = [(0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2),  (0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2),  (0, 2), (0, 2), (0, 2), (0, 2), (0, 3), (0, 3), (0, 3)]


dan_ztq_means = [6,4,2,2,3,1]
dan_ztq_std_devs = [1,1,1,0.5,0.5,0.2]
dan_ztq_ranges = [(0,8), (0,4), (0, 2), (0, 2), (0, 3), (0, 1)]

dan_gj_means = [4,4,3,2,3,2]
dan_gj_std_devs = [1,1,1,1,1,0.5]
dan_gj_ranges = [(0,6), (0,6), (0, 5), (0, 5), (0, 5), (0, 3)]

dan_tj_means = [3.5, 3.7, 3.7, 6.2, 4.2]
dan_tj_std_devs = [0.8, 0.8, 0.8, 1, 0.5]
dan_tj_ranges = [(0, 5), (0, 5), (0, 5), (0, 9), (0, 6)]

dan_sz_means = [6,4 , 3.2]
dan_sz_std_devs = [0.8, 0.8, 0.8]
dan_sz_ranges = [(0, 8), (0, 6), (0, 6)]


gym_exercise_means = [random.uniform(7, 9)]*7
gym_exercise_std_devs = [random.uniform(0.8,1.2)]*7
gym_exercise_ranges = [(3,10)]*7


gym_run_means = [random.uniform(7, 9)]*2
gym_run_std_devs = [random.uniform(0.8,1.2)]*2
gym_run_ranges = [(3,10)]*2

gym_art_means = [random.uniform(3,4)]*2 + [random.uniform(7, 9)]
gym_art_std_devs = [random.uniform(0.8,1.2)]*3
gym_art_ranges = [(1,5)]*2 + [(3,10)]

gym_strength_means = [random.uniform(3,4)]*4
gym_strength_std_devs = [random.uniform(0.8,1.2)]*4
gym_strength_ranges = [(1,5)]*4

gym_balance_means = [random.uniform(3,4)]*4
gym_balance_std_devs = [random.uniform(0.8,1.2)]*4
gym_balance_ranges = [(1,5)]*4


tk_overall_means = [random.uniform(3,4)]*2 + [random.uniform(7, 9)]
tk_overall_std_devs = [random.uniform(0.8,1.2)]*3
tk_overall_ranges = [(1,5)]*2 + [(3,10)]

tk_parts_means = ([random.uniform(4,5)] + [random.uniform(3,4)] * 2) * 5
tk_parts_std_devs = [random.uniform(0.8,1.2)]*15
tk_parts_ranges = ([(1,6)]*2 + [(1,5)]) * 5


written_means = [random.uniform(100,110)] + [random.uniform(74,76)] * 2
written_std_devs = [random.uniform(2,3)] + [random.uniform(1,2)]*2
written_ranges = [(0,150)] + [(0,100)] * 2




prev_means = [70]*15
prev_std_devs = [13 ]*15
prev_ranges = [(0,100)]*15


means = dan_jbg_means + dan_ztq_means + dan_gj_means + dan_tj_means + dan_sz_means \
+ gym_exercise_means + gym_run_means+gym_art_means+gym_strength_means+gym_balance_means\
+ tk_overall_means +tk_parts_means+written_means+prev_means

std_devs = dan_jbg_std_devs + dan_ztq_std_devs + dan_gj_std_devs + dan_tj_std_devs + dan_sz_std_devs \
+ gym_exercise_std_devs + gym_run_std_devs+gym_art_std_devs+gym_strength_std_devs+gym_balance_std_devs\
+ tk_overall_std_devs +tk_parts_std_devs+written_std_devs+prev_std_devs

ranges = dan_jbg_ranges + dan_ztq_ranges + dan_gj_ranges + dan_tj_ranges + dan_sz_ranges \
+ gym_exercise_ranges + gym_run_ranges+gym_art_ranges+gym_strength_ranges+gym_balance_ranges\
+ tk_overall_ranges +tk_parts_ranges+written_ranges+prev_ranges

length = len(means)

print(len(means))
print(len(std_devs))
print(len(ranges ))




# Define the correlation coefficient
correlation = 0.4

# Create the covariance matrix for 5 lists
cov_matrix = np.full((length, length), correlation * std_devs[0] * std_devs[1])
for i in range(length):
    for j in range(length):
        cov_matrix[i, j] = correlation * std_devs[i] * std_devs[j] if i != j else std_devs[i]**2

# Generate 100 samples from a multivariate normal distribution
samples = np.random.multivariate_normal(means, cov_matrix, 100)

# Split the samples into five lists and clip them to the specified ranges
lists = [np.clip(np.round(samples[:, i]), ranges[i][0], ranges[i][1]) for i in range(length)]




dan_jbg_score = np.zeros((1,100))
dan_ztq_score = np.zeros((1,100))
dan_gj_score = np.zeros((1,100))
dan_tj_score = np.zeros((1,100))
dan_sz_score = np.zeros((1,100))
dan_total_score = np.zeros((1,100))





for l in lists[0:23]:
  dan_jbg_score += l
for l in lists[23:29]:
  dan_ztq_score += l
for l in lists[29:35]:
  dan_gj_score += l
for l in lists[35:40]:
  dan_tj_score+= l
for l in lists[40:43]:
  dan_sz_score += l
for l in lists[0:43]:
  dan_total_score += l


gym_exercise_score = np.zeros((1,100))
gym_run_score = np.zeros((1,100))
gym_art_score = np.zeros((1,100))
gym_strength_score = np.zeros((1,100))
gym_balance_score = np.zeros((1,100))
gym_total_score = np.zeros((1,100))


for l in lists[43:50]:
   gym_exercise_score += l
for l in lists[50:52]:
   gym_run_score += l
for l in lists[52:55]:
   gym_art_score += l
for l in lists[55:59]:
   gym_strength_score += l
for l in lists[59:63]:
   gym_balance_score += l
for l in lists[43:63]:
   gym_total_score += l

tk_overall_score = np.zeros((1,100))
tk_neck_score = np.zeros((1,100))
tk_arm_score = np.zeros((1,100))
tk_waist_score = np.zeros((1,100))
tk_leg_score = np.zeros((1,100))
tk_foot_score = np.zeros((1,100))
tk_total_score = np.zeros((1,100))

for l in lists[63:66]:
   tk_overall_score += l
for l in lists[66:69]:
   tk_neck_score += l  
for l in lists[69:72]:
   tk_arm_score += l  
for l in lists[72:75]:
   tk_waist_score += l 
for l in lists[75:78]:
   tk_leg_score += l 
for l in lists[78:81]:
   tk_foot_score += l 
for l in lists[63:81]:
   tk_total_score += l 

written_total_score = np.zeros((1,100))

for l in lists[81:84]:
   tk_total_score += l 


history_list = lists[84:99]

history_total_matrix = np.zeros_like(history_list)
history_total_matrix[0] = history_list[0]
for i in range(1, np.shape(history_list)[0]):
    history_total_matrix[i] = np.sum(history_list[:i+1], axis=0)


history_rank_matrix = np.zeros_like(history_list)
for i in range(0, np.shape(history_list)[0]):
    history_rank_matrix[i] = history_total_matrix[i].argsort()[::-1].argsort() + 1


semester_score = history_total_matrix[-1] + dan_total_score*5
semester_rank = 100 - semester_score.argsort()[::-1].argsort() 

name_list = ['白宇轩', '卞博文', '曹天宇', '常俊杰', '程昊天', '程子涵', '陈思羽', '陈思源', '陈子涵', '崔宇轩', '戴宇翔', '戴宇轩', '邓思羽', '邓子轩', '丁浩天', '翟子涵', '董子睿', '冯子睿', '付子豪', '高俊凯', '高思羽', '郭浩宇', '郭子豪', '韩思源', '何昊然', '贺俊杰', '何天宇', '贺宇翔', '华俊凯', '黄子涵', '胡俊凯', '胡天睿', '蒋睿博', '江宇轩', '蒋子睿', '蒋子轩', '柯昊然', '柯杰尹', '孔维熙', '黎博文', '李浩然', '李俊杰', '李俊熙', '林子轩', '李瑞泽', '刘瑞杰', '刘宇轩', '龙俊杰', '罗宇航', '马子睿', '潘子涵', '彭子航', '钱子豪', '史俊豪', '宋文杰', '孙思远', '孙子涵', '谭博文', '唐子豪', '唐子轩', '王俊豪', '王宇轩', '王子睿', '韦俊豪', '文子睿', '吴昊天', '吴子睿', '萧俊豪', '夏扬', '谢俊杰', '谢子涵', '熊昊天', '许晨曦', '许晨曦', '薛宇航', '徐浩轩', '许睿杰', '徐思远', '许子睿', '杨博文', '杨晨轩', '杨宇轩', '袁俊杰', '袁宇翔', '张俊豪', '张文博', '张宇航', '赵嘉文', '赵云飞', '赵子涵', '赵子睿', '郑浩天', '郑子睿', '周俊豪', '周宇浩', '周宇翔', '周子轩', '朱博文', '朱浩宇', '朱俊熙']
person_num = np.linspace(353, 452, 100, dtype=int)


numbers = list(range(0, 100))
random.shuffle(numbers)
gym_index = numbers[:40]
gym_index.sort()
bal_index = numbers[40:]
bal_index.sort()


gym_class_sequence = [None] * 100
numbers = list(range(0, 40))
random.shuffle(numbers)
for i in range(len(gym_index)):
  gym_class_sequence[gym_index[i]] = numbers[i] /10 + 1
numbers = list(range(40, 100))
random.shuffle(numbers)
for i in range(len(bal_index)):
  gym_class_sequence[bal_index[i]] = numbers[i] /10 + 1


gym_exam_group = [None] * 100
gym_exam_pos = [None] * 100
numbers = list(range(0, 40))
random.shuffle(numbers)
for i in range(len(gym_index)):
  gym_exam_group[gym_index[i]] = numbers[i] /10 + 1
  gym_exam_pos[gym_index[i]] = numbers[i] %10 + 1
numbers = list(range(40, 100))
random.shuffle(numbers)
for i in range(len(bal_index)):
  gym_exam_group[bal_index[i]] = numbers[i] /10 + 1
  gym_exam_pos[bal_index[i]] = numbers[i] %10 + 1


bal_class_sequence = [None] * 100
numbers = list(range(0, 60))
random.shuffle(numbers)
for i in range(len(bal_index)):
  bal_class_sequence[bal_index[i]] = numbers[i]  /10 + 1
numbers = list(range(60, 100))
random.shuffle(numbers)
for i in range(len(gym_index)):
  bal_class_sequence[gym_index[i]] = numbers[i] /10 + 1


bal_exam_group = [None] * 100
bal_exam_pos = [None] * 100
numbers = list(range(0, 60))
random.shuffle(numbers)
for i in range(len(bal_index)):
  bal_exam_group[bal_index[i]] = numbers[i] /10 + 1
  bal_exam_pos[bal_index[i]] = numbers[i] %10 + 1
numbers = list(range(60, 100))
random.shuffle(numbers)
for i in range(len(gym_index)):
  bal_exam_group[gym_index[i]] = numbers[i] /10 + 1
  bal_exam_pos[gym_index[i]] =  numbers[i] %10 + 1


numbers = list(range(0, 100))
random.shuffle(numbers)
tk_exam_group = [None] * 100
tk_exam_pos = [None] * 100
for i in range(len(numbers)):
  tk_exam_group[i] = numbers[i] /15 + 1
  tk_exam_pos[i] =  numbers[i] %15 + 1

tk_class_sequence = list(range(0, 100))
random.shuffle(tk_class_sequence)
for i in range(len(tk_class_sequence)):
  tk_class_sequence[i] = tk_class_sequence[i] / 20+ 1


student_info_intro = ["姓名","专业","学号",  "芭蕾班号", "体操班号", "挠痒班号", "芭蕾考组","", "体操考组","", "挠痒考组"]

major_list = [None] * 100
for i in range(len(gym_class_sequence)):
  if i in gym_index:
     major_list[i] = '体操'
  else:
     major_list[i] = '芭蕾'

student_info = np.vstack(( person_num,bal_class_sequence, 
                          gym_class_sequence, tk_class_sequence,
                          bal_exam_group, bal_exam_pos,
                          gym_exam_group, gym_exam_pos,
                          tk_exam_group, tk_exam_pos ))
student_info = student_info.T
student_info = student_info.astype(int)


with open('student_info.csv', 'a', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(student_info_intro)
   for i in range(len(name_list)):
     writer.writerow([name_list[i]] + [major_list[i]]+  list(student_info[i]))




# dan_csv_intro = ["姓名","学号","班号","排名","总分","基本功","主题曲","个人剧目","团队剧目","素质测评","舞步圆场","四拍舞步","地面练习提、沉、转腰","含、展、横移","踢、撩腿","大环动","压、扳腿","大踢腿（一）","扶把练习","蹲","小踢、弹腿","端、掖腿蹲","吸伸腿","大踢腿（二）","中间练习盘手","弯腰","平转","小跳（一）","小跳（二）","速度反应","蒙古族舞","唯吾尔族舞","傣族舞","技术动作","情感传达","肢体能量","乐感节奏","创新动作","舞台表现","舞蹈技巧","艺术表现","编排创意","舞台表现","音乐理解","服装","技术动作1","技术动作2","技术动作3","团队协作","情感传达","姿态体态","表现力","即兴编舞"]
# dan_csv_total = [0,0, 0,0, 150,50,20,30,30,20, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,8,4,2,2,3,1,6,6,5,5,5,4,5,5,5,9,6,8,6,6]
# dan_csv_average = [0,0,0,0 ] + [sum(dan_jbg_means) + sum(dan_ztq_means) + sum(dan_gj_means) + sum(dan_tj_means) + sum(dan_sz_means)] +  [sum(dan_jbg_means)] + [sum(dan_ztq_means)]  + [sum(dan_gj_means)] + [sum(dan_tj_means)] + [sum(dan_sz_means)] +  dan_jbg_means + dan_ztq_means + dan_gj_means + dan_tj_means + dan_sz_means
# dan_csv_average = np.array(dan_csv_average, dtype  = np.float64)


# dan_ranking = 100 - dan_total_score.argsort()[::-1].argsort() 


# ballet_score = np.vstack(( person_num, bal_class_sequence, dan_ranking, dan_total_score, dan_jbg_score, dan_ztq_score, dan_gj_score ,dan_tj_score, dan_sz_score, lists))
# ballet_score = ballet_score.T
# ballet_score = ballet_score.astype(int)


# with open('ballet_score.csv', 'a', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerow(dan_csv_intro)
#    writer.writerow(dan_csv_total)
#    writer.writerow(dan_csv_average)
#    for i in range(len(ballet_score)):
#      writer.writerow([name_list[i]] + list(ballet_score[i]))




# rank = np.vstack(( person_num,  history_list, history_total_matrix, dan_total_score, semester_score, history_rank_matrix , ranking, semester_rank))
# rank = rank.T
# rank = rank.astype(int)


# csv_ranking_intro = ["姓名", "学号"] + ["第"+str(i + 1)+"周得分" for i in range(15)]  + ["第"+str(i + 1)+"总得分" for i in range(15)] + ["期末考试成绩", "学期成绩"]+ ["第"+str(i + 1)+"周排名" for i in range(15)] + ["期末考试排名", "学期排名"]

# with open('ranking.csv', 'a', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerow(csv_ranking_intro)
#    for i in range(len(rank)):
      
#       writer.writerow([name_list[i]] + list(rank[i]))






