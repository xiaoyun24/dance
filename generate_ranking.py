written_csv_intro = ["姓名","专业","学号",
                 "总分",
                 "挠痒理论","芭蕾理论","体操理论","挠痒排名","专业排名"] 
written_csv_total = [0,0, 0,0,0, 
                 250,
                 150,100,100]
written_csv_average = [0,0,0,0,0 ] + [sum(written_means) ] + written_means
written_csv_average = np.array(written_csv_average, dtype  = np.float64)

written_tickle_ranking = 100 - lists[85].argsort()[::-1].argsort()

written_major_ranking =  np.min(lists[86:88], axis=0)


written_score = np.vstack(( person_num, written_tickle_ranking, written_major_ranking, written_total_score,  lists[85:88]))
written_score = written_score.T
written_score = written_score.astype(int)


with open('written_score.csv', 'a', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(written_csv_intro)
   writer.writerow(written_csv_total)
   writer.writerow(written_csv_average)
   for i in range(len(written_score)):
     writer.writerow([name_list[i]] + [major_list[i]] + list(written_score[i]))