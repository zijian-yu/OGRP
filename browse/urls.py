#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author :yzj
# @FileName :urls.py
# @Time :2022/1/14 22:03


from django.contrib import admin
from django.urls import path, include
from tools import urls
from . import views
# from django.conf.urls import url


urlpatterns = [
    path('dotplot', views.dotplot, name='dotplot_url'),
    path('kaks', views.colinear_kaks, name='colinear_kaks_url'),
    path('Oleaceae_syntenic', views.Oleaceae_syntenic, name='Oleaceae_syntenic_url'),
    path('Sob_Vvi_syntenic', views.Sob_Vvi_syntenic, name='Sob_Vvi_syntenic_url'),
    path('Jsa_Vvi_syntenic', views.Jsa_Vvi_syntenic, name='Jsa_Vvi_syntenic_url'),

    path('ECH_event', views.ECH_event, name='ECH_event_url'),
    path('OCH_event', views.OCH_event, name='OCH_event_url'),
    path('ORT_event', views.ORT_event, name='ORT_event_url'),
    path('event_Chu', views.event_Chu, name='event_Chu_url'),
    path('event_Fpe', views.event_Fpe, name='event_Fpe_url'),
    path('event_Jsa', views.event_Jsa, name='event_Jsa_url'),
    path('event_Oeu', views.event_Oeu, name='event_Oeu_url'),
    path('event_Sob', views.event_Sob, name='event_Sob_url'),
    path('event_Vvi', views.event_Vvi, name='event_Vvi_url'),

    path('genetype_Chu', views.genetype_Chu, name='genetype_Chu_url'),
    path('genetype_Fpe', views.genetype_Fpe, name='genetype_Fpe_url'),
    path('genetype_Jsa', views.genetype_Jsa, name='genetype_Jsa_url'),
    path('genetype_Oeu', views.genetype_Oeu, name='genetype_Oeu_url'),
    path('genetype_Sob', views.genetype_Sob, name='genetype_Sob_url'),
    path('genetype_Vvi', views.genetype_Vvi, name='genetype_Vvi_url'),

    # hybridization_Genes
    path('karyotype', views.karyotype, name='karyotype_url'),
    path('TF_genes', views.TF_genesdx, name='TF_genesdx_url'),
    path('TF_genes/<str:title>/', views.TF_genes, name='TF_genes'),

    # TE
    path('TE_index1', views.TE_index1, name='TE_index1_url'),
    path('TE/<str:sp_name>', views.TE_sp, name='TE'),
    path('TE_type/<str:sp_name>/<str:type>', views.TE_type, name='TE_type'),

    path('kegg', views.kegg, name='kegg_url'),
    path('paper', views.paper, name='paper_url'),

    path('Pfam_index', views.Pfam_index, name='pfam_index_url'),
    path('pfam_index_run', views.pfam_index_run, name='pfam_index_run_url'),

    path('interproscan_index', views.interproscan_index, name='interproscan_index_url'),
    path('interproscan_index_run', views.interproscan_index_run, name='interproscan_index_run_url'),

    path('kegg_index', views.kegg_index, name='kegg_index_url'),
    path('kegg_index_run', views.kegg_index_run, name='kegg_index_run_url'),

    path('gene_family', views.gene_family, name='gene_family_url'),
    path('search_api', views.search_api, name='search_api_url'),
    # 花青素基因
    path('Anthocyanin_genes_index', views.Anthocyanin_genes_index, name='Anthocyanin_genes_index_url'),
    path('Anthocyanin_genes/<str:title>/', views.Anthocyanin_genes, name='Anthocyanin_genes'),
    # 生长素基因
    path('Auxin_genes_index', views.Auxin_genes_index, name='Auxin_genes_index_url'),
    path('Auxin_genes/<str:title>/', views.Auxin_genes, name='Auxin_genes'),
    # 花发育基因
    path('flowerdevelopmentgenes_index', views.flowerdevelopmentgenes_index, name='flowerdevelopmentgenes_index_url'),
    path('flowerdevelopmentgenes/<str:title>/', views.flowerdevelopmentgenes, name='flowerdevelopmentgenes'),
    # 开花时间基因
    path('floweringtimegenes_index', views.floweringtimegenes_index, name='floweringtimegenes_index_url'),
    path('floweringtimegenes/<str:title>/', views.floweringtimegenes, name='floweringtimegenes'),
    # 待决开花时间基因
    path('pendingfloweringtimegenes_index', views.pendingfloweringtimegenes_index, name='pendingfloweringtimegenes_index_url'),
    path('pendingfloweringtimegenes/<str:title>/', views.pendingfloweringtimegenes, name='pendingfloweringtimegenes'),
    # 苯丙氨酸解氨酶
    path('phenylalanineAmmoniaLyase_index', views.phenylalanineAmmoniaLyase_index, name='phenylalanineAmmoniaLyase_index_url'),
    path('phenylalanineAmmoniaLyase/<str:title>/', views.phenylalanineAmmoniaLyase, name='phenylalanineAmmoniaLyase'),
    # 抗性基因
    path('ResistencegenesRLP_index', views.ResistencegenesRLP_index, name='ResistencegenesRLP_index_url'),
    path('ResistencegenesRLP/<str:title>/', views.ResistencegenesRLP, name='ResistencegenesRLP'),
    # 硬脂酰-ACP脱氢酶
    path('stearoylACPdesaturase_index', views.stearoylACPdesaturase_index, name='stearoylACPdesaturase_index_url'),
    path('stearoylACPdesaturase/<str:title>/', views.stearoylACPdesaturase, name='stearoylACPdesaturase'),

    # 功能基因
    path('Functional_genes', views.Functional_genesdx, name='Functional_genesdx_url'),
    path('Functional_genes/<str:title>/', views.Functional_genes, name='Functional_genes'),
    
    # m6a - Wirters 相关基因 --- 页面
    path('m6a_wirters_genes', views.m6a_wirters_genes_index, name='m6a_wirters_genes_index_url'),
    path('m6a_wirters_genes/<str:title>/', views.m6a_wirters_genes, name='m6a_wirters_genes'),
    # m6a - Readers 相关基因 --- 页面
    path('m6a_readers_genes', views.m6a_readers_genes, name='m6a_readers_genes_url'),
    # m6a - Erasers 相关基因 --- 页面
    path('m6a_erasers_genes', views.m6a_erasers_genes, name='m6a_erasers_genes_url'),

    # url("^([0-9]*-.*)", views.Download_file, name="num_download"),
    # url("^(pipeline-.*)", views.Download_file, name="eng_download"),

    # 核型链接
    path('karyotype/Jsa', views.Jsa, name='Jsa_url'),
    path('karyotype/Sob', views.Sob, name='Sob_url'),
    path('karyotype/Fpe', views.Fpe, name='Fpe_url'),
    path('karyotype/Oeu', views.Oeu, name='Oeu_url'),
    path('karyotype/CASOF', views.CASOF, name='CASOF_url'),
    path('karyotype/MRCAO', views.MRCAO, name='MRCAO_url'),

    # 例子 case
    path('case_genome', views.case_genome, name='case_genome_url'),
    path('case_blast', views.case_blast, name='case_blast_url'),
    path('case_block', views.case_block, name='case_block_url'),
    path('case_ks', views.case_ks, name='case_ks_url'),
    path('case_dating', views.case_dating, name='case_dating_url'),
    path('case_ESR', views.case_ESR, name='case_ESR_url'),
    path('case_phylogeny', views.case_phylogeny, name='case_phylogeny_url'),
    path('case_wgd_event', views.case_wgd_event, name='case_wgd_event_url'),

    path('case_CSR', views.case_CSR, name='case_CSR_url'),
    path('case_MCR', views.case_MCR, name='case_MCR_url'),
    path('case_VCP', views.case_VCP, name='case_VCP_url'),
    path('case_AK', views.case_AK, name='case_AK_url'),
    path('case_karyotype', views.case_karyotype, name='case_karyotype_url'),

    path('case_hmmer', views.case_hmmer, name='case_hmmer_url'),
    path('case_tree', views.case_tree, name='case_tree_url'),
    path('case_evolution_event', views.case_evolution_event, name='case_evolution_event_url'),
    path('case_circos', views.case_circos, name='case_circos_url'),
    path('case_structure', views.case_structure, name='case_structure_url'),
    path('case_expression', views.case_expression, name='case_expression_url'),
    path('case_family', views.case_family, name='case_family_url'),

]





