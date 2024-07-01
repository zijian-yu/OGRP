#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author :yuzijian1010@163.com
# @Time : 2023/12/4 16:41
# @Last time: 2023/12/4 16:41
import os
import re
import time
import random
import shutil
import string
import pymysql
import subprocess
from .email import youjian
from Bio import SeqIO
from django.http import HttpResponse
from django.core.files import File
from django.shortcuts import render


path_get = os.getcwd()


# 在文件夹内 创建文件夹
def keep_in_file(na, c, fg=None):
    cmd = '''
        cd %s/file_keep/%s
        mkdir all_file
    ''' % (path_get, c)
    os.system(cmd)

    with open('%s' % os.path.join(f'{path_get}/file_keep/{c}/all_file/', na.name), 'wb') as f:
        for chunk1 in na.chunks():
            f.write(chunk1)
    f.close()


# 保存单个文件
def keep_file(na, c, fg=None):
    if fg is None:
        pass
    else:
        nam = na.name.split(".")
        na.name = nam[0]

    # 被我保存到本地啦，保存到哪里随意啦
    with open(f"{path_get}/file_keep/{c}/{na.name}", 'wb+') as f:
        for chunk1 in na.chunks():
            f.write(chunk1)


# 创建conf配置文件
def text_create(name, msg, place):
    desktop_path = f"{path_get}/file_keep/{place}/"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.conf'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world!
    file.close()


# 保存多个文件
# def keep_files(na, c, fg=None, ret_files=None):
#     cmd = f'''
#         cd {path_get}/file_keep/{c}
#         mkdir orthomcl
#     '''
#     os.system(cmd)
#
#     for file in na:
#         with open('%s' % os.path.join(f'{path_get}/file_keep/{c}/orthomcl/', file.name), 'wb') as f:
#             for i in file.chunks():
#                 f.write(i)
def keep_files(na, c):
    destination_path = os.path.join(path_get, 'file_keep', c, 'orthomcl')
    os.makedirs(destination_path, exist_ok=True)

    for file in na:
        destination_file_path = os.path.join(destination_path, file.name)
        with open(destination_file_path, 'wb') as destination_file, file.open('rb') as source_file:
            shutil.copyfileobj(source_file, destination_file)


# 此模块用于检查 文件是否存在 （b，c，d 参数未补全）
#     e ：文件夹名字
def name_check(e):
    """
    此模块用于检查 文件是否存在 （b，c，d 参数未补全）
    e ：文件夹名字
    """
    global path_get

    a = os.path.isfile('/home/a123123/PycharmProjects/untitled2/file_keep/%s/1.FASTA' % e)
    b = os.path.isfile('/home/a123123/PycharmProjects/untitled2/file_keep/%s/email.txt' % e)
    c = os.path.isfile('/home/a123123/PycharmProjects/untitled2/file_keep/%s/email.txt' % e)
    d = os.path.isfile('/home/a123123/PycharmProjects/untitled2/file_keep/%s/email.txt' % e)
    n = ''
    if b:
        n = '1.FASTA'
    elif a:
        n = 'd'
    elif a:
        n = 'd'
    elif a:
        n = 'd'
    return n


def name_set():
    """ 在file_keep中创建文件夹
    :return: c 随机文件夹名字
    """
    c = ''.join(random.sample(string.digits, 9))
    os.mkdir(f"file_keep/{c}")
    return c


# 保存邮件地址
def keep_email(e, address):
    with open(f'{path_get}/file_keep/{e}/email.txt', 'w') as f:
        f.write(address)


def read_email(place):
    global path_get
    with open(f'{path_get}/file_keep/{place}/email.txt', 'r+') as f:
        return f.read()
# ================================= gfca start  =============================================


# index 保存邮件地址
def keep_email_index(place, name, email, message):
    with open(f'{path_get}/file_keep/{place}/advise.txt', 'w+') as f:
        f.write(name + '\n')
        f.write(email + '\n')
        f.write(message + '\n')

    g = f'{path_get}/file_keep/{place}/advise.txt'
    youjian(a="aboxofchocolates@126.com", b=g, place=place)


