#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author :yuzijian1010@163.com
# @Time : 2023/12/4 16:41
# @Last time: 2023/12/4 16:41

import os
import subprocess
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Bio.Blast import NCBIXML, NCBIWWW
from django.http import HttpResponse, FileResponse
from urllib.parse import quote
from urllib.parse import unquote
from LGBP.tools import *


path_get = os.getcwd()

def download_file_view(request):
    file_path = unquote(request.GET.get('file', ''))
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
    return response


def zip_file(request, place, files):
    cmd = f"""
        cd {path_get}/file_keep/{place}
        zip -r result.zip {files}
    """
    os.system(cmd)
    zip_file_path = f'{path_get}/file_keep/{place}/result.zip'
    download_link = f'/download/?file={quote(zip_file_path)}'
    return render(request, 'successful.html', {'download_link': download_link})


def index(request):
    return render(request, 'index.html')

def index_2(request):
    return render(request, 'index_2.html')

def index_3(request):
    return render(request, 'index_3.html')

def tools(request):
    return render(request, 'tools.html')


def sp_tree_chart(request):
    return render(request, 'sp_tree_chart.html')
    
def diagram_blocks(request):
    return  render(request,'diagram_blocks.html')


def gene_replication_type(request):
    return render(request, 'gene_replication_chart.html')

def diagram_Oleuropein(request):
    return  render(request,'diagram_Oleuropein.html')

def cucpathway(request):
    return  render(request,'cucpathway.html')

def diagram_salt(request):
    return  render(request,'diagram_salt-tolerant.html')

def diagram_TR(request):
    return  render(request,'diagram_TR.html')

def Transcription_factors(request):
    return render(request,'Transcription_factors.html')

def diagram_salt(request):
    return  render(request,'diagram_salt.html')

def diagram_Jsa_acid(request):
    return  render(request,'diagram_Jsa_acid.html')

def diagram_heat_cold(request):
    return  render(request,'diagram_heat_cold.html')

def diagram_drought(request):
    return  render(request,'diagram_drought.html')

def diagram_terpene(request):
    return  render(request,'diagram_terpene.html')


def p_index(request):
    return render(request, 'p_index_chart.html')


def sp_introduce(request):
    return render(request, 'sp_introduce.html')


def sp_introduce2(request):
    return render(request, 'sp_introduce2.html')


def sp_introduce3(request):
    return render(request, 'sp_introduce3.html')


from django.conf import settings
import pandas as pd
from Bio import SeqIO


def get_gene_ids(file_path, start, end, chromosome):
    df = pd.read_csv(file_path, sep="\t", header=None)
    filtered_df = df[df[0] == chromosome]
    final_filtered_df = filtered_df[(filtered_df[2] >= start) & (filtered_df[1] <= end)]
    gene_ids = final_filtered_df[5].tolist()
    return gene_ids


def extract_sequences_by_id(seq_file, gene_ids):
    sequences = {}
    for record in SeqIO.parse(seq_file, "fasta"):
        if record.id in gene_ids:
            sequences[f"{record.id}"] = str(record.seq)
    return sequences


def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    gc_content = (gc_count / len(sequence)) * 100
    # return gc_content
    return round(gc_content, 3)


def compile_gene_info(cds_sequences, pep_sequences):
    gene_info = []
    for gene_id in cds_sequences.keys():
        cds_seq = cds_sequences[gene_id]
        pep_seq = pep_sequences.get(gene_id, "")
        cds_length = len(cds_seq)
        pep_length = len(pep_seq)
        gc_content = calculate_gc_content(cds_seq)
        gene_info.append((gene_id, cds_seq, pep_seq, cds_length, pep_length, gc_content))
    return gene_info


def species_data(request):
    sp_name = request.POST.get("sp_name")
    chromosome_number = request.POST.get('chromosome_number')
    start = request.POST.get('start')
    end = request.POST.get('end')
    print(sp_name, chromosome_number, start, end)

    if start is None or end is None:
        return render(request, 'species_data.html')

    start = int(start)
    end = int(end)
    # 文件夹路径
    folder_path = os.path.join(settings.BASE_DIR, 'file_keep', 'species_data')
    gff_file = os.path.join(folder_path, f"{sp_name}.new.gff")
    chr_number = int(chromosome_number.split()[1])
    gene_ids = get_gene_ids(gff_file, start, end, chr_number)
    print(gene_ids)

    pep_seq_file = os.path.join(folder_path, f"{sp_name}.pep")
    pep_sequences = extract_sequences_by_id(pep_seq_file, gene_ids)
    cds_seq_file = os.path.join(folder_path, f"{sp_name}.cds")
    cds_sequences = extract_sequences_by_id(cds_seq_file, gene_ids)
    # 输出结果
    # print(pep_sequences, cds_sequences)
    # 汇总基因信息
    result = compile_gene_info(cds_sequences, pep_sequences)
    print(result)

    # print(results)
    return render(request, 'species_data.html', {'result': result})



def Transcriptome(request):
    return  render(request, 'Transcriptome.html')

def transcriptome_run(request):
    sp_data_1 = request.POST.get("sp_data_1", None)
    sp_data_2 = request.POST.get("sp_data_2", None)
    return render(request, f'transcriptome_run.html', {"sp_name": sp_data_1, "type": sp_data_2})

def database(request):
    return render(request, 'database.html')


def submit(request):
    return render(request, 'submit.html')

def submit_data(request):
    return render(request, 'submit_data.html')


def documentation(request):
    return render(request, 'documentation.html')


def gfca(request):
    return render(request, 'gfca.html')


def karyotype(request):
    return render(request, 'karyotype.html')

def genetype(request):
    return  render(request,'genetype.html')

def genetype_run(request):
    sp_data_1 = request.POST.get("sp_data_1", None)
    sp_data_2 = request.POST.get("sp_data_2", None)
    return render(request, f'genetype_run.html', {"sp_name": sp_data_1, "type": sp_data_2})


def gene_function(request):
    return render(request, 'interproscan_index.html')


def database(request):
    return render(request, 'database.html')


def about(request):
    return render(request, 'about.html')


def references(request):
    return render(request, 'references.html')

def commands(request):
    return render(request,'commands.html')


def new(request):
    return render(request, 'new.html')

def economic(request):
    return render(request,'econmic.html')

def diseases(request):
    return render(request,'diseases.html')

def pests(request):
    return render(request,'pests.html')

def statistics(request):
    return render(request, 'statistics.html')


def help(request):
    return render(request, 'help.html')


def article(request):
    return render(request, 'article.html')


def contact(request):
    return render(request, 'contact.html')


def successful(request):
    return render(request, 'successful.html')


# 分割线----------------------------------------tools模块
#事件相关基因
def shijian(request):
    return render(request, 'shijian.html')


