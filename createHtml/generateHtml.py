import pandas as pd
import re
import os
import sys

# 同じフォルダにあるExcelファイルのパスを作成
srcExcelFile = os.path.join(os.path.dirname(__file__), 'youtube_list.xlsx')
isExist = os.path.isfile(srcExcelFile)
if(False == isExist):
	sys.exit()

# Excelファイルを開く
df = pd.read_excel(srcExcelFile, sheet_name='2021AllList', index_col=0, header=0)
# print(df)

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
</head>'''

	# 
	fw.write(header)
	fw.write('\n<body>\n')
	fw.write('<h1 align="center">アイドル教室 Youtube 検索</h1>\n')

	# table
	fw.write('<table id="myTable" class="tablesorter tablesorter-blue">\n')

	# 項目名
	fw.write("\t<thead><tr>\n")
	fw.write('\t\t<th>日付</th>\n')
	fw.write('\t\t<th>分類1</th>\n')
	fw.write('\t\t<th>分類2</th>\n')
	fw.write('\t\t<th>タイトル</th>\n')
	fw.write('\t\t<th>タイムテーブル(楽曲)</th>\n')
	fw.write("\t</tr></thead>\n")

	# 表の中身の書き出し
	fw.write("\t<tbody>\n")

	for i in range(len(df)):
		fw.write("\t<tr>\n")

		# 投稿日
		val = df.iloc[i, 0]
		publishday = pd.Timestamp(val).strftime("%Y/%m/%d")
		fw.write('\t\t<td>{0}</td>\n'.format(publishday))

		# 分類1,分類2
		fw.write('\t\t<td>{0}</td>\n'.format(df.iloc[i, 3]))
		fw.write('\t\t<td>{0}</td>\n'.format(df.iloc[i, 4]))

		# タイトル URL
		url = df.iloc[i, 2]
		title = df.iloc[i, 5]
		fw.write('\t\t<td><a href={0}>{1}</a></td>\n'.format(url,title))

		# タイムテーブル
		strTimetable = df.iloc[i, 6]
		if isinstance(strTimetable, str): 
			strTimetable = re.sub("(\r\n)|(\n)", "<br>", strTimetable) # 改行コードはタグに置換
		else :
			strTimetable = " "
		
			fw.write('\t\t<td>{0}</td>\n'.format(strTimetable))
		fw.write("\t</tr>\n")

	fw.write("</tbody></table>\n")
	fw.write("</html>\n")
