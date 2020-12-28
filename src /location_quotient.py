
import pandas as pd
import spacy
import numpy as np
import math

nlp = spacy.load('en_core_web_lg')

# irec
# learn embeddings of keywords 
irec = pd.read_csv('irec_LDA_1.csv')
irecid_keywords_dict = {}
for cid, keywords in zip(irec['cluster_id'], irec['cluster_keyword'].tolist()):
    if cid not in irecid_keywords_dict.keys():
        cid = int('1'+str(cid))
        irecid_keywords_dict[cid] = keywords
irec_id_vec = {}
for cid, cluster in irecid_keywords_dict.items():
    clusters_vecs = []
    cluster = ' '.join(cluster.split(', '))
    for word in nlp(cluster):
        clusters_vecs.append(word.vector)
        # print('a:', word, type(str(word)))
        # if str(word) == 'medicine':
        #     print(word, word.vector[:10])
    cluster_vec = np.mean(np.array(clusters_vecs), axis=0)
    irec_id_vec[cid] = cluster_vec
# count the number of companies 
irec_rids_dict = {}
ireccid_rids_dict = {}
for cid, rids in zip(irec['cluster_id'], irec['COMPANIES']):
    cid = int('1'+str(cid))
    if cid not in ireccid_rids_dict.keys():
        ireccid_rids_dict[cid] = []
    rids = rids.strip().split(', ')
    for i, rid in enumerate(rids):
        if i%2 == 0:
            if rid not in irec_rids_dict.keys():
                irec_rids_dict[rid] = ''
            if rid not in ireccid_rids_dict[cid]:
                ireccid_rids_dict[cid].append(rid)
ireccid_rids_sorted = {k: v for k, v in sorted(ireccid_rids_dict.items(), key=lambda item: item[0])}
ireccid_ridnum_dict = {}
for cid, rids in ireccid_rids_sorted.items():
    ireccid_ridnum_dict[cid] = len(rids)
# compute regional quotient 
print('Number of rid in irec:', len(irec_rids_dict))
ireccid_rq_dict = {}
cid_rq_dict = {}
for cid, ridnum in ireccid_ridnum_dict.items():
    ireccid_rq_dict[cid] = ridnum/len(irec_rids_dict)
    cid_rq_dict[cid] = ridnum/len(irec_rids_dict)


# walmid
# learn embeddings of keywords 
walmid = pd.read_csv('walmid_LDA_1.csv')
walmidid_keywords_dict = {}
for cid, keywords in zip(walmid['cluster_id'], walmid['cluster_keyword'].tolist()):
    cid = int('2'+str(cid))
    if cid not in walmidid_keywords_dict.keys():
        walmidid_keywords_dict[cid] = keywords
walmid_id_vec = {}
for cid, cluster in walmidid_keywords_dict.items():
    clusters_vecs = []
    cluster = ' '.join(cluster.split(', '))
    for word in nlp(cluster):
        clusters_vecs.append(word.vector)
    cluster_vec = np.mean(np.array(clusters_vecs), axis=0)
    walmid_id_vec[cid] = cluster_vec
# count the number of companies 
walmid_rids_dict = {}
walmidcid_rids_dict = {}
for cid, rids in zip(walmid['cluster_id'], walmid['COMPANIES']):
    cid = int('2'+str(cid))
    if cid not in walmidcid_rids_dict.keys():
        walmidcid_rids_dict[cid] = []
    rids = rids.strip().split(', ')
    for i, rid in enumerate(rids):
        if i%2 == 0:
            if rid not in walmid_rids_dict.keys():
                walmid_rids_dict[rid] = ''
            if rid not in walmidcid_rids_dict[cid]:
                walmidcid_rids_dict[cid].append(rid)
walmidcid_rids_sorted = {k: v for k, v in sorted(walmidcid_rids_dict.items(), key=lambda item: item[0])}
walmidcid_ridnum_dict = {}
for cid, rids in walmidcid_rids_sorted.items():
    walmidcid_ridnum_dict[cid] = len(rids)