# 葫芦目_blast--
def f_blast(request):
    return render(request, 'f_blast.html')


def blast_match(request):
    return render(request, 'blast_match.html')


def sequenceserver(request):
    return render(request, 'sequenceserver.html')


# 两个共线性工具
def mcscanx(request):
    return render(request, 'mcscanx.html')


def colinearscan(request):
    return render(request, 'colinearscan.html')


# 4个 WGDI 功能
def wgdi_dotplot(request):
    return render(request, 'wgdi_dotplot.html')


def wgdimcs(request):
    return render(request, 'wgdimcs.html')


def wgdikaks(request):
    return render(request, 'wgdikaks.html')


def wgdikaks_dot(request):
    return render(request, 'wgdikaks_dot.html')


# orther 工具
def file_merge(request):
    return render(request, 'file_merge.html')


def formatTofasta(request):
    return render(request, 'formatTofasta.html')


def find_replace(request):
    return render(request, 'find_replace.html')


def extract_row(request):
    return render(request, 'extract_row.html')


def duplicate_removal(request):
    return render(request, 'quchong.html')


# circos、jbrowse
def circos(request):
    return render(request, 'circos.html')
    
    
def docker(request):
    return render(request, 'docker.html')
    

def pipeline(request):
    return render(request, 'pipeline.html')


def jbrowse(request):
    return render(request, 'jbrowse.html')


def synvisio(request):
    return render(request, 'synvisio.html')


def gsds(request):
    return render(request, 'gsds.html')


def dupgen_finder(request):
    return render(request, 'dupgen_finder.html')


def cpgfinder(request):
    return render(request, 'cpgfinder.html')


def phyml(request):
    return render(request, 'phyml.html')


def sequence_alignment(request):
    return render(request, 'sequence_alignment.html')


def sequence_screening(request):
    return render(request, 'sequence_screening.html')


def Browse(request):
    return render(request, 'Browse.html')


def diamond(request):
    return render(request, 'diamond.html')


def paraat(request):
    return render(request, 'paraat.html')


def kaks_calculator(request):
    return render(request, 'kaks_calculator.html')


def fasttree(request):
    return render(request, 'fasttree.html')


def hmmer(request):
    return render(request, 'hmmer.html')


def meme_suit(request):
    return render(request, 'meme_suit.html')


def pfam(request):
    return render(request, 'pfam.html')


def iq_tree(request):
    return render(request, 'iq_tree.html')


def codonw(request):
    return render(request, 'codonw.html')


# codonw
def codonw_run(request):
    file = request.FILES.get("file", None)

    if file is None:
        return render(request, '../templates/codonw.html')
    c = name_set()
    file_name = file.name.split(".")[0]
    file.name = '1.fasta'
    keep_file(na=file, c=c)

    codonw_run_tools(place=c, file_name=file_name)
    files = f'{file_name}.out {file_name}.blk'
    return zip_file(request, c, files)


# sequence_screening
def sequence_screening_run(request):
    protein = request.FILES.get("protein", None)
    gene = request.FILES.get('gene', None)
    gff = request.FILES.get('gff', None)
    id = request.FILES.get('id', None)

    if protein is None or gene is None or gff is None or id is None:
        return render(request, 'sequence_screening.html')
    c = name_set()
    protein.name = 'protein.fasta'
    gene.name = 'gene.fasta'
    gff.name = 'gff.fasta'
    id.name = 'id.fasta'

    keep_file(na=protein, c=c)
    keep_file(na=gene, c=c)
    keep_file(na=gff, c=c)
    keep_file(na=id, c=c)

    sequence_run(place=c)

    files = 'new_pro.txt new_cds.txt new_gff.txt'
    return zip_file(request, c, files)



# sequence_alignment
def sequence_alignment_run(request):
    myFile1 = request.FILES.get("file1", None)
    patten = request.POST.get('patten', None)
    # email = request.POST.get('email', None)

    if myFile1 is None:
        return render(request, '../templates/sequence_alignment.html')
    c = name_set()
    myFile1.name = "1.fasta"
    keep_file(na=myFile1, c=c)

    sequence_aligment_run_tools(place=c, patten=patten)
    if patten == "mafft":
        files = f'{path_get}/file_keep/{c}/mafft.fasta'
    else:
        files = f'{path_get}/file_keep/{c}/1.aln'
    return zip_file(request, c, files)


# phyml
def phyml_run(request):
    myFile1 = request.FILES.get("file", None)
    patten = request.POST.get('patten', None)
    small = request.POST.get('small', None)
    model = request.POST.get('model', None)
    frequency = request.POST.get('frequency', None)
    nice = request.POST.get('nice', None)
    num = request.POST.get('num', None)

    if myFile1 is None:
        return render(request, '../templates/phyml.html')

    c = name_set()
    myFile1.name = "1.phy"
    keep_file(na=myFile1, c=c)

    phyml_run_tools(place=c, patten=patten, model=model, frequency=frequency, nice=nice, num=num, small=small)
    files = "1.phy_*"
    return zip_file(request, c, files)


# cpgfinder
def cpgfinder_run(request):
    myFile1 = request.FILES.get("file1", None)
    island = request.POST.get('island', None)
    cg_percent = request.POST.get('cg_percent', None)
    gc_ratio = request.POST.get('gc_ratio', None)
    if myFile1 is None:
        return render(request, '../templates/cpgfinder.html')

    c = name_set()
    myFile_name = myFile1.name
    keep_file(na=myFile1, c=c)
    cpgfinder_run_tools(place=c, island=island, cg_percent=cg_percent, gc_ratio=gc_ratio, myFile_name=myFile_name)

    files = 'cpgfinder_result.txt'
    return zip_file(request, c, files)



# diamond
def diamond_run(request):
    patten = request.POST.get('patten', None)
    myFile1 = request.FILES.get('file1', None)
    myFile2 = request.FILES.get('file2', None)
    # email = request.POST.get('email', None)
    e_value = str(request.POST.get('e_value', None))
    sco = request.POST.get('score_1', None)
    iden = request.POST.get('identity_1', None)
    nucl_or_prot = "prot" if patten == 'blastp' else "nucl"
    # 判断文件是否为空 如果为空则刷新页面
    if myFile1 is None or myFile2 is None:
        return render(request, '/templates/diamond.html')
    c = name_set()
    # keep_email(e=c, address=email)
    myFile1_name = myFile1.name.split(".")[0]
    myFile2_name = myFile2.name.split(".")[0]
    myFile1.name = '1.fasta'
    myFile2.name = '2.fasta'
    keep_file(na=myFile1, c=c)
    keep_file(na=myFile2, c=c)
    # diamond_run_tools(place=c, patten=patten, e=e_value, email=email, score=sco, identity=iden, myFile1=myFile1_name, myFile2=myFile2_name)
    diamond_run_tools(place=c, patten=patten, e=e_value, score=sco, identity=iden, myFile1=myFile1_name, myFile2=myFile2_name)
    files = f"{myFile1_name}_{myFile2_name}.fasta sequence.txt"
    return zip_file(request, c, files)
    # return render(request, '../templates/successful.html')

    # # 先执行 zip_file 函数（下载压缩包）
    # zip_response = zip_file(request, c, files)
    # # 在执行成功后，再渲染成功页面
    # if zip_response.status_code == 200:
    #     return render(request, 'successful.html')


