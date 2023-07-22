# 毕业论文数据处理代码
# 前置准备
import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")

# 补6位函数
def zerofill6(numvar):
    strvar = str(numvar)
    return strvar.zfill(6)

# 用于生成年化收益率和方差，在基金特征表出用于groupby apply
def gen_ret(df):
    df = df.dropna(axis=0, how='any')
    if df.shape[0] == 0:
        return np.nan
    startnav = df.iloc[0, 2]
    endnav = df.iloc[df.shape[0] - 1, 2]
    startdate = df.iloc[0, 0]
    enddate = df.iloc[df.shape[0]-1, 0]
    diff = enddate - startdate
    diffint = pd.Timedelta(diff).days
    ret_annual = (endnav - startnav) / startnav * 365 / diffint
    # df_ret = pd.DataFrame({'ret_annual': pd.Series(ret_annual)})
    return ret_annual


def gen_var(df):
    df = df.dropna(axis=0, how='any')
    if df.shape[0] == 0:
        return np.nan
    variance = np.var(df.iloc[:, 2])
    # df_ret = pd.DataFrame({'ret_annual': pd.Series(ret_annual)})
    return variance

#%% 本部分将ESG的表汇总，并且并上机构持股比例，输出df_company包含了公司esg评分（及细分）、券商等类别机构投资者的
# 持股比例信息，后续会再生成其他维度的分组组别的持股比例信息

