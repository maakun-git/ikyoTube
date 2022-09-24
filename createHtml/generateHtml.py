from http.cookiejar import MozillaCookieJar
import pandas as pd
import re
import os
import sys
import mojimoji

# 同じフォルダにあるExcelファイルのパスを作成
srcExcelFile = os.path.join(os.path.dirname(__file__), 'youtube_list.xlsx')
isExist = os.path.isfile(srcExcelFile)
if(False == isExist):
	sys.exit()

# Excelファイルを開く
dfUntil2018 = pd.read_excel(srcExcelFile, sheet_name='until2018AllList',  index_col=0, header=0)
df2019 = pd.read_excel(srcExcelFile, sheet_name='2019alllist', index_col=0, header=0)
df2020 = pd.read_excel(srcExcelFile, sheet_name='2020AllList', index_col=0, header=0)
df2021 = pd.read_excel(srcExcelFile, sheet_name='2021AllList', index_col=0, header=0)
df2022 = pd.read_excel(srcExcelFile, sheet_name='2022AllList', index_col=0, header=0)
dfsubchannel = pd.read_excel(srcExcelFile, sheet_name='subchannel', index_col=0, header=0)
dfmusicChannel = pd.read_excel(srcExcelFile, sheet_name='musicChannel', index_col=0, header=0)
old2ndChannel = pd.read_excel(srcExcelFile, sheet_name='old2ndChannel', index_col=0, header=0)
dfLover = pd.read_excel(srcExcelFile, sheet_name='Lover', index_col=0, header=0)
dfPastel = pd.read_excel(srcExcelFile, sheet_name='pastel', index_col=0, header=0)
df = pd.concat([dfPastel, dfLover, old2ndChannel, dfsubchannel, dfmusicChannel, dfUntil2018, df2019, df2020, df2021, df2022]) 
#print(df2021)
#print(df2022)
#print(df)

