import csv
import pandas as pd
# import xlsx

# sample_data = pd.read_excel('power bi data.xlsx', sheet_name='academic wayback_clusters')
# print('sample_data:', sample_data.shape)


# irec
irec = pd.read_csv('irec_LDA_1.csv')
new_irec_clusterid = []
irec_tps = []
irec_tp = []
irec_clusterid = irec['cluster_id'].tolist()
for i in irec_clusterid:
    new_id = int('1'+str(i))
    new_irec_clusterid.append(new_id)
irec_year = irec['year'].tolist()
print('irec_year;', irec_year)
irec_quarter = irec['quarter'].tolist()
for y, q in zip(irec_year, irec_quarter):
    irec_tps.append(int(str(y)+str(q)))
    irec_tp.append((str(y)+' - Q'+str(q)))

# walmid
walmid = pd.read_csv('walmid_LDA_1.csv')
new_walmid_clusterid = []
walmid_tps = []
walmid_tp = []
walmid_clusterid = walmid['cluster_id'].tolist()
for i in walmid_clusterid:
    new_id = int('2'+str(i))
    new_walmid_clusterid.append(new_id)
walmid_year = walmid['year'].tolist()
walmid_quarter = walmid['quarter'].tolist()
for y, q in zip(walmid_year, walmid_quarter):
    walmid_tps.append(int(str(y)+str(q)))
    walmid_tp.append((str(y)+' - Q'+str(q)))

# scotnor
scortor = pd.read_csv('scotnor_LDA_1.csv')
new_scortor_clusterid = []
scortor_tps = []
scortor_tp = []
scortor_clusterid = scortor['cluster_id'].tolist()
for i in scortor_clusterid:
    new_id = int('3'+str(i))
    new_scortor_clusterid.append(new_id)
scortor_year = scortor['year'].tolist()
scortor_quarter = scortor['quarter'].tolist()
for y, q in zip(scortor_year, scortor_quarter):
    scortor_tps.append(int(str(y)+str(q)))
    scortor_tp.append((str(y)+' - Q'+str(q)))

# sthest
sthest = pd.read_csv('sthest_LDA_1.csv')
new_sthest_clusterid = []
sthest_tps = []
sthest_tp = []
sthest_clusterid = sthest['cluster_id'].tolist()
for i in sthest_clusterid:
    new_id = int('4'+str(i))
    new_sthest_clusterid.append(new_id)
sthest_year = sthest['year'].tolist()
sthest_quarter = sthest['quarter'].tolist()
for y, q in zip(sthest_year, sthest_quarter):
    sthest_tps.append(int(str(y)+str(q)))
    sthest_tp.append((str(y)+' - Q'+str(q)))


# london
london = pd.read_csv('london_LDA_1.csv')
new_london_clusterid = []
london_tps = []
london_tp = []
london_clusterid = london['cluster_id'].tolist()
for i in london_clusterid:
    new_id = int('5'+str(i))
    new_london_clusterid.append(new_id)
london_year = london['year'].tolist()
london_quarter = london['quarter'].tolist()
for y, q in zip(london_year, london_quarter):
    london_tps.append(int(str(y)+str(q)))
    london_tp.append((str(y)+' - Q'+str(q)))

# uk
uk = pd.read_csv('uk_LDA_1.csv')
new_uk_clusterid = []
uk_tps = []
uk_tp = []
uk_clusterid = uk['cluster_id'].tolist()
for i in uk_clusterid:
    new_id = int('6'+str(i))
    new_uk_clusterid.append(new_id)
uk_year = uk['year'].tolist()
uk_quarter = uk['quarter'].tolist()
for y, q in zip(uk_year, uk_quarter):
    uk_tps.append(int(str(y)+str(q)))
    uk_tp.append((str(y)+' - Q'+str(q)))

# ire
ire = pd.read_csv('ire_LDA_1.csv')
new_ire_clusterid = []
ire_tps = []
ire_tp = []
ire_clusterid = ire['cluster_id'].tolist()
for i in ire_clusterid:
    new_id = int('7'+str(i))
    new_ire_clusterid.append(new_id)