# blast_初筛
def blast_choose(place, myFile1, myFile2, identity, score):
    blast_file = open(f'{path_get}/file_keep/{place}/{myFile1}_{myFile2}.fasta', 'w')
    sequence_file = open(f'{path_get}/file_keep/{place}/sequence.txt', 'w')
    pbl_fasta = open(f'{path_get}/file_keep/{place}/result_2.fasta', 'r')
    gather = set()
    for line in pbl_fasta.readlines():
        ind, sco = line.split()[2], line.split()[11]
        if float(ind) >= float(identity):
            if float(sco) >= float(score):
                blast_file.write(line)
                # sequence = line.split()[1]
                gather.add(line.split()[1])
    for line in gather:
        sequence_file.write(line + '\n')


# blast
def blast_run_tools(place, patten, e, score, identity, myFile1, myFile2, nucl_or_prot):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        makeblastdb -in 1.fasta -dbtype {nucl_or_prot} -parse_seqids -out dbname
        {patten} -query 2.fasta -db dbname -outfmt 6 -evalue {e} -out result_2.fasta -num_threads 8
    """
    os.system(cmd)
    blast_choose(place=place, myFile1=myFile1, myFile2=myFile2, identity=identity, score=score)


# blast
def blast_run_tools_re(place, patten, e, email, score, identity, myFile1, myFile2, nucl_or_prot):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        makeblastdb -in {myFile1} -dbtype {nucl_or_prot} -parse_seqids -out dbname
        {patten} -query {myFile2} -db dbname -outfmt 5 -evalue {e} -out result_2.fasta -num_threads 8
    """
    os.system(cmd)

    # blast_choose(place=place, myFile1=myFile1, myFile2=myFile2, identity=identity, score=score)
    # files = f"{myFile1}_{myFile2}.fasta sequence.txt"
    # zip_file(place=place, email=email, files=files)


# blast_初筛_match_blast
def blast_choose_match(place, myFile1, identity, score):
    blast_file = open(f'{path_get}/file_keep/{place}/result_2.fasta', 'w')
    sequence_file = open(f'{path_get}/file_keep/{place}/sequence.txt', 'w')
    pbl_fasta = open(f'{path_get}/file_keep/{place}/{myFile1}', 'r')
    # pbl_fasta = open(f'{path_get}/file_keep/{place}/result_2.fasta', 'r')
    gather = set()
    for line in pbl_fasta.readlines():
        ind, sco = line.split()[2], line.split()[11]
        if float(ind) >= float(identity):
            if float(sco) >= float(score):
                blast_file.write(line)
                # sequence = line.split()[1]
                gather.add(line.split()[1])
    for line in gather:
        sequence_file.write(line + '\n')


# blast_match
def blast_match_run_tools(place, patten, species_data, e, email, score, identity, nucl_or_prot):
    cmd = f"""
source /etc/profile
cd {path_get}/file_keep/{place}
{patten} -query 1.fasta -db /bio/yzj/Web/FGBP/static/blast_match_database/{nucl_or_prot}/{species_data} -outfmt 6 -evalue {e} -out result.txt -num_threads 8 -max_target_seqs 1
    """
    os.system(cmd)

    blast_choose_match(place=place, myFile1="result.txt", identity=identity, score=score)
    g = f'result_2.fasta sequence.txt'
    youjian(a=email, b=g, place=place)
# import os
# import subprocess
# def blast_match_run_tools(place, pattern, species_data, e, email, score, identity, nucl_or_prot):
#     # 设置路径
#     result_path = os.path.join(path_get, 'file_keep', place)
#     database_path = os.path.join('/bio/yzj/Web/FGBP/static/blast_match_database', nucl_or_prot, species_data)

#     # 构建BLAST命令
#     cmd = f"""
#         source /etc/profile
#         cd {result_path}
#         {pattern} -query 1.fasta -db {database_path} -outfmt 6 -evalue {e} -out result.txt -num_threads 8 -max_target_seqs 1
#     """