# paraat
def paraat_run(request):
    patten = request.POST.get('patten', None)
    homologs = request.FILES.get("homologs", None)
    cds = request.FILES.get('cds', None)
    pep = request.FILES.get('pep', None)

    if homologs is None or cds is None or pep is None:
        return render(request, '../templates/paraat.html')
    c = name_set()
    homologs.name = 'hom.homologs'
    cds.name = 'cds.cds'
    pep.name = 'pep.pep'
    keep_file(na=homologs, c=c)
    keep_file(na=cds, c=c)
    keep_file(na=pep, c=c)

    paraat_run_tools(place=c, patten=patten)
    files = f'{path_get}/file_keep/{c}/result.{patten}'
    return zip_file(request, c, files)



# kaks_calculator
def kaks_calculator_run(request):
    patten = request.POST.get('patten', None)
    kaks = request.FILES.get("kaks", None)

    if kaks is None:
        return render(request, '../templates/kaks_calculator.html')
    c = name_set()

    kaks.name = 'kaks.axt'
    keep_file(na=kaks, c=c)
    kaks_calculator_run_tools(place=c, patten=patten)
    files = f'{path_get}/file_keep/{c}/result_kaks.txt'
    return zip_file(request, c, files)


# fasttree
def fasttree_run(request):
    patten = request.POST.get('patten', None)
    myFile1 = request.FILES.get("file1", None)

    if myFile1 is None:
        return render(request, '../templates/fasttree.html')
    c = name_set()
    myFile1.name = "1.phy"
    keep_file(na=myFile1, c=c)

    fasttree_run_tools(place=c, patten=patten)

    files = f'1.nwk'
    return zip_file(request, c, files)



# hmmer
def hmmer_run(request):
    hmm_model = request.FILES.get("hmm_model", None)
    hmm_fa = request.FILES.get('hmm_fa', None)
    e_value = request.POST.get('e_value', None)

    if hmm_fa is None or hmm_model is None:
        return render(request, '../templates/hmmer.html')
    c = name_set()

    hmm_model.name = "hmm_model.fasta"
    hmm_fa.name = "hmm_fa.fasta"
    keep_file(na=hmm_model, c=c)
    keep_file(na=hmm_fa, c=c)

    hmmer_run_tools(place=c, e_value=e_value)
    files = 'result.out'
    return zip_file(request, c, files)


# MEME
def meme_suit_run(request):
    myFile1 = request.FILES.get("file1", None)
    patten = request.POST.get('patten', None)
    motif = request.POST.get('motif', None)
    motif_num = request.POST.get('motif_num', None)
    minw = request.POST.get('minw', None)
    maxw = request.POST.get('maxw', None)
    if myFile1 is None:
        return render(request, '../templates/meme_suit.html')

    c = name_set()
    myFile1.name = '1.fasta'
    keep_file(na=myFile1, c=c)

    meme_run_tools(place=c, patten=patten, motif=motif, motif_num=motif_num, minw=minw, maxw=maxw)

    files = 'logo*.png meme.*'
    return zip_file(request, c, files)


# pfam
def pfam_run(request):
    myFile1 = request.FILES.get("file1", None)
    structure = request.POST.get('structure', None)
    if myFile1 is None:
        return render(request, '../templates/pfam.html')
    c = name_set()
    myFile1.name = "1.fasta"
    keep_file(na=myFile1, c=c)

    pfam_run_tools(place=c, structure=structure)
    files = 'pfam.txt pfam_new.txt'
    return zip_file(request, c, files)


# iqtree
def iq_tree_run(request):
    file = request.FILES.get("file", None)
    patten = request.POST.get('patten', None)
    bs_num = request.POST.get('bs_num', None)
    if file is None:
        return render(request, '../templates/iq_tree.html')
    c = name_set()
    file.name = 'result.phy'
    keep_file(na=file, c=c)
    iqtree_run_tools(place=c, patten=patten, bs_num=bs_num)
    files = f'result.phy.treefile'
    return zip_file(request, c, files)


def synvisio_run(request):
    sp_data_1 = request.POST.get("sp_data_1", None)
    sp_data_2 = request.POST.get("sp_data_2", None)

    synvisio_file = open('templates/synvisio_run.html', 'w')
    synvisio_file.write(f"""
    {{% extends 'index.html' %}}
    {{% block body_index %}}
        <div class="row">
            <div class="col-12">
                <h3 class="h3_1 h3_6" style="background-image:url(../../static/image/ico.png); font-family:'Arial',sans-serif;color:black;">{sp_data_1}_{sp_data_2} Genome Synteny Viewer<i></i>
                </h3>
            </div>
            <iframe src="https://synteny_viewer.cgrpoee.top/#/dashboard/{sp_data_1}_{sp_data_2}" style="height: 3000px;width: 100%"></iframe>
        </div>
    {{% endblock %}}
    """)
    synvisio_file.close()

    return render(request, 'synvisio_run.html')


# index_email
def index_email(request):
    name = request.POST.get("name", None)
    email = request.POST.get("email", None)
    message = request.POST.get("message", None)

    if email is None or name is None or message is None:
        return render(request, '../templates/contact.html')
    else:
        c = name_set()
        keep_email_index(place=c, name=name, email=email, message=message)
        return render(request, '../templates/successful.html')