# compute regional quotient 
print('Number of rid in walmid:', len(walmid_rids_dict))
walmidcid_rq_dict = {}
for cid, ridnum in walmidcid_ridnum_dict.items():
    walmidcid_rq_dict[cid] = ridnum/len(walmid_rids_dict)
    cid_rq_dict[cid] = ridnum/len(walmid_rids_dict)


# scotnor
# learn embeddings of keywords 
scotnor = pd.read_csv('scotnor_LDA_1.csv')
scotnorid_keywords_dict = {}
for cid, keywords in zip(scotnor['cluster_id'], scotnor['cluster_keyword'].tolist()):
    cid = int('3'+str(cid))
    if cid not in scotnorid_keywords_dict.keys():
        scotnorid_keywords_dict[cid] = keywords
scotnor_id_vec = {}
for cid, cluster in scotnorid_keywords_dict.items():
    clusters_vecs = []
    cluster = ' '.join(cluster.split(', '))
    for word in nlp(cluster):
        clusters_vecs.append(word.vector)
    cluster_vec = np.mean(np.array(clusters_vecs), axis=0)
    scotnor_id_vec[cid] = cluster_vec
# count the number of companies 
scotnor_rids_dict = {}
scotnorcid_rids_dict = {}
for cid, rids in zip(scotnor['cluster_id'], scotnor['COMPANIES']):
    cid = int('3'+str(cid))
    if cid not in scotnorcid_rids_dict.keys():
        scotnorcid_rids_dict[cid] = []
    rids = rids.strip().split(', ')
    for i, rid in enumerate(rids):
        if i%2 == 0:
            if rid not in scotnor_rids_dict.keys():
                scotnor_rids_dict[rid] = ''
            if rid not in scotnorcid_rids_dict[cid]:
                scotnorcid_rids_dict[cid].append(rid)
scotnorcid_rids_sorted = {k: v for k, v in sorted(scotnorcid_rids_dict.items(), key=lambda item: item[0])}
scotnorcid_ridnum_dict = {}
for cid, rids in scotnorcid_rids_sorted.items():
    scotnorcid_ridnum_dict[cid] = len(rids)
# compute regional quotient 
scotnorcid_rq_dict = {}
for cid, ridnum in scotnorcid_ridnum_dict.items():
    scotnorcid_rq_dict[cid] = ridnum/len(scotnor_rids_dict)
    cid_rq_dict[cid] = ridnum/len(scotnor_rids_dict)


# sthest
# learn embeddings of keywords 
sthest = pd.read_csv('sthest_LDA_1.csv')
sthestid_keywords_dict = {}
for cid, keywords in zip(sthest['cluster_id'], sthest['cluster_keyword'].tolist()):
    cid = int('4'+str(cid))
    if cid not in sthestid_keywords_dict.keys():
        sthestid_keywords_dict[cid] = keywords
sthest_id_vec = {}
for cid, cluster in sthestid_keywords_dict.items():
    clusters_vecs = []
    cluster = ' '.join(cluster.split(', '))
    for word in nlp(cluster):
        clusters_vecs.append(word.vector)
    cluster_vec = np.mean(np.array(clusters_vecs), axis=0)
    sthest_id_vec[cid] = cluster_vec
# count the number of companies 
sthest_rids_dict = {}
sthestcid_rids_dict = {}
for cid, rids in zip(sthest['cluster_id'], sthest['COMPANIES']):
    cid = int('4'+str(cid))
    if cid not in sthestcid_rids_dict.keys():
        sthestcid_rids_dict[cid] = []
    rids = rids.strip().split(', ')
    for i, rid in enumerate(rids):
        if i%2 == 0:
            if rid not in sthest_rids_dict.keys():
                sthest_rids_dict[rid] = ''
            if rid not in sthestcid_rids_dict[cid]:
                sthestcid_rids_dict[cid].append(rid)
