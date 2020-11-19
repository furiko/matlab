import datetime

today = datetime.date.today()


def main():
	s = 0
	while s != "1" and s != "2":
		print("どっちの表を生成しますか？(1:検討会, 2:松尾川島研GMTG):", end="")
		s = input()
	if s == "1":
		print("何周分生成しますか？:", end="")
		s = input()
		if s == "":
			exit(0)
		s = int(s)
		print("開始日はいつですか？(ex:2020/04/01):", end="")
		start_day = input()
		print("start_day: ", start_day)
		skip_day = "1990/01/01"
		skip_dict = {}
		i = 0
		print("スキップする日付をまとめたファイルがあればパスを入れてください：", end="")
		skip_file = input()
		if skip_file != "":
			skip_dict = read_file(skip_file)
		while skip_day != "" or skip_day == "n":
			if i == 0:
				print("開催しない日はありますか？", end="")
			else:
				print("他に開催しない日はありますか？", end="")
			skip_day = input()
			if skip_day == "":
				break
			skip_dict[skip_day] = True
			i+=1
		if start_day == "":
			res = kentokai(week_num=s, skip_dict=skip_dict)
		else:
			res = kentokai(week_num=s, start_day=start_day, skip_dict=skip_dict)
		for x in res:
			print(x)

		write_to_file(res)
	elif s == "2":
		matsuo()


def matsuo():
	print("🚧===松尾川島研GMTG用表生成システムは現在{0}です===🚧".format("under construction"))
	exit(0)
	for i in range(1, 50):
		after_weeks = datetime.timedelta(weeks=i) #何週間後か
		date = today + after_weeks #差分を足す

		date_string = date.strftime("%-m/%d") # 行頭の日付用
		file_date_string = date.strftime("%Y%m%d") #ファイル内の日付用

		print("||" + date_string + " (火) ||[[attachment:asada-meet-"+file_date_string+".pptx|浅田]] ||[[attachment:dodare-meet-"+file_date_string+".pptx|堂垂]] ||[[attachment:fukushima-meet-"+file_date_string+".pptx|福島]] ||[[attachment:miwa-meet-"+file_date_string+".pptx|三輪]] ||[[attachment:nakayama-meet-"+file_date_string+".pptx|中山]] ||[[attachment:miyamoto-meet-"+file_date_string+".pptx|宮本]] ||[[attachment:kato-meet-"+file_date_string+".pptx|加藤]] ||[[attachment:saito-meet-"+file_date_string+".pptx|齋藤]] ||[[attachment:takeya-meet-"+file_date_string+".pptx|竹谷]] ||[[attachment:hirano-meet-"+file_date_string+".pptx|平野]] ||[[attachment:funahashi-meet-"+file_date_string+".pptx|舟橋]] ||[[attachment:t-watanabe-meet-"+file_date_string+".pptx|渡邉]] ||")
	

