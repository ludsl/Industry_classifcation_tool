
import pandas as pd


# irec
irec = pd.read_csv('irec_LDA_1.csv')
new_irec_clusterid = []
irec_rid = []
irec_weight = []
irec_clusterid = irec['cluster_id'].tolist()
irec_ridweight = irec['COMPANIES'].tolist()
for idx, ridweight in zip(irec_clusterid, irec_ridweight):
    ridweight = ridweight.strip().split(', ')
    new_id = int('1'+str(idx))
    for i in range(0,len(ridweight)-1,2):
        rid = ridweight[i]
        weight = ridweight[i+1]
        new_irec_clusterid.append(new_id)
        irec_rid.append(rid)
        irec_weight.append(weight)

# walmid
walmid = pd.read_csv('walmid_LDA_1.csv')
new_walmid_clusterid = []
walmid_rid = []
walmid_weight = []
walmid_clusterid = walmid['cluster_id'].tolist()
walmid_ridweight = walmid['COMPANIES'].tolist()
for idx, ridweight in zip(walmid_clusterid, walmid_ridweight):
    ridweight = ridweight.strip().split(', ')
    new_id = int('2'+str(idx))
    for i in range(0,len(ridweight)-1,2):
        rid = ridweight[i]
        weight = ridweight[i+1]
        new_walmid_clusterid.append(new_id)
        walmid_rid.append(rid)
        walmid_weight.append(weight)

# scotnor
scortor = pd.read_csv('scotnor_LDA_1.csv')
new_scortor_clusterid = []
scortor_rid = []
scortor_weight = []
scortor_clusterid = scortor['cluster_id'].tolist()
scortor_ridweight = scortor['COMPANIES'].tolist()
for idx, ridweight in zip(scortor_clusterid, scortor_ridweight):
    ridweight = ridweight.strip().split(', ')
    new_id = int('3'+str(idx))
    for i in range(0,len(ridweight)-1,2):
        rid = ridweight[i]
        weight = ridweight[i+1]
        new_scortor_clusterid.append(new_id)
        scortor_rid.append(rid)
        scortor_weight.append(weight)

# sthest
sthest = pd.read_csv('sthest_LDA_1.csv')
new_sthest_clusterid = []
sthest_rid = []
sthest_weight = []
sthest_clusterid = sthest['cluster_id'].tolist()
sthest_ridweight = sthest['COMPANIES'].tolist()
for idx, ridweight in zip(sthest_clusterid, sthest_ridweight):
    ridweight = ridweight.strip().split(', ')
    new_id = int('4'+str(idx))
    for i in range(0,len(ridweight)-1,2):
        rid = ridweight[i]
        weight = ridweight[i+1]
        new_sthest_clusterid.append(new_id)
        sthest_rid.append(rid)
        sthest_weight.append(weight)


# london
london = pd.read_csv('london_LDA_1.csv')
new_london_clusterid = []
london_rid = []
london_weight = []
london_clusterid = london['cluster_id'].tolist()
london_ridweight = london['COMPANIES'].tolist()
for idx, ridweight in zip(london_clusterid, london_ridweight):
    ridweight = ridweight.strip().split(', ')
    new_id = int('5'+str(idx))
    for i in range(0,len(ridweight)-1,2):
        rid = ridweight[i]
        weight = ridweight[i+1]
        new_london_clusterid.append(new_id)
        london_rid.append(rid)
        london_weight.append(weight)

# uk
uk = pd.read_csv('uk_LDA_1.csv')
new_uk_clusterid = []
uk_rid = []
uk_weight = []
uk_clusterid = uk['cluster_id'].tolist()
uk_ridweight = uk['COMPANIES'].tolist()
for idx, ridweight in zip(uk_clusterid, uk_ridweight):
    ridweight = ridweight.strip().split(', ')
    new_id = int('6'+str(idx))
    for i in range(0,len(ridweight)-1,2):
        rid = ridweight[i]
        weight = ridweight[i+1]
        new_uk_clusterid.append(new_id)
        uk_rid.append(rid)
        uk_weight.append(weight)

# ire
ire = pd.read_csv('ire_LDA_1.csv')
new_ire_clusterid = []
ire_rid = []
ire_weight = []
ire_clusterid = ire['cluster_id'].tolist()
ire_ridweight = ire['COMPANIES'].tolist()
for idx, ridweight in zip(ire_clusterid, ire_ridweight):
    ridweight = ridweight.strip().split(', ')
    new_id = int('7'+str(idx))
    for i in range(0,len(ridweight)-1,2):
        rid = ridweight[i]
        weight = ridweight[i+1]
        new_ire_clusterid.append(new_id)
        ire_rid.append(rid)
        ire_weight.append(weight)


cluster_id = new_irec_clusterid + new_walmid_clusterid + new_scortor_clusterid + new_sthest_clusterid + new_london_clusterid + new_uk_clusterid + new_ire_clusterid
rid = irec_rid + walmid_rid + scortor_rid + sthest_rid + london_rid + uk_rid + ire_rid
weight = irec_weight + walmid_weight + scortor_weight + sthest_weight + london_weight + uk_weight + ire_weight

powerbi_pd = pd.DataFrame()
powerbi_pd['cluster_id'] = cluster_id
powerbi_pd['rid'] = rid
powerbi_pd['weight'] = weight
powerbi_pd.to_csv('powerbi1.csv', index=False, header=True)

f = open('powerbi.txt', 'w')
f.write('cluster_id'+' '+'rid'+' '+'weight'+'\n')
for c, r, w in zip(cluster_id, rid, weight):
    f.write(str(c)+' '+str(r)+' '+str(w)+'\n')
f.close()