sthestcid_rids_sorted = {k: v for k, v in sorted(sthestcid_rids_dict.items(), key=lambda item: item[0])}
sthestcid_ridnum_dict = {}
for cid, rids in sthestcid_rids_sorted.items():
    sthestcid_ridnum_dict[cid] = len(rids)
# compute regional quotient 
sthestcid_rq_dict = {}
for cid, ridnum in sthestcid_ridnum_dict.items():
    sthestcid_rq_dict[cid] = ridnum/len(sthest_rids_dict)
    cid_rq_dict[cid] = ridnum/len(sthest_rids_dict)


# london
# learn embeddings of keywords 
london = pd.read_csv('london_LDA_1.csv')
londonid_keywords_dict = {}
for cid, keywords in zip(london['cluster_id'], london['cluster_keyword'].tolist()):
    cid = int('5'+str(cid))
    if cid not in londonid_keywords_dict.keys():
        londonid_keywords_dict[cid] = keywords
london_id_vec = {}
for cid, cluster in londonid_keywords_dict.items():
    clusters_vecs = []
    cluster = ' '.join(cluster.split(', '))
    for word in nlp(cluster):
        clusters_vecs.append(word.vector)
    cluster_vec = np.mean(np.array(clusters_vecs), axis=0)
    london_id_vec[cid] = cluster_vec
# count the number of companies 
london_rids_dict = {}
londoncid_rids_dict = {}
for cid, rids in zip(london['cluster_id'], london['COMPANIES']):
    cid = int('5'+str(cid))
    if cid not in londoncid_rids_dict.keys():
        londoncid_rids_dict[cid] = []
    rids = rids.strip().split(', ')
    for i, rid in enumerate(rids):
        if i%2 == 0:
            if rid not in london_rids_dict.keys():
                london_rids_dict[rid] = ''
            if rid not in londoncid_rids_dict[cid]:
                londoncid_rids_dict[cid].append(rid)
londoncid_rids_sorted = {k: v for k, v in sorted(londoncid_rids_dict.items(), key=lambda item: item[0])}
londoncid_ridnum_dict = {}
for cid, rids in londoncid_rids_sorted.items():
    londoncid_ridnum_dict[cid] = len(rids)
# compute regional quotient 
londoncid_rq_dict = {}
for cid, ridnum in londoncid_ridnum_dict.items():
    londoncid_rq_dict[cid] = ridnum/len(london_rids_dict)
    cid_rq_dict[cid] = ridnum/len(london_rids_dict)

region_quotient_pd = pd.DataFrame()
region_quotient_pd['cluster_id'] = list(cid_rq_dict.keys())
region_quotient_pd['region_quotient'] = list(cid_rq_dict.values())
# print('region_quotient_pd:', region_quotient_pd)
# region_quotient_pd.to_excel('region_quotient.xlsx', index=False)  

def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

irec_id_vec_sorted = {k: v for k, v in sorted(irec_id_vec.items(), key=lambda item: item[0])}
walmid_id_vec_sorted = {k: v for k, v in sorted(walmid_id_vec.items(), key=lambda item: item[0])}
scotnor_id_vec_sorted = {k: v for k, v in sorted(scotnor_id_vec.items(), key=lambda item: item[0])}
sthest_id_vec_sorted = {k: v for k, v in sorted(sthest_id_vec.items(), key=lambda item: item[0])}
london_id_vec_sorted = {k: v for k, v in sorted(london_id_vec.items(), key=lambda item: item[0])}

