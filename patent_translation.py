import numpy as np
import pandas as pd

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

def create_subset_patents(year_lst, subcategory_lst, patent_df):

    year = "GYEAR" #year granted of interest
    subcategory = "SUBCAT" #subcategory

    mask = patent_df.isin({year:year_lst,subcategory:subcategory_lst})
    return patent_df[mask]

def find_citations(patent_subset, cit_df):
    patent_lst = patent_subset["PATENT"].tolist()
    return cit_df[cit_df["CITING"].isin(patent_subset["PATENT"].tolist())]

def create_graph_object(cit_edg):
    return nx.convert_matrix.from_pandas_edgelist(cit_edg, "CITING",'CITED')

def cut_down(column,tokeep, df):
    mask = df["column"] == tokeep
    return df[mask]
