import numpy as np
import pandas as pd
import GraphTools as gt
import community


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
def down_citation_path(cit_df, patent_number,degrees_removed):
    mask = cit_df["CITING"] == patent_number
    citation_list = cit_df[mask]["CITED"].tolist()  #find 1st level of cited docs
    collected_patent_citations_df = cit_df[mask]    #set df that I will add too
    for _ in range(degrees_removed):
        current_lvl_citations = cit_df[cit_df["CITING"].isin(citation_list)]
        citation_list = current_lvl_citations["CITED"].tolist()
        collected_patent_citations_df=collected_patent_citations_df.append(current_lvl_citations, ignore_index=True, sort=False)
    return collected_patent_citations_df

def up_citation_path(cit_df, patent_number,degrees_removed):
    mask = cit_df["CITED"] == patent_number
    citation_list = cit_df[mask]["CITING"].tolist()
    collected_patent_citations_df = pd.DataFrame(cit_df[mask])
    for _ in range(degrees_removed):
        #put in a patten number to
        current_lvl_citations = cit_df[cit_df["CITED"].isin(citation_list)]
        citation_list = current_lvl_citations["CITING"].tolist()
        collected_patent_citations_df=collected_patent_citations_df.append(current_lvl_citations, ignore_index=True, sort=False)
    return collected_patent_citations_df



#needs check
def down_cusip_citation_path(spliced_citation_cusip_df, cusip_id,degrees_removed):
    mask =spliced_citation_cusip_df["CITING_CUSIP"] ==str(cusip_id)
    citation_list = spliced_citation_cusip_df[mask]["CITED_CUSIP"].tolist()
    collected_cusip_citations_df = pd.DataFrame(spliced_citation_cusip_df[mask])
    for _ in range(degrees_removed):
        #put in a patten number to
        current_lvl_citations = spliced_citation_cusip_df[spliced_citation_cusip_df["CITING_CUSIP"].isin(citation_list)]
        citation_list = current_lvl_citations["CITED_CUSIP"].tolist()
        collected_cusip_citations_df=collected_cusip_citations_df.append(current_lvl_citations, ignore_index=True, sort=False)
    return collected_cusip_citations_df



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

#MultiDiGraph.neighbors(n)