# 首先提取ESG各维度数据并合成一个上市公司-日期的面板数据表
os.chdir(r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data')
dict_esg = pd.read_excel('ESG_Wind.xlsx', sheet_name=None)
# 对每个sheet表分别生成stack数据
df_esg_stacked = {}
for key in dict_esg:
    df_raw = dict_esg[key]
    df_raw = df_raw.drop(labels='名称', axis=1)
    ids_raw = df_raw.id
    ids_new = list()
    for id in ids_raw: ids_new.append(str(id[:6]))
    df_raw.id = ids_new
    df = df_raw.melt(id_vars='id', var_name='date', value_name=key)
    df_esg_stacked[key] = df
# 把每个stack之后的sheet横向合并拼成一张表
df_esg_score = df_esg_stacked['esg_all']
for key in df_esg_stacked:
    if key == 'esg_all':
        continue
    df_esg_score = pd.merge(df_esg_score, df_esg_stacked[key], on=['id', 'date'], how='inner')
df_esg_score = df_esg_score.sort_values(by=['id', 'date'], ascending=True)
# 将机构投资者持股比例合并到esg表当中
os.chdir(r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data')
df_insinv = pd.read_excel('机构投资者持股比例.xlsx', sheet_name=0)
# 重新搞一下id，先定义一个补6位的函数，然后apply上去
df_insinv['id'] = df_insinv['id'].apply(zerofill6)
# 同理把date列转成日期
df_insinv['date'] = df_insinv['date'].apply(pd.to_datetime)
df_insinv = df_insinv.sort_values(by=['id', 'date'], ascending=True)
#合并出df_company
df_company = pd.merge(df_esg_score, df_insinv, on=['id', 'date'], how='inner')
# 改个名，便于后续合并
df_company.rename(columns={'id': 'companyid'}, inplace=True)

#%% 基金标签表whole period汇总 输出是df_allfeature_wholeperiod，包含了基金ID和ret，var，equity_prop，asset四个维度的按照全周期的分组组别
# 这个块是先生成ret和var，并和fund成立时间、投资风格等特征进行合并

# 先合并出NAV的全部数据，这部分已经存成了csv文件，直接读取即可，不需要再跑
os.chdir(r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data\Fund_NAV')
# filename_list = os.listdir()
# i = 0
# for filename in filename_list:
#     df_temp = pd.read_excel(filename)
#     df_temp = df_temp.iloc[2:, :]
#     if i == 0:
#         df_res = df_temp
#     else:
#         df_res = pd.concat([df_res, df_temp], ignore_index=1)
#     i += 1
# df_res.to_csv(r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data\Fund_NAV\汇总后的大表\NAV_all.csv')

# 提取一下每个季度的
filepath = r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data\Fund_NAV\汇总后的大表\NAV_all.csv'
df_res = pd.read_csv(filepath, index_col=None)
df_res = df_res.iloc[:, 1:]
df_res['TradingDate'] = pd.to_datetime(df_res['TradingDate'])
# 注意，此处的Symbol列是int格式，但现在改一遍实在是太慢，因此计划等group完之后再提取
# 生成季度'2018Q1'
df_res['quarter'] = df_res['TradingDate'].dt.to_period('Q')
#生成年化收益率
df_res = df_res.sort_values(by=['Symbol', 'TradingDate'], ascending=True)
# print(np.where(df_res.isnull() == True)) 这一步发现NAV列是有缺失值的
# 决定先不管季度的收益率，只做总的收益率、波动率，也就是只groupby Symbol
# MasterFundCode是基金主代码，Fundid留给基金ID
df_res_group_ret = df_res.groupby(df_res['Symbol'], as_index=False).apply(gen_ret)
df_res_group_var = df_res.groupby(df_res['Symbol'], as_index=False).apply(gen_var)
df_res_group_ret.columns=['MasterFundCode', 'ret_annual']
df_res_group_var.columns=['MasterFundCode', 'var']
df_ret_var = pd.merge(df_res_group_ret, df_res_group_var, on='MasterFundCode', how='inner')
df_ret_var['MasterFundCode'] = df_ret_var['MasterFundCode'].apply(zerofill6)


# 然后把CSMAR基金大表里的风格、基金类型数据并上，这样就有了一个基金特征的表，未来和机构投资者明细数据判定分类机构投资者的持股比例
# df_fund_feature这个表就是除了资产/股权占比之外的基金所有的特征都放在一起
os.chdir(r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data')
df_allfund = pd.read_excel('CSMAR全部基金ID对照表.xlsx')
df_allfund = df_allfund.iloc[2:, :]
del df_allfund['FullName']
#直接并
df_fund_feature = pd.merge(df_allfund, df_ret_var, on='MasterFundCode', how='inner')
# 然后需要按照ret和var分别生成一列，分10组，从小到大分别是1-10
quantiles_sep = np.arange(0.1, 1, 0.1)
# 先搞ret，取出9个分位数
quantiles_ret = []
for sep in quantiles_sep: quantiles_ret.append(np.nanquantile(df_fund_feature['ret_annual'], sep, axis=0))
# 然后高出新的一列
df_fund_feature['group_by_ret_wholeperiod'] = np.nan

for groupid in range(len(quantiles_ret) + 1):
    if groupid == 0:
        q_ret = quantiles_ret[0]
        df_fund_feature.iloc[np.array(df_fund_feature['ret_annual']<q_ret), 7] = groupid + 1
    elif groupid == 9:
        q_ret = quantiles_ret[8]
        df_fund_feature.iloc[np.array(df_fund_feature['ret_annual'] > q_ret), 7] = groupid + 1
    else:
        q_ret_current = quantiles_ret[groupid]
        q_ret_previous = quantiles_ret[groupid - 1]
        df_fund_feature.iloc[np.array((df_fund_feature['ret_annual'] > q_ret_previous) & (df_fund_feature['ret_annual'] < q_ret_current)), 7] = groupid + 1
# check一下，发现数据范围是对的，下一步复用到var上
# df_test = df_fund_feature.groupby('group_by_ret').apply(lambda x: [max(x.ret_annual), min(x.ret_annual)])

quantiles_var = []
for sep in quantiles_sep: quantiles_var.append(np.nanquantile(df_fund_feature['var'], sep, axis=0))
df_fund_feature['group_by_var_wholeperiod'] = np.nan
for groupid in range(len(quantiles_var) + 1):
    if groupid == 0:
        q_var = quantiles_var[0]
        df_fund_feature.iloc[np.array(df_fund_feature['var']<q_var), 8] = groupid + 1
    elif groupid == 9:
        q_var = quantiles_var[8]
        df_fund_feature.iloc[np.array(df_fund_feature['var'] > q_var), 8] = groupid + 1
    else:
        q_var_current = quantiles_var[groupid]
        q_var_previous = quantiles_var[groupid - 1]
        df_fund_feature.iloc[np.array((df_fund_feature['var'] > q_var_previous) & (df_fund_feature['var'] < q_var_current)), 8] = groupid + 1
# 至此基金特征按照整体的ret和var已经给每个基金打了标签，各自是一列

#%% 这个块是再并上基金的股权占比、总资产，从而得到df_fund_allfeature_wholeperiod

# 现在从整体的角度处理一下股票投资占比和总资产规模，都按照平均值对基金进行分组
os.chdir(r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data')
df_fund_asset = pd.read_excel('基金股权投资和总资产规模.xlsx')
df_fund_asset = df_fund_asset.iloc[2:, :]
df_fund_asset['EndDate'] = pd.to_datetime(df_fund_asset['EndDate'])
# 删一波乱七八糟的报告期，只保留季报数据
df_fund_asset = df_fund_asset[(df_fund_asset['ReportTypeID'] != '5') & (df_fund_asset['ReportTypeID'] != '6') & (df_fund_asset['ReportTypeID'] != '7')]
del df_fund_asset['ReportTypeID']
del df_fund_asset['CrossName']  # crosscode里1代表账面金额，2代表占基金总资产比例
df_fund_total_asset = df_fund_asset[df_fund_asset['CrossCode'] == '1']
df_fund_equity_prop = df_fund_asset[df_fund_asset['CrossCode'] != '1']
# 至此，生成出来了2个子表，下一步分别清理一下之后合并回来，就能得到每个基金、每个时点的股权占比和总资产规模
del df_fund_equity_prop['CrossCode']
del df_fund_equity_prop['TotalAsset']
del df_fund_total_asset['CrossCode']
del df_fund_total_asset['Equity']
# 合并回来，先删掉total_asset表中的MasterFundCode以免重复
del df_fund_total_asset['MasterFundCode']
df_fund_asset_merged = pd.merge(df_fund_equity_prop, df_fund_total_asset, on=['FundID', 'EndDate'], how='left')
df_fund_asset_merged.rename(columns={'Equity': 'Equity_prop'}, inplace=True)
# 下一步就按照平均值做分组，给基金打上标签，然后和feature的表合并，就得到一张按照whole_period对基金打上分组的总表
# 首先生成平均值的表
df_fund_asset_merged_groupedmean = df_fund_asset_merged.groupby(['FundID', 'MasterFundCode'], as_index=False).agg('mean')
del df_fund_asset_merged_groupedmean['EndDate']
df_fund_asset_merged_groupedmean.rename(columns={'Equity_prop': 'Equity_prop_mean',
                                                 'TotalAsset': 'TotalAsset_mean'}, inplace=True)
# 这一步做分组标签
quantiles_equity = []
quantiles_asset = []
for sep in quantiles_sep: quantiles_equity.append(np.nanquantile(df_fund_asset_merged_groupedmean['Equity_prop_mean'], sep, axis=0))
for sep in quantiles_sep: quantiles_asset.append(np.nanquantile(df_fund_asset_merged_groupedmean['TotalAsset_mean'], sep, axis=0))
# 然后高出新的列
df_fund_asset_merged_groupedmean['group_by_equityprop_wholeperiod'] = np.nan
df_fund_asset_merged_groupedmean['group_by_totalasset_wholeperiod'] = np.nan

for groupid in range(len(quantiles_equity) + 1):
    if groupid == 0:
        q_equity = quantiles_equity[0]
        q_asset = quantiles_asset[0]
        df_fund_asset_merged_groupedmean.iloc[np.array(df_fund_asset_merged_groupedmean['Equity_prop_mean']<q_equity), 4] = groupid + 1
        df_fund_asset_merged_groupedmean.iloc[np.array(df_fund_asset_merged_groupedmean['TotalAsset_mean']<q_asset), 5] = groupid + 1
    elif groupid == 9:
        q_equity = quantiles_equity[8]
        q_asset = quantiles_asset[8]
        df_fund_asset_merged_groupedmean.iloc[np.array(df_fund_asset_merged_groupedmean['Equity_prop_mean'] > q_equity), 4] = groupid + 1
        df_fund_asset_merged_groupedmean.iloc[np.array(df_fund_asset_merged_groupedmean['TotalAsset_mean'] > q_asset), 5] = groupid + 1
    else:
        q_equity_current = quantiles_equity[groupid]
        q_equity_previous = quantiles_equity[groupid - 1]
        q_asset_current = quantiles_asset[groupid]
        q_asset_previous = quantiles_asset[groupid - 1]
        df_fund_asset_merged_groupedmean.iloc[np.array((df_fund_asset_merged_groupedmean['Equity_prop_mean'] > q_equity_previous) & (df_fund_asset_merged_groupedmean['Equity_prop_mean'] < q_equity_current)), 4] = groupid + 1
        df_fund_asset_merged_groupedmean.iloc[np.array((df_fund_asset_merged_groupedmean['TotalAsset_mean'] > q_asset_previous) & (df_fund_asset_merged_groupedmean['TotalAsset_mean'] < q_asset_current)), 5] = groupid + 1
# 和feature的表合并，就得到一张按照whole_period对基金打上分组的总表
df_fund_allfeature_wholeperiod = pd.merge(df_fund_feature, df_fund_asset_merged_groupedmean, on=['FundID', 'MasterFundCode'], how='inner')
# 把其中的Category、InvestmentStyle这两列用文字表述的分组改成数字
category_unique = list(set(df_fund_allfeature_wholeperiod['Category'])) #具体的编号对照就在这个序列表里
for i in range(len(category_unique)):
    cat = category_unique[i]
    groupid = i + 1
    df_fund_allfeature_wholeperiod.iloc[df_fund_allfeature_wholeperiod['Category'] == cat, 3] = groupid

style_unique = list(set(df_fund_allfeature_wholeperiod['InvestmentStyle'])) #具体的编号对照就在这个序列表里
for i in range(len(style_unique)):
    style = style_unique[i]
    groupid = i + 1
    df_fund_allfeature_wholeperiod.iloc[df_fund_allfeature_wholeperiod['InvestmentStyle'] == style, 4] = groupid
# 删一下重复行，没有什么意义
df_fund_allfeature_wholeperiod.drop_duplicates('FundID', inplace=True)

# 至此,df_fund_allfeature_wholeperiod就是用于对照的全部基金分组表
#%% 此部分要将每个时点，每个公司被机构投资者的持股比例进行不同维度的分组加总，得出公司-时间-group_维度一_1组持股比例 etc

# 合一下持股明细,这部分已经存成了csv文件，直接读取即可，不需要再跑
os.chdir(r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data\机构持股明细')
# filename_list = os.listdir()
# i = 0
# for filename in filename_list:
#     df_temp = pd.read_excel(filename)
#     df_temp = df_temp.iloc[3:, :]
#     if i == 0:
#         df_res = df_temp
#     else:
#         df_res = pd.concat([df_res, df_temp], ignore_index=1)
#     i += 1
# df_res.to_csv(r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data\Fund_NAV\汇总后的大表\INI_datail_all.csv')
filepath = r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data\Fund_NAV\汇总后的大表\INI_datail_all.csv'
df_res = pd.read_csv(filepath, index_col=None)
df_res = df_res.iloc[:, 1:]
df_res['EndDate'] = pd.to_datetime(df_res['EndDate'])
# 注意，此处的Symbol列(上市公司代码)是int格式，但现在改一遍实在是太慢，最后再提取
# 现在合并上持股信息和基金的特征信息，这样就可以有一个后面汇总了分组信息的表
df_res.rename(columns={'ShareHolderID': 'FundID'}, inplace=True)
df_res['FundID'] = df_res['FundID'].astype(str)
df_insinv_detail_withgroup = pd.merge(df_res, df_fund_allfeature_wholeperiod, on='FundID', how='left')
# 注意，这样之后有些保险、券商持股的无法被计入，也即没有分组信息，经下面检验，基金持股的有3574067行，都是有分组信息的
# d = df_insinv_detail_withgroup.dropna()
# a = set(d['Systematics'])
# c = df_insinv_detail_withgroup[df_insinv_detail_withgroup['Systematics'] == '基金持股']
# e = c.dropna()
# C和e的行数有差别，说明有些基金持有公司股票，但是基金的特征表没有收入

# 现在按照组别生成持股比例合计
groups = ['Category', 'InvestmentStyle', 'group_by_ret_wholeperiod',
          'group_by_var_wholeperiod', 'group_by_equityprop_wholeperiod',
          'group_by_totalasset_wholeperiod']

# 这个函数是用来生成合计持股比例的
def gen_sumprop_bygroup(group_name):
    temp = df_insinv_detail_withgroup.groupby(['Symbol', 'EndDate', group_name], as_index=False).apply(lambda x: np.nansum(x['HoldProportion']))
    temp.rename(columns={None: 'prop'}, inplace=True)
    temp_unstack = temp.pivot(index=['Symbol', 'EndDate'], columns=group_name, values='prop')
    temp_unstack = temp_unstack.reset_index()
    new_cols = []
    for name in list(temp_unstack.columns):
        if (isinstance(name, int)) | (isinstance(name, float)):
            name = int(name)
            name = 'groupby_' + group_name + '_' + str(name)
        new_cols.append(name)
    temp_unstack.columns = new_cols
    return temp_unstack

# 以下遍历需要分组的变量名
i = 0
for groupi in groups:
    df_temp = gen_sumprop_bygroup(groupi)
    if i == 0:
        df_grouped_sum_prop = df_temp
    else:
        df_grouped_sum_prop = pd.merge(df_grouped_sum_prop, df_temp, on=['Symbol', 'EndDate'], how='outer')
    i += 1

# 然后把symbol给改一下
df_grouped_sum_prop['Symbol'] = df_grouped_sum_prop['Symbol'].apply(zerofill6)
#再改个名
df_grouped_sum_prop.rename(columns={'Symbol': 'companyid',
                                    'EndDate': 'date'}, inplace=True)

#%% df_grouped_sum_prop汇总了每个公司每个时点的各分组机构投资者持股比例信息，df_company汇总了
# 公司ESG得分、总的和按照机构种类划分的机构持股比例信息，将二者合并起来就是for stata的信息
df_final_res_wholeperiod = pd.merge(df_company, df_grouped_sum_prop,
                                    on=['companyid', 'date'],
                                    how='inner')
filepath = r'C:\Users\Lu Zhenjiang\Desktop\毕业论文\data\df_final_res_wholeperiod.xlsx'
df_final_res_wholeperiod.to_excel(filepath)