# dotplot
def dotplot_run(request):
    # 五个文件
    blast = request.FILES.get('blast', None)
    heng_len = request.FILES.get('heng_len', None)
    shu_len = request.FILES.get('shu_len', None)
    heng_gff = request.FILES.get('heng_gff', None)
    shu_gff = request.FILES.get('shu_gff', None)

    # 四种参数-值
    evalue = str(request.POST.get('evalue', None))
    score = request.POST.get('score', None)
    hitnum = request.POST.get('hitnum', None)
    repnum = request.POST.get('repnum', None)

    # 需要保存的染色体数
    heng_chromosomes = str(request.POST.get('heng_chromosomes', None))
    shu_chromosomes = str(request.POST.get('shu_chromosomes', None))

    # 需要保存的物种名称
    heng_species = str(request.POST.get('heng_species', None))
    shu_species = str(request.POST.get('shu_species', None))

    email = request.POST.get('email', None)

    if blast is None or heng_len is None or shu_len is None or heng_gff is None or shu_gff is None:
        return render(request, '../templates/dotplot.html')
    else:
        c = name_set()
        keep_email(e=c, address=email)

        blast_name = blast.name
        shu_gff_name = shu_gff.name
        heng_gff_name = heng_gff.name
        shu_len_name = shu_len.name
        heng_len_name = heng_len.name

        keep_file(na=blast, c=c)
        keep_file(na=heng_len, c=c)
        keep_file(na=shu_len, c=c)
        keep_file(na=heng_gff, c=c)
        keep_file(na=shu_gff, c=c)

        dotplot_run_tools(place=c, email=email, evalue=evalue, score=score, hitnum=hitnum, repnum=repnum,
                          heng_chromosomes=heng_chromosomes, shu_chromosomes=shu_chromosomes,
                          heng_species=heng_species, shu_species=shu_species,
                          blast_name=blast_name,
                          shu_gff_name=shu_gff_name, heng_gff_name=heng_gff_name,
                          shu_len_name=shu_len_name, heng_len_name=heng_len_name
                          )
        return render(request, '../templates/successful.html')



# zu_correspondence_mc_run
def zu_correspondence_mc_run(request):
    blast = request.FILES.get('blast', None)
    block = request.FILES.get('block', None)
    correspondence = request.FILES.get('correspondence', None)

    shu_len = request.FILES.get('shu_len', None)
    shu_gff = request.FILES.get('shu_gff', None)
    heng_len = request.FILES.get('heng_len', None)
    heng_gff = request.FILES.get('heng_gff', None)

    if blast is None or block is None or correspondence is None or heng_len is None or shu_len is None or heng_gff is None or shu_gff is None:
        return render(request, '../templates/zu_correspondence_mc.html')
    c = name_set()

    keep_file(na=blast, c=c)
    keep_file(na=block, c=c)
    keep_file(na=correspondence, c=c)
    keep_file(na=heng_len, c=c)
    keep_file(na=heng_gff, c=c)
    keep_file(na=shu_len, c=c)
    keep_file(na=shu_gff, c=c)

    shu_name = shu_len.name.split('.')[0]
    heng_name = heng_len.name.split('.')[0]

    zu_correspondence_mc_run_tools(place=c, shu_name=shu_name, heng_name=heng_name)
    files = f"*new.blast *.mc.*.txt *_corr.png *.corr.txt"
    return zip_file(request, c, files)


# blast_match_run
# def blast_match_run(request):
#
#     patten = str(request.POST.get('patten', None))
#     myFile1 = request.FILES.get('file1', None)
#     species_name = str(request.POST.get("species_data", None))
#
#     e_value = str(request.POST.get('e_value', None))
#     sco = str(request.POST.get('score_1', None))
#     iden = str(request.POST.get('identity_1', None))
#
#     email = str(request.POST.get('email', None))
#     nucl_or_prot = "prot" if patten == 'blastp' else "nucl"
#
#     if myFile1 is None:
#         return render(request, 'blast_match.html')
#     else:
#         c = name_set()
#         keep_email(e=c, address=email)
#
#         myFile1.name = '1.fasta'
#         keep_file(na=myFile1, c=c)
#
#         blast_match_run_tools(place=c, patten=patten, species_data=species_name, e=e_value, email=email, score=sco, identity=iden, nucl_or_prot=nucl_or_prot)
#         return render(request, '../templates/successful.html')

# blastp 序列比对
def blast_match_run(request):
    com_seq = request.POST.get("SEQUENCE", None)
    patten = request.POST.get("patten", None)
    species_data = request.POST.get("species_data", None)
    myFile1 = request.FILES.get("file1", None)

    e_value = str(request.POST.get('e_value', None))
    sco = request.POST.get('score_1', None)
    iden = request.POST.get('identity_1', None)
    email = request.POST.get("email", None)
    nucl_or_prot = "prot" if patten == 'blastp' else "nucl"

    if com_seq and myFile1:
        return render(request, 'blast_match.html')
    elif not com_seq and myFile1 is None:
        return render(request, 'blast_match.html')
    if com_seq:
        c = name_set()
        keep_email(e=c, address=email)

        myFile1.name = '1.fasta'
        myFile1.write(com_seq)
        keep_file(na=myFile1, c=c)

        blast_match_run_tools(place=c, patten=patten, species_data=species_data, e=e_value, email=email, score=sco,
                              identity=iden, nucl_or_prot=nucl_or_prot)
        results = []
        file_path = os.path.join(f"{path_get}/file_keep/{c}",
                                 f"result_2.fasta")
        blast_records = NCBIXML.parse(open(file_path))
        for record in blast_records:
            for alignment in record.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect < float(e_value) and hsp.score > int(
                            sco) and hsp.identities / hsp.align_length > float(iden):
                        results.append({
                            'query': record.query,
                            'hit': alignment.title,
                            'e_value': hsp.expect,
                            'sco': hsp.score,
                            'iden': hsp.identities / hsp.align_length
                        })
        return render(request, '../templates/blast_results.html',{'results': results})


# file_merge
def file_merge_run(request):
    file = request.FILES.getlist("file", None)
    if file is None:
        return render(request, '../templates/file_merge.html')
    c = name_set()
    keep_files(na=file, c=c)
    file_merge_run_tools(place=c)
    files = f'result.txt'
    return zip_file(request, c, files)


# find_replace
def find_replace_run(request):
    file_up = request.FILES.get("file", None)
    old_name = request.POST.get("old_name", None)
    new_name = request.POST.get("new_name", None)
    
    if file_up is None:
        return render(request, '../templates/find_replace.html')
    
    c = name_set()
    
    file_up.name = "upload.txt"
    keep_file(na=file_up, c=c)
    find_replace_run_tools(place=c, old_name=old_name, new_name=new_name)
    files = f'result.txt'
    return zip_file(request, c, files)


# Extract_column
def extract_column_run(request):
    row = request.FILES.get("row", None)
    row_num = request.POST.get("row_num", None)
    if row is None:
        return render(request, '../templates/extract_row.html')
    c = name_set()
    row_name = row.name.split(".")[0]
    row_last = row.name.split(".")[1]
    keep_file(na=row, c=c)
    extr_row_run(place=c,  row_num=row_num, row_name=row_name, row_last=row_last)
    files = f'{row_name}.new.{row_last}'
    return zip_file(request, c, files)



# duplicate_removal_run
def duplicate_removal_run(request):
    file = request.FILES.get("file", None)
    if file is None:
        return render(request, '../templates/quchong.html')
    c = name_set()
    file.name = '1.fasta'
    keep_file(na=file, c=c)
    quchong_run(place=c)
    files = f'new.fasta'
    return zip_file(request, c, files)