irecid_wssslid_dict = {}
irecid_cs_dict = {}
for irec_idx, irec_vec in irec_id_vec_sorted.items():
    # walmid
    iw_cs_list = []
    iw_wid_list = []
    for walmid_idx, walmid_vec in walmid_id_vec_sorted.items():
        iw_cs = cosine_similarity(irec_vec, walmid_vec)
        iw_cs_list.append(iw_cs)
        iw_wid_list.append(walmid_idx)
    max_iw = max(iw_cs_list)
    max_widx = iw_wid_list[iw_cs_list.index(max(iw_cs_list))]
    max_iw_walmid_vec = walmid_id_vec_sorted[max_widx]
    irecid_wssslid_dict[irec_idx] = [max_widx]
    # scotnor
    iws_cs_list = []
    iws_sid_list = []
    for scotnor_idx, scotnor_vec in scotnor_id_vec_sorted.items():
        is_cs = cosine_similarity(irec_vec, scotnor_vec)
        ws_cs = cosine_similarity(max_iw_walmid_vec, scotnor_vec)
        iws_cs = (is_cs+ws_cs)/2
        iws_cs_list.append(iws_cs)
        iws_sid_list.append(scotnor_idx)
    max_iws = max(iws_cs_list)
    max_sidx = iws_sid_list[iws_cs_list.index(max(iws_cs_list))]
    max_iws_scotnor_vec = scotnor_id_vec_sorted[max_sidx]
    irecid_wssslid_dict[irec_idx].append(max_sidx)
    # sthest 
    iwss_cs_list = []
    iwss_ssid_list = []
    for sthest_idx, sthest_vec in sthest_id_vec_sorted.items():
        iss_cs = cosine_similarity(irec_vec, sthest_vec)
        wss_cs = cosine_similarity(max_iw_walmid_vec, sthest_vec)
        sss_cs = cosine_similarity(max_iws_scotnor_vec, sthest_vec)
        iwss_cs = (iss_cs+wss_cs+sss_cs)/3
        iwss_cs_list.append(iwss_cs)
        iwss_ssid_list.append(sthest_idx)
    max_iwss = max(iwss_cs_list)
    max_ssidx = iwss_ssid_list[iwss_cs_list.index(max(iwss_cs_list))]
    max_iwss_sthest_vec = sthest_id_vec_sorted[max_ssidx]
    irecid_wssslid_dict[irec_idx].append(max_ssidx)
    # london
    iwssl_cs_list = []
    iwssl_lid_list = []
    for london_idx, london_vec in london_id_vec_sorted.items():
        il_cs = cosine_similarity(irec_vec, london_vec)
        wl_cs = cosine_similarity(max_iw_walmid_vec, london_vec)
        sl_cs = cosine_similarity(max_iws_scotnor_vec, london_vec)
        ssl_cs = cosine_similarity(max_iwss_sthest_vec, london_vec)
        iwssl_cs = (il_cs+wl_cs+sl_cs+ssl_cs)/4
        iwssl_cs_list.append(iwssl_cs)
        iwssl_lid_list.append(london_idx)
    max_iwssl = max(iwssl_cs_list)
    max_lidx = iwssl_lid_list[iwssl_cs_list.index(max(iwssl_cs_list))]
    max_iwssl_london_vec = london_id_vec_sorted[max_lidx]
    irecid_wssslid_dict[irec_idx].append(max_lidx)
    irecid_cs_dict[irec_idx] = max_iwssl

irecid_cs_dict_sorted = {k: v for k, v in sorted(irecid_cs_dict.items(), key=lambda item: item[1], reverse=True)}

# print(irecid_wssslid_dict)
# print(cid_rq_dict)
# print(list(irecid_cs_dict_sorted.keys())[:10])

# location quotient
# top k cosine similarity 
topk = 10
top_ireccid_cs = list(irecid_cs_dict_sorted.keys())
top_irec_cid = []
top_walmid_cid = []
top_scotnor_cid = []
top_sthest_cid = []
top_london_cid = []
i = 0
for icid in top_ireccid_cs:
    if i < topk:
        wcid = irecid_wssslid_dict[icid][0]
        scid = irecid_wssslid_dict[icid][1]
        sscid = irecid_wssslid_dict[icid][2]
        lcid = irecid_wssslid_dict[icid][3]
        if wcid not in top_walmid_cid and scid not in top_scotnor_cid and sscid not in top_sthest_cid and lcid not in top_london_cid:
            top_irec_cid.append(icid)
            top_walmid_cid.append(wcid)
            top_scotnor_cid.append(scid)
            top_sthest_cid.append(sscid)
            top_london_cid.append(lcid)
            i += 1

