from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from LGBP.tools import *
from django.urls import reverse

path_get = os.getcwd()
print(path_get)


def index(request):
    return render(request, 'index.html')


def dotplot(request):
    return render(request, 'dotplot.html')

def colinear_kaks(request):
    return render(request,'colinear_kaks.html')

def Oleaceae_syntenic(request):
    return render(request, 'Oleaceae_syntenic.html')

def Sob_Vvi_syntenic(request):
    return render(request, 'Sob_Vvi_syntenic.html')

def Jsa_Vvi_syntenic(request):
    return render(request, 'Jsa_Vvi_syntenic.html')

def karyotype(request):
    return render(request, 'karyotype.html')

def TF_genesdx(request):
    return render(request, 'TF_genedx.html')

def TF_genes(request, title):
    name = title
    return render(request, f'function_genes/TF_gene_family.html', {"name": name})

# 功能基因
def Functional_genesdx(request):
    return render(request, 'Functional_genesdx.html')

def Functional_genes(request, title):
    name = title
    return render(request, f'function_genes/Functional_gene_family.html', {"name": name})

def TE_index1(request):
    return render(request, f'TE/TE_index1.html')

def TE_sp(request, sp_name):
    sp_name = sp_name
    return render(request, f'TE/{sp_name}.te.html')

def TE_type(request, sp_name, type):
    sp_name = sp_name
    type = type
    return render(request, f'TE/TE.html', {"sp_name": sp_name, "type": type})

def kegg(request):
    return render(request, 'kegg_Adu.html')

def kegg_index_run(request):
    sp_data_1 = request.POST.get("sp_data_1", None)
    return render(request, f'kegg/kegg_{sp_data_1}.html')

def paper(request):
    return render(request, 'paper.html')


def duplicate_removal(request):
    return render(request, 'quchong.html')


def ECH_event(request):
    return render(request, 'ECH_event_genes.html')


def OCH_event(request):
    return render(request, 'OCH_event_genes.html')


def ORT_event(request):
    return render(request, 'ORT_event_genes.html')

def event_Chu(request):
    return render(request, 'event_Chu_genes.html')

def event_Fpe(request):
    return render(request, 'event_Fpe_genes.html')

def event_Jsa(request):
    return render(request, 'event_Jsa_genes.html')

def event_Oeu(request):
    return render(request, 'event_Oeu_genes.html')

def event_Sob(request):
    return render(request, 'event_Sob_genes.html')

def event_Vvi(request):
    return render(request, 'event_Vvi_genes.html')

def genetype_Chu(request):
    return render(request, 'genetype_Chu.html')

def genetype_Fpe(request):
    return render(request, 'genetype_Fpe.html')

def genetype_Jsa(request):
    return render(request, 'genetype_Jsa.html')

def genetype_Oeu(request):
    return render(request, 'genetype_Oeu.html')

def genetype_Sob(request):
    return render(request, 'genetype_Sob.html')

def genetype_Vvi(request):
    return render(request, 'genetype_Vvi.html')

def gene_family(request):
    return render(request, 'gene_family.html')


def search_api(request):
    return render(request, 'search_api.html')


def Pfam_Bda(request):
    return render(request, 'Pfam_Bda.html')


def Pfam_Bhi(request):
    return render(request, 'Pfam_Bhi.html')


def Pfam_Blo(request):
    return render(request, 'Pfam_Blo.html')


def Pfam_Bma(request):
    return render(request, 'Pfam_Bma.html')


def Pfam_Bpe(request):
    return render(request, 'Pfam_Bpe.html')


def Pfam_Car(request):
    return render(request, 'Pfam_Car.html')


def Pfam_Chy(request):
    return render(request, 'Pfam_Chy.html')


def Pfam_Cla(request):
    return render(request, 'Pfam_Cla.html')


def Pfam_Cma(request):
    return render(request, 'Pfam_Cma.html')


def Pfam_Cme(request):
    return render(request, 'Pfam_Cme.html')


def Pfam_Cmo(request):
    return render(request, 'Pfam_Cmo.html')


def Pfam_Cpe(request):
    return render(request, 'Pfam_Cpe.html')


def Pfam_Csa(request):
    return render(request, 'Pfam_Csa.html')


def Pfam_Lsi(request):
    return render(request, 'Pfam_Lsi.html')


def Pfam_Vvi(request):
    return render(request, 'Pfam_Vvi.html')


def Pfam_index(request):
    return render(request, 'pfam_index.html')


def pfam_index_run(request):
    sp_data_1 = request.POST.get("sp_data_1", None)
    return render(request, f'pfam_{sp_data_1}.html')


def interproscan_index(request):
    return render(request, 'interproscan_index.html')


def interproscan_index_run(request):
    sp_data_1 = request.POST.get("sp_data_1", None)
    sp_data_2 = request.POST.get("sp_data_2", None)
    return render(request, f'interproscan_index_run.html', {"sp_name": sp_data_1, "type": sp_data_2})


def kegg_index(request):
    return render(request, 'kegg_index.html')


def kegg_index_run(request):
    sp_data_1 = request.POST.get("sp_data_1", None)
    return render(request, f'kegg/kegg_{sp_data_1}.html')