# formatTofasta_run
def formatTofasta_run(request):
    format = request.FILES.get("file1", None)
    patten = request.POST.get("patten", None)
    patten_end = request.POST.get("patten_end", None)

    if format is None:
        return render(request, '../templates/formatTofasta.html')
    c = name_set()
    file_name = format.name.split(".")[0]
    file_last = format.name.split(".")[1]
    keep_file(na=format, c=c)

    format_fasta_run(place=c, file_name=file_name, patten=patten, patten_end=patten_end, file_last=file_last)
    files = f'{file_name}.{patten_end}'
    return zip_file(request, c, files)


# blast
def blast_run(request):
    patten = request.POST.get('patten', None)
    myFile1 = request.FILES.get('file1', None)
    myFile2 = request.FILES.get('file2', None)
    e_value = str(request.POST.get('e_value', None))
    sco = request.POST.get('score_1', None)
    iden = request.POST.get('identity_1', None)
    nucl_or_prot = "prot" if patten == 'blastp' else "nucl"

    if myFile1 is None or myFile2 is None:
        return render(request, 'f_blast.html')
    c = name_set()

    myFile1_name = myFile1.name.split(".")[0]
    myFile2_name = myFile2.name.split(".")[0]
    myFile1.name = '1.fasta'
    myFile2.name = '2.fasta'
    keep_file(na=myFile1, c=c)
    keep_file(na=myFile2, c=c)

    blast_run_tools(place=c, patten=patten, e=e_value, score=sco, identity=iden, myFile1=myFile1_name,
                   myFile2=myFile2_name, nucl_or_prot=nucl_or_prot)

    files = f"{myFile1_name}_{myFile2_name}.fasta sequence.txt"
    return zip_file(request, c, files)



# MCScanX
def mcscanx_run(request):
    myFile1 = request.FILES.get("file1", None)
    myFile2 = request.FILES.get("file2", None)
    # email = request.POST.get('email', None)

    if myFile1 is None or myFile2 is None:
        return render(request, '../templates/mcscanx.html')

    c = name_set()
    file_name = myFile1.name.split(".")[0]

    keep_file(na=myFile1, c=c)
    keep_file(na=myFile2, c=c)

    mcscanx_run_tools(place=c, file_name=file_name)
    files = f'{file_name}.html {file_name}.collinearity {file_name}.tandem gene_classifier.txt'
    return zip_file(request, c, files)



# Colinearscan_run
def colinearscan_run(request):
    blast = request.FILES.get("blast", None)
    gff1 = request.FILES.get("gff1", None)
    gff2 = request.FILES.get("gff2", None)
    e_value = str(request.POST.get('e_value', None))
    score = request.POST.get('score', None)
    hitnum = request.POST.get('hitnum', None)
    pos_order = str(request.POST.get('pos_order', None))
    cdsvchr = request.POST.get('cdsvchr', None)

    if blast is None or gff1 is None or gff2 is None:
        return render(request, '../templates/colinearscan.html')
    c = name_set()

    keep_file(na=blast, c=c)
    keep_file(na=gff1, c=c)
    keep_file(na=gff2, c=c)
    file_name = blast.name.split('.')[0]

    colinearscan_run_tools(place=c, score=score, e_value=e_value, hitnum=hitnum, pos_order=pos_order, cdsvchr=cdsvchr, blast_name=blast.name, gff1_name=gff1.name, gff2_name=gff2.name, file_name=file_name)
    files = 'block pair'
    return zip_file(request, c, files)


# ks_calculate_run
def zu_ks_calculate_run(request):
    cds1 = request.FILES.get('cds1', None)
    cds2 = request.FILES.get('cds2', None)
    block = request.FILES.get('block', None)
    if cds1 is None or cds2 is None or block is None:
        return render(request, '../tools/templates/zu_ks_calculate.html')
    c = name_set()

    keep_file(na=cds1, c=c)
    keep_file(na=cds2, c=c)
    keep_file(na=block, c=c)
    zu_ks_calculate_run_tools(place=c)

    files = f"ks/*"
    return zip_file(request, c, files)


# wgdi 绘制点图
def dotplot_run(request):
    # 五个文件
    blast = request.FILES.get('blast', None)
    heng_len = request.FILES.get('heng_len', None)
    shu_len = request.FILES.get('shu_len', None)
    heng_gff = request.FILES.get('heng_gff', None)
    shu_gff = request.FILES.get('shu_gff', None)
    # 四种参数-值
    evalue = str(request.POST.get('evalue', None))
    score = request.POST.get('score', None)
    # 需要保存的物种名称
    heng_species = str(request.POST.get('heng_species', None))
    shu_species = str(request.POST.get('shu_species', None))
    patten = request.POST.get('patten', None)
    email = request.POST.get('email', None)

    if blast is None or heng_len is None or shu_len is None or heng_gff is None or shu_gff is None:
        return render(request, 'dotplot.html')
    else:
        c = name_set()
        keep_email(e=c, address=email)

        blast.name = 'diamond.fasta'
        shu_gff.name = '11.gff'
        heng_gff.name = '22.gff'
        shu_len.name = '11.len'
        heng_len.name = '22.len'

        keep_file(na=blast, c=c)
        keep_file(na=shu_gff, c=c)
        keep_file(na=heng_gff, c=c)
        keep_file(na=shu_len, c=c)
        keep_file(na=heng_len, c=c)

        dotplot_run(place=c, email=email, evalue=evalue, score=score,
                    heng_species=heng_species, shu_species=shu_species, patten=patten
                    )
        return render(request, 'successful.html')


# wgdi共线性分析
def wgdimcs_run(request):
    # 五个文件
    blast = request.FILES.get('blast', None)
    heng_len = request.FILES.get('heng_len', None)
    shu_len = request.FILES.get('shu_len', None)
    heng_gff = request.FILES.get('heng_gff', None)
    shu_gff = request.FILES.get('shu_gff', None)
    # 四种参数-值
    evalue = str(request.POST.get('evalue', None))
    score = request.POST.get('score', None)
    email = request.POST.get('email', None)

    if blast is None or heng_len is None or shu_len is None or heng_gff is None or shu_gff is None:
        return render(request, 'wgdimcs.html')
    else:
        c = name_set()
        keep_email(e=c, address=email)

        blast.name = 'diamond.fasta'
        shu_gff.name = '11.gff'
        heng_gff.name = '22.gff'
        shu_len.name = '11.len'
        heng_len.name = '22.len'

        keep_file(na=blast, c=c)
        keep_file(na=shu_gff, c=c)
        keep_file(na=heng_gff, c=c)
        keep_file(na=shu_len, c=c)
        keep_file(na=heng_len, c=c)

        wgdimcs_run(place=c, email=email, evalue=evalue, score=score)
        return render(request, 'successful.html')


