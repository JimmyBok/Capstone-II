import numpy as np
import pandas as pd
import GraphTools as gt
import community
# def translate(lst,df2):
#     #takes in a list of patent numbers
#     #turns list into a one column data frame
#     df1 = pd.DataFrame(np.array(lst),columns="PATENT")
#     #returns merged list on "patent_id"
#     return df1.merge(df2,on="PATENT")
#
# def create_graph(year=year_lst, subcategories=subcategory_lst):
#     # Input: a date (or range of dates)
#     #a category or range of categories
#
#     df1 = pd.DataFrame(np.array(year),columns ="year")
#     df2 = pd.DataFrame(np.array(subcategpries),columns = )
#     pass
#     # Output: networkx graph object or edge list for networkx object
#     # Subcategories, and "the ones that work with those"
#     # Out of that patent, search the date and subcategory (???)
#

def create_subset_patents_lst(year_lst, subcategory_lst, patent_df):

    year = "GYEAR" #year granted of interest
    subcategory = "SUBCAT" #subcategory

    mask1 = patent_df.isin({year:year_lst})
    mask2 = patent_df.isin({subcategory:subcategory_lst})
    return patent_df[patent_df[patent_df[mask]][mask2]]

def citing_finder(patent_df, column_tokeep, value_tokeep):
    mask = patent_df[column_tokeep]==value_tokeep
    return patent_df[mask]

def cited_finder(patent_df, cited_column, cited_value):
    mask = patent_df[cited_column] == cited_value
    return patent_df[mask]

def find_citations(patent_subset, cit_df):
    patent_lst = patent_subset["PATENT"].tolist()
    return cit_df[cit_df["CITING"].isin(patent_subset["PATENT"].tolist())]

def create_graph_object(cit_edg):
    return nx.convert_matrix.from_pandas_edgelist(cit_edg, "CITING",'CITED')


def year_cutter(df,start_year, end_year):
    mask = (df["GYEAR"] >=start_year) & (df["GYEAR"]<=end_year)
    return df[mask]

def patent_list_to_df(patent_subset, cit_df):
    patent_lst = patent_subset["PATENT"].tolist()
    return cit_df[cit_df["CITING"].isin(patent_subset["PATENT"].tolist())]



#CREATING Edge Lists
def citation_lists_to_edge_df(cit_df, citing_lst, cited_lst):

    mask = cit_df["CITING"].isin(citing_lst)
    citing = cit_df[mask]
    mask = citing["CITED"].isin(cited_lst)           #only grab edges in the citeations_lst
    edge_citations = citing[mask]                    #pull citation edge list for only those who pass both
    return edge_citations

def patent_df_to_edge_df(citation_df, citing_patents_df, cited_patents_df):
    citing_lst = citing_patents_df["PATENT"].tolist() #turn to list of patents for nodes
    mask = citation_df["CITING"].isin(citing_lst)
    citing = citation_df[mask]

    cited_lst = cited_patents_df["PATENT"].tolist()  #turn to list of potential edges
    mask = citing["CITED"].isin(cited_lst)           #only grabe edges in the citeations_lst

    edge_citations = citing[mask]                    #pull citation edge list for only those who pass both

    return edge_citations

def cusip_df_to_edge_df(cusip_citation_df, citing_patents_df, cited_patents_df):
    """returns cusip_edge_df with CITING_CUSIP AND CITED_CUSIP as cusip numbers"""
    citing_lst = citing_patents_df["PATENT"].tolist()  #Identifies citing patents of interest: for nodes
    mask = cusip_citation_df["CITING"].isin(citing_lst)
    citing = cusip_citation_df[mask]                    #returns df of cusip_citations of interest

    cited_lst = cited_patents_df["PATENT"].tolist()  #Identifies cited patents of interest for edge values
    mask = cited_patents_df["CITED"].isin(cited_lst)           #only grabe edges in the citations_lst

    edge_citations = citing[mask]                    #pull citation edge list for only those who pass both

    cusip_edge_df = edge_citations[['CITING_CUSIP', 'CITED_CUSIP']]

    return cusip_edge_df



#GRAPH STUFF
#Creating Graph - Using graph
def create_graph(edge_lst):
    return nx.convert_matrix.from_pandas_edgelist(edge_lst, "CITING",'CITED',create_using=nx.DiGraph())

def show_graph(graph):
    return nxpd.draw(graph, show='ipynb')#4071008 #4343271

def create_cusip_graph(cusip_edge_df):
    return nx.convert_matrix.from_pandas_edgelist(edge_lst, "CITING_CUSIP",'CITED_CUSIP',create_using=nx.MultiDiGraph())