#     try:
#         # 使用subprocess.run执行命令
#         subprocess.run(cmd, shell=True, check=True)

#         # 处理BLAST结果并发送邮件
#         blast_choose_match(place=place, myFile1="result.txt", identity=identity, score=score)
#         attachment_path = 'result_2.fasta sequence.txt'
#         youjian(a=email, b=attachment_path, place=place)

#     except subprocess.CalledProcessError as e:
#         print(f"Error running BLAST command: {e}")
#         # 处理错误，可能记录日志或采取其他措施



# diamond
# def diamond_run_tools(place, patten, e, email, score, identity, myFile1, myFile2):
def diamond_run_tools(place, patten, e, score, identity, myFile1, myFile2):
    cmd = f"""
    source /etc/profile
    cd {path_get}/file_keep/{place}
    diamond makedb --in 1.fasta -d nr
    diamond {patten} -d nr -q 2.fasta -o result_2.fasta -e {e} -b 2.0 --index-chunks 1
"""
    os.system(cmd)
    blast_choose(place=place, myFile1=myFile1, myFile2=myFile2, identity=identity, score=score)
    # files = f"{myFile1}_{myFile2}.fasta sequence.txt"
    # 调用 zip_file 函数
    # return zip_file(place=place, files=files)


# sequence_screening_clas
class sequence_run2(object):
    def __init__(self, place):
        self.id_list = []
        self.place = place

    def new_prot(self):
        new_prot = open(f'{path_get}/file_keep/{self.place}/new_pro.txt', 'w')
        for line in SeqIO.parse(f'{path_get}/file_keep/{self.place}/protein.fasta', 'fasta'):
            if line.id in self.id_list:
                new_prot.write('>' + str(line.id) + '\n' + str(line.seq) + '\n')

    def new_cds(self):
        new_cds = open(f'{path_get}/file_keep/{self.place}/new_cds.txt', 'w')
        for line in SeqIO.parse(f'{path_get}/file_keep/{self.place}/gene.fasta', 'fasta'):
            if line.id in self.id_list:
                new_cds.write('>' + str(line.id) + '\n' + str(line.seq) + '\n')

    def new_gff(self):
        new_gff = open(f'{path_get}/file_keep/{self.place}/new_gff.txt', 'w')
        gff_file = open(f'{path_get}/file_keep/{self.place}/gff.fasta', 'r')
        for line in gff_file:
            gff_id = line.split()[1]
            if gff_id in self.id_list:
                new_gff.write(line)

    def main(self):
        id_file = open(f'{path_get}/file_keep/{self.place}/id.fasta', 'r')
        for line in id_file.readlines():
            self.id_list.append(line.split()[0])

        self.new_prot()
        self.new_cds()
        self.new_gff()


# sequence_screening
def sequence_run(place):
    run = sequence_run2(place)
    run.main()


# hmmer
def hmmer_run_tools(place, e_value):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        hmmsearch -o result.out --noali -E {e_value} hmm_model.fasta hmm_fa.fasta
    """
    os.system(cmd)



# pfam
def pfam_run_tools(place, structure):
    # pfam_scan.pl -fasta 1.fasta -dir ~/../../../../www/tools/PfamScan/pfamdata -outfile pfam.txt
    cmd = f"""
    source /etc/profile
    cd {path_get}/file_keep/{place}
    pfam_scan.pl -fasta 1.fasta -dir ~/../../../../www/tools/PfamScan/pfamdata -outfile pfam.txt