# wgdi 计算kaks
def wgdikaks_run(request):
    # 五个文件
    pep = request.FILES.get('pep', None)
    cds = request.FILES.get('cds', None)
    colinearity = request.FILES.get('colinearity', None)
    email = request.POST.get('email', None)

    if colinearity is None or cds is None or pep is None:
        return render(request, 'wgdikaks.html')
    else:
        c = name_set()
        keep_email(e=c, address=email)

        pep.name = 'pep.fasta'
        cds.name = 'cds.fasta'
        colinearity.name = 'colinearity.txt'

        keep_file(na=pep, c=c)
        keep_file(na=cds, c=c)
        keep_file(na=colinearity, c=c)

        wgdikaks_run(place=c, email=email)
        return render(request, 'successful.html')


# wgdi 绘制kaks点图
def wgdikaks_dot_run(request):
    # 三个文件
    blockinfo = request.FILES.get('blockinfo', None)
    heng_len = request.FILES.get('heng_len', None)
    shu_len = request.FILES.get('shu_len', None)
    # 需要保存的物种名称
    heng_species = str(request.POST.get('heng_species', None))
    shu_species = str(request.POST.get('shu_species', None))
    email = request.POST.get('email', None)

    if blockinfo is None or heng_len is None or shu_len is None:
        return render(request, 'wgdikaks_dot.html')
    else:
        c = name_set()
        keep_email(e=c, address=email)

        blockinfo.name = 'blockinfo.csv'
        heng_len.name = '11.len'
        shu_len.name = '22.len'

        keep_file(na=blockinfo, c=c)
        keep_file(na=heng_len, c=c)
        keep_file(na=shu_len, c=c)

        wgdikaks_dot_run(place=c, email=email, heng_species=heng_species, shu_species=shu_species)
        return render(request, 'successful.html')

#------------------------------------------------
# 物种介绍
def Fex(request):
    return render(request, 'introduce/Fex.html')

def Fpe(request):
    return render(request, 'introduce/Fpe.html')

def Fam(request):
    return render(request, 'introduce/Fam.html')

def Fsu(request):
    return render(request, 'introduce/Fsu.html')

def Jsa(request):
    return render(request, 'introduce/Jsa.html')

def Ofr(request):
    return render(request, 'introduce/Ofr.html')

def Oeu(request):
    return render(request, 'introduce/Oeu.html')

def Sob(request):
    return render(request, 'introduce/Sob.html')

def Fph(request):
    return render(request, 'introduce/Fph.html')

def Vvi(request):
    return render(request, 'introduce/Vvi.html')

def Adi(request):
    return render(request, 'introduce/Adi.html')

#-------------------------------------------------
def Cba(request):
    return render(request, 'introduce/Cba.html')

def Cbi(request):
    return render(request, 'introduce/Cbi.html')

def Cfl(request):
    return render(request, 'introduce/Cfl.html')

def Cha(request):
    return render(request, 'introduce/Cha.html')

def Cmad(request):
    return render(request, 'introduce/Cmad.html')

def Cmar(request):
    return render(request, 'introduce/Cmar.html')

def Cmi(request):
    return render(request, 'introduce/Cmi.html')

def Cob(request):
    return render(request, 'introduce/Cob.html')

def Cpo(request):
    return render(request, 'introduce/Cpo.html')

def Cse(request):
    return render(request, 'introduce/Cse.html')

#-------------------------------------------------
def Dcr(request):
    return render(request, 'introduce/Dcr.html')

def Feg(request):
    return render(request, 'introduce/Feg.html')

def Feu(request):
    return render(request, 'introduce/Feu.html')

def Fis(request):
    return render(request, 'introduce/Fis.html')

def Fra(request):
    return render(request, 'introduce/Fra.html')

def Fsa(request):
    return render(request, 'introduce/Fsa.html')

def Hin(request):
    return render(request, 'introduce/Hin.html')

def Hpa(request):
    return render(request, 'introduce/Hpa.html')

def Hsa(request):
    return render(request, 'introduce/Hsa.html')
#-------------------------------------------------
def Jab(request):
    return render(request, 'introduce/Jab.html')

def Jco(request):
    return render(request, 'introduce/Jco.html')

def Jtr(request):
    return render(request, 'introduce/Jtr.html')

def Lja(request):
    return render(request, 'introduce/Lja.html')

def Lmo(request):
    return render(request, 'introduce/Lmo.html')

def Lse(request):
    return render(request, 'introduce/Lse.html')

def Lvu(request):
    return render(request, 'introduce/Lvu.html')

def Maf(request):
    return render(request, 'introduce/Maf.html')

def Mne(request):
    return render(request, 'introduce/Mne.html')

def Msc(request):
    return render(request, 'introduce/Msc.html')

def Msm(request):
    return render(request, 'introduce/Msm.html')

def Msp(request):
    return render(request, 'introduce/Msp.html')

#-------------------------------------------------
def Nac(request):
    return render(request, 'introduce/Nac.html')

def Nal(request):
    return render(request, 'introduce/Nal.html')

def Nam(request):
    return render(request, 'introduce/Nam.html')

def Nap(request):
    return render(request, 'introduce/Nap.html')

def Nar(request):
    return render(request, 'introduce/Nar.html')

def Nco(request):
    return render(request, 'introduce/Nco.html')

def Ncu(request):
    return render(request, 'introduce/Ncu.html')

def Nem(request):
    return render(request, 'introduce/Nem.html')

def Nip(request):
    return render(request, 'introduce/Nip.html')

def Nla(request):
    return render(request, 'introduce/Nla.html')

def Nlo(request):
    return render(request, 'introduce/Nlo.html')

def Nmi(request):
    return render(request, 'introduce/Nmi.html')

#-------------------------------------------------
def Oam(request):
    return render(request, 'introduce/Oam.html')

def Ome(request):
    return render(request, 'introduce/Ome.html')

def Osu(request):
    return render(request, 'introduce/Osu.html')

def Pan(request):
    return render(request, 'introduce/Pan.html')

def Pap(request):
    return render(request, 'introduce/Pap.html')

def Paz(request):
    return render(request, 'introduce/Paz.html')

def Pex(request):
    return render(request, 'introduce/Pex.html')

def Pha(request):
    return render(request, 'introduce/Pha.html')

def Pla(request):
    return render(request, 'introduce/Pla.html')

def Pme(request):
    return render(request, 'introduce/Pme.html')

def Sal(request):
    return render(request, 'introduce/Sal.html')

def Sar(request):
    return render(request, 'introduce/Sar.html')