def kentokai(week_num=3, start_day="2020/04/01", skip_dict={}):
	# 将来的には検討会のスタートの日付入れて生成したい
	# コード生成する日から次の検討会まで何日か
	# base_day = today + datetime.timedelta(days=6)
	base_day = datetime.datetime.strptime(start_day, "%Y/%m/%d")
	# print(base_day)
	date3 = base_day - datetime.timedelta(weeks=1)
	for k, v in skip_dict.items():
		print("k: ", k, "v: ", v)
	res = []
	for i in range(0, week_num):
		# after_weeks = datetime.timedelta(weeks=i*3) #何週間後か
		# date = check_valid_day(base_day + after_weeks, skip_dict[0]) #差分を足す
		# date2 = base_day + after_weeks + datetime.timedelta(weeks=1) #何週間後か
		# date3 = base_day + after_weeks + datetime.timedelta(weeks=2) #何週間後か
		date = get_next_held_day(date3, skip_dict)
		date2 = get_next_held_day(date, skip_dict)
		date3 = get_next_held_day(date2, skip_dict)
		# debug_date(date, date2, date3)
		date_string = date.strftime("%-m/%d") # 行頭の日付用
		date2_string = date2.strftime("%-m/%d")
		date3_string = date3.strftime("%-m/%d")
		file_date_string = date.strftime("%Y%m%d") #ファイル内の日付用
		file_date2_string = date2.strftime("%Y%m%d") #ファイル内の日付用
		file_date3_string = date3.strftime("%Y%m%d") #ファイル内の日付用
		# print("||" + date_string + " ||[[attachment:dodare-ken-"+file_date_string+".pptx|資料]]  ||[[attachment:asada-ken-"+file_date_string+".pptx|資料]]  || || ||[[attachment:kawaguti-ken-"+file_date_string+".pptx|資料]] || || || || || || || ||[[attachment:yamasita-ken-"+file_date_string+".pptx|資料]] || || ||[[attachment:takeya-ken-"+file_date_string+".pptx|資料]] ||[[attachment:hirano-ken-"+file_date_string+".pptx|資料]] || || ||[[attachment:okuda-ken-"+file_date_string+".pptx|資料]] || || ||")
		# print("||" + date2_string + " || || || ||[[attachment:miwa-ken-"+file_date2_string+".pptx|資料]] || ||[[attachment:kobayasi-ken-"+file_date2_string+".pptx|資料]] || || || ||[[attachment:nakayama-ken-"+file_date2_string+".pptx|資料]] ||[[attachment:y-asai-ken-"+file_date2_string+".pptx|資料]] || || || || || || ||[[attachment:funahashi-ken-"+file_date2_string+".pptx|資料]] ||[[attachment:t-watanabe-ken-"+file_date2_string+".pptx|資料]] || || ||[[attachment:k-yamamoto-ken-"+file_date2_string+".pptx|資料]] ||")
		# print("||" + date3_string + " || || ||[[attachment:fukushima-ken-"+file_date3_string+".pptx|資料]] || || || ||[[attachment:takaoka-ken-"+file_date3_string+".pptx|資料]] ||[[attachment:takeishi-ken-"+file_date3_string+".pptx|資料]] ||[[attachment:miyamoto-ken-"+file_date3_string+".pptx|資料]] || || ||[[attachment:kuroda-ken-"+file_date3_string+".pptx|資料]] || ||[[attachment:r-kato-ken-"+file_date3_string+".pptx|資料]] ||[[attachment:saito-ken-"+file_date3_string+".pptx|資料]] || || || || || ||[[attachment:nakahara-ken-"+file_date3_string+".pptx|資料]] || ||")

		res.append("||" + date_string + " ||[[attachment:dodare-ken-"+file_date_string+".pptx|資料]]  ||[[attachment:asada-ken-"+file_date_string+".pptx|資料]]  || || ||[[attachment:kawaguti-ken-"+file_date_string+".pptx|資料]] || || || || || || || ||[[attachment:yamasita-ken-"+file_date_string+".pptx|資料]] || || ||[[attachment:takeya-ken-"+file_date_string+".pptx|資料]] ||[[attachment:hirano-ken-"+file_date_string+".pptx|資料]] || || ||[[attachment:okuda-ken-"+file_date_string+".pptx|資料]] || || ||")
		res.append("||" + date2_string + " || || || ||[[attachment:miwa-ken-"+file_date2_string+".pptx|資料]] || ||[[attachment:kobayasi-ken-"+file_date2_string+".pptx|資料]] || || || ||[[attachment:nakayama-ken-"+file_date2_string+".pptx|資料]] ||[[attachment:y-asai-ken-"+file_date2_string+".pptx|資料]] || || || || || || ||[[attachment:funahashi-ken-"+file_date2_string+".pptx|資料]] ||[[attachment:t-watanabe-ken-"+file_date2_string+".pptx|資料]] || || ||[[attachment:k-yamamoto-ken-"+file_date2_string+".pptx|資料]] ||")
		res.append("||" + date3_string + " || || ||[[attachment:fukushima-ken-"+file_date3_string+".pptx|資料]] || || || ||[[attachment:takaoka-ken-"+file_date3_string+".pptx|資料]] ||[[attachment:takeishi-ken-"+file_date3_string+".pptx|資料]] ||[[attachment:miyamoto-ken-"+file_date3_string+".pptx|資料]] || || ||[[attachment:kuroda-ken-"+file_date3_string+".pptx|資料]] || ||[[attachment:r-kato-ken-"+file_date3_string+".pptx|資料]] ||[[attachment:saito-ken-"+file_date3_string+".pptx|資料]] || || || || || ||[[attachment:nakahara-ken-"+file_date3_string+".pptx|資料]] || ||")

	return res


# TODO:
# スキップするとは？→順番は進めず、日付だけ進める
#

def check_valid_day(day, skip_day):
	if day == skip_day:
		return day + datetime.timedelta(weeks=1)
	return day


def get_next_held_day(day, skip_dict):
	next_day = day + datetime.timedelta(weeks=1)
	if skip_dict.get(next_day.strftime("%Y/%m/%d")):
		return next_day + datetime.timedelta(weeks=1)
	return next_day


def debug_date(day1, day2, day3):
	print("day1:", day1, " day2:", day2, " day3:", day3)


def write_to_file(lines):
	with open("./table.txt", "w") as f:
		for line in lines:
			f.write(line+"\n")


def read_file(path):
	with open(path, "r") as f:
		lines = f.readlines()
	res = {}
	for line in lines:
		res[line.strip("\n")] = True
	return res

if __name__ == '__main__':
	main()
