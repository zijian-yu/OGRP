#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author :yzj
# @FileName :urls.py
# @Time :2022/1/14 22:03

from . import views
from tools import urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('dupgen_finder', views.dupgen_finder, name='dupgen_finder_url'),

    path('Vvi', views.Vvi, name='Vvi_url'),

    #事件相关基因
    path('shijian', views.shijian, name='shijian_url'),
    # 三个blast
    path('f_blast', views.f_blast, name='f_blast_url'),
    path('blast_match', views.blast_match, name='blast_match_url'),
    path('sequenceserver', views.sequenceserver, name='sequenceserver_url'),

    # 两个共线性，一个可视化
    path('mcscanx', views.mcscanx, name='mcscanx_url'),
    path('colinearscan', views.colinearscan, name='colinearscan_url'),
    path('synvisio', views.synvisio, name='synvisio_url'),
    path('synvisio_run', views.synvisio_run, name='synvisio_run_url'),
    # 四个WGDI
    path('wgdi_dotplot', views.wgdi_dotplot, name='wgdi_dotplot_url'),
    path('wgdimcs', views.wgdimcs, name='wgdimcs_url'),
    path('wgdikaks', views.wgdikaks, name='wgdikaks_url'),
    path('wgdikaks_dot', views.wgdikaks_dot, name='wgdikaks_dot_url'),
    # Other 工具
    path('formatTofasta', views.formatTofasta, name='formatTofasta_url'),
    path('duplicate_removal', views.duplicate_removal, name='quchong_url'),
    path('extract_row', views.extract_row, name='extract_row_url'),
    path('file_merge', views.file_merge, name='file_merge_url'),
    path('find_replace', views.find_replace, name='find_replace_url'),
    # 圈图、jbrowse
    path('circos', views.circos, name='circos_url'),
    
    path('jbrowse', views.jbrowse, name='jbrowse_url'),
    path('gsds', views.gsds, name='gsds_url'),
    # Gene_family
    path('diamond', views.diamond, name='diamond_url'),
    path('paraat', views.paraat, name='paraat_url'),
    path('kaks_calculator', views.kaks_calculator, name='kaks_calculator_url'),
    path('fasttree', views.fasttree, name='fasttree_url'),
    path('meme_suit', views.meme_suit, name='meme_suit_url'),
    path('hmmer', views.hmmer, name='hmmer_url'),
    path('pfam', views.pfam, name='pfam_url'),
    path('iq_tree', views.iq_tree, name='iq_tree_url'),

    path('cpgfinder', views.cpgfinder, name='cpgfinder_url'),
    #path('hmmer', views.hmmer, name='hmmer_url'),
    path('phyml', views.phyml, name='phyml_url'),
    path('sequence_alignment', views.sequence_alignment, name='sequence_alignment_url'),
    path('sequence_screening', views.sequence_screening, name='sequence_screening_url'),
    path('codonw', views.codonw, name='codonw_url'),

    path('dotplot_run', views.dotplot_run, name='dotplot_run_url'),
    path('index_email', views.index_email, name='index_email_url'),
    path('blast_run', views.blast_run, name='blast_run_url'),
    path('mcscanx_run', views.mcscanx_run, name='mcscanx_run_url'),
    # path('colinearscan_run', views.colinearscan_run_tools, name='colinearscan_run_url'),
    path('colinearscan_run', views.colinearscan_run, name='colinearscan_run_url'),

    path('dupgen_finder_run', views.dupgen_finder_run_tools, name='dupgen_finder_run_url'),

    path('blast_match_run', views.blast_match_run, name='blast_match_run_url'),

    path('wgdikaks_run', views.wgdikaks_run, name='wgdikaks_run_url'),
    path('wgdikaks_dot_run', views.wgdikaks_dot_run, name='wgdikaks_dot_url'),
    path('wgdimcs_run', views.wgdimcs_run, name='wgdimcs_url'),
    path('file_merge_run', views.file_merge_run, name='file_merge_run_url'),
    path('find_replace_run', views.find_replace_run, name='find_replace_run_url'),
    path('extract_column_run', views.extract_column_run, name='extract_column_run_url'),
    path('duplicate_removal_run', views.duplicate_removal_run, name='duplicate_removal_run_url'),
    path('formatTofasta_run', views.formatTofasta_run, name='formatTofasta_run_url'),
    # path('karyotype/Step1.html', views.Step1, name='Step1_url'),


    path('zu_ks_calculate', views.zu_ks_calculate, name='zu_ks_calculate_url'),
    path('zu_ks_calculate_run', views.zu_ks_calculate_run, name='zu_ks_calculate_run_url'),

    # Gene_family
    path('diamond_run', views.diamond_run, name='diamond_run_url'),
    path('paraat_run', views.paraat_run, name='paraat_run_url'),
    path('kaks_calculator_run', views.kaks_calculator_run, name='kaks_calculator_run_url'),
    path('fasttree_run', views.fasttree_run, name='fasttree_run_url'),
    path('meme_suit_run', views.meme_suit_run, name='meme_suit_run_url'),
    path('hmmer_run', views.hmmer_run, name='hmmer_run_url'),
    path('pfam_run', views.pfam_run, name='pfam_run_url'),
    path('iq_tree_run', views.iq_tree_run, name='iq_tree_run_url'),

    path('sequence_screening_run', views.sequence_screening_run, name='sequence_screening_run_url'),
    # path('hmmer_run', views.hmmer_run, name='hmmer_run_url'),
    path('cpgfinder_run', views.cpgfinder_run, name='cpgfinder_run_url'),
    path('sequence_alignment_run', views.sequence_alignment_run, name='sequence_alignment_run_url'),
    path('phyml_run', views.phyml_run, name='phyml_run_url'),
    path('codonw_run', views.codonw_run, name='codonw_run_url'),

    # 组-基因分馏
    path('zu_correspondence_mc', views.zu_correspondence_mc, name='zu_correspondence_mc_url'),
    path('zu_correspondence_mc_run', views.zu_correspondence_mc_run, name='zu_correspondence_run_mc_url'),
    path('zu_pindex', views.zu_pindex, name='zu_pindex_url'),
    path('zu_pindex_run', views.zu_pindex_run, name='zu_pindex_run_url'),
    path('zu_retention', views.zu_retention, name='zu_retention_url'),
    path('zu_retention_run', views.zu_retention_run, name='zu_retention_run_url'),
    path('zu_loss', views.zu_loss, name='zu_loss_url'),
    path('zu_loss_run', views.zu_loss_run, name='zu_loss_run_url'),

    path('zu_blast_dotplot', views.zu_blast_dotplot, name='zu_blast_dotplot_url'),
    path('zu_blast_dotplot_run', views.zu_blast_dotplot_run, name='zu_blast_dotplot_run_url'),
    path('zu_block_dotplot', views.zu_block_dotplot, name='zu_block_dotplot_url'),
    path('zu_block_dotplot_run', views.zu_block_dotplot_run, name='zu_block_dotplot_run_url'),
    path('zu_ks_dotplot', views.zu_ks_dotplot, name='zu_ks_dotplot_url'),
    path('zu_ks_dotplot_run', views.zu_ks_dotplot_run, name='zu_ks_dotplot_run_url'),

    path('zu_ks_distribution', views.zu_ks_distribution, name='zu_ks_distribution_url'),
    path('zu_ks_distribution_run', views.zu_ks_distribution_run, name='zu_ks_distribution_run_url'),
    path('blast_results', views.blast_results_run, name='blast_results'),
    
    path('docker', views.docker, name='docker_url'),
        
    path('pipeline', views.pipeline, name='pipeline_url'),
]


