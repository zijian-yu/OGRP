"""LGBP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tools import urls, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    path('shijian', views.shijian, name='shijian_url'),

    path('index', views.index, name='index_url'),
    path('index_2', views.index_2, name='index_2_url'),
    path('index_3', views.index_3, name='index_3_url'),
    path('tools', views.tools, name='tools_url'),
    path('browse', views.Browse, name='Browse_url'),

    path('sp_tree', views.sp_tree_chart, name='sp_tree_chart_url'),
    path('gene_replication_type', views.gene_replication_type, name='gene_replication_type_url'),
    
    path('diagram_blocks',views.diagram_blocks,name='diagram_blocks_url'),
    
    # 橄榄苦苷合成基因
    path('diagram_Oleuropein',views.diagram_Oleuropein,name='diagram_Oleuropein_url'),

    path('cucpathway',views.cucpathway,name='cucpathway_url'),

    path('diagram_salt-tolerant',views.diagram_salt,name='diagram_salt-tolerant_url'),

    path('diagram_TR',views.diagram_TR,name='diagram_TR_url'),

    path('Transcription_factors',views.Transcription_factors,name = 'Transcription_factors_url'),

    path('diagram_salt', views.diagram_salt, name='diagram_salt_url'),

    path('diagram_Jsa_acid', views.diagram_Jsa_acid, name='diagram_Jsa_acid_url'),

    path('diagram_heat_cold', views.diagram_heat_cold, name='diagram_heat_cold_url'),

    path('diagram_drought', views.diagram_drought, name='diagram_drought_url'),

    path('diagram_terpene', views.diagram_terpene, name='diagram_terpene_url'),

    path('p_index', views.p_index, name='p_index_url'),
    # path('Pfam_index', views.Pfam_index, name='pfam_index_url'),
    # path('pfam_index_run', views.pfam_index_run, name='pfam_index_run_url'),

    path('species_data', views.species_data, name='species_data_url'),
    # path('species_data_run', views.species_data_run, name='species_data_run_url'),
    path('Transcriptome',views.Transcriptome, name='Transcriptome_url'),
    path('transcriptome_run', views.transcriptome_run, name='transcriptome_run_url'),
    path('sp_introduce', views.sp_introduce, name='sp_introduce_url'),
    path('sp_introduce2', views.sp_introduce2, name='sp_introduce2_url'),
    path('sp_introduce3', views.sp_introduce3, name='sp_introduce3_url'),

    path('database', views.database, name='database_url'),
    path('submit', views.submit, name='submit_url'),
    path('submit_data', views.submit_data, name='submit_data_url'),
    path('documentation', views.documentation, name='documentation_url'),
    path('contact', views.contact, name='contact_url'),

    path('commands',views.commands,name='commands_url'),
    path('gfca', views.gfca, name='gfca_url'),
    path('karyotype', views.karyotype, name='karyotype_url'),
    path('gene_type',views.genetype,name='genetype_url'),
    path('genetype_run', views.genetype_run, name='genetype_run_url'),
    path('database', views.database, name='database_url'),
    path('about', views.about, name='about_url'),
    path('references', views.references, name='references_url'),
    path('new', views.new, name='new_url'),
    path('economic',views.economic, name='economic_url'),
    path('diseases',views.diseases,name='diseases_url'),
    path('pasts',views.pests,name='pests_url'),
    path('statistics', views.statistics, name='statistics_url'),


    path('article', views.article, name='article_url'),


    path('successful', views.successful, name='successful_url'),
    path('help', views.help, name='help_url'),
    path('index_email', views.index_email, name='index_email_url'),

    path('tools/', include('tools.urls')),
    path('browse/', include('browse.urls')),


    # introduce
    path("Fex", views.Fex, name="Fex_url"),
    path("Fpe", views.Fpe, name="Fpe_url"),
    path("Fam", views.Fam, name="Fam_url"),
    path("Fsu", views.Fsu, name="Fsu_url"),
    path("Jsa", views.Jsa, name="Jsa_url"),
    path("Ofr", views.Ofr, name="Ofr_url"),
    path("Oeu", views.Oeu, name="Oeu_url"),
    path("Sob", views.Sob, name="Sob_url"),
    #path("Vvi", views.Vvi, name="Vvi_urls"),
    path("Fph", views.Fph, name="Fph_url"),
    path("Adi", views.Adi, name="Adi_url"),

    path("Cba", views.Cba, name="Cba_url"),
    path("Cbi", views.Cbi, name="Cbi_url"),
    path("Cfl", views.Cfl, name="Cfl_url"),
    path("Cha", views.Cha, name="Cha_url"),
    path("Cmad", views.Cmad, name="Cmad_url"),
    path("Cmar", views.Cmar, name="Cmar_url"),
    path("Cmi", views.Cmi, name="Cmi_url"),
    path("Cob", views.Cob, name="Cob_url"),
    path("Cpo", views.Cpo, name="Cpo_url"),
    path("Cse", views.Cse, name="Cse_url"),

    path("Dcr", views.Dcr, name="Dcr_url"),
    path("Feg", views.Feg, name="Feg_url"),
    path("Feu", views.Feu, name="Feu_url"),
    path("Fis", views.Fis, name="Fis_url"),
    path("Fra", views.Fra, name="Fra_url"),
    path("Fsa", views.Fsa, name="Fsa_url"),
    path("Hin", views.Hin, name="Hin_url"),
    path("Hpa", views.Hpa, name="Hpa_url"),
    path("Hsa", views.Hsa, name="Hsa_url"),

    path("Jab", views.Jab, name="Jab_url"),
    path("Jco", views.Jco, name="Jco_url"),
    path("Jtr", views.Jtr, name="Jtr_url"),
    path("Lja", views.Lja, name="Lja_url"),
    path("Lmo", views.Lmo, name="Lmo_url"),
    path("Lse", views.Lse, name="Lse_url"),
    path("Lvu", views.Lvu, name="Lvu_url"),
    path("Maf", views.Maf, name="Maf_url"),
    path("Mne", views.Mne, name="Mne_url"),
    path("Msc", views.Msc, name="Msc_url"),
    path("Msm", views.Msm, name="Msm_url"),
    path("Msp", views.Msp, name="Msp_url"),

    path("Nac", views.Nac, name="Nac_url"),
    path("Nal", views.Nal, name="Nal_url"),
    path("Nam", views.Nam, name="Nam_url"),
    path("Nap", views.Nap, name="Nap_url"),
    path("Nar", views.Nar, name="Nar_url"),
    path("Nco", views.Nco, name="Nco_url"),
    path("Ncu", views.Ncu, name="Ncu_url"),
    path("Nem", views.Nem, name="Nem_url"),
    path("Nip", views.Nip, name="Nip_url"),
    path("Nla", views.Nla, name="Nla_url"),
    path("Nlo", views.Nlo, name="Nlo_url"),
    path("Nmi", views.Nmi, name="Nmi_url"),

    path("Oam", views.Oam, name="Oam_url"),
    path("Ome", views.Ome, name="Ome_url"),
    path("Osu", views.Osu, name="Osu_url"),
    path("Pan", views.Pan, name="Pan_url"),
    path("Pap", views.Pap, name="Pap_url"),
    path("Paz", views.Paz, name="Paz_url"),
    path("Pex", views.Pex, name="Pex_url"),
    path("Pha", views.Pha, name="Pha_url"),
    path("Pla", views.Pla, name="Pla_url"),
    path("Pme", views.Pme, name="Pme_url"),
    path("Sal", views.Sal, name="Sal_url"),
    path("Sar", views.Sar, name="Sar_url"),
    path("Sca", views.Sca, name="Sca_url"),
    path("Sma", views.Sma, name="Sma_url"),
    path("Str", views.Str, name="Str_url"),

    path("Cax", views.Cax, name="Cax_url"),
    path("Cbr", views.Cbr, name="Cbr_url"),
    path("Cdo", views.Cdo, name="Cdo_url"),
    path("Cho", views.Cho, name="Cho_url"),
    path("Cim", views.Cim, name="Cim_url"),
    path("Cpan", views.Cpan, name="Cpan_url"),
    path("Cpu", views.Cpu, name="Cpu_url"),
    path("Cqu", views.Cqu, name="Cqu_url"),
    path("Cra", views.Cra, name="Cra_url"),
    path("Cre", views.Cre, name="Cre_url"),
    path("Cod", views.Cod, name="Cod_url"),
    path("Cpar", views.Cpar, name="Cpar_url"),
    path("Csu", views.Csu, name="Csu_url"),

    path("Fan", views.Fan, name="Fan_url"),
    path("Fgi", views.Fgi, name="Fgi_url"),
    path("Fja", views.Fja, name="Fja_url"),
    path("Fko", views.Fko, name="Fko_url"),
    path("Fna", views.Fna, name="Fna_url"),
    path("Fov", views.Fov, name="Fov_url"),

    path("Fap", views.Fap, name="Fap_url"),
    path("Fbe", views.Fbe, name="Fbe_url"),
    path("Fbu", views.Fbu, name="Fbu_url"),
    path("Fca", views.Fca, name="Fca_url"),
    path("Fch", views.Fch, name="Fch_url"),
    path("Fcu", views.Fcu, name="Fcu_url"),
    path("Fdi", views.Fdi, name="Fdi_url"),
    path("Fla", views.Fla, name="Fla_url"),
    path("For", views.For, name="For_url"),
    path("Fqu", views.Fqu, name="Fqu_url"),
    path("Ftr", views.Ftr, name="Ftr_url"),

    path("Jad", views.Jad, name="Jad_url"),
    path("Jal", views.Jal, name="Jal_url"),
    path("Jau", views.Jau, name="Jau_url"),
    path("Jbr", views.Jbr, name="Jbr_url"),
    path("Jcu", views.Jcu, name="Jcu_url"),
    path("Jla", views.Jla, name="Jla_url"),
    path("Jma", views.Jma, name="Jma_url"),
    path("Jne", views.Jne, name="Jne_url"),
    path("Jpa", views.Jpa, name="Jpa_url"),

    path("Lau", views.Lau, name="Lau_url"),
    path("Lco", views.Lco, name="Lco_url"),
    path("Lex", views.Lex, name="Lex_url"),
    path("Lgr", views.Lgr, name="Lgr_url"),
    path("Lli", views.Lli, name="Lli_url"),
    path("Lob", views.Lob, name="Lob_url"),
    path("Lqu", views.Lqu, name="Lqu_url"),
    path("Lsi", views.Lsi, name="Lsi_url"),
    path("Lun", views.Lun, name="Lun_url"),

    path("Nsa", views.Nsa, name="Nsa_url"),
    path("Nba", views.Nba, name="Nba_url"),
    path("Nbr", views.Nbr, name="Nbr_url"),
    path("Nin", views.Nin, name="Nin_url"),
    path("Npe", views.Npe, name="Npe_url"),
    path("Nsp", views.Nsp, name="Nsp_url"),
    path("Nte", views.Nte, name="Nte_url"),

    path("Och", views.Och, name="Och_url"),
    path("Oex", views.Oex, name="Oex_url"),
    path("Oja", views.Oja, name="Oja_url"),
    path("Ope", views.Ope, name="Ope_url"),
    path("Oro", views.Oro, name="Oro_url"),
    path("Osc", views.Osc, name="Osc_url"),
    path("Owe", views.Owe, name="Owe_url"),
    path("Oyu", views.Oyu, name="Oyu_url"),
    path("Ocy", views.Ocy, name="Ocy_url"),
    path("Oen", views.Oen, name="Oen_url"),
    path("Ove", views.Ove, name="Ove_url"),

    path("Sem", views.Sem, name="Sem_url"),
    path("Sju", views.Sju, name="Sju_url"),
    path("Spi", views.Spi, name="Spi_url"),
    path("Spu", views.Spu, name="Spu_url"),
    path("Sre", views.Sre, name="Sre_url"),
    path("Ssw", views.Ssw, name="Ssw_url"),
    path("Sti", views.Sti, name="Sti_url"),
    path("Sto", views.Sto, name="Sto_url"),
    path("Svi", views.Svi, name="Svi_url"),
    path("Swo", views.Swo, name="Swo_url"),

    path('download/', views.download_file_view, name='download_file'),

]