"""
    os.system(cmd)
    # structure_list = list(structure.split(';'))
    # # 根据用户设置的结构域进行筛选
    # file = open(f'{path_get}/file_keep/{place}/pfam.txt', 'r')
    # pfam_new = open(f'{path_get}/file_keep/{place}/pfam_new.txt', 'w')
    # deal = ('#', ' ', '\n')
    # for line in file:
    #     if line.startswith(deal):
    #         continue
    #     structure = line.split()[6]
    #     if structure in structure_list:
    #         pfam_new.write(line)

    # deal = ('#', ' ', '\n')
    # with open(f'{path_get}/file_keep/{place}/pfam.txt', 'r') as file, open(f'{path_get}/file_keep/{place}/pfam_new.txt', 'w') as pfam_new:
    #     structure_list = set(structure.split(';'))
    #     for line in file:
    #         if not line.startswith(deal):
    #             structure = line.split()[6]
    #             if structure in structure_list:
    #                 pfam_new.write(line)

    deal = ('#', ' ', '\n')
    with open(f'{path_get}/file_keep/{place}/pfam.txt', 'r') as file, open(f'{path_get}/file_keep/{place}/pfam_new.txt', 'w') as pfam_new:
        structure_list = set(structure.split(';'))
        pfam_new.writelines(line for line in file if not line.startswith(deal) and line.split()[6] in structure_list)


# meme
def meme_run_tools(place, patten, motif, motif_num, minw, maxw):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        meme 1.fasta -{patten} -oc . -mod {motif} -nmotifs {motif_num} -minw {minw} -maxw {maxw}
    """
    subprocess.run(cmd, shell=True, check=True)


# codonw_run
def codonw_run_tools(place, file_name):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        codonw 1.fasta -all_indices -nomenu {file_name}.out {file_name}.blk
    """
    os.system(cmd)


# cpgfinder_run
def cpgfinder_run_tools(place, island, cg_percent, gc_ratio, myFile_name):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        cpgfinder -f {myFile_name} -l {island} -p {cg_percent} -r {gc_ratio} > cpgfinder_result.txt
    """
    os.system(cmd)



# dupgen_finder_run
def dupgen_finder_run_tools(email, place, patten, target, outgroup):
    if patten == 'general':
        cmd = f"""
source /etc/profile
cd {path_get}/file_keep/{place}
mv {target}* ../programs/dupgen_finder/data/
cd ../programs/dupgen_finder
perl DupGen_finder.pl -i data -t {target} -c {outgroup} -o results
zip -r result.zip results/
mv result.zip {path_get}/file_keep/{place}
rm -rf data/*
rm -rf result*
        """
        os.system(cmd)

        g = f'{path_get}/file_keep/{place}/result.zip'
        youjian(a=email, b=g, place=place)

    else:
        cmd = f"""
source /etc/profile
cd {path_get}/file_keep/{place}
mv {target}* ../programs/dupgen_finder/data/
cd ../programs/dupgen_finder
perl DupGen_finder-unique.pl -i data -t {target} -c {outgroup} -o results
zip -r result.zip results/
mv result.zip {path_get}/file_keep/{place}
rm -rf data/*
rm -rf result*
        """
        os.system(cmd)

        g = f'{path_get}/file_keep/{place}/result.zip'
        youjian(a=email, b=g, place=place)