#FINDING CITATIONS OF CITATIONS
#citations of citations
def down_citation_path(cit_df, patent_number,jumps_down_rabit_hole):
    citation_list = cit_df[cit_df["CITING"] == patent_number]["CITED"].tolist()
    collected_patent_citations_df = pd.DataFrame()
    for _ in range(jumps_down_rabit_hole):
        #put in a patten number to
        current_lvl_citations = cit_df[cit_df["CITING"].isin(citation_list)]
        citation_list = current_lvl_citations["CITED"].tolist()
        collected_patent_citations_df=collected_patent_citations_df.append(current_lvl_citations, ignore_index=True, sort=False)
    return collected_patent_citations_df

def up_citation_path(cit_df, patent_number,climbs_out_rabit_hole):
    citation_list = cit_df[cit_df["CITED"] == patent_number]["CITING"].tolist()
    collected_patent_citations_df = pd.DataFrame(cit_df[cit_df["CITED"] == patent_number])
    for _ in range(climbs_out_rabit_hole):
        #put in a patten number to
        current_lvl_citations = cit_df[cit_df["CITED"].isin(citation_list)]
        citation_list = current_lvl_citations["CITING"].tolist()
        collected_patent_citations_df=collected_patent_citations_df.append(current_lvl_citations, ignore_index=True, sort=False)
    return collected_patent_citations_df

def down_citation_path_list(cit_df, patent_lst,jumps_down_rabit_hole):
    citation_list = cit_df[cit_df["CITING"].isin(patent_lst)]["CITED"].tolist()
    collected_patent_citations_df = pd.DataFrame(cit_df[cit_df["CITING"].isin(patent_lst)])
    for _ in range(jumps_down_rabit_hole):
        #put in a patten number to
        current_lvl_citations = cit_df[cit_df["CITING"].isin(citation_list)]
        citation_list = current_lvl_citations["CITED"].tolist()
        collected_patent_citations_df=collected_patent_citations_df.append(current_lvl_citations, ignore_index=True, sort=False)
    return collected_patent_citations_df


#needs check
def down_cusip_citation_path(spliced_citation_cusip_df, cusip_id,jumps_down_rabit_hole):
    citation_list = spliced_citation_cusip_df[spliced_citation_cusip_df["CITING_CUSIP"] ==str(cusip_id)]["CITED_CUSIP"].tolist()
    collected_cusip_citations_df = pd.DataFrame()
    for _ in range(jumps_down_rabit_hole):
        #put in a patten number to
        current_lvl_citations = spliced_citation_cusip_df[spliced_citation_cusip_df["CITING_CUSIP"].isin(citation_list)]
        citation_list = current_lvl_citations["CITED_CUSIP"].tolist()
        collected_cusip_citations_df=collected_cusip_citations_df.append(current_lvl_citations, ignore_index=True, sort=False)
    return collected_cusip_citations_df



#write to cut out citations with only limited number of connections
# edge_lst_dict = dict(drug_edgelst_85.CITING.value_counts())
# citing_lst =[]
# for key in edge_lst_dict:
#     if edge_lst_dict[key] >2:
#         citing_lst.append(key)
# edge_lst_dict = dict(drug_edgelst_85.CITED.value_counts())
# edge_lst =[]
# for key in edge_lst_dict:
#     if edge_lst_dict[key] >2:
#         edge_lst.append(key)




#WORKING WITH GRAPHS
#need to import graph tools as gt
def show_graph_between_edge_centrality(graph):
    between_centralities = gt.format_dict_of_floats(nx.edge_betweenness_centrality(graph))
    gt.label_edges(graph,between_centralities)

    return show_graph(graph)

#for undirected graphs only :(
def biggest_connected_piece(cur_graph):
    if not nx.is_connected(cur_graph):
        # get a list of unconnected networks
        sub_graphs = nx.connected_component_subgraphs(cur_graph)

        main_graph = sub_graphs[0]

        # find the largest network in that list
        for sg in sub_graphs:
            if len(sg.nodes()) > len(main_graph.nodes()):
                main_graph = sg
        return main_graph

def color_nodes():
    pass #import starter code from gt
def label_nodes():
    pass #import starter code from gt

#for undirected graphs only :(
def biggest_connected_piece(cur_graph):
    if not nx.is_connected(cur_graph):
        # get a list of unconnected networks
        sub_graphs = nx.connected_component_subgraphs(cur_graph)
        main_graph = sub_graphs[0]
        # find the largest network in that list
        for sg in sub_graphs:
            if len(sg.nodes()) > len(main_graph.nodes()):
                main_graph = sg

        return main_graph

#MultiDiGraph.neighbors(n)
