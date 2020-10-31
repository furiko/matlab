import datetime

today = datetime.date.today()


def main():
	s = 0
	while s != "1" and s != "2":
		print("どっちの表を生成しますか？(1:検討会, 2:松尾川島研GMTG):", end="")
		s = input()
	if s == "1":
		print("何周分生成しますか？:", end="")
		s = int(input())
		print("開始日はいつですか？(ex:2020/04/01):", end="")
		start_day = input()
		print(start_day)
		kentokai(week_num=s, start_day=start_day)
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
	

def kentokai(week_num=3, start_day="2020/04/01"):
	# 将来的には検討会のスタートの日付入れて生成したい
	# コード生成する日から次の検討会まで何日か
	# base_day = today + datetime.timedelta(days=6)
	base_day = datetime.datetime.strptime(start_day, "%Y/%m/%d")
	# print(base_day)
	for i in range(0, week_num):
		after_weeks = datetime.timedelta(weeks=i*3) #何週間後か
		date = base_day + after_weeks #差分を足す
		date2 = base_day + after_weeks + datetime.timedelta(weeks=1) #何週間後か
		date3 = base_day + after_weeks + datetime.timedelta(weeks=2) #何週間後か
		date_string = date.strftime("%-m/%d") # 行頭の日付用
		date2_string = date2.strftime("%-m/%d")
		date3_string = date3.strftime("%-m/%d")
		file_date_string = date.strftime("%Y%m%d") #ファイル内の日付用
		file_date2_string = date2.strftime("%Y%m%d") #ファイル内の日付用
		file_date3_string = date3.strftime("%Y%m%d") #ファイル内の日付用
		print("||" + date_string + " ||[[attachment:dodare-ken-"+file_date_string+".pptx|資料]]  ||[[attachment:asada-ken-"+file_date_string+".pptx|資料]]  || || ||[[attachment:kawaguti-ken-"+file_date_string+".pptx|資料]] || || || || || || || ||[[attachment:yamasita-ken-"+file_date_string+".pptx|資料]] || || ||[[attachment:takeya-ken-"+file_date_string+".pptx|資料]] ||[[attachment:hirano-ken-"+file_date_string+".pptx|資料]] || || ||[[attachment:okuda-ken-"+file_date_string+".pptx|資料]] || || ||")
		print("||" + date2_string + " || || || ||[[attachment:miwa-ken-"+file_date2_string+".pptx|資料]] || ||[[attachment:kobayasi-ken-"+file_date2_string+".pptx|資料]] || || || ||[[attachment:nakayama-ken-"+file_date2_string+".pptx|資料]] ||[[attachment:y-asai-ken-"+file_date2_string+".pptx|資料]] || || || || || || ||[[attachment:funahashi-ken-"+file_date2_string+".pptx|資料]] ||[[attachment:t-watanabe-ken-"+file_date2_string+".pptx|資料]] || || ||[[attachment:k-yamamoto-ken-"+file_date2_string+".pptx|資料]] ||")
		print("||" + date3_string + " || || ||[[attachment:fukushima-ken-"+file_date3_string+".pptx|資料]] || || || ||[[attachment:takaoka-ken-"+file_date3_string+".pptx|資料]] ||[[attachment:takeishi-ken-"+file_date3_string+".pptx|資料]] ||[[attachment:miyamoto-ken-"+file_date3_string+".pptx|資料]] || || ||[[attachment:kuroda-ken-"+file_date3_string+".pptx|資料]] || ||[[attachment:r-kato-ken-"+file_date3_string+".pptx|資料]] ||[[attachment:saito-ken-"+file_date3_string+".pptx|資料]] || || || || || ||[[attachment:nakahara-ken-"+file_date3_string+".pptx|資料]] || ||")


if __name__ == '__main__':
	main()
