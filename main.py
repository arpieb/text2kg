import warnings

warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import spacy
import textacy

nlp = spacy.load("en_core_web_sm")


def kg_from_corpus(txt):
    # Process corpus
    doc = nlp(txt)
    lst_docs = list(doc.sents)

    # Entity and relation extraction
    dic = {
        "id": [], 
        "text": [], 
        "entity": [], 
        "relation": [], 
        "object": []
    }

    for n, sentence in enumerate(lst_docs):
        lst_generators = list(textacy.extract.subject_verb_object_triples(sentence))
        for sent in lst_generators:
            subj = "_".join(map(str, sent.subject))
            obj = "_".join(map(str, sent.object))
            relation = "_".join(map(str, sent.verb))
            dic["id"].append(n)
            dic["text"].append(sentence.text)
            dic["entity"].append(subj)
            dic["object"].append(obj)
            dic["relation"].append(relation)

    dtf = pd.DataFrame(dic)

    # Generate knowledge graph
    G = nx.from_pandas_edgelist(
        dtf,
        source="entity",
        target="object",
        edge_attr="relation",
        create_using=nx.DiGraph()
    )
    return G


def plot_kg(G):
    plt.figure(figsize=(15, 10))

    # pos = nx.nx_agraph.graphviz_layout(G, prog="fdp")
    pos = nx.spring_layout(G, k=1)

    node_color = "skyblue"
    edge_color = "black"

    nx.draw(G, pos=pos, with_labels=True, node_color=node_color, edge_color=edge_color, cmap=plt.cm.Dark2,
            node_size=2000, connectionstyle='arc3,rad=0.1')

    nx.draw_networkx_edge_labels(G, pos=pos, label_pos=0.5, edge_labels=nx.get_edge_attributes(G, 'relation'),
                                 font_size=12, font_color='black', alpha=0.6)
    plt.show()


if __name__ == '__main__':
    with open('data/corpus.txt') as ifs:
        doc = ifs.read()
    kg = kg_from_corpus(doc)

    print(f"num nodes: {kg.number_of_nodes()}")
    print(f"num edges: {kg.number_of_edges()}")

    plot_kg(kg)