# htmlファイルへの出力
with open("index.html", "w", encoding="utf-8-sig") as fw:
	# ヘッダ部
	fw.write('<html lang="ja">\n')
	header = '''<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

	<title>アイドル教室 Youtube検索 2022.09.17</title>
	<!--<head>内-->
	<script src="https://code.jquery.com/jquery-3.3.1.min.js"
			integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
			crossorigin="anonymous"></script>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/css/theme.bootstrap_4.min.css" />
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/css/theme.blue.min.css">
	<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/js/jquery.tablesorter.min.js"></script>
	<!-- 追加機能(widgets)を使用する場合は次も追加する -->
	<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/js/jquery.tablesorter.widgets.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/js/parsers/parser-duration.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/js/widgets/widget-sort2Hash.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/js/widgets/widget-cssStickyHeaders.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/js/widgets/widget-columnSelector.min.js"></script>
	<script type="text/javascript">
		$(document).ready(function () {
			$("#myTable").tablesorter({
                //スタイルを設定(theme.blue.css)
                theme: 'blue',
                widthFixed: true,
                //zebra:1行ごとに色を変える
                //columns:選択した列の色を変える
                //filter:列にフィルタ機能を追加する
                //resizable:列のリサイズをする
                //stickyHeaders:スクロールの際にヘッダを固定する
                widgets: ['zebra', 'columns', 'filter', 'resizable', 'stickyHeaders'],
                //フィルタのリセットボタンを追加する場合に設定する。
                widgetOptions: {
                    filter_reset: 'button.reset-filter-button',
                    resizable: true,
                }
            });
		}
		);
	</script>
	<style>
	body {
		text-size-adjust: 100%;
		-webkit-text-size-adjust: 100%;
	}
	.description{
		cursor: pointer;
		overflow:hidden;
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 1;
	}
	</style>
</head>'''

	fw.write(header)
	
	# body タイトル等
	fw.write('\n<body>\n<br>\n')
	fw.write('<h1 align="center">アイドル教室 Youtube 検索</h1>\n')

	fw.write('<h2 align="center">チャンネル リンク：\n')
	fw.write('<a target="_blank" href="https://www.youtube.com/c/pops262">メインch</a> \n')
	fw.write('<a target="_blank" href="https://www.youtube.com/channel/UCJlJX_UnSegdENRPWtOFXLw">2nd</a> \n')
	fw.write('<a target="_blank" href="https://www.youtube.com/channel/UCkSDNSZxvWCMC_mRhT2z-sQ">music</a> \n')
	fw.write('<a target="_blank" href="https://www.youtube.com/channel/UCFCwO4zhO84JDUvs8QUDM-w">旧2nd</a> \n')
	fw.write('<a target="_blank" href="https://www.youtube.com/channel/UCVWpv6M08brx2VfEZC7uOsg">ラバー</a> \n')
	fw.write('<a target="_blank" href="https://www.youtube.com/channel/UCPKzKqWwVWR_ph46bV3ayTA">パスガレ</a> \n')
	fw.write('</h2>\n')

	fw.write("※2022年9月24日までの分をリストに反映済み。<br><br>")
	fw.write("※セットリスト抜けてる公演も多数あります。<br>")
	fw.write("※全チャンネルの動画を横断的に検索できます。<br>")
	fw.write("※検索のコツ①…動画タイトルのみで検索する場合は「タイトル」の列で検索。タイムテーブルも含めて検索する場合は「タイムテーブル」の列で検索。<br>")
	fw.write("※検索のコツ②…曲名の一部分でOKです「SKY OF DREAMS」なら「SKY」で検索できます。<br>")
	fw.write("※検索のコツ③…メンバー名で検索する際は、漢字やひらがなや愛称など色々ためしてみてください。<br>")
	fw.write("　　　　　　　　(「真野」「まの」「福沢」「あすみ」「ありす」「ありにゃん」など)<br>")
	

	# table
	fw.write('<table id="myTable" class="tablesorter tablesorter-blue">\n')

	# 項目名
	fw.write("\t<thead><tr>\n")
	fw.write('\t\t<th>通し#</th>\n')
	fw.write('\t\t<th>チャンネル</th>\n')
	fw.write('\t\t<th>日付</th>\n')
	# 分類分けの抜けが多くて現状はあんまり使えないので非表示にする
	# fw.write('\t\t<th>分類1</th>\n')
	# fw.write('\t\t<th>分類2</th>\n')
	fw.write('\t\t<th>タイトル</th>\n')
	fw.write('\t\t<th width="40%">タイムテーブル(楽曲)</th>\n')
	fw.write("\t</tr></thead>\n")

	# 表の中身の書き出し
	fw.write("\t<tbody>\n")

	for i in reversed(range(len(df))):
		fw.write("\t<tr>\n")

		fw.write('\t\t<td>{0}</td>\n'.format(i+1))
		fw.write('\t\t<td>{0}</td>\n'.format(df.iloc[i, 0]))

		# 投稿日
		val = df.iloc[i, 1]
		publishday = pd.Timestamp(val).strftime("%Y/%m/%d")
		fw.write('\t\t<td>{0}</td>\n'.format(publishday))

		# 分類1,分類2
		category1 = df.iloc[i, 4]
		if False == isinstance(category1, str): 
			category1 = " "
		category2 = df.iloc[i, 5]
		if False == isinstance(category2, str): 
			category2 = " "

		# 分類分けの抜けが多くて現状はあんまり使えないので非表示にする
		#fw.write('\t\t<td>{0}</td>\n'.format(category1))
		#fw.write('\t\t<td>{0}</td>\n'.format(category2))

		# タイトル URL
		url = df.iloc[i, 3]
		title = df.iloc[i, 6]
		fw.write('\t\t<td><a href="{0}" target="_blank">{1}</a></td>\n'.format(url,title))

		# タイムテーブル
		strTimetable = df.iloc[i, 7]
		if isinstance(strTimetable, str): 
			trCss = '<style>#showtext' + str(i) + '{display:none;} #showtext' + str(i) + ':checked ~ .description{display:block;}</style>\r\n'
			collapsibleStart = '<input type="checkbox" id="showtext' + str(i) + '"><label for="showtext' + str(i) + '" class="description"><font color=red>クリック(タップ)でセットリストを開く</font><br>\r\n'
			strTimetable = re.sub("(\r\n)|(\n)", "</br>", strTimetable) # 改行コードはタグに置換
			collapsibleEnd = '</lavel>\r\n'
			strTimetable = trCss + collapsibleStart + strTimetable + collapsibleEnd
		else :
			strTimetable = " "

		# 全角→半角
		# https://sy-base.com/myrobotics/python/mojimoji/
		strTimetable = mojimoji.zen_to_han(strTimetable, kana = False)
		fw.write('\t\t<td>{0}<br>{1}</td>\n'.format(title,strTimetable))
		fw.write("\t</tr>\n")

	fw.write("</tbody></table>\n")
	fw.write("</html>\n")
