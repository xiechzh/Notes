import pandas as pd
import numpy as np


#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#**************************************************************************************************************
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

#****************************************************************
#****************************************************************
# 数据库

# 一对一关系
table1: 人
table2: 身份证
一人一张身份证

# 一对多关系 ***
table1: 班级 -- parent
table2: 学生 -- child 含 table1 主键
一个班级有多个学生

# 多对多关系
talbe1: 课程
table2: 学生

#****************************************************************
#****************************************************************

# pandas sql查询
sql = "select * from telecaster.recording limit 1"
# 这里的sql不能包含ilike + % 查询，会报错，不知道为什么
df = pd.read_sql_query(sql,con=database.engine)

# create DataFrame
data = {
    'recording': ['Nice Speech Coach', 'Somersault', 'Lit Match'],
    'release': ['Longshot (Original Soundtrack)', 'Traveling Light', 'For All Mankind: Season 1 (Apple TV+ Original Series Soundtrack)'],
    'isrc': ['CAN111700236', 'USIR20500339', 'USJPL1900313']
}
df = pd.DataFrame(data)
print(">>>>>>>>>CREATE DATAFRAME<<<<<<<<<")
print(df)

# read file
filename = "test_duplicate.xlsx"
df = pd.read_excel(filename)
# change type when read file
df_raw = pd.read_excel(filename, dtype={"Certification Date": str})

# delete columns
df = df.drop(["Release ID.1"], axis=1)  # method 1
delete_col_df = df.drop(columns=["Release Cline"])  # method 2

# delete rows
delete_row_df = df.drop([1, 2])  # delete first and second rows
delete_row_df = df.drop(index=[1, 2])  # method 2

# delete a row
# delete rows: 'Recording Title'=='Nice Speech Coach'
delete_row_df = df.drop(index=(df.loc[(df['Recording Title']=='Nice Speech Coach')].index))

# remove rows 重复的行
rows = df.duplicated(["Recording ID"])
print("ROWS", rows)

# remove rows specidal columns duplicate
remove_duplicate_df = df.drop_duplicates(subset=['Recording ID','Release ID'], keep='first')  # 去除了 列'Recording ID' 和 列'Release ID' 重复的，保留第一次出现的行

# remove duplicate
df = df.drop_duplicates()  # 要赋值给 df

# rename columns 重命名
df = df.rename(columns={
    "title": "title_raw",
    "id": "award_nomination_id"
})
df = df.rename(
        columns={col: col.replace("_raw", "") for col in df.columns}
)

# write to excel
df.to_excel("test.xlsx")

# ==== 写入已存在文件 ====
with pd.ExcelWriter(f'report_award_{filename}.xlsx') as writer:
    df_award.to_excel(writer, sheet_name=filename)

# values in row or column to list
df.values.tolist()

# ==== 查看df信息 ====
# display all columns or rows
pd.set_option('display.max_columns', None)
df.info()

# chech type
df["name"].dtypes

# ==== 选择 ====
# clip 切片 : choose only column No.3-end 选取第三列到后面
df.iloc[:,3:]  # select by position
df.iloc[[1,3,5], 1:3] 
df.loc[:, ['a', 'b']]  # select by label
df.ix[:3, ['a', 'b']]  # mixed selection 【可能已经不能用了】
df["a"]  # equal df.a 
df[df.a < 8]  # boolean indexing 是或者否来筛选

# ==== 赋值 ====
df.iloc[2,2] = 111
df.loc['row_1', 'a']  = 222
df[df.a > 4] = 0  # 会把 a > 4 的行里所有的值 赋值 0
df.a[df.a > 4] = 0  # 只把 列a 里a>4 的行 赋值 0
df.b[df.a > 4] = 0  # 只把 列a 中 a>4 的行 的 列b 里的值 赋值 0
# 加 一列
df['f'] = np.nan

# ==== 合并 ====
# 合并行
df = pd.concat((df_one, df_two), axis=0, join='outer')
# 合并列 ？？不太确定
df = pd.concat((df_one, df_two), axis=1, join='outer')

# ==== 数据处理 ====
# 一行变多行
pd.explode

# ==== 时间 ====
x = pd.to_datetime(['2020/6/8 14.05'], format='%Y/%d/%m $H.%M')
# 在read_csv 或者 read_excel 的时候，将 cell 转换成timestamp 时间格式
d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
df = pd.read_csv('filename', parse_dates=['Date'], date_parser=d_parser)
# change column certification_date format from timestamps to int year
df_raw["certification_date"] = [int(year[:4]) for year in df_raw["certification_date"]]





# pandas error
error = 'A value is trying to be set on a copy of a slice from a DataFrame'
why = 'When setting values in a pandas object, care must be taken to avoid what is called chained indexing.'