def Anthocyanin_genes_index(request):
    return render(request, f'function_genes/Anthocyanin_genes_index.html')

def Anthocyanin_genes(request, title):
    name = title
    # return render(request, f'Anthocyanin_genes/anthocyanin_{name}.html', {"name": name})
    return render(request, f'function_genes/Anthocyanin_genes.html', {"name": name})

def Auxin_genes_index(request):
    return render(request, f'function_genes/Auxin_genes_index.html')

def Auxin_genes(request, title):
    name = title
    return render(request, f'function_genes/Auxin_genes.html', {"name": name})

def flowerdevelopmentgenes_index(request):
    return render(request, f'function_genes/flowerdevelopmentgenes_index.html')

def flowerdevelopmentgenes(request, title):
    name = title
    return render(request, f'function_genes/flowerdevelopmentgenes.html', {"name": name})

def floweringtimegenes_index(request):
    return render(request, f'function_genes/floweringtimegenes_index.html')

def floweringtimegenes(request, title):
    name = title
    return render(request, f'function_genes/floweringtimegenes.html', {"name": name})

def pendingfloweringtimegenes_index(request):
    return render(request, f'function_genes/pendingfloweringtimegenes_index.html')

def pendingfloweringtimegenes(request, title):
    name = title
    return render(request, f'function_genes/pendingfloweringtimegenes.html', {"name": name})

def phenylalanineAmmoniaLyase_index(request):
    return render(request, f'function_genes/phenylalanineAmmoniaLyase_index.html')

def phenylalanineAmmoniaLyase(request, title):
    name = title
    return render(request, f'function_genes/phenylalanineAmmoniaLyase.html', {"name": name})

def ResistencegenesRLP_index(request):
    return render(request, f'function_genes/ResistencegenesRLP_index.html')

def ResistencegenesRLP(request, title):
    name = title
    return render(request, f'function_genes/ResistencegenesRLP.html', {"name": name})

def stearoylACPdesaturase_index(request):
    return render(request, f'function_genes/stearoylACPdesaturase_index.html')

def stearoylACPdesaturase(request, title):
    name = title
    return render(request, f'function_genes/stearoylACPdesaturase.html', {"name": name})
    
# m6a-Wirters 相关基因 --- 页面
def m6a_wirters_genes_index(request):
    return render(request, 'm6a_wirters_genes_index.html')

def m6a_wirters_genes(request, title):
    name = title
    return render(request, f'function_genes/m6a_wirters_genes.html', {"name": name})

# m6a-Readers 相关基因 --- 页面
def m6a_readers_genes(request):
    return render(request, 'function_genes/m6a_readers_genes.html')

# m6a-Erasers 相关基因 --- 页面
def m6a_erasers_genes(request):
    return render(request, 'function_genes/m6a_erasers_genes.html')


def MRCAO(request):
    return render(request, 'karyotype/Step1.html')

def CASOF(request):
    return render(request, 'karyotype/Step3.html')

def Jsa(request):
    return render(request, 'karyotype/Step2.html')

def Sob(request):
    return render(request, 'karyotype/sob.html')

def Fpe(request):
    return render(request, 'karyotype/fpe.html')

def Oeu(request):
    return render(request, 'karyotype/oeu.html')

def case_genome(request):
    return render(request, 'case_genome.html')

def case_blast(request):
    return render(request, 'case_blast.html')

def case_block(request):
    return render(request, 'case_block.html')

def case_ks(request):
    return render(request, 'case_ks.html')

def case_dating(request):
    return render(request, 'case_dating.html')

def case_ESR(request):
    return render(request, 'case_ESR.html')

def case_phylogeny(request):
    return render(request, 'case_phylogeny.html')

def case_wgd_event(request):
    return render(request, 'case_wgd_event.html')

def case_CSR(request):
    return render(request, 'case_CSR.html')
    
def case_MCR(request):
    return render(request, 'case_MCR.html')

def case_VCP(request):
    return render(request, 'case_VCP.html')

def case_AK(request):
    return render(request, 'case_AK.html')
    
def case_karyotype(request):
    return render(request, 'case_karyotype.html')

def case_hmmer(request):
    return render(request, 'case_hmmer.html')

def case_tree(request):
    return render(request, 'case_tree.html')

def case_evolution_event(request):
    return render(request, 'case_evolution_event.html')

def case_circos(request):
    return render(request, 'case_circos.html')

def case_structure(request):
    return render(request, 'case_structure.html')

def case_expression(request):
    return render(request, 'case_expression.html')
    
def case_family(request):
    return render(request, 'case_family.html')




def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


def Download_file(request, name_path):
    # print(name_path)
    file_name = name_path.split("-")[1]
    file_path = name_path.split("-")[0]
    the_file_name = file_name  # 显示在弹出对话框中的默认的下载文件名

    filename = os.path.join(path_get, "file_keep", file_path, file_name)  # 要下载的文件路径

    if not os.path.exists(filename):
        return HttpResponse("Build file not found! Please change the sequence and try again.")

    response = StreamingHttpResponse(readFile(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response