# cd_hit_run
def cd_hit_run_tools(place, email, similar, patten):
    """
    cd-hit -i db -o db90 -c 0.9 -n 5 -M 16000 -d 0 -T 8
        -i 输入文件，fasta格式的序列
        -o 输出文件路径和名字
        -c 相似性（clustering threshold），0.9表示相似性大于等于90%的为一类
        -n 两两序列进行序列比对时选择的 word size
        -d 0表示使用 fasta 标题中第一个空格前的字段作为序列名字
        -M 16000，16GB RAM
        -T 使用的线程数
        Choose of word size:
        -n 5 for thresholds 0.7 ~ 1.0
        -n 4 for thresholds 0.6 ~ 0.7
        -n 3 for thresholds 0.5 ~ 0.6
        -n 2 for thresholds 0.4 ~ 0.5
        -aL：控制代表序列比对严格程度的参数，默认为0，若设为0.8则表示比对区间要占到代表（长）序列的80%。
        -AL：控制代表序列比对严格程度的参数，默认为99999999，若设为40则表示代表序列的非比对区间要短于40bp。
        -aS：控制短序列比对严格程度的参数，默认为0，若设为0.8则表示比对区间要占到短序列的80%。
        -AS：控制短序列比对严格程度的参数，默认为99999999，若设为40则表示短序列的非比对区间要短于40bp。
    """
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        cd-hit -i 1.fasta -o cd_hit_result.fasta -c {similar} -n {patten} -d 0 -T 1
    """
    os.system(cmd)

    files = 'cd_hit_result.fasta.clstr cd_hit_result.fasta'
    zip_file(email=email, place=place, files=files)


# sequence_aligment
def sequence_aligment_run_tools(place, patten):
    if patten == "clustalw2":
        cmd = f"""
            source /etc/profile
            cd {path_get}/file_keep/{place}
            clustalw2 1.fasta
        """
        os.system(cmd)
    elif patten == "muscle":
        cmd = f"""
            source /etc/profile
            cd {path_get}/file_keep/{place}
            muscle -in 1.fasta -clwout 1.aln
        """
        os.system(cmd)
    elif patten == "mafft":
        cmd = f"""
            source /etc/profile
            cd {path_get}/file_keep/{place}
            mafft --auto 1.fasta > mafft.fasta
        """
        os.system(cmd)


# mcscanx
def mcscanx_run_tools(place, file_name):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        MCScanX {file_name}
        duplicate_gene_classifier {file_name} > gene_classifier.txt
    """
    os.system(cmd)



# colinearscan
def colinearscan_run_tools(place, score, e_value, hitnum, pos_order, cdsvchr, blast_name, gff1_name, gff2_name, file_name):
    # perl ../programs/run_colinearscan.pl ZM-OS.filter.blast 1e-5 0 30 ZM.gff OS.gff order n ZM_OS
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        perl ../programs/run_colinearscan.pl {blast_name} {e_value} {score} {hitnum} {gff1_name} {gff2_name} {pos_order} {cdsvchr} {file_name}
    """
    subprocess.run(cmd, shell=True, check=True)


# orthofinder
def orthfinder_run_tools(place, email, gene_tree, blast, alignment, tree_way, number):
    # -M    基因树推断方法（默认为dendroblast）可选：dendroblast ，msa
    # -S    序列比对使用的程序 （默认为Blast）可选：blast, mmseqs, blast_gz, diamond（推荐使用diamond，比对速度快）
    # # -A    多序列联配方式，该选项仅当 - M    msa    选项时才有效（默认为mafft）可选：muscle, mafft
    # # -T    建树方式，该选项仅当 - M    msa    选项时才有效 （默认为fasttree）可选：iqtree, raxml - ng, fasttree, raxml
    # -I    设定MCL的膨胀系数（默认为1.5）
    if gene_tree == str("msa"):
        cmd = f"""
            source /etc/profile
            cd {path_get}/file_keep/{place}
            orthofinder -f orthomcl -M {gene_tree} -S {blast} -A {alignment} -T {tree_way} -I {number} 
        """
        os.system(cmd)
    else:
        cmd = f"""
            source /etc/profile
            cd {path_get}/file_keep/{place}
            orthofinder -f orthomcl/ -M {gene_tree} -S {blast} -I {number} 
        """
        os.system(cmd)

    cmd2 = f"""
        cd {path_get}/file_keep/{place}/orthomcl/OrthoFinder
        zip -r result.zip *
        mv result.zip ../../
    """
    os.system(cmd2)

    g = f'{path_get}/file_keep/{place}/result.zip'
    youjian(a=email, b=g, place=place)


# paraAT
def paraat_run_tools(place, patten):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        ParaAT.pl -h hom.homologs -n cds.cds -a pep.pep -p ../programs/proc -o result -f {patten}
        cat result/*.{patten} > result.{patten}
    """
    subprocess.run(cmd, shell=True, check=True)