ii_lq_dict = {}
iw_lq_dict = {}
is_lq_dict = {}
iss_lq_dict = {}
il_lq_dict = {}

wi_lq_dict = {}
ww_lq_dict = {}
ws_lq_dict = {}
wss_lq_dict = {}
wl_lq_dict = {}

si_lq_dict = {}
sw_lq_dict = {}
scsc_lq_dict = {}
scst_lq_dict = {}
sl_lq_dict = {}

ssi_lq_dict = {}
ssw_lq_dict = {}
stsc_lq_dict = {}
stst_lq_dict = {}
ssl_lq_dict = {}

li_lq_dict = {}
lw_lq_dict = {}
ls_lq_dict = {}
lss_lq_dict = {}
ll_lq_dict = {}

locale_left = []
locale_right = []
cluster_id_left = []
cluster_id_right = []
location_quotient = []

for icid, wcid, scid, sscid, lcid in zip(top_irec_cid, top_walmid_cid, top_scotnor_cid, top_sthest_cid, top_london_cid):
    ii_lq = cid_rq_dict[icid]/cid_rq_dict[icid]
    locale_left.append('IRELAND COMBINED')
    locale_right.append('IRELAND COMBINED')
    cluster_id_left.append(icid)
    cluster_id_right.append(icid)
    location_quotient.append(ii_lq)

    iw_lq = cid_rq_dict[icid]/cid_rq_dict[wcid]
    locale_left.append('IRELAND COMBINED')
    locale_right.append('WALES/MIDLANDS')
    cluster_id_left.append(icid)
    cluster_id_right.append(wcid)
    location_quotient.append(iw_lq)

    is_lq = cid_rq_dict[icid]/cid_rq_dict[scid]
    locale_left.append('IRELAND COMBINED')
    locale_right.append('SCOTLAND / NORTH ENGLAND')
    cluster_id_left.append(icid)
    cluster_id_right.append(scid)
    location_quotient.append(is_lq)

    iss_lq = cid_rq_dict[icid]/cid_rq_dict[sscid]
    locale_left.append('IRELAND COMBINED')
    locale_right.append('SOUTH/EASTERN')
    cluster_id_left.append(icid)
    cluster_id_right.append(sscid)
    location_quotient.append(iss_lq)

    il_lq = cid_rq_dict[icid]/cid_rq_dict[lcid]
    locale_left.append('IRELAND COMBINED')
    locale_right.append('LONDON')
    cluster_id_left.append(icid)
    cluster_id_right.append(lcid)
    location_quotient.append(il_lq)

    ii_lq_dict[str(icid)+'_'+str(icid)] = ii_lq
    iw_lq_dict[str(icid)+'_'+str(wcid)] = iw_lq
    is_lq_dict[str(icid)+'_'+str(scid)] = is_lq
    iss_lq_dict[str(icid)+'_'+str(sscid)] = iss_lq
    il_lq_dict[str(icid)+'_'+str(lcid)] = il_lq

    wi_lq = cid_rq_dict[wcid]/cid_rq_dict[icid]
    locale_left.append('WALES/MIDLANDS')
    locale_right.append('IRELAND COMBINED')
    cluster_id_left.append(wcid)
    cluster_id_right.append(icid)
    location_quotient.append(wi_lq)

    ww_lq = cid_rq_dict[wcid]/cid_rq_dict[wcid]
    locale_left.append('WALES/MIDLANDS')
    locale_right.append('WALES/MIDLANDS')
    cluster_id_left.append(wcid)
    cluster_id_right.append(wcid)
    location_quotient.append(ww_lq)

    ws_lq = cid_rq_dict[wcid]/cid_rq_dict[scid]
    locale_left.append('WALES/MIDLANDS')
    locale_right.append('SCOTLAND / NORTH ENGLAND')
    cluster_id_left.append(wcid)
    cluster_id_right.append(scid)
    location_quotient.append(ws_lq)

    wss_lq = cid_rq_dict[wcid]/cid_rq_dict[sscid]
    locale_left.append('WALES/MIDLANDS')
    locale_right.append('SOUTH/EASTERN')
    cluster_id_left.append(wcid)
    cluster_id_right.append(sscid)
    location_quotient.append(wss_lq)

    wl_lq = cid_rq_dict[wcid]/cid_rq_dict[lcid]
    locale_left.append('WALES/MIDLANDS')
    locale_right.append('LONDON')
    cluster_id_left.append(wcid)
    cluster_id_right.append(lcid)
    location_quotient.append(wl_lq)

    wi_lq_dict[str(wcid)+'_'+str(icid)] = wi_lq
    ww_lq_dict[str(wcid)+'_'+str(wcid)] = ww_lq
    ws_lq_dict[str(wcid)+'_'+str(scid)] = ws_lq
    wss_lq_dict[str(wcid)+'_'+str(sscid)] = wss_lq
    wl_lq_dict[str(wcid)+'_'+str(lcid)] = wl_lq

    si_lq = cid_rq_dict[scid]/cid_rq_dict[icid]
    locale_left.append('SCOTLAND / NORTH ENGLAND')
    locale_right.append('IRELAND COMBINED')
    cluster_id_left.append(scid)
    cluster_id_right.append(icid)
    location_quotient.append(si_lq)

    sw_lq = cid_rq_dict[scid]/cid_rq_dict[wcid]
    locale_left.append('SCOTLAND / NORTH ENGLAND')
    locale_right.append('WALES/MIDLANDS')
    cluster_id_left.append(scid)
    cluster_id_right.append(wcid)
    location_quotient.append(sw_lq)

    scsc_lq = cid_rq_dict[scid]/cid_rq_dict[scid]
    locale_left.append('SCOTLAND / NORTH ENGLAND')
    locale_right.append('SCOTLAND / NORTH ENGLAND')
    cluster_id_left.append(scid)
    cluster_id_right.append(scid)
    location_quotient.append(scsc_lq)

    scst_lq = cid_rq_dict[scid]/cid_rq_dict[sscid]
    locale_left.append('SCOTLAND / NORTH ENGLAND')
    locale_right.append('SOUTH/EASTERN')
    cluster_id_left.append(scid)
    cluster_id_right.append(sscid)
    location_quotient.append(scst_lq)

    sl_lq = cid_rq_dict[scid]/cid_rq_dict[lcid]
    locale_left.append('SCOTLAND / NORTH ENGLAND')
    locale_right.append('LONDON')
    cluster_id_left.append(scid)
    cluster_id_right.append(lcid)
    location_quotient.append(sl_lq)

    si_lq_dict[str(scid)+'_'+str(icid)] = si_lq
    sw_lq_dict[str(scid)+'_'+str(wcid)] = sw_lq
    scsc_lq_dict[str(scid)+'_'+str(scid)] = scsc_lq
    scst_lq_dict[str(scid)+'_'+str(sscid)] = scst_lq
    sl_lq_dict[str(scid)+'_'+str(lcid)] = sl_lq

    ssi_lq = cid_rq_dict[sscid]/cid_rq_dict[icid]
    locale_left.append('SOUTH/EASTERN')
    locale_right.append('IRELAND COMBINED')
    cluster_id_left.append(sscid)
    cluster_id_right.append(icid)
    location_quotient.append(ssi_lq)

    ssw_lq = cid_rq_dict[sscid]/cid_rq_dict[wcid]
    locale_left.append('SOUTH/EASTERN')
    locale_right.append('WALES/MIDLANDS')
    cluster_id_left.append(sscid)
    cluster_id_right.append(wcid)
    location_quotient.append(ssw_lq)

    stsc_lq = cid_rq_dict[sscid]/cid_rq_dict[scid]
    locale_left.append('SOUTH/EASTERN')
    locale_right.append('SCOTLAND / NORTH ENGLAND')
    cluster_id_left.append(sscid)
    cluster_id_right.append(scid)
    location_quotient.append(stsc_lq)

    stst_lq = cid_rq_dict[sscid]/cid_rq_dict[sscid]
    locale_left.append('SOUTH/EASTERN')
    locale_right.append('SOUTH/EASTERN')
    cluster_id_left.append(sscid)
    cluster_id_right.append(sscid)
    location_quotient.append(stst_lq)

    ssl_lq = cid_rq_dict[sscid]/cid_rq_dict[lcid]
    locale_left.append('SOUTH/EASTERN')
    locale_right.append('LONDON')
    cluster_id_left.append(sscid)
    cluster_id_right.append(lcid)
    location_quotient.append(ssl_lq)

    ssi_lq_dict[str(sscid)+'_'+str(icid)] = ssi_lq
    ssw_lq_dict[str(sscid)+'_'+str(wcid)] = ssw_lq
    stsc_lq_dict[str(sscid)+'_'+str(scid)] = stsc_lq
    stst_lq_dict[str(sscid)+'_'+str(sscid)] = stst_lq
    ssl_lq_dict[str(sscid)+'_'+str(lcid)] = ssl_lq

    li_lq = cid_rq_dict[lcid]/cid_rq_dict[icid]
    locale_left.append('LONDON')
    locale_right.append('IRELAND COMBINED')
    cluster_id_left.append(lcid)
    cluster_id_right.append(icid)
    location_quotient.append(li_lq)

    lw_lq = cid_rq_dict[lcid]/cid_rq_dict[wcid]
    locale_left.append('LONDON')
    locale_right.append('WALES/MIDLANDS')
    cluster_id_left.append(lcid)
    cluster_id_right.append(wcid)
    location_quotient.append(lw_lq)

    ls_lq = cid_rq_dict[lcid]/cid_rq_dict[scid]
    locale_left.append('LONDON')
    locale_right.append('SCOTLAND / NORTH ENGLAND')
    cluster_id_left.append(lcid)
    cluster_id_right.append(scid)
    location_quotient.append(ls_lq)

    lss_lq = cid_rq_dict[lcid]/cid_rq_dict[sscid]
    locale_left.append('LONDON')
    locale_right.append('SOUTH/EASTERN')
    cluster_id_left.append(lcid)
    cluster_id_right.append(sscid)
    location_quotient.append(lss_lq)

    ll_lq = cid_rq_dict[lcid]/cid_rq_dict[lcid]
    locale_left.append('LONDON')
    locale_right.append('LONDON')
    cluster_id_left.append(lcid)
    cluster_id_right.append(lcid)
    location_quotient.append(ll_lq)

    li_lq_dict[str(lcid)+'_'+str(icid)] = li_lq
    lw_lq_dict[str(lcid)+'_'+str(wcid)] = lw_lq
    ls_lq_dict[str(lcid)+'_'+str(scid)] = ls_lq
    lss_lq_dict[str(lcid)+'_'+str(sscid)] = lss_lq
    ll_lq_dict[str(lcid)+'_'+str(lcid)] = ll_lq

location_quotient_pd = pd.DataFrame()
location_quotient_pd['locale_left'] = locale_left
location_quotient_pd['locale_right'] = locale_right
location_quotient_pd['cluster_id_left'] = cluster_id_left
location_quotient_pd['cluster_id_right'] = cluster_id_right
location_quotient_pd['location_quotient'] = location_quotient
location_quotient_pd.to_excel('location_quotient.xlsx', index=False)  


# Testing
irec_39 = irec_id_vec[139]
walmid_8 = walmid_id_vec[28]
scotnor_4 = scotnor_id_vec[34]
sthest_21 = sthest_id_vec[421]
london_16 = london_id_vec[516]

irec_28 = irec_id_vec[128]
walmid_25 = walmid_id_vec[225]
scotnor_51 = scotnor_id_vec[351]
sthest_40 = sthest_id_vec[440]
london_12 = london_id_vec[512]

c = cosine_similarity(walmid_8, scotnor_4)