def Sca(request):
    return render(request, 'introduce/Sca.html')

def Sma(request):
    return render(request, 'introduce/Sma.html')

def Str(request):
    return render(request, 'introduce/Str.html')

#------------------------------------------------
def Cax(request):
    return render(request, 'introduce/Cax.html')

def Cbr(request):
    return render(request, 'introduce/Cbr.html')

def Cdo(request):
    return render(request, 'introduce/Cdo.html')

def Cho(request):
    return render(request, 'introduce/Cho.html')

def Cim(request):
    return render(request, 'introduce/Cim.html')

def Cpan(request):
    return render(request, 'introduce/Cpan.html')

def Cpu(request):
    return render(request, 'introduce/Cpu.html')

def Cqu(request):
    return render(request, 'introduce/Cqu.html')

def Cra(request):
    return render(request, 'introduce/Cra.html')

def Cre(request):
    return render(request, 'introduce/Cre.html')

def Cod(request):
    return render(request, 'introduce/Cod.html')

def Cpar(request):
    return render(request, 'introduce/Cpar.html')

def Csu(request):
    return render(request, 'introduce/Csu.html')

def Fan(request):
    return render(request, 'introduce/Fan.html')

def Fgi(request):
    return render(request, 'introduce/Fgi.html')

def Fja(request):
    return render(request, 'introduce/Fja.html')

def Fko(request):
    return render(request, 'introduce/Fko.html')

def Fna(request):
    return render(request, 'introduce/Fna.html')

def Fov(request):
    return render(request, 'introduce/Fov.html')

#-------------------------------------------------
def Fap(request):
    return render(request, 'introduce/Fap.html')

def Fbe(request):
    return render(request, 'introduce/Fbe.html')

def Fbu(request):
    return render(request, 'introduce/Fbu.html')

def Fca(request):
    return render(request, 'introduce/Fca.html')

def Fch(request):
    return render(request, 'introduce/Fch.html')

def Fcu(request):
    return render(request, 'introduce/Fcu.html')

def Fdi(request):
    return render(request, 'introduce/Fdi.html')

def Fla(request):
    return render(request, 'introduce/Fla.html')

def For(request):
    return render(request, 'introduce/For.html')

def Fqu(request):
    return render(request, 'introduce/Fqu.html')

def Ftr(request):
    return render(request, 'introduce/Ftr.html')

#------------------------------------------------
def Jad(request):
    return render(request, 'introduce/Jad.html')

def Jal(request):
    return render(request, 'introduce/Jal.html')

def Jau(request):
    return render(request, 'introduce/Jau.html')

def Jbr(request):
    return render(request, 'introduce/Jbr.html')

def Jcu(request):
    return render(request, 'introduce/Jcu.html')

def Jla(request):
    return render(request, 'introduce/Jla.html')

def Jma(request):
    return render(request, 'introduce/Jma.html')

def Jne(request):
    return render(request, 'introduce/Jne.html')

def Jpa(request):
    return render(request, 'introduce/Jpa.html')
#------------------------------------------------

def Lau(request):
    return render(request, 'introduce/Lau.html')

def Lco(request):
    return render(request, 'introduce/Lco.html')

def Lex(request):
    return render(request, 'introduce/Lex.html')

def Lgr(request):
    return render(request, 'introduce/Lgr.html')

def Lli(request):
    return render(request, 'introduce/Lli.html')

def Lob(request):
    return render(request, 'introduce/Lob.html')

def Lqu(request):
    return render(request, 'introduce/Lqu.html')

def Lsi(request):
    return render(request, 'introduce/Lsi.html')

def Lun(request):
    return render(request, 'introduce/Lun.html')
#------------------------------------------------
def Nsa(request):
    return render(request, 'introduce/Nsa.html')

def Nba(request):
    return render(request, 'introduce/Nba.html')

def Nbr(request):
    return render(request, 'introduce/Nbr.html')

def Nin(request):
    return render(request, 'introduce/Nin.html')

def Npe(request):
    return render(request, 'introduce/Npe.html')

def Nsp(request):
    return render(request, 'introduce/Nsp.html')

def Nte(request):
    return render(request, 'introduce/Nte.html')
#------------------------------------------------
def Och(request):
    return render(request, 'introduce/Och.html')

def Oex(request):
    return render(request, 'introduce/Oex.html')

def Oja(request):
    return render(request, 'introduce/Oja.html')

def Ope(request):
    return render(request, 'introduce/Ope.html')

def Oro(request):
    return render(request, 'introduce/Oro.html')

def Osc(request):
    return render(request, 'introduce/Osc.html')

def Owe(request):
    return render(request, 'introduce/Owe.html')

def Oyu(request):
    return render(request, 'introduce/Oyu.html')

def Ocy(request):
    return render(request, 'introduce/Ocy.html')

def Oen(request):
    return render(request, 'introduce/Oen.html')

def Ove(request):
    return render(request, 'introduce/Ove.html')

#-------------------------------------------------
def Sem(request):
    return render(request, 'introduce/Sem.html')

def Sju(request):
    return render(request, 'introduce/Sju.html')

def Spi(request):
    return render(request, 'introduce/Spi.html')

def Spu(request):
    return render(request, 'introduce/Spu.html')

def Sre(request):
    return render(request, 'introduce/Sre.html')

def Ssw(request):
    return render(request, 'introduce/Ssw.html')

def Sti(request):
    return render(request, 'introduce/Sti.html')

def Sto(request):
    return render(request, 'introduce/Sto.html')

def Svi(request):
    return render(request, 'introduce/Svi.html')

def Swo(request):
    return render(request, 'introduce/Swo.html')


#-------------------------------------------------
def zu_blast_dotplot(request):
    return render(request, 'zu_blast_dotplot.html')

def zu_block_dotplot(request):
    return render(request, 'zu_block_dotplot.html')

def zu_blast_dotplot_run(request):
    blast = request.FILES.get('blast', None)
    shu_len = request.FILES.get('shu_len', None)
    shu_gff = request.FILES.get('shu_gff', None)
    heng_len = request.FILES.get('heng_len', None)
    heng_gff = request.FILES.get('heng_gff', None)

    if blast is None or heng_len is None or shu_len is None or heng_gff is None or shu_gff is None:
        return render(request, '../tools/templates/zu_blast_dotplot.html')
    c = name_set()

    shu_len_name = shu_len.name.split(".")[0]
    heng_len_name = heng_len.name.split(".")[0]

    keep_file(na=blast, c=c)
    keep_file(na=heng_len, c=c)
    keep_file(na=shu_len, c=c)
    keep_file(na=heng_gff, c=c)
    keep_file(na=shu_gff, c=c)

    zu_blast_dotplot_run_tools(place=c, shu_len_name=shu_len_name, heng_len_name=heng_len_name)
    files = f"*.png"
    return zip_file(request, c, files)