# kaks_calculator
def kaks_calculator_run_tools(place, patten):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        KaKs_Calculator -i kaks.axt -o result_kaks.txt -m {patten}
    """
    subprocess.run(cmd, shell=True, check=True)


# kaks_calculator
def zu_ks_calculate_run_tools(place):
    cmd = f"""
        cd {path_get}/file_keep/{place}
        cp ../programs/run_ks_pro/* .
        mkdir cds
        mv *.cds cds
        mkdir blk
        mv *.txt blk
        mkdir ks
        python3 run_ks.py
    """
    subprocess.run(cmd, shell=True, check=True)


# zu_correspondence_mc_run_tools
def zu_correspondence_mc_run_tools(place, shu_name, heng_name):
    cmd = f"""
        cd {path_get}/file_keep/{place}
        cp ../programs/run_mc/* .
        sed -i 's/\r$//' run_all_1_6.sh
        sh run_all_1_6.sh {shu_name} {heng_name}
    """
    subprocess.run(cmd, shell=True, check=True)


# zu_pindex_run
def zu_pindex_run_tools(place, sliding_window, buchang, sigema_start, sigema_end):
    cmd = f"""
        cd {path_get}/file_keep/{place}
        cp ../programs/p_index.py .
        mkdir output
        python3 p_index.py {sliding_window} {buchang} {sigema_start} {sigema_end} > pindex_result.txt
    """
    subprocess.run(cmd, shell=True, check=True)



def zu_retention_run_tools(place):
    cmd = f"""
        cd {path_get}/file_keep/{place}
        cp ../programs/baoliu.py .
        mkdir output
        python3 baoliu.py
    """
    subprocess.run(cmd, shell=True, check=True)


def zu_loss_run_tools(place):
    cmd = f"""
        cd {path_get}/file_keep/{place}
        cp ../programs/lost.py .
        mkdir output
        python3 lost.py
    """
    subprocess.run(cmd, shell=True, check=True)


def zu_blast_dotplot_run_tools(place, shu_len_name, heng_len_name):
    cmd = f"""
        cd {path_get}/file_keep/{place}
        cp ../programs/corr_dotplot_spc_last.py .
        python3 corr_dotplot_spc_last.py {shu_len_name} {heng_len_name}
    """
    subprocess.run(cmd, shell=True, check=True)


def zu_block_dotplot_run_tools(place, shu_len_name, heng_len_name, block_num):
    cmd = f"""
        cd {path_get}/file_keep/{place}
        cp ../programs/dotplot_block.2400.pd.py .
        python3 dotplot_block.2400.pd.py {shu_len_name} {heng_len_name} {block_num}
    """
    subprocess.run(cmd, shell=True, check=True)

# ks_distribution_run
def zu_ks_distribution_run_tools(place):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        Rscript ../programs/new-ksdistribution.V3.R *.csv ksargs.png 6 5 300
    """
    os.system(cmd)

def zu_ks_dotplot_run_tools(place, shu_len_name, heng_len_name):
    cmd = f"""
        cd {path_get}/file_keep/{place}
        cp ../programs/ks_dot/* .
        python3 run_ks_dot.py {shu_len_name} {heng_len_name}
    """
    subprocess.run(cmd, shell=True, check=True)


# fasttree
def fasttree_run_tools(place, patten):
    if patten == "JTT+CAT":
        cmd = f"""
            source /etc/profile
            cd {path_get}/file_keep/{place}
            FastTree 1.phy > 1.nwk
        """
        os.system(cmd)
    else:
        cmd = f"""
            source /etc/profile
             cd {path_get}/file_keep/{place}
            FastTree -gtr -nt  1.phy > 1.nwk
        """
        os.system(cmd)



# iqtree
def iqtree_run_tools(place, patten, bs_num):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        iqtree2 -s result.phy -m {patten} -bb {bs_num} -bnni -redo
    """
    os.system(cmd)



# phyml
def phyml_run_tools(place, patten, nice, model, frequency, num, small):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        phyml -i 1.phy -d {patten} -b {num} -m {small} -f {frequency} -v e -a e -o {nice}
    """
    os.system(cmd)




# paml_deal
def paml_run_one(patten, small, path, email, place):
    file_data = ""
    codeml_file = open(f'{path_get}/file_keep/paml/{patten}/{small}/codeml.ctl', 'r')
    for line in codeml_file.readlines():
        hh = re.sub(r'\d{9,}', f'{path}', line)
        file_data += hh
    co_new = open(f'{path_get}/file_keep/paml/{patten}/{small}/codeml.ctl', 'w')
    co_new.write(file_data)


# paml
def paml_run_two(place, email, patten, small):
    cmd = f"""
        source /etc/profile
        cd {path_get}/file_keep/{place}
        codeml ../paml/{patten}/{small}/codeml.ctl
    """
    os.system(cmd)

    g = '%s/file_keep/%s/resoult.txt' % (path_get, place)
    youjian(a=email, b=g, place=place)


# ================================= gfca end  ==============================================


# ================================= tools start =============================================


# dotplot
def dotplot_run_tools(place, email, evalue, score, hitnum, repnum, heng_chromosomes, shu_chromosomes, heng_species,
                      shu_species, blast_name, shu_gff_name, heng_gff_name, shu_len_name, heng_len_name):
    global path_get
    # perl ../programs/dotplot.pl 1e-5 100 5 20 1_2_3 1_2_3 si.lens zm.lens si.gff zm.gff zm_si.blast zm si
    cmd = f"""
        cd {path_get}/file_keep/{place}
        perl ../programs/dotplot.pl {evalue} {score} {hitnum} {repnum} {heng_chromosomes} {shu_chromosomes} {shu_len_name} {heng_len_name} {shu_gff_name} {heng_gff_name} {blast_name} {heng_species} {shu_species} 
    """
    os.system(cmd)

    g = f'{path_get}/file_keep/{place}/result.png'
    youjian(a=email, b=g, place=place)


# file_merge_run
# def file_merge_run_tools(place, email, file_name):
def file_merge_run_tools(place):
    cmd = f"""
        cd '{path_get}/file_keep/{place}'
        cat orthomcl/* >> result.txt
    """
    subprocess.run(cmd, shell=True, check=True)


# find_replace_run
def find_replace_run_tools(place, old_name, new_name):
    cmd = f"""
        cd '{path_get}/file_keep/{place}'
        sed -e 's/{old_name}/{new_name}/g' upload.txt > result.txt
    """
    subprocess.run(cmd, shell=True, check=True)



# extr_row_run
def extr_row_run(place, row_num, row_name, row_last):
    cmd = f"""
        cd {path_get}/file_keep/{place}
        cut -f {row_num} {row_name}.{row_last} > {row_name}.new.{row_last}
    """
    subprocess.run(cmd, shell=True, check=True)


# quchong_run
def quchong_run(place):
    id_list = []
    new_file = open(f'{path_get}/file_keep/{place}/new.fasta', 'w')
    for line in SeqIO.parse(f'{path_get}/file_keep/{place}/1.fasta', 'fasta'):
        if line.id not in id_list:
            id_list.append(line.id)
            new_file.write(">" + str(line.id) + "\n" + str(line.seq) + "\n")
    new_file.close()


# formatTofasta
def format_fasta_run(place, file_name, patten, patten_end, file_last):
    SeqIO.convert(f"{path_get}/file_keep/{place}/{file_name}.{file_last}", f"{patten}",
                  f"{path_get}/file_keep/{place}/{file_name}.{patten_end}", f"{patten_end}")



# WGDI ---blast_dotplot---
def dotplot_run(place, email, evalue, score, heng_species, shu_species, patten):
    global path_get

    write_txt = (str("[dotplot]") + "\n" + str(f"blast = diamond.fasta") + "\n" +
                 str("gff1 =  11.gff") + "\n" + str("gff2 =  22.gff") + "\n" + str("lens1 = 11.len") + "\n" +
                 str("lens2 = 22.len") + "\n" + str(f"genome1_name =  {shu_species}") + "\n" + str(
                f"genome2_name =  {heng_species}") + "\n" +
                 str("multiple  = 1") + "\n" + str(f"score = {score}") + "\n" + str(f"evalue = {evalue}") + "\n" +
                 str("repeat_number = 10") + "\n" + str("position = order") + "\n" + str(
                "blast_reverse = false") + "\n" +
                 str("ancestor_left = none") + "\n" + str("ancestor_top = none") + "\n" + str(
                "markersize = 0.5") + "\n" +
                 str("figsize = 10,10") + "\n" + str(f"savefig = result.{patten}") + "\n" + "\n"
                 )
    text_create('ath', str(write_txt), place)

    cmd = f"""
        cd {path_get}/file_keep/{place}
        wgdi -d ath.conf
"""
    os.system(cmd)

    g = f'{path_get}/file_keep/{place}/result.{patten}'
    youjian(a=email, b=g, place=place)


# WGDI ---wgdi_共线性分析---
def wgdimcs_run(place, email, evalue, score):
    global path_get

    write_txt = (str("[collinearity]") + "\n" + str("gff1 =  11.gff") + "\n" + str("gff2 =  22.gff") + "\n" +
                 str("lens1 = 11.len") + "\n" + str("lens2 = 22.len") + "\n" + str(f"blast = diamond.fasta") + "\n" +
                 str("blast_reverse = false") + "\n" + str("multiple  = 1") + "\n" + str("process = 8") + "\n" +
                 str(f"evalue = {evalue}") + "\n" + str(f"score = {score}") + "\n" + str("grading = 50,40,25") + "\n" +
                 str("mg = 40,40") + "\n" + str("pvalue = 0.2") + "\n" + str("repeat_number = 10") + "\n" +
                 str("positon = order") + "\n" + str("savefile = result.collinearity.txt") + "\n" + "\n"
                 )
    text_create('ath', str(write_txt), place)

    cmd = f"""
        cd {path_get}/file_keep/{place}
        wgdi -icl ath.conf
"""
    os.system(cmd)

    g = f'{path_get}/file_keep/{place}/result.collinearity.txt'
    youjian(a=email, b=g, place=place)


# WGDI ---wgdi_ks分析---
def wgdikaks_run(place, email):
    global path_get

    write_txt = (str("[ks]") + "\n" + str("cds_file = cds.fasta") + "\n" + str("pep_file = 	pep.fasta") + "\n" +
                 str("align_software = muscle") + "\n" + str("pairs_file = colinearity.txt") + "\n" +
                 str("ks_file = ks_result.txt") + "\n"
                 )
    text_create('ath', str(write_txt), place)

    cmd = f"""
        cd {path_get}/file_keep/{place}
        wgdi -ks ath.conf
"""
    os.system(cmd)

    g = f'{path_get}/file_keep/{place}/ks_result.txt'
    youjian(a=email, b=g, place=place)


# WGDI ---绘制kaks点图---
def wgdikaks_dot_run(place, email, heng_species, shu_species):
    global path_get

    write_txt = (str("[blockks]") + "\n" + str(f"lens1 = 11.len") + "\n" +
                 str("lens2 = 22.len") + "\n" + str(f"genome1_name =  {heng_species}") + "\n" +
                 str(f"genome2_name =  {shu_species}") + "\n" + str("blockinfo =  blockinfo.csv") + "\n" +
                 str("pvalue = 0.05") + "\n" + str("tandem = true") + "\n" +
                 str("tandem_length = 200") + "\n" + str("markersize = 1") + "\n" + str("area = 0,3") + "\n" +
                 str("block_length =  5") + "\n" + str("figsize = 8,8") + "\n" +
                 str("savefig = ks.dotplot.pdf") + "\n" + "\n")
    text_create('ath', str(write_txt), place)

    cmd = f"""
        cd {path_get}/file_keep/{place}
        wgdi -bk ath.conf
"""
    os.system(cmd)

    g = f'{path_get}/file_keep/{place}/ks.dotplot.pdf'
    youjian(a=email, b=g, place=place)



