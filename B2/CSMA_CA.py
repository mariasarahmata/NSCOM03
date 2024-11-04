import matplotlib.pyplot as plt
import networkx as nx

def csma_ca_flowchart():
    G = nx.DiGraph()

    # Define nodes and their positions
    nodes = {
        "Start": (0, 4),
        "K = 0": (2, 4),
        "Channel Idle?": (4, 4),
        "Wait IFS time": (6, 4),
        "Idle after IFS?": (8, 4),
        "Choose random slots": (10, 4),
        "Wait R slots": (12, 4),
        "Transmit Frame": (14, 5),
        "Timeout for ACK": (14, 3),
        "ACK received?": (16, 4),
        "Success": (18, 5),
        "Abort": (18, 3)
    }

    # Add nodes to graph
    for node, pos in nodes.items():
        G.add_node(node, pos=pos)

    # Define edges
    edges = [
        ("Start", "K = 0"), ("K = 0", "Channel Idle?"),
        ("Channel Idle?", "Wait IFS time"), ("Wait IFS time", "Idle after IFS?"),
        ("Idle after IFS?", "Choose random slots"), ("Choose random slots", "Wait R slots"),
        ("Wait R slots", "Transmit Frame"), ("Transmit Frame", "Timeout for ACK"),
        ("Timeout for ACK", "ACK received?"), ("ACK received?", "Success"),
        ("ACK received?", "Abort"), ("Idle after IFS?", "Abort")
    ]
    G.add_edges_from(edges)

    # Draw flowchart
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(14, 8))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgreen", 
            font_size=8, font_weight="bold", arrows=True, arrowstyle="->", arrowsize=15)
    plt.title("CSMA/CA Flow Diagram")
    plt.show()

csma_ca_flowchart()