def zu_block_dotplot_run(request):
    blast = request.FILES.get('blast', None)
    block = request.FILES.get('block', None)
    shu_len = request.FILES.get('shu_len', None)
    shu_gff = request.FILES.get('shu_gff', None)
    heng_len = request.FILES.get('heng_len', None)
    heng_gff = request.FILES.get('heng_gff', None)
    block_num = request.POST.get('block_num')

    if blast is None or heng_len is None or shu_len is None or heng_gff is None or shu_gff is None or block is None:
        return render(request, '../tools/templates/zu_block_dotplot.html')
    c = name_set()

    shu_len_name = shu_len.name.split(".")[0]
    heng_len_name = heng_len.name.split(".")[0]

    keep_file(na=blast, c=c)
    keep_file(na=block, c=c)
    keep_file(na=heng_len, c=c)
    keep_file(na=shu_len, c=c)
    keep_file(na=heng_gff, c=c)
    keep_file(na=shu_gff, c=c)

    zu_block_dotplot_run_tools(place=c, shu_len_name=shu_len_name, heng_len_name=heng_len_name, block_num=block_num)
    files = f"*.png"
    return zip_file(request, c, files)


def zu_ks_dotplot_run(request):
    blast = request.FILES.get('blast', None)
    block = request.FILES.get('block', None)
    ks = request.FILES.get('ks', None)
    shu_len = request.FILES.get('shu_len', None)
    shu_gff = request.FILES.get('shu_gff', None)
    heng_len = request.FILES.get('heng_len', None)
    heng_gff = request.FILES.get('heng_gff', None)

    if blast is None or heng_len is None or shu_len is None or heng_gff is None or shu_gff is None or block is None or ks is None:
        return render(request, '../tools/templates/zu_ks_dotplot.html')
    c = name_set()

    shu_len_name = shu_len.name.split(".")[0]
    heng_len_name = heng_len.name.split(".")[0]

    keep_file(na=blast, c=c)
    keep_file(na=block, c=c)
    keep_file(na=ks, c=c)
    keep_file(na=heng_len, c=c)
    keep_file(na=shu_len, c=c)
    keep_file(na=heng_gff, c=c)
    keep_file(na=shu_gff, c=c)

    zu_ks_dotplot_run_tools(place=c, shu_len_name=shu_len_name, heng_len_name=heng_len_name)
    files = f"*.png"
    return zip_file(request, c, files)



def zu_ks_calculate(request):
    return render(request, 'zu_ks_calculate.html')

def zu_ks_distribution(request):
    return render(request, 'zu_ks_distribution.html')
    
# ks_distribution
def zu_ks_distribution_run(request):
    file = request.FILES.get('file', None)
    if file is None:
        return render(request, '../templates/zu_ks_distribution.html')
    c = name_set()
    keep_file(na=file, c=c)
    zu_ks_distribution_run_tools(place=c)
    files = f"ksargs.png"
    return zip_file(request, c, files)

def zu_ks_dotplot(request):
    return render(request, 'zu_ks_dotplot.html')

def zu_correspondence_mc(request):
    return render(request, 'zu_correspondence_mc.html')

def zu_retention(request):
    return render(request, 'zu_retention.html')


def zu_loss(request):
    return render(request, 'zu_loss.html')


def zu_pindex(request):
    return render(request, 'zu_pindex.html')


def blast_results_run(request):
    if request.method == 'POST':
        # Parse form data
        subroutine = request.POST.get('subroutine')
        target_file = request.FILES['target_file']
        query_file = request.FILES['query_file']
        evalue = request.POST.get('evalue')
        score = request.POST.get('score')
        identity = request.POST.get('identity')
        email = request.POST.get('email')
        nucl_or_prot = "prot" if subroutine == 'blastp' else "nucl"
        if target_file is None or query_file is None:
            return render(request, 'f_blast.html')
        else:
            c = name_set()
            keep_email(e=c, address=email)

            keep_file(na=target_file, c=c)
            keep_file(na=query_file, c=c)

            blast_run_tools_re(place=c, patten=subroutine, e=evalue, email=email, score=score, identity=identity, myFile1=target_file.name, myFile2=query_file.name, nucl_or_prot=nucl_or_prot)


            # Generate results table
            results = []
            # output_file = f"{c}/output_file.txt"
            # Construct full path to file
            file_path = os.path.join(f"{path_get}/file_keep/{c}",
                                     f"result_2.fasta")
            blast_records = NCBIXML.parse(open(file_path))
            for record in blast_records:
                for alignment in record.alignments:
                    for hsp in alignment.hsps:
                        if hsp.expect < float(evalue) and hsp.score > int(
                                score) and hsp.identities / hsp.align_length > float(identity):
                            results.append({
                                'query': record.query,
                                'hit': alignment.title,
                                'evalue': hsp.expect,
                                'score': hsp.score,
                                'identity': hsp.identities / hsp.align_length
                            })
            # Render results template
            return render(request, 'blast_results.html', {'results': results})
    else:
        return render(request, 'f_blast.html')


def file_merge_run(request):
    file = request.FILES.getlist("file", None)
    if file is None:
        return render(request, '../templates/file_merge.html')
    c = name_set()
    keep_files(na=file, c=c)
    file_merge_run_tools(place=c)
    files = f'result.txt'
    return zip_file(request, c, files)


def zu_pindex_run(request):
    mc_files = request.FILES.getlist("mc_files", None)
    sliding_window = request.POST.get('sliding_window')
    buchang = request.POST.get('buchang')
    sigema_start = request.POST.get('sigema_start')
    sigema_end = request.POST.get('sigema_end')
    if mc_files is None:
        return render(request, '../templates/zu_pindex.html')
    c = name_set()
    keep_files(na=mc_files, c=c)

    zu_pindex_run_tools(place=c, sliding_window=sliding_window, buchang=buchang, sigema_start=sigema_start, sigema_end=sigema_end)
    files = f"output pindex_result.txt"
    return zip_file(request, c, files)


def zu_retention_run(request):
    mc_files = request.FILES.getlist("mc_files", None)
    if mc_files is None:
        return render(request, '../templates/zu_retention.html')
    c = name_set()
    keep_files(na=mc_files, c=c)
    zu_retention_run_tools(place=c)
    files = f"output"
    return zip_file(request, c, files)


def zu_loss_run(request):
    mc_files = request.FILES.getlist("mc_files", None)
    if mc_files is None:
        return render(request, '../templates/zu_loss.html')
    c = name_set()
    keep_files(na=mc_files, c=c)
    zu_loss_run_tools(place=c)
    files = f"output"
    return zip_file(request, c, files)