ire_year = ire['year'].tolist()
ire_quarter = ire['quarter'].tolist()
for y, q in zip(ire_year, ire_quarter):
    ire_tps.append(int(str(y)+str(q)))
    ire_tp.append((str(y)+' - Q'+str(q)))



cluster_id = []
locale = []
year = []
quarter = []
cluster_no_companies = []
cluster_keyword = []
cluster_analysis_result = []
time_points = []
time_point = []

cluster_id = new_irec_clusterid + new_walmid_clusterid + new_scortor_clusterid+ new_sthest_clusterid + new_london_clusterid + new_uk_clusterid + new_ire_clusterid
locale = irec['locale'].tolist() + walmid['locale'].tolist() + scortor['locale'].tolist() + sthest['locale'].tolist() + london['locale'].tolist() + uk['locale'].tolist() + ire['locale'].tolist()
year = irec['year'].tolist() + walmid['year'].tolist() + scortor['year'].tolist() + sthest['year'].tolist() + london['year'].tolist() + uk['year'].tolist() + ire['year'].tolist()
quarter = irec['quarter'].tolist() + walmid['quarter'].tolist() + scortor['quarter'].tolist() + sthest['quarter'].tolist() + london['quarter'].tolist() + uk['quarter'].tolist() + ire['quarter'].tolist()
cluster_no_companies = irec['cluster_no_companies'].tolist() + walmid['cluster_no_companies'].tolist() + scortor['cluster_no_companies'].tolist() + sthest['cluster_no_companies'].tolist() + london['cluster_no_companies'].tolist() + uk['cluster_no_companies'].tolist() + ire['cluster_no_companies'].tolist()
cluster_keyword = irec['cluster_keyword'].tolist() + walmid['cluster_keyword'].tolist() + scortor['cluster_keyword'].tolist() + sthest['cluster_keyword'].tolist() + london['cluster_keyword'].tolist() + uk['cluster_keyword'].tolist() + ire['cluster_keyword'].tolist()
cluster_analysis_result = irec['cluster_analysis_result'].tolist() + walmid['cluster_analysis_result'].tolist() + scortor['cluster_analysis_result'].tolist() + sthest['cluster_analysis_result'].tolist() + london['cluster_analysis_result'].tolist() + uk['cluster_analysis_result'].tolist() + ire['cluster_analysis_result'].tolist()
time_points = irec_tps + walmid_tps + scortor_tps + sthest_tps + london_tps + uk_tps + ire_tps
time_point = irec_tp + walmid_tp + scortor_tp + sthest_tp + london_tp + uk_tp + ire_tp

print('cluster_id:', len(cluster_id))
print('locale:', len(locale))
print('year:', len(year))
print('quarter:', len(quarter))
print('cluster_no_companies:', len(cluster_no_companies))
print('cluster_keyword:', len(cluster_keyword))
print('cluster_analysis_result:', len(cluster_analysis_result))
print('time_points:', len(time_points))
print('time_point:', len(time_point))

powerbi_pd = pd.DataFrame()
powerbi_pd['cluster_id'] = cluster_id
powerbi_pd['locale'] = locale
powerbi_pd['year'] = year
powerbi_pd['quarter'] = quarter
powerbi_pd['cluster_no_companies'] = cluster_no_companies
powerbi_pd['cluster_keyword'] = cluster_keyword
powerbi_pd['cluster_analysis_result'] = cluster_analysis_result
powerbi_pd['time_points'] = time_points
powerbi_pd['time_point'] = time_point

fame = pd.read_excel('power bi data.xlsx', sheet_name='academic wayback_companies')

writer = pd.ExcelWriter('powerbidata.xlsx', engine='xlsxwriter')

powerbi_pd.to_excel(writer, sheet_name='academic wayback_clusters', index=False)
fame.to_excel(writer, sheet_name='academic wayback_companies', index=False)
writer.save()









